import logging

from PySide6.QtCore import *
from vimba import *

from src.logger import LogStringHandler
from src.variables import *

class Blueberry(QThread):
    thread_signal = Signal(str, list)
    thread_logger_signal = Signal(str, str)
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.connected = False
        self.name = "Network Camera"

        self.idx = None
        self.frame = None
        self.exposure_time = None

    def initialize(self):
        try:
            #self.camera = Vimba().get_instance().get_all_cameras()[0]
            self.connected = True
            ### Get Default values....
            self.frame = float(30 / 60)
            self.exposure_time = 500
        except:
            return
        
    def run(self):
        while True:
            if self.idx == CAMERA_EXIT:
                break
            elif self.idx == CAMERA_CAPTURE:
                self.take_pictures()
            elif self.idx == CAMERA_GAIN:
                self.change_parameter()
            elif self.idx == CAMERA_FPS:
                self.change_parameter()
            else:
                self.show_screen()
            self.sleep(self.frame)
        self.terminate()
        self.quit()

    @Slot(int, int)
    def receive_signal(self, idx, value):
        self.idx = idx
        self.value = value

    def take_pictures(self):
        for i in range(0, self.value):
            if self.idx == CAMERA_STOP:
                self.thread_logger_signal.emit('INFO', str("Stop taking picgures"))
                break
            self.thread_logger_signal.emit('INFO', str(f"Take a picture{i}"))
            self.sleep(self.exposure_time * 0.001)
        self.idx = CAMERA_SHOW

    def change_parameter(self):
        if self.idx == CAMERA_GAIN:
            return
        elif self.idx == CAMERA_FPS:
            self.frame = float(self.value / 60)

    def show_screen(self):
        return
        #self.thread_logger_signal.emit('INFO', str("Update screen"))
