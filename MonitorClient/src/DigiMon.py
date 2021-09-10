import os, sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

BASE_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from src.variables import *
from src.blackberry import *
from src.mainwindow import *

if __name__ == '__main__':
    #os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = pg.mkQApp()
    #app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())