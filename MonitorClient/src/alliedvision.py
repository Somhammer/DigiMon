from PySide6.QtCore import *

from vimba import *

from src.camera import Camera

class Camera():
    def __init__(self):
        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None
        
    # Camera controling
    def set_parameter(self):
        print("MELONA")

    def connect_camera(self):
        with Vimba.get_instance() as vimba:
            cams = vimba.get_all_cameras()
            if len(cams) < 1:
                self.connected = False
            else:
                self.connected = False
        return self.connected

    def take_a_picture(self):
        with Vimba.get_instance() as vimba:
            cams = vimba.get_all_cameras()
            with cams[0] as cam:
                frame = cam.get_frame()
                frame.convert_pixel_format(PixelFormat.Mono8)
                image = frame.as_opencv_image()
        return image