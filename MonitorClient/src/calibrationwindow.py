import os, sys
import math
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
    def __init__(self):
        super(CalibrationWindow, self).__init__()
        self.setupUi(self)

        self.original_points = []
        self.resized_points = []

        self.labelOrigin = DigiLabel(self.labelOrigin)
        self.image_origin = None
        self.transformed_image = None

        self.set_image("/home/seohyeon/work/BeamMonitor/SCFC/cali/20170330.bmp")
        self.set_action()
        self.show()

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

    def trace(self, widget):
        class Filter(QObject):
            trace = Signal()
            def eventFilter(self, obj, event):
                if obj  == widget:
                    if event.type() == QEvent.MouseMove:
                        if obj.rect().contains(event.pos()):
                            self.trace.emit()
                            return True
                return False

        custom_filter = Filter(widget)
        widget.installEventFilter(custom_filter)
        return custom_filter.trace

    def set_action(self):
        self.buttonBox.accepted.connect(self.click_ok)
        self.buttonBox.rejected.connect(self.click_cancel)

        self.clickable(self.labelOrigin).connect(self.draw_circle)
        #self.trace(self.labelOrigin).connect(self.draw_circle)

        self.pushOpen.clicked.connect(self.open_image)
        self.pushConvert.clicked.connect(self.convert_image)

    def open_image(self):
        fname = QFileDialog.getOpenFileName(self, "Select Image")[0]
        if fname != '':
            self.set_image(fname)
    
    def set_image(self, name):
        if name == "": return
        self.image_origin = cv2.imread(name)
        self.labelFile.setText(f"Image: {name}")
        self.image = cv2.resize(self.image_origin, dsize=(400,400), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.image.shape
        qImg = QImage(self.image.data, width, height, width*channel, QImage.Format_BGR888)
        self.pixmap = QPixmap.fromImage(qImg)
        self.labelOrigin.resize(self.pixmap.width(), self.pixmap.height())
        self.labelOrigin.setPixmap(self.pixmap)

    def draw_circle(self):
        self.labelPosition.setText(f"Position: {self.labelOrigin.x}, {self.labelOrigin.y}")
        halflength = 100

        if self.labelOrigin.left:
            if len(self.resized_points) == 4: return
            self.resized_points.append((self.labelOrigin.x, self.labelOrigin.y))
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
                self.resized_points.remove((x,y))

            for point in self.resized_points:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])
            
            painter.end()
            self.labelOrigin.setPixmap(self.pixmap)

    def convert_image(self):
        if len(self.resized_points) != 4: return

        height, width, channel = self.image_origin.shape
        ratio_width = width / self.pixmap.width()
        ratio_height = height / self.pixmap.height()
        
        for point in self.resized_points:
            x, y = point[0], point[1]
            x *= ratio_width
            y *= ratio_height
            self.original_points.append((int(x), int(y)))

        half_width = width / 2
        half_height = height / 2

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

        # 좌표: 좌상, 좌하, 우상, 우하
        original_points = np.float32([upper_left, lower_left, upper_right, lower_right])
        destination_points = np.float32([[0,0],[0,800],[800,0],[800,800]]) # 이미지 크기는 나중에 바꿀 수 있음...?
        transform_matrix = cv2.getPerspectiveTransform(original_points, destination_points)
        self.transformed_image = cv2.warpPerspective(self.image_origin, transform_matrix, (800,800))

        self.transformed_image2 = cv2.resize(self.transformed_image, dsize=(400,400), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.transformed_image2.shape
        qImg = QImage(self.transformed_image2.data, width, height, width*channel, QImage.Format_BGR888)
        self.pixmap2 = QPixmap.fromImage(qImg)
        self.labelTrans.resize(self.pixmap2.width(), self.pixmap2.height())
        self.labelTrans.setPixmap(self.pixmap2)

    def click_ok(self):
        self.accept()

    def click_cancel(self):
        self.reject()
    
    def return_para(self):
        return super().exec_()