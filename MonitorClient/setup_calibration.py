import os, sys
import cv2 
import math
import copy
import datetime

import numpy as np

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from digilabel import DigiLabel
from ui_imagewindow import Ui_ImageWindow
import utilities as ut

class ExpandedImage(QDialog, Ui_ImageWindow):
    def __init__(self, para, image_name):
        super(ExpandedImage, self).__init__()
        self.setupUi(self)

        self.flag = False
        self.para = para
        self.image = cv2.imread(image_name)
        self.imagesize = [self.frameImage.width(), self.frameImage.height()]
        self.target_points = []
        self.resized_points = []
        self.labelImage = DigiLabel(self.labelImage)
        self.gridLayout_2.addWidget(self.labelImage, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.labelImage.clicked.connect(self.draw_circle)
        self.showMaximized()

    def showMaximized(self) -> None:
        super().showMaximized()
        self.flag = True

    def draw_image(self):
        resized_image = cv2.resize(self.image, dsize=self.imagesize, interpolation=cv2.INTER_LINEAR)
        if len(resized_image.shape) == 3:
            height, width, channel = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qImg)

        halflength = 100
        painter = QPainter(pixmap)
        for point in self.resized_points:
            painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
            painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
            painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
            painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
            #painter.drawPoint(point[0], point[1])
        painter.end()

        self.labelImage.resize(pixmap.width(), pixmap.height())
        self.labelImage.setPixmap(pixmap)

        self.flag = False
    
    def draw_circle(self):
        if self.labelImage.left:
            if len(self.resized_points) == 4: return
            self.resized_points.append([self.labelImage.x, self.labelImage.y])
        else:
            x,y = 999, 999
            radius = 40
            for point in self.resized_points:
                distance = math.sqrt(pow((point[0] - self.labelImage.x),2) + pow((point[1] - self.labelImage.y), 2))
                if distance < radius:
                    x = point[0]
                    y = point[1]

            if x != 999 and y != 999:
                self.resized_points.remove([x,y])

        self.draw_image()

    def move_circle(self, key):
        if len(self.resized_points) < 1: return

        x, y = self.resized_points[-1][0], self.resized_points[-1][1]

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
        
        self.draw_image()

    def resizeEvent(self, event):
        if self.flag: 
            self.imagesize = [self.frameImage.width(), self.frameImage.height()]
            self.draw_image()

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            self.labelImage.setFocus()
            if any(i == event.key() for i in [Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down]):
                self.move_circle(event.key())

    def return_para(self):
        return super().exec_()

#--------------------------- SetupWindow ---------------------------#
def open_calibration_image(self):
    extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
    fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
    
    if fname != '':
        self.calibration_image_name = fname
        self.original_points = []
        self.destination_points = []
        self.resized_points = []
        self.load_calibration_image()

def load_calibration_image(self):
    self.calibration_image = cv2.imread(self.calibration_image_name)
    self.calibration_image_backup = self.calibration_image.copy()
    if self.calibration_image_aratio is None:
        self.calibration_image_aratio = float(self.calibration_image.shape[1]) / float(self.calibration_image.shape[0])

    if self.calibration_image_aratio > 1:
        self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
        self.ratio_height = float(self.calibration_image.shape[0] / (self.calibration_image_screen_size[0] / self.calibration_image_aratio))
    elif self.calibration_image_aratio < 1:
        self.ratio_width = float(self.calibration_image.shape[1] / (self.calibration_image_screen_size[0] * self.calibration_image_aratio))
        self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
    else:
        self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
        self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])

    if len(self.original_points) > 0:
        for point in self.original_points:
            x, y = point[0]/self.ratio_width, point[1]/self.ratio_height
            self.resized_points.append([round(x), round(y)])
        
    self.convert_calibration_image()
    self.draw_calibration_image(self.calibration_image)

def capture_calibration_image(self):
    self.take_a_picture(True)

    if self.calibration_image_aratio > 1:
        self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
        self.ratio_height = float(self.calibration_image.shape[0] / (self.calibration_image_screen_size[0] / self.calibration_image_aratio))
    elif self.calibration_image_aratio < 1:
        self.ratio_width = float(self.calibration_image.shape[1] / (self.calibration_image_screen_size[0] * self.calibration_image_aratio))
        self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
    else:
        self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
        self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
        
    base_path = os.path.abspath(os.path.dirname(__file__))
    self.calibration_image_name = os.path.join(base_path, 'setup', f"Calibration_{datetime.datetime.today().strftime('%H-%M-%S_%f')}.png").replace('\\', '/')
    cv2.imwrite(self.calibration_image_name, self.calibration_image)

