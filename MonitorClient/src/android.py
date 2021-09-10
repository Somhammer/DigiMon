import cv2
import numpy as np

class Camera():
    def __init__(self):
        self.camera = None
        self.connected = False

        self.url = None

        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None

    # Camera controling
    def set_parameter(self, idx, value):
        return
        # 제대로 카메라 연결 시킬려면 앱을 만들어서 설치하게 해야는데 앱까지 만들 시간은 없음 ㅋ
        # OpenCV exposure time: 2^(exposure_time_value)
        # exposure_time_value range: 0 ~ -13
        self.exposure_time = float(value)
        if self.exposure_time >= 1000: value = 0
        elif self.exposure_time < 1000 and self.exposure_time >= 500: value = -1
        elif self.exposure_time < 500 and self.exposure_time >= 250: value = -2
        elif self.exposure_time < 250 and self.exposure_time >= 125: value = -3
        elif self.exposure_time < 125 and self.exposure_time >= 62.5: value = -4
        elif self.exposure_time < 62.5 and self.exposure_time >= 31.3: value = -5
        elif self.exposure_time < 31.3 and self.exposure_time >= 15.6: value = -6
        elif self.exposure_time < 15.6 and self.exposure_time >= 7.8: value = -7
        elif self.exposure_time < 7.8 and self.exposure_time >= 3.9: value = -8
        elif self.exposure_time < 3.9 and self.exposure_time >= 2: value = -9
        elif self.exposure_time < 2 and self.exposure_time >= 0.9766: value = -10
        self.camera.set(cv2.CAP_PROP_EXPOSURE, value)
        #return "Android IP webcam does not support well changing gain, exposure time"

    def connect_camera(self, url):
        self.url = url
        try:
            img_resp = cv2.VideoCapture(self.url)
            print("L1")
            if not img_resp.isOpened():
                msg = "Connected camera won't be opened"
                self.connected = False
            else:
                msg = 'Connection successful'
                self.connected = True
        except:
            msg = 'Connection is failed'
            self.connected = False

        print(msg)
        return msg, self.connected

    def take_a_picture(self):
        if not self.connected: return
        img_resp = cv2.VideoCapture(self.url)
        retval, image = img_resp.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image