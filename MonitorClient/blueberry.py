# -------------------------------------------------------
# Blueberry
# Author: Seohyeon An
# Date: 2022-04-21
#
# This class controls the network camera.
#   Functions
#   1. It connects between the client and the network camera.
#   2. It captures images and send them to stream_input_queue or analyze_queue.
# -------------------------------------------------------

import time
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

from variables import *
from DigiMon import mutex

class Blueberry(QThread):
    thread_logger_signal = Signal(str, str)
    save_signal = Signal(list, int)

    def __init__(self, para, main, stream_input_queue, analysis_input_queue):
        super().__init__()
        self.name = "Network Camera"

        self.para = para
        self.main = main
        self.stream_input_queue = stream_input_queue
        self.analysis_input_queue = analysis_input_queue

        self.para.cam_conn = False

        self.camera = None
        self.prev_time = 0 # Only for OpenCV
        self.count = 0 # Image Taking
        self.fps = 20

        self.converter = None # Only for Pylon

        self.working = True
        self.current = str(0.0)

        self.idx = None
        self.frame = None

        self.repeat = None

        self.set_action()

    def clear_queue(self):
        mutex.acquire()
        while not self.analysis_input_queue.empty():
            self.analysis_input_queue.get()
        while not self.stream_input_queue.empty():
            self.stream_input_queue.get()
        mutex.release()

    def set_action(self):
        self.thread_logger_signal.connect(self.main.receive_log)
        self.save_signal.connect(self.main.save_image)

    def connect_device(self):
        if "OpenCV" in self.para.sdk:
            self.camera, message, self.para.cam_conn = self.connect_opencv()
        elif "Pylon" in self.para.sdk:
            self.camera, message, self.para.cam_conn = self.connect_pylon()
        
        return message

    def connect_opencv(self):
        try:
            camera = cv2.VideoCapture(self.para.url)
            if not camera.isOpened():
                return None, f"ERROR Camera won't be opened, {self.para.url}", False
            return camera, "INFO Connection successful with OpenCV.", True
        except Exception as e:
            return None, f"ERROR Connection failed with OpenCV. Exception: {str(e)}", False
        
    def connect_pylon(self):
        if not import_pylon:
            return None, 'ERROR Please install pylon module.', False
        try:
            import re
            p = re.compile(r'[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+')
            result = p.search(self.para.url)
            if result is not None:
                ip_address = result[0]
            else:
                ip_address = ''

            self.converter = pylon.ImageFormatConverter()
            # Camera: ace acA1600-20gm
            # Supported pixel format: Mono 8, Mono 12, Mono 12 Packed, YUV 4:2:2 Packed, YUV  4:2:2 (YUYV) Packed
            self.converter.OutputPixelFormat = pylon.PixelType_Mono8
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            
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
            camera = pylon.InstantCamera(factory.CreateDevice(empty_camera_info))
            if camera is None:
                return None, f'ERROR There is no connected GigE camera.', False

            camera.Open()
            camera.AcquisitionFrameRateEnable.SetValue(True)
            #self.camera.AcquisitionMode.SetValue('Continuous')
            camera.StartGrabbing()

            return camera, f'INFO Using device, {camera.GetDeviceInfo().GetModelName()} at {camera.GetDeviceInfo().GetIpAddress()}', True
        except Exception as e:
            return None, f'ERROR Connection is failed.', False

    def disconnect_device(self):
        try:
            if "OpenCV" in self.para.sdk:
                self.camera.Close()
                message = f"INFO {self.para.url} is successfully disconnected."

            elif "Pylon" in self.para.sdk:
                self.camera.Close()
                message = f"INFO {self.camera.GetDeviceInfo().GetModelName()} is successfully disconnected."

            self.para.cam_conn = False
        except:
            message = f"ERROR Disconnection is failed."

        return message

    def reconnect_device(self):
        for i in range(5):
            try:
                self.connect_device()
            except Exception as e:
                pass
            
        if not self.para.cam_conn:
            self.thread_logger_signal.emit('ERROR', str(f'Reconnection was failed. Streaming is stopped.'))
            return False
        return True
            
    def run(self):
        while self.working:
            if not self.para.cam_conn or self.para.cam_request == CAMERA_REQUEST_NOTHING: continue
            if self.para.cam_request == CAMERA_REQUEST_CAPTURE and self.count == 0: pass
                #self.clear_queue()
            if self.para.cam_request == CAMERA_REQUEST_DISCONNECT: 
                self.disconnect_device()
                break

            image = None
            if 'OpenCV' in self.para.sdk:
                try:
                    retval, tmp = self.camera.read()
                    image = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
                except:
                    self.reconnect_device()
                    if not self.para.cam_conn: break

            elif 'Pylon' in self.para.sdk:
                try:
                    if not self.camera.IsGrabbing():
                        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                except:
                    self.reconnect_device()
                    if not self.para.cam_conn: break

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

                if self.camera.IsGrabbing():
                    try:
                        result = self.camera.RetrieveResult(100000, pylon.TimeoutHandling_ThrowException)
                        if result.GrabSucceeded():
                            image = self.converter.Convert(result)
                            image = image.GetArray()
                            result.Release()
                    except:
                        time.sleep(1)

            if image is None: continue

            self.stream_input_queue.put([image, self.para])
            if self.para.cam_request == CAMERA_REQUEST_CAPTURE:
                if self.count < self.para.repeat:
                    self.thread_logger_signal.emit('INFO', str(f'Take a picture. {self.count + 1}'))
                    self.save_signal.emit(image.tolist(), RAW_IMAGE)
                    self.analysis_input_queue.put([image, self.para])
                    self.count += 1
                elif self.count == self.para.repeat:
                    self.count = 0
                    self.para.set_parameter(CAMERA_REQUEST_STREAM)

            self.msleep(round(1.0/self.para.fps*1000))

    def stop(self):
        self.working = False
        self.quit()
        self.wait(1000)

    def take_a_picture(self, image):
        # It is only used for setup.
        image = None
        if 'OpenCV' in self.para.sdk:
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

        elif 'Pylon' in self.para.sdk:
            try:
                if self.camera.IsGrabbing():
                    self.camera.StopGrabbing()
                    time.sleep(0.2)
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

                #if self.camera.AcquisitionFrameRate.GetValue() != self.para.fps:
                #    try:
                #        self.camera.AcquisitionFrameRate.SetValue(self.para.fps)
                #        self.thread_logger_signal.emit('INFO', str(f"Set camera frame rate: {self.para.fps}"))
                #    except:
                #        self.thread_logger_signal.emit('ERROR', str(f'Setting frame rate is failed.'))
            except:
                connect = False
                for i in range(5):
                    try:
                        if self.camera.IsGrabbing():
                            self.camera.StopGrabbing()
                        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                        connect = True
                    except:
                        time.sleep(0.5)
                
                if not connect:
                    self.para.cam_conn = False
                    self.thread_logger_signal.emit('ERROR', str(f'Reconnection was failed. Streaming is stopped.'))

            if self.camera.IsGrabbing():
                result = self.camera.RetrieveResult(100000, pylon.TimeoutHandling_ThrowException)
                if result.GrabSucceeded():
                    image = self.converter.Convert(result)
                    image = image.GetArray()
                    if len(image.shape) == 3:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    result.Release()
                self.camera.StopGrabbing()

        if image is None:
            self.thread_logger_signal.emit('ERROR', 'Image is None. Taking a picture is failed.')
            return
        else:
            return image

    @Slot(int, int)
    def set_camera_parameter(self, idx, value):
        self.para.set_parameter(idx, value)

    @Slot(str)
    def set_current(self, current):
        self.current = current