import os, sys
import platform
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from variables import *
from blackberry import *
from mainwindow import *

if __name__ == '__main__':
    #app = pg.mkQApp()
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())