import os, sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import numpy as np
import cv2

from src.variables import *
from src.ui_filterwindow import Ui_FilterWindow

class FilterWindow(QDialog, Ui_FilterWindow):
    logger_signal = Signal(str, str)

    def __init__(self, parent, image):
        super(FilterWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)

        self.image = image
        image = cv2.resize(self.image, dsize=(300, 300), interpolation=cv2.INTER_LINEAR)
        height, width, channel = image.shape
        qImg = QImage(image.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)

        self.labelImage.resize(width, height)
        self.labelImage.setPixmap(pixmap)

        self.code = None
        self.parameters = None

        self.set_action()
        self.show()
    
    def set_action(self):
        self.logger_signal.connect(self.parent.receive_log)

        self.pushApply.clicked.connect(self.apply_filter)
        self.pushOk.clicked.connect(self.click_ok)
        self.pushCancel.clicked.connect(self.click_cancel)

        self.comboFilter.currentTextChanged.connect(self.load_parameters)

    def load_parameters(self):
        class Item(QWidget):
            def __init__(self):
                QWidget.__init__(self)
                self.layout = QBoxLayout(QBoxLayout.LeftToRight)

            def add_lineedit(self, name, makebtn=False):
                self.label = QLabel(name)
                self.linevalue = QLineEdit()
                self.layout.addWidget(self.label)
                self.layout.addWidget(self.linevalue)
                if makebtn:
                    def click_open(line):
                        fname = QFileDialog.getExistingDirectory(self, "Select Background Image File")
                        line.setText(fname)
                    self.pushbtn = QPushButton("Open")
                    self.pushbtn.clicked.connect(lambda: click_open(self.linevalue))
                    self.layout.addWidget(self.pushbtn)
                self.layout.setSizeConstraint(QBoxLayout.SetFixedSize)
                self.setLayout(self.layout)

        def set_value(name, value):
            if value == '': return
            if name == 'background file':
                value = str(value)
            else:
                value = int(value)
            self.parameters[name] = value

        if self.comboFilter.currentText() == 'Background Substraction':
            self.code = BKG_SUBSTRACTION
            self.parameters = {'background file':''}
        elif self.comboFilter.currentText() == 'Gaussian':
            self.code = GAUSSIAN_FILTER
            self.parameters = {'x kernal size':0, 'y kernal size':0, 'sigmaX':0}
        elif self.comboFilter.currentText() == 'Median':
            self.code = MEDIAN_FILTER
            self.parameters = {'kernal size':0}
        elif self.comboFilter.currentText() == 'Bilateral':
            self.code = BILATERAL_FILTER
            self.parameters = {'kernal size':0, 'sigma color':0, 'sigma space':0}
        else:
            return

        self.listParameters.clear()
        for name in self.parameters.keys():
            flag = False
            if name == 'background file': flag = True
            witem = QListWidgetItem(self.listParameters)
            item = Item()
            item.add_lineedit(name, makebtn=flag)
            item.linevalue.textChanged.connect(lambda: set_value(item.label.text(), item.linevalue.text()))
            item.linevalue.returnPressed.connect(lambda: set_value(item.label.text(), item.linevalue.text()))
            self.listParameters.setItemWidget(witem, item)
            self.listParameters.addItem(witem)
            witem.setSizeHint(item.sizeHint())

    def apply_filter(self):
        if self.code == BKG_SUBSTRACTION:
            background = cv2.imread(self.parameters['background file'])
            filtered_image = cv2.subtract(self.image, background)
        if self.code == GAUSSIAN_FILTER:
            ksize = (self.parameters['x kernal size'], self.parameters['y kernal size'])
            sigmaX = self.parameters['sigmaX']
            filtered_image = cv2.GaussianBlur(self.image, ksize=ksize, sigmaX=sigmaX)
        elif self.code == MEDIAN_FILTER:
            ksize = self.parameters['kernal size']
            filtered_image = cv2.medianBlur(self.image, ksize=ksize)
        elif self.code == BILATERAL_FILTER:
            ksize = self.parameters['kernal size']
            scolor = self.parameters['sigma color']
            sspace = self.parameters['sigma space']
            filtered_image = cv2.bilateralFilter(self.image, d=ksize, sigmaColor=scolor, sigmaSpace=sspace)
                
        image = cv2.resize(filtered_image, dsize=(300, 300), interpolation=cv2.INTER_LINEAR)
        height, width, channel = image.shape
        qImg = QImage(image.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)

        self.labelImage.resize(width, height)
        self.labelImage.setPixmap(pixmap)

    def closeEvent(self, event):
        self.click_cancel()

    def click_ok(self):
        self.logger_signal.emit('INFO', str(f"Apply {self.comboFilter.currentText()} Filter"))
        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()
        else:
            return
    
    def return_para(self):
        return super().exec_()