import requests
import cv2
import numpy as np
import imutils

class Camera():
    def __init__(self):
        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None
        self.repeat = None

        self.url = "http://192.168.3.25:8080/shot.jpg"

        while True:
            #img_resp = requests.get(url)
            img_resp = cv2.VideoCapture(self.url)
            res, img = img_resp.read()
            #img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            #img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1000)
            cv2.imshow("Android_cam", img)

            if cv2.waitKey(1) == 27:
                break
        cv2.destroyAllWindows()

cam = Camera()