# -------------------------------------------------------
# Strawberry
# Author: Seohyeon An
# Date: 2022-04-21
#
# This class handles captured images in return_queue.
#   Functions
#   1. It sends signals to mainwindow class for image showing.
#   2. It draws pretty plots and saves them.
#   3. When the user double-clicks a line of the profile table at the MainWindow, redraw the image to the plot panel.
# -------------------------------------------------------
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import *

class Strawberry(QThread):
    signal = Signal(list)
    def __init__(self, para, slot, return_queue):
        super().__init__()
        self.para = para
        self.return_queue = return_queue
        self.working = True

        self.signal.connect(slot)

    def run(self):
        while self.working:
            if not self.return_queue.empty():
                element = self.return_queue.get()
                self.signal.emit(element)

    def stop(self):
        self.working = False
        self.quit()
        self.wait(1000)