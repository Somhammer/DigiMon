import os, sys
from multiprocessing import Process, Queue

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from mainwindow import *
from utilities import analyze_image

if __name__ == '__main__':
    #app = pg.mkQApp()
    queue_for_analyze = Queue()
    # Queue for analyze
    # Element type: List
    # Element[0] = Image array
    # Element[1] = Intensity line [x, y]
    # Element[2] = Pixel size per millimeter [x, y]
    # Element[3] = Original pixel size [x, y]
    # Element[4] = Pixel size in screen [x, y]
    # Element[5] = Captured image(True) or Streaming image(False)
    return_queue = Queue()
    # Intensity histogram queue
    # Element type: List
    # If input image is captured image:
    # Element length = 8
    # If input image is streaming image:
    # Element length = 6
    # Common variable in queue element list
    # Element[0, 1] = x, y axis projected intensity histogram
    # Element[2, 3] = x, y axis projected intensity percent histogram
    # Element[4, 5] = Maximum intensity bin location and beam size for each axis
    # Variable for captured image
    # Element[6, 7] = Fitting curve for each axis

    app = QApplication(sys.argv)
    w = MainWindow(queue_for_analyze, return_queue)
    proc = Process(target=analyze_image, args=(queue_for_analyze, return_queue), daemon=True)
    proc.start()

    sys.exit(app.exec())