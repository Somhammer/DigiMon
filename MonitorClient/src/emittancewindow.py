import os, sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.ui_emittancewindow import Ui_EmittanceWindow

class EmittanceWindow(QDialog, Ui_EmittanceWindow):
    def __init__(self):
        super(EmittanceWindow, self).__init__()
        self.setupUi(self)
        self.set_action()
        self.show()
    
    def set_action(self):
        pass