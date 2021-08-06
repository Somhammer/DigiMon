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
        self.code = None
        self.parameters = {}

        self.set_action()
        self.show()
    
    def set_action(self):
        self.logger_signal.connect(self.parent.receive_log)

        self.buttonBox.accepted.connect(self.click_ok)
        self.buttonBox.rejected.connect(self.click_cancel)

        self.comboFilter.currentTextChanged.connect(self.load_parameters)

    def load_parameters(self):
        def add_widget(layout, name, push=False):
            print('1:', layout.rowCount(), layout.columnCount())
            label = QLabel(name)
            if not push:
                widget = QLineEdit('0')
            else:
                widget = QPushButton('Apply')
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            row = layout.rowCount()+1
            print('2:', layout.rowCount(), layout.columnCount())
            layout.addWidget(label, row, 0, 1, 1)
            print('3:', layout.rowCount(), layout.columnCount())
            layout.addWidget(widget, row, 1)
            print('4:', layout.rowCount(), layout.columnCount())

        if self.comboFilter.currentText() == 'Gaussian':
            self.code = GAUSSIAN_FILTER
            self.parameters = {'ksize':[0,0], 'sigmaX':0}

            gridParameters = QGridLayout()
            names = ['x kernal size', 'y kernal size', 'Sigma']
            for name in names:
                add_widget(gridParameters, name)
            add_widget(gridParameters, '', push=True)
            print(gridParameters.rowCount())
            #push = gridParameters.itemAtPosition(gridParameters.rowCount(), 1).widget()
            #push.clicked.connect(self.apply_filter)
            self.groupBox.setLayout(gridParameters)
            #layout = self.add_line(name='x kernal size')
            #self.gridParameters.addWidget(layout)
            #self.gridParameters.addWidget(self.add_line(name='y kernal size'))
            #self.gridParameters.addWidget(self.add_line(name='Sigma'))
            #self.gridParameters.addWidget(self.add_line(name='',push=True))
            
        elif self.comboFilter.currentText() == 'Median':
            self.code = MEDIAN_FILTER
            self.parameters = {'ksize':0}
        elif self.comboFilter.currentText() == 'Bilateral':
            self.code = BILATERAL_FILTER
            self.parameters = {'ksize':0, 'scolor':0, 'sspace':0}
        else:
            return

    def apply_filter(self):
        self.logger_signal.emit('INFO', str("Apply Filter"))

        print("Apply Filter")
        pass

    def click_ok(self):
        self.accept()

    def click_cancel(self):
        self.reject()
    
    def return_para(self):
        return super().exec_()