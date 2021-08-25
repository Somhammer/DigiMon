import os, sys
import math
import textwrap
import yaml

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import cv2
import numpy as np

from src.ui_calibrationwindow import Ui_CalibrationWindow

class DigiLabel(QLabel):
    def __init__(self, parent):
        super(DigiLabel, self).__init__(parent)

        self.x = None
        self.y = None
        self.left = None

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.RightButton:
            self.left = False
        elif event.button() == Qt.LeftButton:
            self.left = True

class CalibrationWindow(QDialog, Ui_CalibrationWindow):
    def __init__(self, image='', original_points=[], destination_points=[], mm_per_pixel=[1.0, 1.0]):
        super(CalibrationWindow, self).__init__()
        self.setupUi(self)

        self.original_points = original_points
        self.destination_points = destination_points
        self.resized_points = []

        self.labelOrigin = DigiLabel(self.labelOrigin)
        self.image_name = image
        self.image_origin = None
        self.transformed_image = None

        self.mm_per_pixel = mm_per_pixel

        self.ratio_width = 1
        self.ratio_height = 1

        if image != '' and len(self.original_points + self.destination_points) > 0:
            self.load()

        self.set_action()
        self.show()

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if any(i == event.key() for i in [Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down]):
                self.move_circle(event.key())

    def closeEvent(self, event):
        if self.transformed_image is not None:
            self.click_ok()
        else:
            self.click_cancel()

    def clickable(self, widget):
        class Filter(QObject):
            clicked = Signal()
            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            return True
                return False

        custom_filter = Filter(widget)
        widget.installEventFilter(custom_filter)
        return custom_filter.clicked

    def set_action(self):
        self.clickable(self.labelOrigin).connect(self.draw_circle)

        def set_value(width, height):
            if width == '': width = 1.0
            if height == '': height = 1.0
            self.mm_per_pixel = [float(width), float(height)]

        self.linePixelWidth.editingFinished.connect(lambda: set_value(self.linePixelWidth.text(), self.linePixelHeight.text()))
        self.linePixelHeight.editingFinished.connect(lambda: set_value(self.linePixelWidth.text(), self.linePixelHeight.text()))

        #self.pushSave.clicked.connect(self.save)
        self.pushOpen.clicked.connect(lambda: self.open())
        self.pushConvert.clicked.connect(self.convert_image)
        self.pushOk.clicked.connect(self.click_ok)
        self.pushCancel.clicked.connect(self.click_cancel)

    def open(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            self.set_image(fname)
            self.original_points = []
            self.destination_points = []
            self.resized_points = []

    def load(self):
        self.set_image(self.image_name)
        if len(self.original_points) > 0:
            for point in self.original_points:
                x, y = point[0]/self.ratio_width, point[1]/self.ratio_height
                self.resized_points.append([int(x), int(y)])

            halflength = 100
            painter = QPainter(self.pixmap)
            for point in self.resized_points:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])

            painter.end()
            self.labelOrigin.setPixmap(self.pixmap)
            print("1",self.original_points, self.resized_points, self.ratio_width, self.ratio_height)

        if len(self.destination_points) > 1:
            w = round(self.destination_points[2][0] - self.destination_points[0][0])
            h = round(self.destination_points[1][1] - self.destination_points[0][1])
            print(self.destination_points, w,h)
            self.lineWidth.setText(str(w))
            self.lineHeight.setText(str(h))

        if len(self.mm_per_pixel) > 1:
            self.linePixelWidth.setText(str(self.mm_per_pixel[0]))
            self.linePixelHeight.setText(str(self.mm_per_pixel[1]))
        
        self.convert_image()
                
    def set_image(self, name):
        if name == "": return
        self.image_name = name
        self.image_origin = cv2.imread(name)
        self.image = cv2.resize(self.image_origin, dsize=(450,450), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.image.shape
        self.ratio_width = self.image_origin.shape[1] / width
        self.ratio_height = self.image_origin.shape[0] / height
        qImg = QImage(self.image.data, width, height, width*channel, QImage.Format_BGR888)
        self.pixmap = QPixmap.fromImage(qImg)
        self.labelOrigin.resize(self.pixmap.width(), self.pixmap.height())
        self.labelOrigin.setPixmap(self.pixmap)

    def draw_circle(self):
        self.labelPosition.setText(f"Position: {self.labelOrigin.x}, {self.labelOrigin.y} ({int(self.labelOrigin.x*self.ratio_width)}, {int(self.labelOrigin.y*self.ratio_height)})")
        halflength = 100

        if self.labelOrigin.left:
            if len(self.resized_points) == 4: return
            self.resized_points.append([self.labelOrigin.x, self.labelOrigin.y])
            painter = QPainter(self.pixmap)
            painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
            painter.drawLine(self.labelOrigin.x - halflength, self.labelOrigin.y, self.labelOrigin.x + halflength, self.labelOrigin.y)
            painter.drawLine(self.labelOrigin.x, self.labelOrigin.y - halflength, self.labelOrigin.x, self.labelOrigin.y + halflength)
            painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
            painter.drawPoint(self.labelOrigin.x, self.labelOrigin.y)

            painter.end()
            self.labelOrigin.setPixmap(self.pixmap)
        else:
            height, width, channel = self.image.shape
            qImg = QImage(self.image.data, width, height, width*channel, QImage.Format_BGR888)
            self.pixmap = QPixmap.fromImage(qImg)
            painter = QPainter(self.pixmap)
            x,y = 999, 999
            radius = 40
            for point in self.resized_points:
                distance = math.sqrt(pow((point[0] - self.labelOrigin.x),2) + pow((point[1] - self.labelOrigin.y), 2))
                if distance < radius:
                    x = point[0]
                    y = point[1]

            if x != 999 and y != 999:
                self.resized_points.remove([x,y])

            for point in self.resized_points:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])
            
            painter.end()
            self.labelOrigin.setPixmap(self.pixmap)
        
    def move_circle(self, key):
        if len(self.resized_points) < 1:
            return

        halflength = 100
        x, y = self.resized_points[-1][0], self.resized_points[-1][1]
        height, width, channel = self.image.shape
        qImg = QImage(self.image.data, width, height, width*channel, QImage.Format_BGR888)
        self.pixmap = QPixmap.fromImage(qImg)
        painter = QPainter(self.pixmap)

        last_point = self.resized_points[-1]
        if key == Qt.Key_Right:
            x = x + 1
        elif key == Qt.Key_Left:
            x = x - 1
        elif key == Qt.Key_Up:
            y = y - 1
        elif key == Qt.Key_Down:
            y = y + 1

        self.resized_points.pop(-1)
        self.resized_points.append([x, y])

        for point in self.resized_points:
            painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
            painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
            painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
            painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
            painter.drawPoint(point[0], point[1])
            
        painter.end()
        self.labelOrigin.setPixmap(self.pixmap)
        self.labelPosition.setText(f"Position: {self.resized_points[-1][0]}, {self.resized_points[-1][1]} ({int(self.resized_points[-1][0]*self.ratio_width)}, {int(self.resized_points[-1][1]*self.ratio_height)})")

    def convert_image(self):
        if len(self.resized_points) != 4: return

        for point in self.resized_points:
            x, y = point[0], point[1]
            x *= self.ratio_width
            y *= self.ratio_height
            if len(self.original_points) == 4:
                self.original_points = []
            self.original_points.append([int(x), int(y)])

        half_width = self.image_origin.shape[1] / 2
        half_height = self.image_origin.shape[0] / 2

        upper_left, lower_left, upper_right, lower_right = [0,0], [0,0], [0,0], [0,0]
        for point in self.original_points:
            if point[0] < half_width and point[1] < half_height:
                upper_left = point
            elif point[0] < half_width and point[1] > half_height:
                lower_left = point
            elif point[0] > half_width and point[1] < half_height:
                upper_right = point
            else:
                lower_right = point

        self.original_points = [upper_left, lower_left, upper_right, lower_right]
        w = int(max(math.sqrt((upper_left[0] - upper_right[0])**2 + (upper_left[1] - upper_right[1])**2), math.sqrt((lower_left[0] - lower_right[0])**2 + (lower_left[1] - lower_right[1])**2)))
        h = int(max(math.sqrt((upper_left[0] - lower_left[0])**2 + (upper_left[1] - lower_left[0])**2), math.sqrt((upper_right[0] - lower_right[0])**2 + (upper_right[1] - lower_right[0])**2)))
        if not (self.lineWidth.text() == '' and self.lineHeight.text() == ''):
            print(self.lineWidth.text(), self.lineHeight.text())
            w = int(self.lineWidth.text())
            h = int(self.lineHeight.text())
        self.destination_points = [upper_left, [upper_left[0], upper_left[1]+h], [upper_left[0]+w, upper_left[1]], [upper_left[0]+w, upper_left[1]+h]]

        # 좌표: 좌상, 좌하, 우상, 우하
        transform_matrix = cv2.getPerspectiveTransform(np.float32(self.original_points), np.float32(self.destination_points))
        self.transformed_image = cv2.warpPerspective(self.image_origin, transform_matrix, (self.image_origin.shape[1], self.image_origin.shape[0]))

        self.transformed_image2 = cv2.resize(self.transformed_image, dsize=(450,450), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.transformed_image2.shape
        qImg = QImage(self.transformed_image2.data, width, height, width*channel, QImage.Format_BGR888)
        self.pixmap2 = QPixmap.fromImage(qImg)

        painter = QPainter(self.pixmap2)
        painter.setPen(QPen(QColor(178, 54, 245), 4, Qt.DashLine))
        start_point = (self.destination_points[0][0] / self.ratio_width, self.destination_points[0][1] / self.ratio_height)
        width = w / self.ratio_width
        height = h / self.ratio_height
        painter.drawRect(start_point[0], start_point[1], width, height)
        painter.end()

        self.labelTrans.resize(self.pixmap2.width(), self.pixmap2.height())
        self.labelTrans.setPixmap(self.pixmap2)

    def click_ok(self):
        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()
        else:
            return

    def return_para(self):
        return super().exec_()