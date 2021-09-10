import os, sys
import time
import datetime
import logging
import numpy as np
from scipy.optimize import curve_fit
import copy


# 카메라가 특별한 툴킷을 제공한다면 그것으로 바꿀 예정임. 지금은 테스트를 위해 opencv를 이용함
import cv2

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import *

import pyqtgraph as pg

from src.logger import LogStringHandler
from src.variables import *

class Blueberry(QThread):
    thread_signal = Signal(str, list)
    thread_logger_signal = Signal(str, str)
    screen_signal = Signal(int, np.ndarray)
    graph_signal = Signal(int, list, list)
    save_signal = Signal(str)
    plot_signal = Signal(np.ndarray, list, list, np.ndarray, np.ndarray, list, list)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.connected = False
        self.name = "Network Camera"

        self.camera = None
        self.url = None

        self.image = None
        self.original_image = None
        self.last_picture = None

        self.filter_code = None
        self.filter_para = {}

        self.do_transformation = False
        self.destination_points = np.float32([[0,0],[0,800],[800,0],[800,800]]) # 이미지 크기는 나중에 바꿀 수 있음...?
        self.mm_per_pixel = [1.0, 1.0]

        self.original_pixel = None

        self.working = True

        self.idx = None
        self.frame = None

        self.gain = None
        self.exposure_time = None
        self.ROI = [[0,0], [0,0]]

        self.repeat = None
        self.rotation = 0
        self.flip_rl = 0
        self.flip_ud = 0
        
        self.thread_logger_signal.connect(self.parent.receive_log)
        self.screen_signal.connect(self.parent.update_screen)
        self.graph_signal.connect(self.parent.update_screen)
        self.save_signal.connect(self.parent.save_image)
        self.plot_signal.connect(self.parent.save_pretty_plot)

    def initialize(self, url):
        self.url = url

        self.outdir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        if not os.path.exists(os.path.join(self.outdir, 'image')):
            os.makedirs(os.path.join(self.outdir, 'image'))
        if not os.path.exists(os.path.join(self.outdir, 'profile')):
            os.makedirs(os.path.join(self.outdir, 'profile'))
        if not os.path.exists(os.path.join(self.outdir, 'emittance')):
            os.makedirs(os.path.join(self.outdir, 'emittance'))

        #self.sdk = 'Test'
        if "OpenCV" in self.sdk:
            from src.android import Camera
            self.camera = Camera()
        elif "Vimba" in self.sdk:
            from src.alliedvision import Camera
            self.camera = Camera()
        elif "Pylon" in self.sdk:
            from src.basler import Camera
            self.camera = Camera()
        else:
            from src.testcamera import Camera
            self.camera = Camera()

        self.msg, self.connected = self.camera.connect_camera(url)

    def run(self):
        while self.working:
            if not self.connected: continue
            self.camera.idx = self.idx
            if self.idx == CAMERA_EXIT:
                break
            elif self.idx == CAMERA_CAPTURE:
                self.take_pictures()
            self.show_screen()

    def stop(self):
        self.working = False
        self.sleep(1)
        self.quit()

    def rotate_image(self, image):
        if self.rotation == 90:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif self.rotation == 180:
            image = cv2.rotate(image, cv2.ROTATE_180)
        elif self.rotation == 270:
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        if self.flip_rl == 1:
            image = cv2.flip(image, 1)
        
        if self.flip_ud == 1:
            image = cv2.flip(image, 0)

        return image

    def filter_image(self, image):
        if self.filter_code == BKG_SUBSTRACTION:
            background = cv2.imread(self.filter_para['background file'])
            filtered_image = cv2.subtract(image, background)
        if self.filter_code == GAUSSIAN_FILTER:
            ksize = (self.filter_para['x kernal size'], self.filter_para['y kernal size'])
            sigmaX = self.filter_para['sigmaX']
            filtered_image = cv2.GaussianBlur(image, ksize=ksize, sigmaX=sigmaX)
        elif self.filter_code == MEDIAN_FILTER:
            ksize = self.filter_para['kernal size']
            filtered_image = cv2.medianBlur(image, ksize=ksize)
        elif self.filter_code == BILATERAL_FILTER:
            ksize = self.filter_para['kernal size']
            scolor = self.filter_para['sigma color']
            sspace = self.filter_para['sigma space']
            filtered_image = cv2.bilateralFilter(image, d=ksize, sigmaColor=scolor, sigmaSpace=sspace)
        else:
            filtered_image = image
        
        return filtered_image

    def transform_image(self, image):
        if self.do_transformation:
            width = self.destination_points[2][0] - self.destination_points[0][0]
            height = self.destination_points[1][1] - self.destination_points[0][1]
            #destination_points = [(0,0),(0,height),(width,0),(width,height)]
            transform_matrix = cv2.getPerspectiveTransform(np.float32(self.transform_points), np.float32(self.destination_points))

            # 단순 perspective transformation은 왜곡이 발생함. -> 실험으로 확인
            width, height = self.image.shape[1], self.image.shape[0]
            transformed_image = cv2.warpPerspective(image, transform_matrix, (width, height))
        else:
            transformed_image = image
        
        return transformed_image

    def slice_image(self, image):
        if self.ROI == [[0,0],[0,0]]: return image
        x, y, width, height = self.ROI[0][0], self.ROI[0][1], self.ROI[1][0], self.ROI[1][1]
        src = image.copy()
        image = src[y:y+height, x:x+width]
        height, width = image.shape
        image = cv2.resize(image, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
        return image

    def take_pictures(self):
        if not self.connected: return

        for i in range(1, self.repeat+1):
            if not self.working: break
            if self.idx == CAMERA_STOP:
                self.thread_logger_signal.emit('INFO', str("Stop taking picgures"))
                break
            self.image = self.camera.take_a_picture()

            self.image = self.rotate_image(self.image)
            self.image = self.filter_image(self.image)
            self.image = self.transform_image(self.image)
            self.image = self.slice_image(self.image)
            
            self.last_picture = self.image
            outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H:%M:%S.%f')}.png")
            cv2.imwrite(outname, self.last_picture)
            self.save_signal.emit(outname)
            transformed_image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline = self.analyze_picture(shot=True)
            xmax, ymax = np.argmax(xhist_percent), np.argmax(yhist_percent)
            xlength = len(np.where(xhist_percent > 32)[0]) * self.mm_per_pixel[0]
            ylength = len(np.where(yhist_percent > 32)[0]) * self.mm_per_pixel[1]  
        
            self.graph_signal.emit(PROFILE_SCREEN, transformed_image, [xbin[xmax], ybin[ymax], xlength, ylength])
            self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
            self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)
            self.plot_signal.emit(transformed_image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline)

            self.thread_logger_signal.emit('INFO', str(f"Take a picture {i} - Saved as {outname}"))
            #key = cv2.waitKey(self.frame)
            self.sleep(self.exposure_time * 0.001)
        self.idx = CAMERA_SHOW

    def show_screen(self):
        if not self.connected: return
        if not self.working: return

        self.image = self.camera.take_a_picture()

        # 아래 세 친구의 순서는 어떻게 할 것인가...
        self.image = self.rotate_image(self.image)
        self.image = self.filter_image(self.image)
        self.image = self.transform_image(self.image)
        self.image = self.slice_image(self.image)

        self.original_pixel = [self.image.shape[1], self.image.shape[0]]

        transformed_image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline = self.analyze_picture(self.image)
        xmax, ymax = np.argmax(xhist_percent), np.argmax(yhist_percent)
        xlength = len(np.where(xhist_percent > 32)[0]) * self.mm_per_pixel[0]
        ylength = len(np.where(yhist_percent > 32)[0]) * self.mm_per_pixel[1]

        self.screen_signal.emit(PICTURE_SCREEN, self.image)
        self.graph_signal.emit(LIVE_XPROFILE_SCREEN, list(zip(xbin, xhist_percent)), [xbin[xmax], xlength])
        self.graph_signal.emit(LIVE_YPROFILE_SCREEN, list(zip(ybin, yhist_percent)), [ybin[ymax], ylength])

        self.msleep(int((1.0/self.frame)*1000))
    
    def analyze_picture(self, image=None, shot=False):
        if image is None:
            image = self.last_picture
        else:
            image = image
    
        height, width = image.shape

        transformed_image = image
        if len(transformed_image.shape) == 3:
            transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)
        
        # PyqtGraph에서 90도 돌아져서 그림이 그려져서 돌림...
        #transformed_image = cv2.rotate(transformed_image, cv2.ROTATE_90_CLOCKWISE)

        nypixel, nxpixel = transformed_image.shape

        total_x = self.original_pixel[0] * self.mm_per_pixel[0]
        total_y = self.original_pixel[1] * self.mm_per_pixel[1]
        mm_per_pixel_x = total_x / nxpixel
        mm_per_pixel_y = total_y / nypixel
        self.xmin = -round(total_x / 2.0)
        self.ymin = -round(total_y / 2.0)
        xbin = [self.xmin + float(i) * mm_per_pixel_x for i in range(nxpixel)]
        ybin = [self.ymin + float(i) * mm_per_pixel_y for i in range(nypixel)]

        xhist = [0 for i in range(nxpixel)]
        yhist = [0 for i in range(nypixel)]
        for xidx in range(nxpixel):
            for yidx in range(nypixel):
                xhist[xidx] += transformed_image[yidx][xidx]
                yhist[yidx] += transformed_image[yidx][xidx]

        gauss = lambda x, a, b, c: a*np.exp(-(x-b)**2/2*c**2)
        xhist_percent = np.asarray(xhist)/max(xhist) * 100
        yhist_percent = np.asarray(yhist)/max(yhist) * 100
        if shot:
            try:
                xfitpara, xfitconv = curve_fit(gauss, xbin, xhist_percent)
                xfit = gauss(xbin, *xfitpara)
                xfitline = list(zip(xbin, xfit))
            except:
                xfitline = list(zip(xbin, [0 for i in range(len(xbin))]))
            try:
                yfitpara, yfitconv = curve_fit(gauss, ybin, yhist_percent)
                yfit = gauss(ybin, *yfitpara)
                yfitline = list(zip(ybin, yfit))
            except:
                yfitline = list(zip(xbin, [0 for i in range(len(ybin))]))
        else:
            xfitline = list(zip(xbin, [0 for i in range(len(xbin))]))
            yfitline = list(zip(ybin, [0 for i in range(len(ybin))]))

        xmax, ymax = np.argmax(xhist_percent), np.argmax(yhist_percent)
        xlength = len(np.where(xhist_percent > 32)[0]) * self.mm_per_pixel[0]
        ylength = len(np.where(yhist_percent > 32)[0]) * self.mm_per_pixel[1]  
        
        return transformed_image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline

    @Slot(int, list)
    def receive_signal_from_setup(self, idx, value):
        if idx == CONNECT_CAMERA:
            self.connect_camera()

    @Slot(int, int)
    def receive_signal(self, idx, value):
        self.idx = idx
        # OpenCV can not control IP webcam's parameters...
        ### Camera Control
        if self.idx == CAMERA_GAIN:
            if self.connected:
                self.camera.set_parameter(idx, value)
        elif self.idx == CAMERA_EXPOSURE_TIME:
            if self.connected:
                self.camera.set_parameter(idx, value)
            self.exposure_time = float(value)
        elif self.idx == CAMERA_FPS:
            self.frame = int(value)
        elif self.idx == CAMERA_REPEAT:
            self.repeat = value
        elif self.idx == CAMERA_ROTATION_RIGHT:
            self.rotation += 90
            self.rotation = self.rotation % 360
        elif self.idx == CAMERA_ROTATION_LEFT:
            self.rotation += 270
            self.rotation = self.rotation % 360
        elif self.idx == CAMERA_FLIP_UP_DOWN:
            self.flip_ud += 1
            self.flip_ud = self.flip_ud % 2
        elif self.idx == CAMERA_FLIP_RIGHT_LEFT:
            self.flip_rl += 1
            self.flip_rl = self.flip_rl % 2
    
    @Slot(str)
    def redraw_signal(self, name):
        image = cv2.imread(name)
        self.analyze_picture(image)