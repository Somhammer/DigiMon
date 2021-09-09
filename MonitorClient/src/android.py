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
        # 제대로 카메라 연결 시킬려면 앱을 만들어서 설치하게 해야는데 앱까지 만들 시간은 없음 ㅋ
        pass
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