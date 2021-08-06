import os, sys
import time
import datetime
import logging
import numpy as np
from scipy.optimize import curve_fit

# 카메라가 특별한 툴킷을 제공한다면 그것으로 바꿀 예정임. 지금은 테스트를 위해 opencv를 이용함
import cv2
import requests
import imutils

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import *

import pyqtgraph as pg

from src.logger import LogStringHandler
from src.variables import *

class Blueberry(QThread):
    thread_signal = Signal(str, list)
    thread_logger_signal = Signal(str, str)
    screen_signal = Signal(int, QPixmap)
    graph_signal = Signal(int, list, list)

    #chart_signal = Signal(QChart)
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.connected = False
        self.name = "Network Camera"

        self.url = "http://192.168.3.25:8080/shot.jpg"

        self.image = None
        self.last_picture = None
        
        self.picture_width = None
        self.picture_height = None

        self.profile_width = None
        self.profile_height = None

        self.xsize_width = None
        self.xsize_height = None

        self.ysize_width = None
        self.ysize_height = None

        self.working = True

        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None
        self.repeat = None

        self.previous = 1
        self.set_action()

    def initialize(self):
        self.outdir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        if not os.path.exists(os.path.join(self.outdir, 'image')):
            os.makedirs(os.path.join(self.outdir, 'image'))
        if not os.path.exists(os.path.join(self.outdir, 'profile')):
            os.makedirs(os.path.join(self.outdir, 'profile'))
        if not os.path.exists(os.path.join(self.outdir, 'emittance')):
            os.makedirs(os.path.join(self.outdir, 'emittance'))
        try:
            self.camera = cv2.VideoCapture(self.url)
            retval, frame = self.camera.read()
            if not retval:
                self.connected = False
            else:
                self.connected = True
        except:
            self.connected = False
        finally:
            if not self.connected:
                self.thread_logger_signal.emit('ERROR', str("There is no connected camera"))

    def set_action(self):
        self.thread_logger_signal.connect(self.parent.receive_log)
        self.screen_signal.connect(self.parent.update_screen)
        self.graph_signal.connect(self.parent.update_screen)

    def run(self):
        while self.working:

            if self.idx == CAMERA_EXIT:
                break
            elif self.idx == CAMERA_CAPTURE:
                self.take_pictures()
            
            self.show_screen()
        
    def stop(self):
        self.working = False
        self.sleep(1)
        self.quit()

    @Slot(int, int)
    def receive_signal(self, idx, value):
        self.idx = idx
        # OpenCV can not control IP webcam's parameters...
        ### Camera Control
        if self.idx == CAMERA_GAIN:
            self.gain = int(value)
            self.camera.set(cv2.CAP_PROP_GAIN, self.gain)
        elif self.idx == CAMERA_FPS:
            self.frame = int(value)
            self.camera.set(cv2.CAP_PROP_FPS, self.frame)
        elif self.idx == CAMERA_EXPOSURE_TIME:
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
        elif self.idx == CAMERA_REPEAT:
            self.repeat = value
        ### Filter Settiing
        else:
            self.filter_code = idx

    def take_pictures(self):
        if not self.connected: return
        for i in range(1, self.repeat+1):
            if not self.working: break
            if self.idx == CAMERA_STOP:
                self.thread_logger_signal.emit('INFO', str("Stop taking picgures"))
                break
            self.last_picture = self.image
            self.show_screen()
            self.analyze_picture()
            outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H:%M:%S.%f')}.png")
            cv2.imwrite(outname, self.image)
            self.thread_logger_signal.emit('INFO', str(f"Take a picture {i} - Saved as {outname}"))
            #key = cv2.waitKey(self.frame)
            self.sleep(self.exposure_time * 0.001)
        self.idx = CAMERA_SHOW

    def show_screen(self):
        if not self.connected: return
        if not self.working: return

        self.camera = cv2.VideoCapture(self.url)
        self.camera.set(3,self.picture_width)
        self.camera.set(4,self.picture_height)
        retval, self.image = self.camera.read()
        image = imutils.resize(self.image, width=self.picture_width, height=self.picture_height)

        height, width, channel = image.shape
        qImg = QImage(image.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        self.screen_signal.emit(PICTURE_SCREEN, pixmap)

    def analyze_picture(self, image=None, filter=None):
        if image is None:
            image = self.last_picture
        else:
            image = image
        height, width, channel = image.shape
        # 좌표: 좌상, 좌하, 우상, 우하
        original_points = np.float32([[0,0],[0,height],[width,0],[width,height]])
        destination_points = np.float32([[0,0],[0,height],[width,0],[width,height]])
        transform_matrix = cv2.getPerspectiveTransform(original_points, destination_points)
        transformed_image = cv2.warpPerspective(image, transform_matrix, (height, width))
        
        bightness = []
        #self.screen_signal.emit(var.DRAW_PROFILE, pixmap)
        # 사진에서 pixel profile로 이미지 바꾸는 코드 만들어야 함!

        # Generate Test Image...
        transformed_image = np.random.normal(size=(200,200))
        transformed_image[40:80, 40:120] += 4
        transformed_image = pg.gaussianFilter(transformed_image, (15,15))
        transformed_image += np.random.normal(size=(200,200)) * 0.1
        #data = data.astype(np.uint8)
        if self.filter_code == GAUSSIAN_FILTER:
            ksize = self.filter_para['ksize']
            sigmaX = self.filter_para['sigmaX']
            filtered_image = cv2.GaussianBlur(transformed_image, ksize=ksize, sigmaX=sigmaX)
        elif self.filter_code == MEDIAN_FILTER:
            ksize = self.filter_para['ksize']
            filtered_image = cv2.medianBlur(transformed_image, ksize=ksize)
        elif self.filter_code == BILATERAL_FILTER:
            ksize = self.filter_para['ksize']
            scolor = self.filter_para['scolor']
            sspace = self.filter_para['sspace']
            filtered_image = cv2.bilateralFilter(transformed_image, d=ksize, sigmaColor=scolor, sigmaSpace=sspace)
        else:
            filtered_image = transformed_image

        nxpixel, nypixel = filtered_image.shape
        
        xbin_for_filling = [i for i in range(nxpixel)] * nypixel
        ybin_for_filling = [i for i in range(nypixel)] * nxpixel
        pixel_brightness = filtered_image.flatten()

        xhist, xbin = np.histogram(xbin_for_filling, bins=nxpixel, weights=pixel_brightness)
        yhist, ybin = np.histogram(ybin_for_filling, bins=nypixel, weights=pixel_brightness)
        xhist_percent = np.asarray(xhist)/max(xhist) * 100
        yhist_percent = np.asarray(yhist)/max(yhist) * 100

        xbin = np.delete(xbin, -1)
        ybin = np.delete(ybin, -1)

        def func(x, a, b, c):
            return a*np.exp(-(x-b)**2/2*c**2)

        xfitpara, xfitconv = curve_fit(func, xbin, xhist_percent)
        xfit = func(xbin, *xfitpara)
        yfitpara, yfitconv = curve_fit(func, ybin, yhist_percent)
        yfit = func(ybin, *yfitpara)

        self.graph_signal.emit(PROFILE_SCREEN, filtered_image.tolist(), transformed_image.tolist())
        self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), list(zip(xbin, xfit)))
        self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), list(zip(ybin, yfit)))

    @Slot(int, int, int)
    def resize_image(self, target, width, height):
        if target == PICTURE_SCREEN:
            self.picture_width = width
            self.picture_height = height
        elif target == PROFILE_SCREEN:
            self.profile_width = width
            self.profile_height = height
        elif target == XSIZE_SCREEN:
            self.xsize_width = width
            self.xsize_height = height
        elif target == YSIZE_SCREEN:
            self.ysize_width = width
            self.ysize_height = height


