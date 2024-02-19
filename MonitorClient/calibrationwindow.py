import os, sys
import time
import datetime
import logging
import copy
import yaml
import math
import textwrap
import cv2
import numpy as np

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

from logger import LogStringHandler
from variables import *
import utilities as ut
from digilabel import DigiLabel
from ui_calibrationwindow import Ui_CalibrationWindow
from ui_imagewindow import Ui_ImageWindow

class ExpandedImage(QDialog, Ui_ImageWindow):
    def __init__(self, para, image_name):
        super(ExpandedImage, self).__init__()
        self.setupUi(self)

        self.flag = False
        self.para = para
        self.image = cv2.imread(image_name)
        self.image_size = [self.frameImage.width(), self.frameImage.height()]
        self.image_points = []
        self.labelImage = DigiLabel(self.labelImage)
        self.gridLayout_2.addWidget(self.labelImage, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.labelImage.clicked.connect(self.draw_circle)
        self.showMaximized()

    def showMaximized(self) -> None:
        super().showMaximized()
        self.flag = True

    def draw_image(self):
        resized_image = cv2.resize(self.image, dsize=self.image_size, interpolation=cv2.INTER_LINEAR)
        if len(resized_image.shape) == 3:
            height, width, channel = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qImg)

        halflength = 100
        painter = QPainter(pixmap)
        for point in self.image_points:
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
            if len(self.image_points) == 4: return
            self.image_points.append([self.labelImage.x, self.labelImage.y])
        else:
            x,y = 999, 999
            radius = 40
            for point in self.image_points:
                distance = math.sqrt(pow((point[0] - self.labelImage.x),2) + pow((point[1] - self.labelImage.y), 2))
                if distance < radius:
                    x = point[0]
                    y = point[1]

            if x != 999 and y != 999:
                self.image_points.remove([x,y])

        self.draw_image()

    def move_circle(self, key):
        if len(self.image_points) < 1: return

        x, y = self.image_points[-1][0], self.image_points[-1][1]

        if key == Qt.Key_Right:
            x = x + 1
        elif key == Qt.Key_Left:
            x = x - 1
        elif key == Qt.Key_Up:
            y = y - 1
        elif key == Qt.Key_Down:
            y = y + 1

        self.image_points.pop(-1)
        self.image_points.append([x, y])
        
        self.draw_image()

    def resizeEvent(self, event):
        if self.flag: 
            self.image_size = [self.frameImage.width(), self.frameImage.height()]
            self.draw_image()

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            self.labelImage.setFocus()
            if any(i == event.key() for i in [Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down]):
                self.move_circle(event.key())

    def return_para(self):
        return super().exec_()

