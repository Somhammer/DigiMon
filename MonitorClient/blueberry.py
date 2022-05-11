# -------------------------------------------------------
# Blueberry
# Author: Seohyeon An
# Date: 2022-04-21
#
# This class controls the network camera.
#   Functions
#   1. It connects between the client and the network camera.
#   2. It captures images and send them to stream_queue or analyze_queue.
# -------------------------------------------------------

import os, sys
import time
import datetime
import logging
import numpy as np
from scipy.optimize import curve_fit
import copy
import cv2

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
import utilities as util
from DigiMon import mutex

class Blueberry(QThread):
    watch_signal = Signal(bool)
    thread_logger_signal = Signal(str, str)
    screen_signal = Signal(int, np.ndarray)
    graph_signal = Signal(int, list, list)
    save_signal = Signal(str)
    plot_signal = Signal(np.ndarray, list, list, np.ndarray, np.ndarray, list, list)

    def __init__(self, para, main, stream_queue, analysis_queue, return_queue):
        super().__init__()
        self.name = "Network Camera"

        self.para = para
        self.main = main
        self.stream_queue = stream_queue
        self.analysis_queue = analysis_queue
        self.return_queue = return_queue

        self.para.cam_conn = False

        self.camera = None
        self.prev_time = 0 # Only for OpenCV
        self.count = 1 # Image Taking
        self.para.url = None

        self.original_image = None

        self.filter_code = None
        self.filter_para = {}

        self.rotate_angle = 0.0
        self.destination_points = np.float32([[0,0],[0,800],[800,0],[800,800]]) # 이미지 크기는 나중에 바꿀 수 있음...?
        self.pixel_per_mm = [1.0, 1.0]

        self.original_pixel = None
        self.resized_pixel = None

        self.working = True

        self.idx = None
        self.frame = None

        self.gain = None
        self.exposure_time = None
        self.ROI = [[0,0], [0,0]]
        self.intensity_line = [-1,-1]

        self.calibration_angle = 0

        self.repeat = None
        self.rotation = 0
        self.flip_rl = 0
        self.flip_ud = 0

        self.current = 0.0

        self.outdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        if not os.path.exists(os.path.join(self.outdir, 'image')):
            os.makedirs(os.path.join(self.outdir, 'image'))
        if not os.path.exists(os.path.join(self.outdir, 'profile')):
            os.makedirs(os.path.join(self.outdir, 'profile'))
        if not os.path.exists(os.path.join(self.outdir, 'emittance')):
            os.makedirs(os.path.join(self.outdir, 'emittance'))

        self.set_action()

    def set_action(self):
        self.watch_signal.connect(self.main.stopwatch)
        self.thread_logger_signal.connect(self.main.receive_log)
        self.save_signal.connect(self.main.save_image)

    def connect_device(self):
        if not "OpenCV" in self.para.sdk:
            import re
            p = re.compile(r'[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+')
            result = p.search(self.para.url)
            if result is not None:
                ip_address = result[0]
            else:
                ip_address = ''

        if "OpenCV" in self.para.sdk:
            try:
                img_resp = cv2.VideoCapture(self.para.url)
                if not img_resp.isOpened():
                    message = f"ERROR Camera won't be opened, {self.para.url}"
                    self.para.cam_conn = False
                else:
                    message = 'INFO Connection successful'
                    self.para.cam_conn = True
            except:
                message = 'ERROR Connection is failed'
                self.para.cam_conn = False
        elif "Pylon" in self.para.sdk:
            if not import_pylon:
                message = 'ERROR Please install pylon module'
                self.para.cam_conn = False
            else:
                self.converter = pylon.ImageFormatConverter()
                # Camera: ace acA1600-20gm
                # Supported pixel format: Mono 8, Mono 12, Mono 12 Packed, YUV 4:2:2 Packed, YUV  4:2:2 (YUYV) Packed
                self.converter.OutputPixelFormat = pylon.PixelType_Mono8
                self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

                #self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
                try:
                    factory = pylon.TlFactory.GetInstance()
                    ptl = factory.CreateTl('BaslerGigE')
                    empty_camera_info = pylon.DeviceInfo()
                    empty_camera_info.SetPropertyValue('IpAddress', ip_address)
                    #camera_info = factory.CreateTl('BaslerGigE').CreateDeviceInfo()
                    #camera_info.SetPropertyValue('PersistentIP', 'True')
                    #camera_info.SetPropertyValue('DHCP', 'False')
                    #camera_info.SetPropertyValue('IpAddress', ip_address)
                    #camera_info.SetPropertyValue('SubnetMask', '255.255.255.0')
                    #camera_info.SetPropertyValue('DefaultGateway', '10.1.30.1')                
                    self.camera = pylon.InstantCamera(factory.CreateDevice(empty_camera_info))
                    #self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
                    if self.camera is None:
                        message = f'ERROR There is no connected GigE camera.'
                        self.para.cam_conn = False
                    else:
                        self.camera.Open()
                        self.camera.AcquisitionFrameRateEnable.SetValue(True)

                        #self.camera.AcquisitionMode.SetValue('Continuous')

                        message = f'INFO Using device, {self.camera.GetDeviceInfo().GetModelName()} at {self.camera.GetDeviceInfo().GetIpAddress()}'
                        self.para.cam_conn = True
                except:
                    if self.camera is None:
                        message = f'ERROR There is no connected GigE camera.'
                    else:
                        message = f'ERROR {self.camera.GetDeviceInfo().GetModelName()} connection is failed.'
                    self.para.cam_conn = False
        
        return message

    def disconnect_device(self):
        pass

    def run(self):
        if self.para.sdk == 'OpenCV':
            try:
                img_resp = cv2.VideoCapture(self.para.url)
            except:
                connect = False
                for i in range(5):
                    try:
                        img_resp = cv2.VideoCapture(self.para.url)
                        connect = True
                        break
                    except:
                        pass
                
                if not connect: 
                    self.para.cam_conn = False
                    self.thread_logger_signal.emit('ERROR', str(f'Reconnection was failed. Streaming is stopped.'))

            gain = self.para.gain

        elif self.para.sdk == 'Pylon':
            try:
                self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                
                if float(self.camera.ExposureTimeRaw.GetValue()) != self.para.exp_time:
                    minimum = self.camera.ExposureTimeRaw.Min
                    maximum = self.camera.ExposureTimeRaw.Max
                    try:
                        if minimum <= self.para.exp_time <= maximum:
                            self.camera.ExposureTimeRaw.SetValue(self.para.exp_time)
                        self.thread_logger_signal.emit('INFO', str(f"Set camera exposure Time: {self.para.exp_time}"))
                    except:
                        self.thread_logger_signal.emit('ERROR', str(f'Setting exposure time is failed.'))
            

                minimum = self.camera.GainRaw.Min
                maximum = self.camera.GainRaw.Max
                gain = round(minimum + round((maximum - minimum) * self.para.gain / 100.0))
                if float(self.camera.GainRaw.GetValue()) != gain:
                    try:
                        self.camera.GainRaw.SetValue(gain)
                        self.thread_logger_signal.emit('INFO', str(f"Set camera gain: {gain}"))
                    except:
                        self.thread_logger_signal.emit('ERROR', str(f'Setting gain is failed.'))

                if self.camera.AcquisitionFrameRate.GetValue() != self.para.fps:
                    try:
                        self.camera.AcquisitionFrameRate.SetValue(self.para.fps)
                        self.thread_logger_signal.emit('INFO', str(f"Set camera frame rate: {self.para.fps}"))
                    except:
                        self.thread_logger_signal.emit('ERROR', str(f'Setting frame rate is failed.'))
            except:
                connect = False
                for i in range(5):
                    try:
                        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                        connect = True
                    except:
                        pass
                
                if not connect:
                    self.para.cam_conn = False
                    self.thread_logger_signal.emit('ERROR', str(f'Reconnection was failed. Streaming is stopped.'))

        while self.working:
            if not self.para.cam_conn or  self.para.cam_request == CAMERA_REQUEST_NOTHING: continue
            if self.para.cam_request == CAMERA_REQUEST_STREAM and self.count == 1:
                self.watch_signal.emit(True)
            
            if self.para.cam_request == CAMERA_REQUEST_DISCONNECT: break
            image = None
            if self.para.sdk == 'OpenCV':
                retval, image = img_resp.read()
                current_time = time.time() - self.prev_time
                if retval and (current_time > 1.0/self.para.fps):
                    self.prev_time = time.time()
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            elif self.para.sdk == 'Pylon':
                if not self.camera.IsGrabbing(): 
                    self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                    self.thread_logger_signal.emit('INFO', str(f'Reconnect camera.'))

                if self.camera.IsGrabbing():
                    result = self.camera.RetrieveResult(100000, pylon.TimeoutHandling_ThrowException)
                    if result.GrabSucceeded():
                        image = self.converter.Convert(result)
                        image = image.GetArray()
                        result.Release()

            if image is not None:
                if self.para.cam_request == CAMERA_REQUEST_CAPTURE:
                    if not os.path.exists(os.path.join(self.outdir, 'image', self.para.current, 'raw')):
                        os.makedirs(os.path.join(self.outdir, 'image', self.para.current, 'raw'))
                    if not os.path.exists(os.path.join(self.outdir, 'image', self.para.current, 'analyzed')):
                        os.makedirs(os.path.join(self.outdir, 'image', self.para.current, 'analyzed'))
                    imagename = f"{datetime.datetime.today().strftime('%H-%M-%S-%f')[:-3]}_Exp{self.para.exp_time}_Gain{gain}.png"
                    outname = os.path.join(self.outdir, 'image/raw', imagename)
                    cv2.imwrite(outname, image)
                    self.save_signal.emit(outname)

                image = util.filter_image(self.para, image)
                image = util.transform_image(self.para, image)
                image = util.slice_image(self.para, image)
                image = util.rotate_image(self.para, image)

                if self.para.cam_request == CAMERA_REQUEST_STREAM:
                    self.stream_queue.put([image, self.para])
                elif self.para.cam_request == CAMERA_REQUEST_CAPTURE:
                    imagename = f"{datetime.datetime.today().strftime('%H-%M-%S-%f')[:-3]}_Exp{self.para.exp_time}_Gain{gain}.png"
                    outname = os.path.join(self.outdir, 'image/analyzed', imagename)
                    cv2.imwrite(outname, image)

                    self.analysis_queue.put([image, self.para])

                    if self.count < self.para.repeat:
                        self.count += 1
                    elif self.count == self.para.repeat:
                        self.count == 1
                        self.para.cam_request = CAMERA_REQUEST_STREAM
                        self.watch_signal.emit(False)

    def stop(self):
        self.working = False
        self.sleep(1)
        self.quit()

    def take_a_picture(self, image):
        # It is only used for setup.
        image = None
        if self.para.sdk == 'OpenCV':
            try:
                img_resp = cv2.VideoCapture(self.para.url)
            except:
                connect = False
                for i in range(5):
                    try:
                        img_resp = cv2.VideoCapture(self.para.url)
                        connect = True
                        break
                    except:
                        pass
                
                if not connect: 
                    self.para.cam_conn = False
                    self.thread_logger_signal.emit('ERROR', str(f'Reconnection was failed. Streaming is stopped.'))

            gain = self.para.gain

            retval, image = img_resp.read()
            current_time = time.time() - self.prev_time
            if retval and (current_time > 1.0/self.para.fps):
                self.prev_time = time.time()
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        elif self.para.sdk == 'Pylon':
            try:
                self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                
                if float(self.camera.ExposureTimeRaw.GetValue()) != self.para.exp_time:
                    minimum = self.camera.ExposureTimeRaw.Min
                    maximum = self.camera.ExposureTimeRaw.Max
                    try:
                        if minimum <= self.para.exp_time <= maximum:
                            self.camera.ExposureTimeRaw.SetValue(self.para.exp_time)
                        self.thread_logger_signal.emit('INFO', str(f"Set camera exposure Time: {self.para.exp_time}"))
                    except:
                        self.thread_logger_signal.emit('ERROR', str(f'Setting exposure time is failed.'))
            

                minimum = self.camera.GainRaw.Min
                maximum = self.camera.GainRaw.Max
                gain = round(minimum + round((maximum - minimum) * self.para.gain / 100.0))
                if float(self.camera.GainRaw.GetValue()) != gain:
                    try:
                        self.camera.GainRaw.SetValue(gain)
                        self.thread_logger_signal.emit('INFO', str(f"Set camera gain: {gain}"))
                    except:
                        self.thread_logger_signal.emit('ERROR', str(f'Setting gain is failed.'))

                if self.camera.AcquisitionFrameRate.GetValue() != self.para.fps:
                    try:
                        self.camera.AcquisitionFrameRate.SetValue(self.para.fps)
                        self.thread_logger_signal.emit('INFO', str(f"Set camera frame rate: {self.para.fps}"))
                    except:
                        self.thread_logger_signal.emit('ERROR', str(f'Setting frame rate is failed.'))
            except:
                connect = False
                for i in range(5):
                    try:
                        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                        connect = True
                    except:
                        pass
                
                if not connect:
                    self.para.cam_conn = False
                    self.thread_logger_signal.emit('ERROR', str(f'Reconnection was failed. Streaming is stopped.'))

            if self.camera.IsGrabbing():
                result = self.camera.RetrieveResult(100000, pylon.TimeoutHandling_ThrowException)
                if result.GrabSucceeded():
                    image = self.converter.Convert(result)
                    image = image.GetArray()
                    result.Release()

        if image is None:
            self.thread_logger_signal.emit('ERROR', 'Taking a picture is failed.')
            return
        else:
            return image

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
            self.parent.self.para.gain = float(value)
        elif self.idx == CAMERA_EXPOSURE_TIME:
            self.exposure_time = round(value)
        elif self.idx == CAMERA_FPS:
            if self.frame != value:
                mutex.acquire()
                while not self.analysis_queue.empty():
                    self.analysis_queue.get()
                mutex.release()
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

        self.save_signal.emit(name)
        self.original_image = image
        self.original_pixel = [self.original_image.shape[1], self.original_image.shape[0]]

        #xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, xrange, yrange = ut.analyze_picture(image=image, shot=True)
        #beam_range = xrange + yrange

        self.analysis_queue.put([image, self.para])