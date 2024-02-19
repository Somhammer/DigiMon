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
from ui_roiwindow import Ui_ROIWindow

class ROIWindow(QDialog, Ui_ROIWindow):
    def __init__(self, para, blueberry):
        super(ROIWindow, self).__init__()

        self.setupUi(self)

        self.para = para
        self.blueberry = blueberry

        self.captured_image = None
        self.captured_image_aratio = None
        self.screen_size = (300, 300)

        self.ratio_width = 1.0
        self.ratio_height = 1.0

        self.select_roi = False
        self.draw_square = False
        self.roi = [[0,0],[0,0]]
        self.resized_roi = [[0,0],[0,0]]

        #self.labelImage = DigiLabel(self.labelImage)
        #item = self.gridLayout.itemAt(0)
        #self.gridLayout.removeWidget(item.widget())
        #self.gridLayout.addWidget(self.labelImage, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.labelImage.resize(self.screen_size[0], self.screen_size[1])

        self.set_action()

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            self.sliderX0.setSingleStep(10)
            self.sliderY0.setSingleStep(10)
            self.sliderWidth.setSingleStep(10)
            self.sliderHeight.setSingleStep(10)
            self.labelImage.ctrdclick = True
        elif event.modifiers() & Qt.ShiftModifier:
            self.sliderX0.setSingleStep(100)
            self.sliderY0.setSingleStep(100)
            self.sliderWidth.setSingleStep(100)
            self.sliderHeight.setSingleStep(100)
            self.draw_square = True

    def keyReleaseEvent(self, event):
        self.labelImage.ctrdclick = False
        if any(event.key() == i for i in [Qt.Key_Control, Qt.Key_Shift]):
            self.sliderX0.setSingleStep(1)
            self.sliderY0.setSingleStep(1)
            self.sliderWidth.setSingleStep(1)
            self.sliderHeight.setSingleStep(1)
            self.draw_square = False

    def return_para(self):
        sender = self.sender()
        if sender == self.buttonBox:
            button = self.buttonBox.standardButton(sender.button(sender.clickedButton()))
            if button == QDialogButtonBox.Ok:
                self.accept()
            else:
                self.reject()
        return super().exec_()

    def set_action(self):
        self.labelImage.move.connect(self.set_roi)
        self.labelImage.ldclicked.connect(self.apply_roi)
        self.labelImage.rdclicked.connect(lambda: self.apply_roi(True))

        self.sliderX0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_X0))
        self.sliderY0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_Y0))
        self.sliderWidth.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_WIDTH))
        self.sliderHeight.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_HEIGHT))

    def set_photo_para(self, idx, value=None):
        if self.para.cam_conn and self.captured_image is not None:
            if idx == CAMERA_ROI_X0:
                if value is not None:
                    self.roi[0][0] = value
                    self.sliderX0.setValue(self.roi[0][0] * 1000.0 / self.captured_image.shape[1])
                else:
                    self.roi[0][0] = round(self.captured_image.shape[1] * self.sliderX0.value() / 1000.0)

                self.lineX0.setText(str(self.sliderX0.value()/10))
                self.labelSPPixel.setText(f"({self.roi[0][0]}, {self.roi[0][1]}) () pixel")
            elif idx == CAMERA_ROI_Y0:
                if value is not None:
                    self.roi[0][1] = value
                    self.roi[0][1] = round(value * self.ratio_height)
                    self.sliderY0.setValue(self.roi[0][1] * 1000.0 / self.captured_image.shape[0])
                else:
                    self.roi[0][1] = round(self.captured_image.shape[0] * self.sliderY0.value() / 1000.0)
                self.lineY0.setText(str(self.sliderY0.value()/10))
                self.labelSPPixel.setText(f"({self.roi[0][0]}, {self.roi[0][1]}) pixel")
            elif idx == CAMERA_ROI_WIDTH:
                if value is not None:
                    self.roi[1][0] = value
                    self.roi[1][0] = round(value * self.ratio_width)
                    self.sliderWidth.setValue(self.roi[1][0] * 1000.0 / self.captured_image.shape[1])
                else:
                    self.roi[1][0] = round(self.captured_image.shape[1] * self.sliderWidth.value() / 1000.0)
                self.lineWidth.setText(str(self.sliderWidth.value()/10))
                self.labelSizePixel.setText(f"({self.roi[1][0]}, {self.roi[1][1]}) pixel")
            elif idx == CAMERA_ROI_HEIGHT:
                if value is not None:
                    self.roi[1][1] = value
                    self.roi[1][1] = round(value * self.ratio_height)
                    self.sliderHeight.setValue(self.roi[1][1] * 1000.0 / self.captured_image.shape[0])
                else:
                    self.roi[1][1] = round(self.captured_image.shape[0] * self.sliderHeight.value() / 1000.0)
                self.lineHeight.setText(str(self.sliderHeight.value()/10))
                self.labelSizePixel.setText(f"({self.roi[1][0]}, {self.roi[1][1]}) pixel")

    def take_a_picture(self):
        if not self.para.cam_conn: return

        self.captured_image = self.blueberry.take_a_picture(True)
        if self.captured_image is None: return
        if self.captured_image_aratio is None:
            self.captured_image_aratio = float(self.captured_image.shape[1]) / float(self.captured_image.shape[0])

        if self.captured_image_aratio > 1:
            self.ratio_width = float(self.captured_image.shape[1] / self.screen_size[0])
            self.ratio_height = float(self.captured_image.shape[0] / (self.screen_size[0] / self.captured_image_aratio))
        elif self.captured_image_aratio < 1:
            self.ratio_width = float(self.captured_image.shape[1] / (self.screen_size[0] * self.captured_image_aratio))
            self.ratio_height = float(self.captured_image.shape[0] / self.screen_size[1])
        else:
            self.ratio_width = float(self.captured_image.shape[1] / self.screen_size[0])
            self.ratio_height = float(self.captured_image.shape[0] / self.screen_size[1])
        
        self.draw_roi_image()

    def draw_roi_image(self, apply=False):
        #if self.select_roi or self.captured_image is None: return
        if self.captured_image is None: return

        image_copy = copy.deepcopy(self.captured_image)

        if apply and self.roi != [[0,0],[0,0]] and self.roi != [[0,0], [self.captured_image.shape[1], self.captured_image.shape[0]]]:
            x, y, width, height = self.roi[0][0], self.roi[0][1], self.roi[1][0], self.roi[1][1]
            src = image_copy.copy()
            image_copy = src[self.roi[0][1]:self.roi[0][1]+self.roi[1][1], self.roi[0][0]:self.roi[0][0]+self.roi[1][0]]
            if len(image_copy) <= 0: return
    
        dsize = (self.screen_size[0], self.screen_size[1])

        resized_image = cv2.resize(image_copy, dsize=dsize, interpolation=cv2.INTER_LINEAR)

        if len(resized_image.shape) == 3:
            height, width, channel = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qImg)

        if not apply:
            painter = QPainter(pixmap)
            painter.setPen(QPen(QColor(3, 252, 127), 1.5, Qt.DashLine))

            x = self.resized_roi[0][0]
            y = self.resized_roi[0][1]
            width = self.resized_roi[1][0]
            height = self.resized_roi[1][1]

            painter.drawRect(x, y, width, height)
            painter.end()

        self.labelImage.setPixmap(pixmap)

    def set_roi(self):
        if not self.para.cam_conn or self.select_roi or not self.labelImage.left: return

        if self.labelImage.x < self.labelImage.x_end and self.labelImage.y < self.labelImage.y_end:
            x = self.labelImage.x
            y = self.labelImage.y
        elif self.labelImage.x > self.labelImage.x_end and self.labelImage.y < self.labelImage.y_end:
            x = self.labelImage.x_end
            y = self.labelImage.y
        elif self.labelImage.x > self.labelImage.x_end and self.labelImage.y > self.labelImage.y_end:
            x = self.labelImage.x_end
            y = self.labelImage.y_end
        else:
            x = self.labelImage.x
            y = self.labelImage.y_end
        width = abs(self.labelImage.x - self.labelImage.x_end)
        height = abs(self.labelImage.y - self.labelImage.y_end)

        if self.draw_square:
            height = width

        self.resized_roi = [[x,y],[width,height]]

        self.sliderX0.setValue((x / self.screen_size[0]) * 1000)
        self.sliderY0.setValue((y / self.screen_size[1]) * 1000)
        self.sliderWidth.setValue((width / self.screen_size[0]) * 1000)
        self.sliderHeight.setValue((height / self.screen_size[1]) * 1000)

        self.draw_roi_image()

    def apply_roi(self, reset=False):
        initial_roi = [[0,0],[0,0]]
        if reset:
            self.roi = initial_roi
            self.resized_roi = initial_roi

            self.sliderX0.setValue(0)
            self.sliderY0.setValue(0)
            self.sliderWidth.setValue(0)
            self.sliderHeight.setValue(0)

            self.select_roi = False
        else:
            if self.roi != initial_roi:
                self.select_roi = True

        self.draw_roi_image(self.select_roi)