class CalibrationWindow(QDialog, Ui_CalibrationWindow):
    def __init__(self, para, blueberry):
        super(CalibrationWindow, self).__init__()

        self.setupUi(self)

        self.para = para
        self.blueberry = blueberry

        self.labelOrigin = DigiLabel(self.labelOrigin)
        self.gridLayout_9.addWidget(self.labelOrigin, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.calibration_image = None
        self.calibration_image_aratio = None
        self.calibration_image_name = ""
        self.calibration_image_backup = None
        self.calibration_image_screen_size = (400, 400)

        self.transformed_image = None

        self.cal_target_points = self.cal_dest_points = self.cal_reduced_target = self.cal_real_target  = []

        self.set_action()
    
    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            self.labelOrigin.setFocus()
            if any(i == event.key() for i in [Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down]):
                self.move_circle(event.key())
            else:
                self.labelOrigin.ctrdclick = True
    
    def keyReleaseEvent(self, event):
        self.labelOrigin.ctrdclick = False

    def set_action(self):
        # Calibration
        ### Basic button & image
        self.labelOrigin.clicked.connect(self.draw_circle)
        self.labelOrigin.rdclicked.connect(self.expand_calibration_image)
        self.pushOpenImage.clicked.connect(self.open_calibration_image)
        self.pushCalCapture.clicked.connect(self.capture_calibration_image)
        self.pushConvert.clicked.connect(self.convert_calibration_image)
        self.pushReset.clicked.connect(self.reset_calibration)
        ### Perspective matrix
        ##### Points
        self.lineReal1x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal1y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal2x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal2y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal3x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal3y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal4x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineReal4y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.linePixel1x.setValidator(QIntValidator(-9999, 9999))
        self.linePixel1y.setValidator(QIntValidator(-9999, 9999))
        self.linePixel2x.setValidator(QIntValidator(-9999, 9999))
        self.linePixel2y.setValidator(QIntValidator(-9999, 9999))
        self.linePixel3x.setValidator(QIntValidator(-9999, 9999))
        self.linePixel3y.setValidator(QIntValidator(-9999, 9999))
        self.linePixel4x.setValidator(QIntValidator(-9999, 9999))
        self.linePixel4y.setValidator(QIntValidator(-9999, 9999))

    def reset_calibration(self):
        self.para.calibrated = False
        self.para.pixel_per_mm = [1.0,1.0]
        self.para.coordinate_center = [0,0]
        self.para.transform_matrix = np.array([])
        self.para.cal_target_points = {}
        self.para.cal_dest_points = {}


        self.calibration_image = None
        self.calibration_image_aratio = None
        self.calibration_image_name = ""
        self.calibration_image_backup = None
        self.transformed_image = None

        self.cal_target_points = self.cal_dest_points = self.cal_reduced_target = self.cal_real_target  = []

        self.labelOrigin.setPixmap(None)
        self.labelTrans.setPixmap(None)

        self.lineReal1x.setText("")
        self.lineReal1y.setText("")
        self.lineReal2x.setText("")
        self.lineReal2y.setText("")
        self.lineReal3x.setText("")
        self.lineReal3y.setText("")
        self.lineReal4x.setText("")
        self.lineReal4y.setText("")
        self.linePixel1x.setText("")
        self.linePixel1y.setText("")
        self.linePixel2x.setText("")
        self.linePixel2y.setText("")
        self.linePixel3x.setText("")
        self.linePixel3y.setText("")
        self.linePixel4x.setText("")
        self.linePixel4y.setText("")



    def return_para(self):
        sender = self.sender()
        if sender == self.buttonBox:
            button = self.buttonBox.standardButton(sender.button(sender.clickedButton()))
            if button == QDialogButtonBox.Ok:
                self.accept()
            else:
                self.reject()
        return super().exec_()
    
    def draw_image(self, image, label, screen_size, aspect_ratio):
        if image is None: return
        
        image_copy = copy.deepcopy(image)

        if aspect_ratio > 1:
            dsize = (screen_size[0], round(screen_size[0] / aspect_ratio))
        elif aspect_ratio < 1:
            dsize = (round(screen_size[1] * aspect_ratio), screen_size[1])
        else:
            dsize = (screen_size[0], screen_size[1])

        height, width = image_copy.shape[0], image_copy.shape[1]

        if 0.99 < width / height < 1.01:
            dsize = (screen_size[0], screen_size[1])

        resized_image = cv2.resize(image_copy, dsize=dsize, interpolation=cv2.INTER_LINEAR)
        self.image_for_ROI = copy.deepcopy(resized_image)

        if len(resized_image.shape) == 3:
            height, width, channel = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qImg)

        label.resize(width, height)
        label.setPixmap(pixmap)

    def open_calibration_image(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            self.calibration_image_name = fname
            self.cal_target_points = []
            self.cal_dest_points = []
            self.cal_reduced_target = []
            self.load_calibration_image()

    def load_calibration_image(self):
        if self.calibration_image_name == '': return
        self.calibration_image = cv2.imread(self.calibration_image_name)
        if self.calibration_image is None: return
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

        if len(self.cal_real_target) > 0:
            for point in self.cal_real_target:
                x, y = point[0]/self.ratio_width, point[1]/self.ratio_height
                self.cal_reduced_target.append([round(x), round(y)])
            
        self.convert_calibration_image()
        self.draw_calibration_image(self.calibration_image)

    def capture_calibration_image(self):
        if not self.para.cam_conn: return

        self.calibration_image = self.blueberry.take_a_picture(True)
        if self.calibration_image is None: return
        if self.calibration_image_aratio is None:
            self.calibration_image_aratio = float(self.calibration_image.shape[1]) / float(self.calibration_image.shape[0])
        
        self.calibration_image_backup = self.calibration_image.copy()
        self.draw_image(self.calibration_image, self.labelOrigin, self.calibration_image_screen_size, self.calibration_image_aratio)

        if self.calibration_image_aratio > 1:
            self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
            self.ratio_height = float(self.calibration_image.shape[0] / (self.calibration_image_screen_size[0] / self.calibration_image_aratio))
        elif self.calibration_image_aratio < 1:
            self.ratio_width = float(self.calibration_image.shape[1] / (self.calibration_image_screen_size[0] * self.calibration_image_aratio))
            self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
        else:
            self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
            self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
            
        self.calibration_image_name = os.path.join(BASE_PATH, 'setup', f"Calibration_{datetime.datetime.today().strftime('%H-%M-%S_%f')}.png").replace('\\', '/')
        cv2.imwrite(self.calibration_image_name, self.calibration_image)

    def draw_calibration_image(self, image, origin=True):
        if image is None: return
        #resized_image = cv2.resize(image, dsize=self.calibration_image_screen_size, interpolation=cv2.INTER_LINEAR)
        #height, width, channel = resized_image.shape
        #qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        #pixmap = QPixmap.fromImage(qImg)
        if origin:
            center = (round(image.shape[1]/2), round(image.shape[0]/2))

            self.draw_image(image, self.labelOrigin, self.calibration_image_screen_size, self.calibration_image_aratio)

            pixmap = self.labelOrigin.pixmap()
            halflength = 100
            painter = QPainter(pixmap)
            for point in self.cal_reduced_target:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])
            painter.end()
            self.labelOrigin.resize(pixmap.width(), pixmap.height())
            self.labelOrigin.setPixmap(pixmap)
        else:
            self.draw_image(image, self.labelTrans, self.calibration_image_screen_size, self.calibration_image_aratio)
            pixmap = self.labelTrans.pixmap()
            painter = QPainter(pixmap)

            painter.setPen(QPen(QColor(90, 94, 99), 2 , Qt.SolidLine))
            halflength = 100
            for point in self.cal_dest_points:
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
            self.cal_target_points = []
            self.cal_reduced_target = []
            for ipoint in dialog.image_points:
                point = [round(ipoint[0]*ratio[0]), round(ipoint[1]*ratio[1])]
                self.cal_target_points.append(point)
                point = [round(point[0]/self.ratio_width), round(point[1]/self.ratio_height)]
                self.cal_reduced_target.append(point)
            
            self.draw_calibration_image(self.calibration_image)

    def convert_calibration_image(self):
        if len(self.cal_reduced_target) != 4: return

        self.cal_target_points = [
            [int(self.linePixel1x.text()), int(self.linePixel1y.text())],
            [int(self.linePixel2x.text()), int(self.linePixel2y.text())],
            [int(self.linePixel3x.text()), int(self.linePixel3y.text())],
            [int(self.linePixel4x.text()), int(self.linePixel4y.text())]
        ]

        self.cal_real_target = [
            [float(self.lineReal1x.text()), float(self.lineReal1y.text())],
            [float(self.lineReal2x.text()), float(self.lineReal2y.text())],
            [float(self.lineReal3x.text()), float(self.lineReal3y.text())],
            [float(self.lineReal4x.text()), float(self.lineReal4y.text())]
        ]

        try:
            tmp = np.array([0.0, 0.0])
            tmp2 = 0
            for i in range(len(self.cal_target_points)):
                if i == 4: continue
                for j in range(i+1, len(self.cal_target_points)):
                    pixel1 = np.array(self.cal_target_points[i])
                    pixel2 = np.array(self.cal_target_points[j])
                    real1 = np.array(self.cal_real_target[i])
                    real2 = np.array(self.cal_real_target[j])
                    if real1[0] == real2[0] or real1[1] == real2[1]: continue
                    tmp += abs(pixel1 - pixel2) / abs(real1 - real2)
                    tmp2 += 1

            avg_pixel_per_mm = (tmp / tmp2).tolist()
            coordinate_center = np.array([self.cal_target_points[0][0] - self.cal_real_target[0][0]*avg_pixel_per_mm[0], 
                                        self.cal_target_points[0][1] - self.cal_real_target[0][1]*avg_pixel_per_mm[1]])

            self.cal_dest_points = []
            for i in range(len(self.cal_real_target)):
                point = self.cal_real_target[i]
                self.cal_dest_points.append([round(coordinate_center[0] + point[0]*avg_pixel_per_mm[0]), 
                                            round(coordinate_center[1] + point[1]*avg_pixel_per_mm[1])])
                #([round(half_width + point[0] * avg_pixel_per_mm[0]), round(half_height - point[1] * avg_pixel_per_mm[1])])

            tmp = np.array([0.0, 0.0])
            tmp2 = 0
            for i in range(len(self.cal_dest_points)):
                if i == 4: continue
                for j in range(i+1, len(self.cal_dest_points)):
                    pixel1 = np.array(self.cal_dest_points[i])
                    pixel2 = np.array(self.cal_dest_points[j])
                    real1 = np.array(self.cal_real_target[i])
                    real2 = np.array(self.cal_real_target[j])
                    if real1[0] == real2[0] or real1[1] == real2[1]: continue
                    tmp += abs(pixel1 - pixel2) / abs(real1 - real2)
                    tmp2 += 1

            self.para.pixel_per_mm = (tmp / tmp2).tolist()
            self.para.coordinate_center = coordinate_center
            self.para.transform_matrix = cv2.getPerspectiveTransform(np.float32(self.cal_target_points), np.float32(self.cal_dest_points))

            image = self.calibration_image

            self.transformed_image = cv2.warpPerspective(image, self.para.transform_matrix, (image.shape[1], image.shape[0]))
            self.para.calibrated = True
        except:
            self.para.calibarated = False

        self.draw_calibration_image(self.transformed_image, False)
        self.para.cal_target_points['Point1'] = [self.cal_target_points[0], self.cal_real_target[0]]
        self.para.cal_target_points['Point2'] = [self.cal_target_points[1], self.cal_real_target[1]]
        self.para.cal_target_points['Point3'] = [self.cal_target_points[2], self.cal_real_target[2]]
        self.para.cal_target_points['Point4'] = [self.cal_target_points[3], self.cal_real_target[3]]
        self.para.cal_dest_points['Point1'] = [self.cal_dest_points[0], self.cal_real_target[0]]
        self.para.cal_dest_points['Point2'] = [self.cal_dest_points[1], self.cal_real_target[1]]
        self.para.cal_dest_points['Point3'] = [self.cal_dest_points[2], self.cal_real_target[2]]
        self.para.cal_dest_points['Point4'] = [self.cal_dest_points[3], self.cal_real_target[3]]

    def update_p_coord(self, point):
        idx = len(self.cal_reduced_target)
        if idx == 1:
            self.linePixel1x.setText(str(point[0]))
            self.linePixel1y.setText(str(point[1]))
        elif idx == 2:
            self.linePixel2x.setText(str(point[0]))
            self.linePixel2y.setText(str(point[1]))
        elif idx == 3:
            self.linePixel3x.setText(str(point[0]))
            self.linePixel3y.setText(str(point[1]))
        elif idx == 4:
            self.linePixel4x.setText(str(point[0]))
            self.linePixel4y.setText(str(point[1]))
        else:
            return
        
    def draw_circle(self):
        if self.labelOrigin.ctrdclick: return

        point = [int(self.labelOrigin.x*self.ratio_width), int(self.labelOrigin.y*self.ratio_height)]

        self.labelPosition.setText(f"Position: {self.labelOrigin.x}, {self.labelOrigin.y} ({point[0]}, {point[1]})")
        if self.labelOrigin.left:
            if len(self.cal_reduced_target) == 4: return
            self.cal_reduced_target.append([self.labelOrigin.x, self.labelOrigin.y])
            self.update_p_coord(point)
        else:
            x,y = 999, 999
            radius = 40
            for point in self.cal_reduced_target:
                distance = math.sqrt(pow((point[0] - self.labelOrigin.x),2) + pow((point[1] - self.labelOrigin.y), 2))
                if distance < radius:
                    x = point[0]
                    y = point[1]

            if x != 999 and y != 999:
                #self.update_p_coord(point, remove=True)
                self.cal_reduced_target.remove(point)

        self.draw_calibration_image(self.calibration_image)

    def move_circle(self, key):
        if len(self.cal_reduced_target) < 1: return

        x, y = self.cal_reduced_target[-1][0], self.cal_reduced_target[-1][1]

        if key == Qt.Key_Right:
            x = x + 1
        elif key == Qt.Key_Left:
            x = x - 1
        elif key == Qt.Key_Up:
            y = y - 1
        elif key == Qt.Key_Down:
            y = y + 1

        self.cal_reduced_target.pop(-1)
        self.cal_reduced_target.append([x, y])

        point = [int(self.cal_reduced_target[-1][0]*self.ratio_width), int(self.cal_reduced_target[-1][1]*self.ratio_height)]

        self.labelPosition.setText(f"Position: {self.cal_reduced_target[-1][0]}, {self.cal_reduced_target[-1][1]} ({point[0]}, {point[1]})")
        self.draw_calibration_image(self.calibration_image)