# -------------------------------------------------------
# DigiMon
# Author: Seohyeon An
# Date: 2022-04-21
#
# This file is the main function.
# -------------------------------------------------------

# coding: UTF-8
from queue import Queue
from threading import Thread
import multiprocessing
import os, sys
from multiprocessing import Process, Queue, Lock

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from variables import BASE_PATH
sys.path.append(BASE_PATH)

#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

from mainwindow import *
from image_queue import stream_image, analyze_image
from variables import Parameters

mutex = Lock()
para = Parameters()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    #app = pg.mkQApp()
    stream_input_queue = Queue()
    # Queue for Image Stream
    # Element: Image array
    analysis_input_queue = Queue()
    # Queue for analyze
    # Element type: List
    # Element[0] = Image array
    # Element[1] = Intensity line [x, y]
    # Element[2] = Pixel size per millimeter [x, y]
    # Element[3] = Original pixel size [x, y]
    # Element[4] = Pixel size in screen [x, y]
    # Element[5] = Captured image(True) or Streaming image(False)
    stream_output_queue = Queue()
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
    analysis_output_queue = Queue()

    app = QApplication(sys.argv)
    w = MainWindow(para, stream_input_queue, analysis_input_queue, stream_output_queue, analysis_output_queue)

    #Thread(target=stream_image, args=(stream_input_queue, stream_output_queue), daemon=True).start()
    #Thread(target=analyze_image, args=(analysis_input_queue, analysis_output_queue), daemon=True).start()

    stream = Process(target=stream_image, args=(stream_input_queue, stream_output_queue), daemon=True)
    stream.start()
    analyze = Process(target=analyze_image, args=(analysis_input_queue, analysis_output_queue), daemon=True)
    analyze.start()

    if app.exec() == 0:
        stream_input_queue.put(['EXIT'])
        analysis_input_queue.put(['EXIT'])
        import time
        time.sleep(3)

        stream.join()
        """
        while not stream_input_queue.empty():
            stream_input_queue.get()
        while not analysis_input_queue.empty():
            analysis_input_queue.get()
        while not stream_output_queue.empty():
            stream_output_queue.get()
        while not analysis_output_queue.empty():
            analysis_output_queue.get()
        """
    sys.exit(0)
    #sys.exit(app.exec())
