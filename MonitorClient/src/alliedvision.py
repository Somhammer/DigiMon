import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from vimba import *

from variables import *

class Camera():
    def __init__(self):
        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None
        self.repeat = None
        
    def try_connection(self):
        with Vimba.get_instance() as vimba:
            cams = vimba.get_all_cameras()
            if len(cams) < 1:
                return "There is no connected camera", False
            elif len(cams) == 1:
                return "1 camera is connected", True
            else:
                return f"{len(cams)} cameras are connected", False

    def control_camera(self, idx, value):
        if self.idx == CAMERA_GAIN:
            self.camera.Gain = value
            self.gain = int(self.value)
        elif self.idx == CAMERA_FPS:
            self.frame = float(self.value / 60)
        elif self.idx == CAMERA_EXPOSURE_TIME:
            self.exposure_time = float(self.value)
        elif self.idx == CAMERA_REPEAT:
            self.repeat = self.value
    
    def take_a_picture(self):
        #with self.camera as vimba:
        with Vimba().get_instance().get_all_cameras()[0] as vimba:
            cams = vimba.get_all_cameras()
            with cams[0] as cam:
                for frame in cam.get_frame_generator(limit=10):
                    frame.convert_pixel_format(PixelFormat.Mono8)
                    
                    
    
    def update_screen(self):
        self.camera.start_streaming(frame)

camera = Camera()