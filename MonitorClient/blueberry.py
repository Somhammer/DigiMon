import os, sys
import time
import datetime
import logging
import numpy as np
from scipy.optimize import curve_fit
import copy
import cv2

import_vimba = False
try:
    from vimba import *
    import_vimba = True
except ImportError:
    import_vimba = False

import_pylon = False
try:
    from pypylon import pylon
    import_pylon = True
except ImportError:
    import_pylon = False

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import *

import pyqtgraph as pg

from logger import LogStringHandler
from variables import *


class Blueberry(QThread):
    watch_signal = Signal(bool)
    thread_logger_signal = Signal(str, str)
    screen_signal = Signal(int, np.ndarray)
    graph_signal = Signal(int, list, list)
    save_signal = Signal(str)
    plot_signal = Signal(np.ndarray, list, list, np.ndarray, np.ndarray, list, list)

    def __init__(self, parent=None):
        super().__init__()
        self.name = "Network Camera"
        self.parent = parent

        self.set_action()
        self.initialize()

    def set_action(self):
        self.watch_signal.connect(self.parent.stopwatch)
        self.thread_logger_signal.connect(self.parent.receive_log)
        self.screen_signal.connect(self.parent.update_screen)
        self.graph_signal.connect(self.parent.update_screen)
        self.save_signal.connect(self.parent.save_image)
        self.plot_signal.connect(self.parent.save_pretty_plot)

    def initialize(self):
        self.connected = False

        self.camera = None
        self.url = None

        self.image = None
        self.original_image = None

        self.filter_code = None
        self.filter_para = {}

        self.rotate_angle = 0.0
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
        self.intensity_line = [-1,-1]

        self.repeat = None
        self.rotation = 0
        self.flip_rl = 0
        self.flip_ud = 0

        self.outdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        if not os.path.exists(os.path.join(self.outdir, 'image')):
            os.makedirs(os.path.join(self.outdir, 'image'))
        if not os.path.exists(os.path.join(self.outdir, 'profile')):
            os.makedirs(os.path.join(self.outdir, 'profile'))
        if not os.path.exists(os.path.join(self.outdir, 'emittance')):
            os.makedirs(os.path.join(self.outdir, 'emittance'))

    def connection(self, url):
        self.url = url
        if "OpenCV" in self.sdk:
            self.url = url
            try:
                img_resp = cv2.VideoCapture(self.url)
                if not img_resp.isOpened():
                    self.msg = "Connected camera won't be opened"
                    self.connected = False
                else:
                    self.msg = 'Connection successful'
                    self.connected = True
            except:
                self.msg = 'Connection is failed'
                self.connected = False
        elif "Vimba" in self.sdk:
            if not import_vimba:
                self.msg = 'ERRORPlease install vimba module'
                self.connected = False
            else:
                self.url = url
                try:
                    with Vimba.get_instance() as vimba:
                        cams = vimba.get_all_cameras()
                        if len(cams) < 1:
                            self.msg = f'There is no connected GigE camera.'
                            self.connected = False
                    self.camera = cams[0]
                    self.msg = f'Connection successful'
                    self.connected = True
                except:
                    self.msg = f'connection is failed.'
                    self.connected = False
        elif "Pylon" in self.sdk:
            if not import_pylon:
                self.msg = 'ERRORPlease install pylon module'
                self.connected = False
            else:
                self.converter = pylon.ImageFormatConverter()
                # Camera: ace acA1600-20gm
                # Supported pixel format: Mono 8, Mono 12, Mono 12 Packed, YUV 4:2:2 Packed, YUV  4:2:2 (YUYV) Packed
                self.converter.OutputPixelFormat = pylon.PixelType_Mono8
                self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
                try:
                    self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
                    if self.camera is None:
                        self.msg = f'ERROR There is no connected GigE camera.'
                        self.connected = False
                    self.camera.Open()
                    self.msg = f'INFO Using device, {self.camera.GetDeviceInfo().GetModelName()}'#' at {self.camera.GetIpAddress()}'
                    self.connected = True
                except:
                    if self.camera is None:
                        self.msg = f'ERROR There is no connected GigE camera.'
                    else:
                        self.msg = f'ERROR {self.camera.GetDeviceInfo().GetModelName()} connection is failed.'
                    self.connected = False

    def run(self):
        if "OpenCV" in self.sdk:
            try:
                while self.working:
                    if not self.connected: continue
                    if self.idx == CAMERA_EXIT: break
                    if self.idx == CAMERA_CAPTURE:
                        self.watch_signal.emit(True)
                        queue = []
                        for i in range(1, self.repeat+1):
                            if self.idx == CAMERA_STOP: break
                            queue.append(self.take_a_picture())
                            #self.msleep(self.exposure_time)
                            self.thread_logger_signal.emit('INFO', str(f"Take a picture {i}"))

                        self.thread_logger_signal.emit('INFO', f"Analyze pictures")
                        for image in queue:
                            outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H-%M-%S_%f')}.png")
                            cv2.imwrite(outname, image)
                            self.save_signal.emit(outname)
                            xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, xrange, yrange = self.analyze_picture(image=image, shot=True)
                            beam_range = xrange + yrange

                            self.graph_signal.emit(PROFILE_SCREEN, image, beam_range)
                            self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
                            self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)
                            self.plot_signal.emit(image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline)
                        self.thread_logger_signal.emit('INFO', f'Analysis is completed')
                        self.watch_signal.emit(False)
                        self.idx = CAMERA_SHOW

                    img_resp = cv2.VideoCapture(self.url)
                    retval, image = img_resp.read()
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    self.show_screen(image)
                    self.msleep(int((1.0/self.frame)*1000))
            except:
                self.thread_logger_signal.emit('ERROR', f'Connection was broken.')
                self.connected = False

        elif "Vimba" in self.sdk:
            while self.working:
                if not self.connected: continue
                if self.idx == CAMERA_EXIT: break
                if self.idx == CAMERA_CAPTURE:
                    self.watch_signal.emit(True)
                    queue = []
                    for i in range(1, self.repeat+1):
                        if self.idx == CAMERA_STOP: break
                        queue.append(self.take_a_picture())
                        #self.msleep(self.exposure_time)
                        self.thread_logger_signal.emit('INFO', str(f"Take a picture {i}"))

                    self.thread_logger_signal.emit('INFO', f"Analyze pictures")
                    for image in queue:
                        outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H-%M-%S_%f')}.png")
                        cv2.imwrite(outname, image)
                        self.save_signal.emit(outname)
                        xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, xrange, yrange = self.analyze_picture(image=image, shot=True)
                        beam_range = xrange + yrange

                        self.graph_signal.emit(PROFILE_SCREEN, image, beam_range)
                        self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
                        self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)
                        self.plot_signal.emit(image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline)
                    self.thread_logger_signal.emit('INFO', f'Analysis is completed')
                    self.watch_signal.emit(False)
                    self.idx = CAMERA_SHOW

                with Vimba.get_instance() as vimba:
                    cams = vimba.get_all_cameras()
                    with cams[0] as cam:
                        try:
                            minimum, maximum = cam.ExposureTimeAbs.get_range()
                            if minimum <= self.exposure_time <= maximum:
                                cam.ExposureAuto.set('Off')
                                cam.ExposureTimeAbs.set(self.exposure_time)
                        except(AttributeError, VimbaFeatureError):
                            pass
                        try:
                            cam.GainAuto.set('Off')
                            cam.GainRaw.set(self.gain)
                        except(AttributeError, VimbaFeatureError):
                            pass
                        try:
                            frame = cam.get_frame()
                            frame.convert_pixel_format(PixelFormat.Mono8)
                            image = frame.as_opencv_image()
                        except:
                            image = None
                        self.show_screen(image)
                        self.msleep(int((1.0/self.frame)*1000))

        elif "Pylon" in self.sdk:
            try:
                if self.connected:
                    self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                
                    minimum = self.camera.ExposureTimeRaw.Min
                    maximum = self.camera.ExposureTimeRaw.Max
                    exposure_time = round(self.exposure_time * 1000.0)
                    try:
                        if self.camera.ExposureTimeRaw.GetValue() != exposure_time:
                            if minimum <= exposure_time <= maximum:
                                self.camera.ExposureTimeRaw.SetValue(exposure_time)
                    except:
                        pass
                
                    minimum = self.camera.GainRaw.Min
                    maximum = self.camera.GainRaw.Max
                    delta = maximum - minimum
                    gain = minimum + round(0.01 * self.gain * delta)
                    try:
                        if self.camera.GainRaw.SetValue() != gain:
                            self.camera.GainRaw.SetValue(gain)
                    except:
                        pass

                while self.working:
                        if self.idx == CAMERA_CAPTURE:
                            self.watch_signal.emit(True)
                            self.camera.StopGrabbing()
                            queue = []
                            for i in range(1, self.repeat+1):
                                if self.idx == CAMERA_STOP: break
                                queue.append(self.take_a_picture())
                                #self.msleep(self.exposure_time)
                                self.thread_logger_signal.emit('INFO', str(f"Take a picture {i}"))

                            self.thread_logger_signal.emit('INFO', f"Analyze pictures")
                            for image in queue:
                                outname = os.path.join(self.outdir, 'image', f"out{datetime.datetime.today().strftime('%H-%M-%S_%f')}.png")
                                cv2.imwrite(outname, image)
                                self.save_signal.emit(outname)
                                xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, xrange, yrange = self.analyze_picture(image=image, shot=True)
                                beam_range = xrange + yrange

                                self.graph_signal.emit(PROFILE_SCREEN, image, beam_range)
                                self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
                                self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)
                                self.plot_signal.emit(image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline)
                            self.thread_logger_signal.emit('INFO', f'Analysis is completed')

                            self.idx = CAMERA_SHOW
                            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                            self.watch_signal.emit(False)
                        else:
                            if self.camera.IsGrabbing():
                                result = self.camera.RetrieveResult(100000, pylon.TimeoutHandling_ThrowException)
                                if result.GrabSucceeded():
                                    image = self.converter.Convert(result)
                                    image = image.GetArray()
                                    result.Release()
                                else:
                                    image = None
                            self.show_screen(image)
                            self.msleep(int((1.0/self.frame)*1000))
            except:
                self.thread_logger_signal.emit('ERROR', f'Connection was broken.')
                self.connected = False

    def stop(self):
        self.working = False
        self.sleep(1)
        self.quit()

    def rotate_image(self, image):
        center = (round(image.shape[1]/2), round(image.shape[0]/2))
        angle = float(self.rotate_angle)
        matrix = cv2.getRotationMatrix2D(center, angle, 1)
        image = cv2.warpAffine(image, matrix, (0,0))

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
            width, height = image.shape[1], image.shape[0]
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

    def take_a_picture(self, setup=False):
        image = None
        if 'OpenCV' in self.sdk:
            img_resp = cv2.VideoCapture(self.url)
            retval, image = img_resp.read()
            if not image is None:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif "Vimba" in self.sdk:
            with Vimba.get_instance() as vimba:
                cams = vimba.get_all_cameras()
                with cams[0] as cam:
                    if cam.ExposureTimeAbs.get() != round(self.exposure_time * 1000.0): 
                        try:
                            minimum, maximum = cam.ExposureTimeAbs.get_range()
                            if minimum <= round(self.exposure_time * 1000.0) <= maximum:
                                cam.ExposureAuto.set('Off')
                                cam.ExposureTimeAbs.set(round(self.exposure_time * 1000.0))
                        except(AttributeError, VimbaFeatureError):
                            pass
                        
                    minimum, maximum = cam.GainRaw.get_range()
                    gain = minimum + round((maximum - minimum) * self.gain / 200.0)                    
                    if cam.GainRaw.get() != gain:
                        try:
                            cam.GainAuto.set('Off')
                            cam.GainRaw.set(gain)
                        except(AttributeError, VimbaFeatureError):
                            pass
                    try:
                        frame = cam.get_frame()
                        frame.convert_pixel_format(PixelFormat.Mono8)
                        image = frame.as_opencv_image()
                    except:
                        image = None
        elif "Pylon" in self.sdk:
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            minimum = self.camera.ExposureTimeRaw.Min
            maximum = self.camera.ExposureTimeRaw.Max
            exposure_time = round(self.exposure_time * 1000.0)
            try:
                if self.camera.ExposureTimeRaw.GetValue() != exposure_time:
                    if minimum <= round(self.exposure_time * 1000.0) <= maximum:
                        self.camera.ExposureTimeRaw.SetValue(round(self.exposure_time * 1000.0))
            except:
                pass
                
            minimum = self.camera.GainRaw.Min
            maximum = self.camera.GainRaw.Max
            delta = maximum - minimum
            gain = minimum + round(0.01 * self.gain * delta)
            try:
                if self.camera.GainRaw.SetValue() != gain:
                    self.camera.GainRaw.SetValue(gain)
            except:
                pass

            result = self.camera.RetrieveResult(100000, pylon.TimeoutHandling_ThrowException)
            if result.GrabSucceeded():
                image = self.converter.Convert(result)
                image = image.GetArray()
                result.Release()
            else:
                image = None
            self.camera.StopGrabbing()

        if setup:
            return image

        if image is None:
            self.thread_logger_signal.emit('ERROR', 'Taking a picture is failed.')
            return

        self.original_image = image.copy()
        self.original_pixel = [self.original_image.shape[1], self.original_image.shape[0]]

        image = self.rotate_image(image)
        image = self.filter_image(image)
        image = self.transform_image(image)
        image = self.slice_image(image)

        return image
            
    def show_screen(self, image):
        #print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
        if not self.connected: return
        if not self.working: return

        self.original_image = image.copy()
        self.original_pixel = [self.original_image.shape[1], self.original_image.shape[0]]

        image = self.rotate_image(image)
        image = self.filter_image(image)
        image = self.transform_image(image)
        image = self.slice_image(image)
        self.image = image

        xbin, ybin, xhist_percent, yhist_percent, xrange, yrange = self.analyze_picture(image=image)

        self.screen_signal.emit(PICTURE_SCREEN, image)
        self.graph_signal.emit(LIVE_XPROFILE_SCREEN, list(zip(xbin, xhist_percent)), xrange)
        self.graph_signal.emit(LIVE_YPROFILE_SCREEN, list(zip(ybin, yhist_percent)), yrange)
    
    def analyze_picture(self, image, shot=False):
        image = image
        #self.original_pixel = [image.shape[1], image.shape[0]]

        if len(image.shape) == 3:
            grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            grayimage = image
        nypixel, nxpixel = grayimage.shape

        total_x = self.original_pixel[0] * self.mm_per_pixel[0]
        total_y = self.original_pixel[1] * self.mm_per_pixel[1]
        mm_per_pixel_x = total_x / nxpixel
        mm_per_pixel_y = total_y / nypixel
        self.xmin = -round(total_x / 2.0)
        self.ymin = -round(total_y / 2.0)
        xbin = [self.xmin + float(i) * mm_per_pixel_x for i in range(nxpixel)]
        ybin = [self.ymin + float(i) * mm_per_pixel_y for i in range(nypixel)]

        xhist, yhist = [], []
        if shot:
            xhist = [0 for i in range(nxpixel)]
            yhist = [0 for i in range(nypixel)]
            
            for xidx in range(nxpixel):
                for yidx in range(nypixel):
                    xhist[xidx] += grayimage[yidx][xidx]
                    yhist[yidx] += grayimage[yidx][xidx]
        else:
            intensity_line = self.intensity_line
            if intensity_line[0] == -1:
                intensity_line[0] = round(len(xbin) / 2)
            if intensity_line[1] == -1:
                intensity_line[1] = round(len(ybin) / 2)
            
            xhist, yhist = grayimage[intensity_line[0],:], grayimage[:,intensity_line[1]]

        xhist_percent = np.asarray(xhist)/max(xhist) * 100
        yhist_percent = np.asarray(yhist)/max(yhist) * 100

        xmax, ymax = np.argmax(xhist_percent), np.argmax(yhist_percent)

        xlength = len(np.where(xhist_percent > 32)[0]) * self.mm_per_pixel[0]
        ylength = len(np.where(yhist_percent > 32)[0]) * self.mm_per_pixel[1]

        if shot:
            gauss = lambda x, a, b, c: a*np.exp(-(x-b)**2/2*c**2)
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

            return xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, [xbin[xmax], xlength], [ybin[ymax], ylength]

        else:
            return xbin, ybin, xhist_percent, yhist_percent, [xbin[xmax], xlength], [ybin[ymax], ylength]

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
            self.gain = value
        elif self.idx == CAMERA_EXPOSURE_TIME:
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
        try:
            image = cv2.imread(name)
        except:
            self.thread_logger_signal("ERROR", "Wrong image")
            return
        if image is None: 
            self.thread_logger_signal("ERROR", "Wrong image")
            return
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        self.original_image = image
        self.original_pixel = [self.original_image.shape[1], self.original_image.shape[0]]

        xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, xrange, yrange = self.analyze_picture(image=image, shot=True)
        beam_range = xrange + yrange

        self.graph_signal.emit(PROFILE_SCREEN, image, beam_range)
        self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
        self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)
        self.plot_signal.emit(image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline)