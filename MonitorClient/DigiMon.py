# -------------------------------------------------------
# DigiMon
# Author: Seohyeon An
# Date: 2022-04-21
#
# This file is the main function.
# -------------------------------------------------------

# coding: UTF-8

import multiprocessing
import os, sys
from multiprocessing import Process, Queue, Lock

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

from mainwindow import *
from image_queue import stream_image, analyze_image
from variables import Parameters

mutex = Lock()
para = Parameters()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    #app = pg.mkQApp()
    stream_queue = Queue()
    # Queue for Image Stream
    # Element: Image array
    analysis_queue = Queue()
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
    # Element length = 9
    # If input image is streaming image:
    # Element length = 7
    # Common variable in queue element list
    # Element[0] = Image array
    # Element[1, 2] = x, y axis projected intensity histogram
    # Element[3, 4] = x, y axis projected intensity percent histogram
    # Element[5, 6] = Maximum intensity bin location and beam size for each axis
    # Variable for captured image
    # Element[7, 8] = Fitting curve for each axis

    app = QApplication(sys.argv)
    w = MainWindow(para, stream_queue, analysis_queue, return_queue)

    stream_proc = Process(target=stream_image, args=(stream_queue, return_queue), daemon=True)
    analysis_proc = Process(target=analyze_image, args=(analysis_queue, return_queue), daemon=True)
    stream_proc.start()
    analysis_proc.start()

    sys.exit(app.exec())