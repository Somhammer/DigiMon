import numpy as np

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
            img_resp = cv2.VideoCapture(self.url)
            if not img_resp.isOpened():
                self.connected = False
            else:
                self.connected = False
        except:
            self.connected = False

        return self.connected

    def take_a_picture(self):
        img_resp = cv2.VideoCapture(self.url)
        retval, image = img_resp.read()
        return image