def draw_calibration_image(self, image, origin=True):
    if image is None: return
    #resized_image = cv2.resize(image, dsize=self.calibration_image_screen_size, interpolation=cv2.INTER_LINEAR)
    #height, width, channel = resized_image.shape
    #qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
    #pixmap = QPixmap.fromImage(qImg)
    if origin:
        # FIXME
        angle = float(self.lineRotationAngle.text())
        self.para.rotation = angle
        image = ut.rotate_image(self.para, image)
        self.draw_image(image, self.labelOrigin, self.calibration_image_screen_size, self.calibration_image_aratio, image_processing=False)
        pixmap = self.labelOrigin.pixmap()
        halflength = 100
        painter = QPainter(pixmap)
        for point in self.resized_points:
            painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
            painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
            painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
            painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
            painter.drawPoint(point[0], point[1])
        painter.end()
        self.labelOrigin.resize(pixmap.width(), pixmap.height())
        self.labelOrigin.setPixmap(pixmap)
    else:
        self.draw_image(image, self.labelTrans, self.calibration_image_screen_size, self.calibration_image_aratio, image_processing=False)
        pixmap = self.labelTrans.pixmap()
        painter = QPainter(pixmap)
        if self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()) == "Rectangle":
            painter.setPen(QPen(QColor(178, 54, 245), 4, Qt.DashLine))
            start_point = (self.destination_points[0][0] / self.ratio_width, self.destination_points[0][1] / self.ratio_height)
            end_point = (self.destination_points[3][0] / self.ratio_width, self.destination_points[3][1] / self.ratio_height)
            width = end_point[0] - start_point[0]
            height = end_point[1] - start_point[1]
            painter.drawRect(start_point[0], start_point[1], width, height)
        else:
            painter.setPen(QPen(QColor(90, 94, 99), 2 , Qt.SolidLine))
            halflength = 100
            for point in self.destination_points:
                x, y = point[0] / self.ratio_width, point[1] / self.ratio_height
                painter.drawLine(x - halflength, y, x + halflength, y)
                painter.drawLine(x, y - halflength, x, y + halflength)
        painter.end()
        self.labelTrans.resize(pixmap.width(), pixmap.height())
        self.labelTrans.setPixmap(pixmap)

def expand_calibration_image(self):
    if not self.labelOrigin.ctrdclick: return
    dialog = ExpandedImage(self.para, self.calibration_image_name)

    r = dialog.return_para()
    self.labelOrigin.ctrdclick = False
    if r:
        ratio = [dialog.image.shape[1]/dialog.labelImage.width(), dialog.image.shape[0]/dialog.labelImage.height()]
        self.original_points = []
        self.resized_points = []
        for ipoint in dialog.resized_points:
            point = [round(ipoint[0]*ratio[0]), round(ipoint[1]*ratio[1])]
            self.original_points.append(point)
            point = [round(point[0]/self.ratio_width), round(point[1]/self.ratio_height)]
            self.resized_points.append(point)

        print(self.original_points, self.resized_points)
        
        self.draw_calibration_image(self.calibration_image)

