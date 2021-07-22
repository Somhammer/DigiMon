import os, sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.ui_hiddenwindow import Ui_HiddenWindow

class HiddenWindow(QDialog, Ui_HiddenWindow):
    def __init__(self):
        super(HiddenWindow, self).__init__()
        self.__password = None
        self.setupUi(self)
        self.set_action()
        self.show()

    @property
    def password(self):
        return self.__password

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