import os, sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.ui_calibrationwindow import Ui_CalibrationWindow

class CalibrationWindow(QDialog, Ui_CalibrationWindow):
    def __init__(self):
        super(CalibrationWindow, self).__init__()
        self.setupUi(self)
        self.set_action()
        self.show()
    
    def set_action(self):
        self.buttonBox.accepted.connect(self.click_ok)
        self.buttonBox.rejected.connect(self.click_cancel)

    def click_ok(self):
        self.__password = self.lineEdit.text()
        self.accept()

    def click_cancel(self):
        self.reject()
    
    def return_para(self):
        return super().exec_()