def convert_calibration_image(self):
    if len(self.resized_points) != 4: return

    for point in self.resized_points:
        x, y = point[0], point[1]
        x *= self.ratio_width
        y *= self.ratio_height
        if len(self.original_points) == 4:
            self.original_points = []
        self.original_points.append([int(x), int(y)])

    half_width = self.calibration_image.shape[1] / 2
    half_height = self.calibration_image.shape[0] / 2

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

    if self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()) == "Rectangle":
        w, h = -9999, -9999
        for coordinate in self.original_points:
            w_tmp = round(abs(half_width - coordinate[0]))
            h_tmp = round(abs(half_height - coordinate[1]))
            if w < w_tmp: w = w_tmp
            if h < h_tmp: h = h_tmp
        
        self.destination_points = [
            [round(half_width - w), round(half_height - h)],
            [round(half_width - w), round(half_height + h)],
            [round(half_width + w), round(half_height - h)],
            [round(half_width + w), round(half_height + h)]
        ]

        self.para.pixel_per_mm = [float(self.linePixelPerMM_x.text()), float(self.linePixelPerMM_y.text())]
    else:
        x1, y1, x2, y2 = float(self.lineQuad1x.text()), float(self.lineQuad1y.text()), float(self.lineQuad2x.text()), float(self.lineQuad4y.text())
        self.para.pixel_per_mm = [abs(upper_right[0] - upper_left[0])/abs(x2 - x1), abs(upper_right[1] - lower_right[1])/abs(y2 - y1)]

        self.points = [self.lineQuad1x.text(), self.lineQuad2x.text(), self.lineQuad3x.text(), self.lineQuad4x.text(),
                        self.lineQuad1y.text(), self.lineQuad2y.text(), self.lineQuad3y.text(), self.lineQuad4y.text()]

        self.destination_points = [
            [half_width - abs(float(self.lineQuad2x.text()))*self.para.pixel_per_mm[0], half_height - abs(float(self.lineQuad2y.text()))*self.para.pixel_per_mm[1]],
            [half_width - abs(float(self.lineQuad3x.text()))*self.para.pixel_per_mm[0], half_height + abs(float(self.lineQuad3y.text()))*self.para.pixel_per_mm[1]],
            [half_width + abs(float(self.lineQuad1x.text()))*self.para.pixel_per_mm[0], half_height - abs(float(self.lineQuad1y.text()))*self.para.pixel_per_mm[1]],
            [half_width + abs(float(self.lineQuad4x.text()))*self.para.pixel_per_mm[0], half_height + abs(float(self.lineQuad4y.text()))*self.para.pixel_per_mm[1]]
        ]

        x1, y1, x2, y2 = float(self.lineQuad1x.text()), float(self.lineQuad1y.text()), float(self.lineQuad3x.text()), float(self.lineQuad3y.text())
        self.para.pixel_per_mm = [
            abs(self.destination_points[0][0] - self.destination_points[1][0])/abs(x2 - x1),
            abs(self.destination_points[2][1] - self.destination_points[1][1])/abs(y2 - y1)
        ]
    self.transform_matrix = cv2.getPerspectiveTransform(np.float32(self.original_points), np.float32(self.destination_points))
    self.calibration_angle = float(self.lineRotationAngle.text())
    image = ut.rotate_image(self.para, self.calibration_image)

    self.transformed_image = cv2.warpPerspective(image, self.transform_matrix, (image.shape[1], image.shape[0]))

    self.draw_calibration_image(self.transformed_image, False)
    self.calibrated = True
    self.set_checked(self.checkCalibration, True)
    self.perspective_method = self.tabWidget_2.tabText(self.tabWidget_2.currentIndex())

def set_rotation_angle(self, up=True):
    if self.sliderAngle.value() == 0: unit = 0.01
    elif self.sliderAngle.value() == 1: unit = 0.1
    elif self.sliderAngle.value() == 2: unit = 1
    elif self.sliderAngle.value() == 3: unit = 10
    else: unit = 100

    value = float(self.lineRotationAngle.text())
    if up: value = value + unit
    else: value = value - unit
    value = round(value, 2)
    
    if value < 0.0: value = 360.0 + value
    elif value > 360.0: value = value - 360.0
    if up:
        self.lineRotationAngle.setText(str(value))
    else:
        self.lineRotationAngle.setText(str(value))
    self.draw_calibration_image(self.calibration_image)

def draw_circle(self):
    if self.labelOrigin.ctrdclick: return
    self.labelPosition.setText(f"Position: {self.labelOrigin.x}, {self.labelOrigin.y} ({int(self.labelOrigin.x*self.ratio_width)}, {int(self.labelOrigin.y*self.ratio_height)})")
    if self.labelOrigin.left:
        if len(self.resized_points) == 4: return
        self.resized_points.append([self.labelOrigin.x, self.labelOrigin.y])
    else:
        x,y = 999, 999
        radius = 40
        for point in self.resized_points:
            distance = math.sqrt(pow((point[0] - self.labelOrigin.x),2) + pow((point[1] - self.labelOrigin.y), 2))
            if distance < radius:
                x = point[0]
                y = point[1]

        if x != 999 and y != 999:
            self.resized_points.remove([x,y])

    self.draw_calibration_image(self.calibration_image)

def move_circle(self, key):
    if len(self.resized_points) < 1: return

    x, y = self.resized_points[-1][0], self.resized_points[-1][1]

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

    self.labelPosition.setText(f"Position: {self.resized_points[-1][0]}, {self.resized_points[-1][1]} ({int(self.resized_points[-1][0]*self.ratio_width)}, {int(self.resized_points[-1][1]*self.ratio_height)})")
    self.draw_calibration_image(self.calibration_image)

