import requests
import time
import cv2
import numpy as np
import imutils

from src.variables import *

class Camera():
    def __init__(self):
        super().__init__()

        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None

        self.url = None

    # Camera controling
    def set_parameter(self):
        print("MELONA")

    def connect_camera(self, url):
        self.url = url
        self.connected = True
        return self.connected
        try:
            image = cv2.VideoCapture(self.url)
            if not image.isOpened():
                self.connected = False
            else:
                self.connected = False
        except:
            self.connected = False

        return self.connected

    def take_a_picture(self):
        image = cv2.imread("/home/seohyeon/work/BeamMonitor/SCFC/data/raw_data/500ms_6db.bmp")
        return image

        img_resp = cv2.VideoCapture(self.url)
        retval, image = img_resp.read()
        return image