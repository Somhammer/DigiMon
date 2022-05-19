import os, sys
import time
import datetime
import logging
import copy
import yaml
import math
import textwrap
import cv2
import numpy as np

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

from logger import LogStringHandler
from variables import *
import utilities as ut
from digilabel import DigiLabel
from ui_setupwindow import Ui_SetupWindow

class SetupWindow(QDialog, Ui_SetupWindow):
    def __init__(self, para, blueberry, blackberry):
        super(SetupWindow, self).__init__()
        self.para = para
        self.blueberry = blueberry
        self.blackberry = blackberry

        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textConnectionLog)
        self.logger.addHandler(handler)

        self.labelImage = DigiLabel(self.labelImage)
        self.gridLayout.addWidget(self.labelImage, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.labelOrigin = DigiLabel(self.labelOrigin)
        self.gridLayout_9.addWidget(self.labelOrigin, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.ratio_width = self.ratio_height = 1

        self.select_roi = self.draw_square = False

        self.captured_image = None
        self.captured_image_aratio = None
        self.captured_image_screen_size = (400, 400)

        self.calibration_image = None
        self.calibration_image_aratio = None
        self.calibration_image_name = ""
        self.calibration_image_backup = None
        self.calibration_image_screen_size = (400, 400)

        self.cal_target_points = self.cal_dest_points = self.cal_reduced_target = self.cal_real_target  = []

        self.set_action()
        self.set_widgets_default()

    def keyPressEvent(self, event):
        if self.tabWidget.currentIndex() == 2:
            if event.key() == Qt.Key_Control:
                self.sliderGain.setSingleStep(10)
                self.sliderExposureTime.setSingleStep(10)
                self.sliderX0.setSingleStep(10)
                self.sliderY0.setSingleStep(10)
                self.sliderWidth.setSingleStep(10)
                self.sliderHeight.setSingleStep(10)
            elif event.key() == Qt.Key_Shift:
                self.sliderGain.setSingleStep(100)
                self.sliderExposureTime.setSingleStep(100)
                self.sliderX0.setSingleStep(100)
                self.sliderY0.setSingleStep(100)
                self.sliderWidth.setSingleStep(100)
                self.sliderHeight.setSingleStep(100)
                self.draw_square = True
        elif self.tabWidget.currentIndex() == 1:
            if event.modifiers() & Qt.ControlModifier:
                self.labelOrigin.setFocus()
                if any(i == event.key() for i in [Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down]):
                    self.move_circle(event.key())
                else:
                    self.labelOrigin.ctrdclick = True

    def keyReleaseEvent(self, event):
        self.labelOrigin.ctrdclick = False
        if any(event.key() == i for i in [Qt.Key_Control, Qt.Key_Shift]):
            self.sliderGain.setSingleStep(1)
            self.sliderExposureTime.setSingleStep(1)
            self.sliderX0.setSingleStep(1)
            self.sliderY0.setSingleStep(1)
            self.sliderWidth.setSingleStep(1)
            self.sliderHeight.setSingleStep(1)
            self.draw_square = False

    def closeEvent(self, event):
        reply = self.click_cancel()
        if reply == True: event.accept()
        else: event.ignore()

    def click_ok(self):
        if self.checkSaveLast.isChecked(): self.save(last=True)
        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()
            return True
        else:
            return False

    def return_para(self):
        return super().exec_()

    def set_checked(self, checkbox, state):
        if state:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def set_widgets_default(self):
        self.labelImage.resize(self.captured_image_screen_size[0], self.captured_image_screen_size[1])
        self.labelOrigin.resize(self.calibration_image_screen_size[0], self.calibration_image_screen_size[1])
        self.labelTrans.resize(self.calibration_image_screen_size[0], self.calibration_image_screen_size[1])
        #self.framePVHist.resize(self.captured_image_screen_size[0], self.framePVHist.height())

        self.plotPVHist = pg.PlotWidget()
        self.plotPVHist.setBackground('w')
        self.plotPVHist.setLabel('bottom', 'Pixel Value')
        self.plotPVHist.hideAxis('left')       
        self.gridPVHist.addWidget(self.plotPVHist)
        self.plotPVHist.setXRange(-1,256)

        if self.para.ctl_conn:
            self.checkUseControlServer.setChecked(True)
        self.connect_camera()
        self.connect_server()
        
        if self.tabWidget_2.currentIndex() == 0: # Rectangle
            if len(self.para.pixel_per_mm) == 2:
                self.linePixelPerMM_x.setText(str(self.para.pixel_per_mm[0]))
                self.linePixelPerMM_y.setText(str(self.para.pixel_per_mm[1]))
        elif self.tabWidget_2.currentIndex() == 1: # Points
            if len(self.cal_real_target) == 4:
                self.lineQuad1x.setText(str(self.cal_real_target[0][0]))
                self.lineQuad2x.setText(str(self.cal_real_target[0][1]))
                self.lineQuad3x.setText(str(self.cal_real_target[1][0]))
                self.lineQuad4x.setText(str(self.cal_real_target[1][1]))
                self.lineQuad1y.setText(str(self.cal_real_target[2][0]))
                self.lineQuad2y.setText(str(self.cal_real_target[2][1]))
                self.lineQuad3y.setText(str(self.cal_real_target[3][0]))
                self.lineQuad4y.setText(str(self.cal_real_target[3][1]))

        self.lineRotationAngle.setText(str(self.para.calibration_angle))

        self.load_calibration_image()

        self.set_photo_para(CAMERA_GAIN, value=self.para.gain)
        self.set_photo_para(CAMERA_EXPOSURE_TIME, value=self.para.exp_time)
        self.set_photo_para(CAMERA_ROI_X0, value=self.para.roi[0][0])
        self.set_photo_para(CAMERA_ROI_Y0, value=self.para.roi[0][1])
        self.set_photo_para(CAMERA_ROI_WIDTH, value=self.para.roi[1][0])
        self.set_photo_para(CAMERA_ROI_HEIGHT, value=self.para.roi[1][1])
        self.apply_roi()

        if self.para.filter_code is not None:
            self.comboFilter.setCurrentIndex(self.para.filter_code - 60000 + 1)
            self.load_filter_parameters(reset=False)
            for idx in range(self.listParameters.count()):
                widget = self.listParameters.itemWidget(self.listParameters.item(idx))
                for key, value in self.para.filter_para.items():
                    if widget.label.text() == key:
                        widget.linevalue.setText(str(value))

    def set_action(self):
        # Signal
        # Outside tab widgets
        self.pushSave.clicked.connect(self.save)
        self.pushLoad.clicked.connect(self.load)
        self.pushReset.clicked.connect(self.reset_all)

        
        self.pushOk.clicked.connect(self.click_ok)
        self.pushCancel.clicked.connect(self.click_cancel)

        base_path = os.path.abspath(os.path.dirname(__file__))
        self.comboSetup.addItem('')
        for item in os.listdir(os.path.join(base_path, 'setup')):
            if any(item.endswith(i) for i in ['yaml','yml']):
                self.comboSetup.addItem(os.path.join(base_path, 'setup', item))
        self.comboSetup.currentTextChanged.connect(lambda: self.load(self.comboSetup.currentText()))

        # Connection
        self.lineControllerIP1.setValidator(QIntValidator(self))
        self.lineControllerIP2.setValidator(QIntValidator(self))
        self.lineControllerIP3.setValidator(QIntValidator(self))
        self.lineControllerIP3.setValidator(QIntValidator(self))
        self.lineControllerIP5.setValidator(QIntValidator(self))

        self.checkCameraConnected.clicked.connect(lambda: self.set_checked(self.checkCameraConnected, self.para.cam_conn))
        self.checkControllerConnected.clicked.connect(lambda: self.set_checked(self.checkControllerConnected, self.para.ctl_conn))

        self.pushConnectCamera.clicked.connect(self.connect_camera)
        self.pushDisconnectCamera.clicked.connect(self.disconnect_camera)
        self.pushConnectController.clicked.connect(self.connect_server)
        self.pushDisconnectController.clicked.connect(self.disconnect_server)

        self.comboMonitor.addItem('')
        for i in range(NUMBER_OF_MONITORS):
            self.comboMonitor.addItem(f"{PV_NAME_RANK1}{i}")

        # Calibration
        ### Basic button & image
        self.labelOrigin.clicked.connect(self.draw_circle)
        self.labelOrigin.ldclicked.connect(self.expand_calibration_image)
        self.pushOpenImage.clicked.connect(self.open_calibration_image)
        self.pushCalCapture.clicked.connect(self.capture_calibration_image)
        self.pushConvert.clicked.connect(self.convert_calibration_image)
        ### Rotation
        self.lineRotationAngle.setValidator(QDoubleValidator(0.0, 360.0, 3))
        self.lineRotationAngle.editingFinished.connect(self.set_rotation_angle(2))
        self.pushAngleUp.clicked.connect(lambda: self.set_rotation_angle(0))
        self.pushAngleDown.clicked.connect(lambda: self.set_rotation_angle(1))
        ### Perspective matrix
        ##### Rectangle
        self.linePixelPerMM_x.setValidator(QDoubleValidator(0.0, 9999.99, 2))
        self.linePixelPerMM_y.setValidator(QDoubleValidator(0.0, 9999.99, 2))
        ##### Points
        self.lineQuad1x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad1y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad2x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad2y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad3x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad3y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad4x.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))
        self.lineQuad4y.setValidator(QDoubleValidator(-9999.99, 9999.99, 2))

        # Photo
        # FIXME
        self.checkConnection.clicked.connect(lambda: self.set_checked(self.checkConnection, self.para.cam_conn))
        self.checkCalibration.clicked.connect(lambda: self.set_checked(self.checkCalibration, self.para.cam_conn))


        self.pushConnectCamera_2.clicked.connect(self.connect_camera)
        self.pushCalibrate.clicked.connect(self.convert_calibration_image)
        self.pushCaptureImage.clicked.connect(lambda: self.take_a_picture(False))

        self.labelImage.move.connect(self.set_roi)
        self.labelImage.ldclicked.connect(self.apply_roi)
        self.labelImage.rdclicked.connect(lambda: self.apply_roi(True))

        self.sliderGain.valueChanged.connect(lambda: self.set_photo_para(CAMERA_GAIN, slider=True))
        self.sliderExposureTime.valueChanged.connect(lambda: self.set_photo_para(CAMERA_EXPOSURE_TIME, slider=True))
        
        self.lineGain.setValidator(QIntValidator(self))
        self.lineExposureTime.setValidator(QIntValidator(self))
        self.lineGain.textEdited.connect(lambda: self.set_photo_para(CAMERA_GAIN, slider=False))
        self.lineExposureTime.textEdited.connect(lambda: self.set_photo_para(CAMERA_EXPOSURE_TIME, slider=False))

        self.pushApplyConf.clicked.connect(self.take_a_picture)

        self.sliderX0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_X0, slider=True))
        self.sliderY0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_Y0, slider=True))
        self.sliderWidth.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_WIDTH, slider=True))
        self.sliderHeight.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_HEIGHT, slider=True))

        self.comboFilter.currentTextChanged.connect(self.load_filter_parameters)
        self.pushApplyFilter.clicked.connect(self.apply_filter_parameters)

    def save(self, last=False):
        base_path = os.path.abspath(os.path.dirname(__file__))
        if not last:
            fname = QFileDialog.getSaveFileName(self, 'Save', os.path.join(base_path, 'setup'), filter="Yaml file (*.yaml *.yml)")[0]
            if not (fname.endswith('.yaml') or fname.endswith('.yml')):
                fname = fname + '.yaml'
        else:
            fname = os.path.join(base_path, 'setup', 'last.yaml')

        if self.para.calibrated:
            if self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()) == 'Rectangle':
                para = {'Width': self.para.pixel_per_mm[0], 'Height': self.para.pixel_per_mm[1]}
            else:
                para = {'Point1': self.cal_real_target[0],
                        'Point2': self.cal_real_target[1],
                        'Point3': self.cal_real_target[2],
                        'Point4': self.cal_real_target[3],
                        }
        else:
            if self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()) == 'Rectangle':
                para = {'Width': 1.0, 'Height': 1.0}
            else:
                para = {'Point1': [[0,0],[0,0]],
                        'Point2': [[0,0],[0,0]],
                        'Point3': [[0,0],[0,0]],
                        'Point4': [[0,0],[0,0]],
                        }

        perspective_para = {"TargetPoints":self.cal_target_points,
                            "Parameter":para}

        fout = open(fname, 'w')
        fout.write(textwrap.dedent(f"""\
            CameraSDK: "{self.para.sdk}"
            CameraURL: "{self.para.url}"
            ControllerUse: {str(self.checkUseControlServer.isChecked())}
            ControllerIP: {str(self.para.server_ip)}
            MonitorNumber: {self.para.monitor_id}
            Gain: {self.para.gain}
            ExposureTime: {self.para.exp_time}
            ROI: {str(self.para.roi)}
            FilterType: "{self.para.filter_code}"
            FilterParameter: {str(self.para.filter_para)}
            CalibrationImage: "{str(self.calibration_image_name)}"
            CalibrationAngle: {self.para.calibration_angle}
            PerspectiveMatrixMethod: {str(self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()))}
            PerspectiveMatrixParameters: {str(perspective_para)}
            """))
        fout.close()

    def load(self, fname=''):
        if fname == '':
            extension = ["Yaml file (*.yaml *.yml)"]
            fname = QFileDialog.getOpenFileName(self, "Select Setup file", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            self.logger.info(f"Open Configuration file {fname}.")
            with open(fname, 'r') as f:
                cfg = yaml.load(f, Loader=yaml.FullLoader)

                # Network tab
                ### Camera
                self.para.sdk = str(cfg['CameraSDK'])
                self.para.url = str(cfg['CameraURL'])

                self.lineCameraAddr.setText(self.para.url)
                for idx in range(self.comboSDKType.count()):
                    if self.comboSDKType.itemText(idx) == self.para.sdk:
                        self.comboSDKType.setCurrentIndex(idx)
                        break

                self.connect_camera()

                ### Controller
                self.para.server_ip = str(cfg['ControllerIP'])
                self.para.monitor_id = str(cfg['MonitorNumber'])
                self.checkUseControlServer.setChecked(cfg['ControllerUse'])
                ip, port = self.server_ip.split(':')
                ip = ip.split('.')
                if len(ip) == 4:
                    self.lineControllerIP1.setText(ip[0]) 
                    self.lineControllerIP2.setText(ip[1])
                    self.lineControllerIP3.setText(ip[2])
                    self.lineControllerIP4.setText(ip[3])
                if port != '':
                    self.lineControllerIP5.setText(port)

                self.connect_server()

                # Calibration tab
                self.calibration_image_name = str(cfg['CalibrationImage'])
                self.cal_target_points = cfg['PerspectiveMatrixParameters']['TargetPoints']
                if self.tabWidget_2.tabText(0) == cfg['PerspectiveMatrixMethod']:
                    self.para.pixel_per_mm = [float(cfg['PerspectiveMatrixParameters']['Parameter']['Width']), float(cfg['PerspectiveMatrixParameters']['Parameter']['Height'])]
                else:
                    tmp = cfg['PerspectiveMatrixParameters']['Parameter']
                    self.cal_real_target = [tmp['Point1'], tmp['Point2'], tmp['Point3'], tmp['Point4']]

                self.para.calibration_angle = cfg['CalibrationAngle']

                for i in range(len(self.tabWidget_2.count())):
                    if str(cfg['PerspectiveMatrixMethod']) == self.tabWidget_2.tabText(i):
                        self.tabWidget_2.setCurrentIndex(i)
                        break

                if self.tabWidget_2.currentIndex() == 0: # Rectangle
                    self.linePixelPerMM_x.setText(str(self.para.pixel_per_mm[0]))
                    self.linePixelPerMM_y.setText(str(self.para.pixel_per_mm[1]))
                elif self.tabWidget_2.currentIndex() == 1: # Points
                    self.lineQuad1x.setText(str(self.cal_real_target[0][0]))
                    self.lineQuad2x.setText(str(self.cal_real_target[0][1]))
                    self.lineQuad3x.setText(str(self.cal_real_target[1][0]))
                    self.lineQuad4x.setText(str(self.cal_real_target[1][1]))
                    self.lineQuad1y.setText(str(self.cal_real_target[2][0]))
                    self.lineQuad2y.setText(str(self.cal_real_target[2][1]))
                    self.lineQuad3y.setText(str(self.cal_real_target[3][0]))
                    self.lineQuad4y.setText(str(self.cal_real_target[3][1]))

                self.lineRotationAngle.setText(str(self.para.calibration_angle))

                self.load_calibration_image()

                # Image tab
                self.set_photo_para(CAMERA_GAIN, value=cfg['Gain'])
                self.set_photo_para(CAMERA_EXPOSURE_TIME, value=cfg['ExposureTime'])

                self.take_a_picture()

                self.para.filter_code = int(cfg['FilterType'])
                self.para.filter_para = cfg['FilterParameter']
                for idx in range(self.comboFilter.count()):
                    if self.comboFilter.itemText(idx) == cfg['FilterType']:
                        self.comboFilter.setCurrentIndex(idx)
                        break

                self.load_filter_parameters()
                self.apply_filter_parameters()

                self.set_photo_para(CAMERA_ROI_X0, value=cfg['ROI'][0][0])
                self.set_photo_para(CAMERA_ROI_Y0, value=cfg['ROI'][0][1])
                self.set_photo_para(CAMERA_ROI_WIDTH, value=cfg['ROI'][1][0])
                self.set_photo_para(CAMERA_ROI_HEIGHT, value=cfg['ROI'][1][1])
                self.apply_roi()

    def reset_all(self):
        pass

    ### Methods for Connection
    from setup_connection import connect_camera
    from setup_connection import disconnect_camera
    from setup_connection import connect_server
    from setup_connection import disconnect_server

    ### Methods for Calibration
    from setup_calibration import open_calibration_image
    from setup_calibration import draw_calibration_image
    from setup_calibration import load_calibration_image
    from setup_calibration import capture_calibration_image
    from setup_calibration import expand_calibration_image
    from setup_calibration import convert_calibration_image
    from setup_calibration import set_rotation_angle
    from setup_calibration import draw_circle
    from setup_calibration import move_circle

    ### Methods for Image setup
    from setup_image import set_photo_para
    from setup_image import take_a_picture
    from setup_image import draw_image
    from setup_image import draw_roi_rectangle
    from setup_image import set_roi
    from setup_image import apply_roi
    from setup_image import load_filter_parameters
    from setup_image import apply_filter_parameters
    from setup_image import draw_pvhist
