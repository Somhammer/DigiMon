import os, sys
import time
import datetime
import logging
import numpy as np
from scipy.optimize import curve_fit

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
    screen_signal = Signal(int, QPixmap)
    graph_signal = Signal(int, list, list)
    save_signal = Signal(str)

    #chart_signal = Signal(QChart)
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.connected = False
        self.name = "Network Camera"

        self.url = "http://192.168.3.25:8080/shot.jpg"

        self.image = None
        self.last_picture = None

        self.filter_code = None
        self.filter_para = {}

        self.do_transformation = False
        self.destination_points = np.float32([[0,0],[0,800],[800,0],[800,800]]) # 이미지 크기는 나중에 바꿀 수 있음...?
        self.mm_per_pixel = [1.0, 1.0]

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
        """
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
        """
        self.connected = True

    def set_action(self):
        self.thread_logger_signal.connect(self.parent.receive_log)
        self.screen_signal.connect(self.parent.update_screen)
        self.graph_signal.connect(self.parent.update_screen)
        self.save_signal.connect(self.parent.save_image)

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
            #self.camera.set(cv2.CAP_PROP_GAIN, self.gain)
        elif self.idx == CAMERA_FPS:
            self.frame = int(value)
            #self.camera.set(cv2.CAP_PROP_FPS, self.frame)
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
            #self.camera.set(cv2.CAP_PROP_EXPOSURE, value)
        elif self.idx == CAMERA_REPEAT:
            self.repeat = value
    
    @Slot(str)
    def redraw_signal(self, image):
        self.analyze_picture(image)

    def take_pictures(self):
        if not self.connected: return
        self.last_picture = self.image
        outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H:%M:%S.%f')}.png")
        self.save_signal.emit(outname)
        self.analyze_picture()
        self.idx = CAMERA_SHOW

        return
        for i in range(1, self.repeat+1):
            if not self.working: break
            if self.idx == CAMERA_STOP:
                self.thread_logger_signal.emit('INFO', str("Stop taking picgures"))
                break
            self.last_picture = self.image
            self.show_screen()
            outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H:%M:%S.%f')}.png")
            self.save_signal.emit(outname)
            cv2.imwrite(outname, self.image)
            self.analyze_picture()
            self.thread_logger_signal.emit('INFO', str(f"Take a picture {i} - Saved as {outname}"))
            #key = cv2.waitKey(self.frame)
            self.sleep(self.exposure_time * 0.001)
        self.idx = CAMERA_SHOW

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
            destination_points = [(0,0),(0,height),(width,0),(width,height)]
            transform_matrix = cv2.getPerspectiveTransform(np.float32(self.transform_points), np.float32(destination_points))

            # 단순 perspective transformation은 왜곡이 발생함. -> 실험으로 확인
            #destination_points = [(0,0), ()]
            transformed_image = cv2.warpPerspective(image, transform_matrix, (int(width), int(height)))
        else:
            transformed_image = image
        
        return transformed_image

    def show_screen(self):
        if not self.connected: return
        if not self.working: return

        """
        self.camera = cv2.VideoCapture(self.url)
        self.camera.set(3,self.picture_width)
        self.camera.set(4,self.picture_height)
        retval, self.image = self.camera.read()
        """

        self.image = cv2.imread("/home/seohyeon/work/BeamMonitor/SCFC/data/raw_data/500ms_6db.bmp")
        image = self.filter_image(self.image)

        height, width, channel = image.shape
        qImg = QImage(image.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        self.screen_signal.emit(PICTURE_SCREEN, pixmap)

    def analyze_picture(self, image=None):
        if image is None:
            image = self.last_picture
        elif str(type(image)) == "<class 'str'>":
            image = cv2.imroad(image)
        else:
            image = image
        image = self.filter_image(image)
        height, width, channel = image.shape
        # 좌표: 좌상, 좌하, 우상, 우하
        #destination_points = np.float32([[0,0],[0,800],[800,0],[800,800]]) # 이미지 크기는 나중에 바꿀 수 있음...?
        #transform_matrix = cv2.getPerspectiveTransform(np.float32(self.transform_points), destination_points)
        #transformed_image = cv2.warpPerspective(image, transform_matrix, (800, 800))

        transformed_image = self.transform_image(image)
        
        transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)

        nxpixel, nypixel = transformed_image.shape
        print(self.mm_per_pixel)
        xbin = [0 - float(i) * self.mm_per_pixel[0] for i in range(int(nxpixel/2))] + [0 + float(i) * self.mm_per_pixel[0] for i in range(int(nxpixel/2))]
        xbin.sort()
        ybin = [0 - float(i) * self.mm_per_pixel[1] for i in range(int(nypixel/2))] + [0 + float(i) * self.mm_per_pixel[1] for i in range(int(nypixel/2))]
        ybin.sort()

        #xbin_for_filling = []
        #for j in range(nypixel):
        #    xbin_for_filling += [-20 + float(j) * self.pixel_to_mm for i in range(nxpixel)]
        #ybin_for_filling = [-20 + float(i) * self.pixel_to_mm for i in range(nypixel)] * nxpixel
        #pixel_brightness = transformed_image.flatten()

        #hist2d, xbin, ybin = np.histogram2d(xbin_for_filling, ybin_for_filling, bins=[nxpixel, nypixel], weights=pixel_brightness)
        #hist2d = hist2d.T
        # Numpy histogram 으로 1d histogram 만들면 filling이 이상하게 됨... 왜지?
        #xhist, xbin = np.histogram(xbin_for_filling, bins=nxpixel, weights=pixel_brightness)
        #yhist, ybin = np.histogram(ybin_for_filling, bins=nypixel, weights=pixel_brightness)
        #xhist_percent = np.asarray(xhist)/max(xhist) * 100
        #yhist_percent = np.asarray(yhist)/max(yhist) * 100

        xhist = [0 for i in range(nxpixel)]
        yhist = [0 for i in range(nypixel)]
        for xidx, irow in enumerate(transformed_image):
            for yidx, val in enumerate(irow):
                xhist[xidx] += val
                yhist[yidx] += val

        gauss = lambda x, a, b, c: a*np.exp(-(x-b)**2/2*c**2)
        xhist_percent = np.asarray(xhist)/max(xhist) * 100
        yhist_percent = np.asarray(yhist)/max(yhist) * 100
        
        try:
            xfitpara, xfitconv = curve_fit(gauss, xbin, xhist_percent)
            xfit = gauss(xbin, *xfitpara)
            xfitline = list(zip(xbin, xfit))
        except:
            xfitline = None
        try:
            yfitpara, yfitconv = curve_fit(gauss, ybin, yhist_percent)
            yfit = gauss(ybin, *yfitpara)
            yfitline = list(zip(ybin, yfit))
        except:
            yfitline = None
        
        xmax, ymax = np.argmax(xhist), np.argmax(yhist)
        xlength = len(np.where(xhist_percent > 32)[0]) * self.mm_per_pixel[0]
        ylength = len(np.where(yhist_percent > 32)[0]) * self.mm_per_pixel[1]
        
        self.graph_signal.emit(PROFILE_SCREEN, transformed_image, [xbin[xmax], ybin[ymax], xlength, ylength])
        self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
        self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)

