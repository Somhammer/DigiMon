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
import utilities as ut
from DigiMon import mutex

class Blueberry(QThread):
    watch_signal = Signal(bool)
    thread_logger_signal = Signal(str, str)
    screen_signal = Signal(int, np.ndarray)
    graph_signal = Signal(int, list, list)
    save_signal = Signal(str)
    plot_signal = Signal(np.ndarray, list, list, np.ndarray, np.ndarray, list, list)

    def __init__(self, queue_for_analyze, return_queue, parent=None):
        super().__init__()
        self.name = "Network Camera"
        self.queue_for_analyze = queue_for_analyze
        self.return_queue = return_queue
        self.parent = parent

        self.connected = False

        self.camera = None
        self.url = None

        self.original_image = None

        self.filter_code = None
        self.filter_para = {}

        self.rotate_angle = 0.0
        self.do_transformation = False
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
        self.watch_signal.connect(self.parent.stopwatch)
        self.thread_logger_signal.connect(self.parent.receive_log)
        self.screen_signal.connect(self.parent.update_screen)
        self.graph_signal.connect(self.parent.update_screen)
        self.save_signal.connect(self.parent.save_image)
        self.plot_signal.connect(self.parent.save_pretty_plot)

    def connection(self, url):
        self.url = url
        if not "OpenCV" in self.sdk:
            import re
            p = re.compile(r'[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+')
            result = p.search(self.url)
            if result is not None:
                ip_address = result[0]
            else:
                ip_address = ''
        if "OpenCV" in self.sdk:
            try:
                img_resp = cv2.VideoCapture(self.url)
                if not img_resp.isOpened():
                    message = "ERROR Camera won't be opened"
                    self.connected = False
                else:
                    message = 'INFO Connection successful'
                    self.connected = True
            except:
                message = 'ERROR Connection is failed'
                self.connected = False
        elif "Vimba" in self.sdk:
            if not import_vimba:
                message = 'ERROR Please install vimba module'
                self.connected = False
            else:
                try:
                    with Vimba.get_instance() as vimba:
                        cams = vimba.get_all_cameras()
                        if len(cams) < 1:
                            message = f'ERROR There is no connected GigE camera.'
                            self.connected = False
                    self.camera = cams[0]
                    message = f'INFO Connection successful'
                    self.connected = True
                except:
                    message = f'ERROR connection is failed.'
                    self.connected = False
        elif "Pylon" in self.sdk:
            if not import_pylon:
                message = 'ERROR Please install pylon module'
                self.connected = False
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
                        self.connected = False
                    self.camera.Open()
                    #self.camera.AcquisitionMode.SetValue('Continuous')

                    message = f'INFO Using device, {self.camera.GetDeviceInfo().GetModelName()} at {self.camera.GetDeviceInfo().GetIpAddress()}'
                    self.connected = True
                except:
                    if self.camera is None:
                        message = f'ERROR There is no connected GigE camera.'
                    else:
                        message = f'ERROR {self.camera.GetDeviceInfo().GetModelName()} connection is failed.'
                    self.connected = False
        
        return message

    def run(self):
        if "OpenCV" in self.sdk:
            try:
                while self.working:
                    if not self.connected: continue
                    if self.idx == CAMERA_EXIT: break
                    if self.idx == CAMERA_CAPTURE:
                        self.watch_signal.emit(True)
                        self.watch_signal.emit(True)
                        for i in range(1, self.repeat+1):
                            if self.idx == CAMERA_STOP: break
                            self.take_a_picture()
                            self.thread_logger_signal.emit('INFO', str(f"Take a picture {i}"))

                        self.idx = CAMERA_SHOW
                        self.watch_signal.emit(False)
                    else:
                        img_resp = cv2.VideoCapture(self.url)
                        retval, image = img_resp.read()
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        self.show_screen(image)
                        self.msleep(int((1.0/self.frame)*1000))
                    self.take_data_from_queue()

            except:
                self.thread_logger_signal.emit('ERROR', f'Connection was broken.')
                self.connected = False

        elif "Vimba" in self.sdk:
            while self.working:
                if not self.connected: continue
                if self.idx == CAMERA_EXIT: break
                if self.idx == CAMERA_CAPTURE:
                    self.watch_signal.emit(True)
                    for i in range(1, self.repeat+1):
                        if self.idx == CAMERA_STOP: break
                        self.take_a_picture()
                        self.thread_logger_signal.emit('INFO', str(f"Take a picture {i}"))
                   
                    self.idx = CAMERA_SHOW
                    self.watch_signal.emit(False)

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
                    self.take_data_from_queue()
                        #self.msleep(int((1.0/self.frame)*1000))

        elif "Pylon" in self.sdk:
            try:
                if self.connected:
                    self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                
                    minimum = self.camera.ExposureTimeRaw.Min
                    maximum = self.camera.ExposureTimeRaw.Max
                    try:
                        if self.camera.ExposureTimeRaw.GetValue() != self.exposure_time:
                            if minimum <= self.exposure_time <= maximum:
                                self.camera.ExposureTimeRaw.SetValue(self.exposure_time)
                    except:
                        pass
                
                    minimum = self.camera.GainRaw.Min
                    maximum = self.camera.GainRaw.Max
                    gain = round(minimum + round((maximum - minimum) * self.gain / 100.0))
                    try:
                        if self.camera.GainRaw.GetValue() != gain:
                            self.camera.GainRaw.SetValue(gain)
                    except:
                        pass

                while self.working:
                    if self.idx == CAMERA_CAPTURE:
                        self.watch_signal.emit(True)
                        self.camera.StopGrabbing()
                        for i in range(1, self.repeat+1):
                            if self.idx == CAMERA_STOP: break
                            self.take_a_picture()
                            self.thread_logger_signal.emit('INFO', str(f"Take a picture {i}"))

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
                    self.take_data_from_queue()
                        #self.msleep(int((1.0/self.frame)*1000))
            except:
                self.thread_logger_signal.emit('ERROR', f'Connection was broken.')
                self.connected = False

    def stop(self):
        self.working = False
        self.sleep(1)
        self.quit()

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
                    if cam.ExposureTimeAbs.get() != self.exposure_time: 
                        try:
                            minimum, maximum = cam.ExposureTimeAbs.get_range()
                            if minimum <= self.exposure_time <= maximum:
                                cam.ExposureAuto.set('Off')
                                cam.ExposureTimeAbs.set(self.exposure_time)
                        except(AttributeError, VimbaFeatureError):
                            pass
                        
                    minimum, maximum = cam.GainRaw.get_range()
                    gain = minimum + round((maximum - minimum) * self.gain / 100.0)                    
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
            #self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            if self.camera.IsGrabbing(): self.camera.StopGrabbin()
            self.camera.StartGrabbing()
            minimum = self.camera.ExposureTimeRaw.Min
            maximum = self.camera.ExposureTimeRaw.Max
            try:
                if self.camera.ExposureTimeRaw.GetValue() != self.exposure_time:
                    if minimum <= self.exposure_time <= maximum:
                        self.camera.ExposureTimeRaw.SetValue(self.exposure_time)
            except:
                pass
                
            minimum = self.camera.GainRaw.Min
            maximum = self.camera.GainRaw.Max
            gain = round(minimum + round((maximum - minimum) * self.gain / 100.0))
            try:
                if self.camera.GainRaw.GetValue() != gain:
                    self.camera.GainRaw.SetValue(gain)
            except:
                pass

            result = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
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
        
        image = ut.filter_image(image, self.filter_code, self.filter_para)
        image = ut.rotate_image(image, angle=self.calibration_angle)
        image = ut.transform_image(image, self.transform_points, self.destination_points)
        image = ut.slice_image(image, self.ROI)
        image = ut.rotate_image(image, angle=0, quadrant = self.rotation, flip_rl = self.flip_rl, flip_ud = self.flip_ud)
                        
        outname = os.path.join(self.outdir, 'image', f"{datetime.datetime.today().strftime('%H-%M-%S_%f')[:-3]}_{self.current}A_Exp{self.exposure_time}_Gain{self.gain}.png")
        cv2.imwrite(outname, image)
        self.save_signal.emit(outname)

        element = [image, self.intensity_line, self.pixel_per_mm, self.original_pixel, self.resized_pixel, True]
        self.queue_for_analyze.put(element)
            
    def show_screen(self, image):
        if not self.connected: return
        if not self.working: return

        self.original_image = image.copy()
        self.original_pixel = [self.original_image.shape[1], self.original_image.shape[0]]
        image = ut.filter_image(image, self.filter_code, self.filter_para)
        image = ut.rotate_image(image, angle=self.calibration_angle)
        image = ut.transform_image(image, self.transform_points, self.destination_points)
        image = ut.slice_image(image, self.ROI)
        image = ut.rotate_image(image, angle=0, quadrant = self.rotation, flip_rl = self.flip_rl, flip_ud = self.flip_ud)
        element = [image, self.intensity_line, self.pixel_per_mm, self.original_pixel, self.resized_pixel, False]
        self.queue_for_analyze.put(element)

    def take_data_from_queue(self):
        #if not self.return_queue.empty():
        while not self.return_queue.empty():
            element = self.return_queue.get()
            if len(element) == 7:
                self.screen_signal.emit(PICTURE_SCREEN, element[0])
                self.graph_signal.emit(LIVE_XPROFILE_SCREEN, list(zip(element[1], element[3])), element[5])
                self.graph_signal.emit(LIVE_YPROFILE_SCREEN, list(zip(element[2], element[4])), element[6])
            else:
                self.graph_signal.emit(PROFILE_SCREEN, element[0], element[5]+element[6])
                self.graph_signal.emit(XSIZE_SCREEN, list(zip(element[1], element[3])), element[7])
                self.graph_signal.emit(YSIZE_SCREEN, list(zip(element[2], element[4])), element[8])
                self.plot_signal.emit(element[0], element[1], element[2], element[3], element[4], element[7], element[8])

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
            self.gain = float(value)
        elif self.idx == CAMERA_EXPOSURE_TIME:
            self.exposure_time = round(value)
        elif self.idx == CAMERA_FPS:
            if self.frame != value:
                mutex.acquire()
                while not self.queue_for_analyze.empty():
                    self.queue_for_analyze.get()
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

        self.original_image = image
        self.original_pixel = [self.original_image.shape[1], self.original_image.shape[0]]

        xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline, xrange, yrange = self.analyze_picture(image=image, shot=True)
        beam_range = xrange + yrange

        self.graph_signal.emit(PROFILE_SCREEN, image, beam_range)
        self.graph_signal.emit(XSIZE_SCREEN, list(zip(xbin, xhist_percent)), xfitline)
        self.graph_signal.emit(YSIZE_SCREEN, list(zip(ybin, yhist_percent)), yfitline)
        self.plot_signal.emit(image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline)