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
        self.captured_image_screen_size = (550, 550)

        self.calibration_image = None
        self.calibration_image_aratio = None
        self.calibration_image_name = ""
        self.calibration_image_backup = None
        self.calibration_image_screen_size = (450, 450)

        self.perspective_method = None
        self.original_points = self.destination_points = self.resized_points  = []

        self.set_widgets_default()
        self.set_action()

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
        if reply == True:
            event.accept()
        else:
            event.ignore()

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

        self.set_checked(self.checkUseControlServer, self.para.ctl_conn)
        if self.para.cam_conn:
            self.connect_camera()
        if self.para.ctl_conn:
            self.connect_server()

        self.sliderGain.setValue(self.para.gain)
        self.sliderExposureTime.setValue(self.para.exp_time)
        self.sliderX0.setValue(self.para.roi[0][0])
        self.sliderY0.setValue(self.para.roi[0][1])
        self.sliderWidth.setValue(self.para.roi[1][0])
        self.sliderHeight.setValue(self.para.roi[1][1])
        if not self.para.roi == [[0,0], [0,0]]:
            self.select_roi = True
        else:
            self.select_roi = False
        if self.para.filter_code is not None:
            self.comboFilter.setCurrentIndex(self.para.filter_code - 60000 + 1)
            self.load_filter_parameters(reset=False)
            for idx in range(self.listParameters.count()):
                widget = self.listParameters.itemWidget(self.listParameters.item(idx))
                for key, value in self.para.filter_para.items():
                    if widget.label.text() == key:
                        widget.linevalue.setText(str(value))
        if self.perspective_method == 'Rectangle':
            self.tabWidget_2.setCurrentIndex(0)
            self.linePixelPerMM_x.setText(str(self.para.pixel_per_mm[0]))
            self.linePixelPerMM_y.setText(str(self.para.pixel_per_mm[1]))
        elif self.perspective_method == 'Point':
            self.tabWidget_2.setCurrentIndex(1)
            self.lineQuad1x.setText(str(self.points[0]))
            self.lineQuad2x.setText(str(self.points[1]))
            self.lineQuad3x.setText(str(self.points[2]))
            self.lineQuad4x.setText(str(self.points[3]))
            self.lineQuad1y.setText(str(self.points[4]))
            self.lineQuad2y.setText(str(self.points[5]))
            self.lineQuad3y.setText(str(self.points[6]))
            self.lineQuad4y.setText(str(self.points[7]))
    
    def set_action(self):
        # Signal
        # Outside tab widgets
        self.pushSave.clicked.connect(self.save)
        self.pushLoad.clicked.connect(lambda: self.load())
        #self.pushReset.clicked.connect(self.reset_parameters)
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

        self.pushConnectCamera.clicked.connect(self.connect_camera())
        self.pushDisconnectCamera.clicked.connect(self.disconnect_camera())
        self.pushConnectController.clicked.connect(self.connect_server())
        self.pushDisconnectController.clicked.connect(self.disconnect_server())

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
        self.lineRotationAngle.editingFinished.connect(lambda: self.draw_calibration_image(self.calibration_image))
        self.pushAngleUp.clicked.connect(lambda: self.set_rotation_angle(True))
        self.pushAngleDown.clicked.connect(lambda: self.set_rotation_angle(False))
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
        self.labelImage.move.connect(self.set_roi)
        self.labelImage.ldclicked.connect(self.apply_roi)
        self.labelImage.rdclicked.connect(lambda: self.apply_roi(True))

        self.sliderGain.valueChanged.connect(lambda: self.set_photo_para(CAMERA_GAIN))
        self.sliderExposureTime.valueChanged.connect(lambda: self.set_photo_para(CAMERA_EXPOSURE_TIME))
        
        self.lineGain.setValidator(QIntValidator(self))
        self.lineExposureTime.setValidator(QIntValidator(self))
        self.lineGain.textEdited.connect(lambda: self.set_photo_para(CAMERA_GAIN, slider=False))
        self.lineExposureTime.textEdited.connect(lambda: self.set_photo_para(CAMERA_EXPOSURE_TIME, slider=False))

        self.pushApplyConf.clicked.connect(self.take_a_picture)

        self.sliderX0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_X0))
        self.sliderY0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_Y0))
        self.sliderWidth.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_WIDTH))
        self.sliderHeight.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_HEIGHT))

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

        camera_url = self.lineCameraAddr.text()
        controller_ip = '.'.join(i.text() for i in[self.lineControllerIP1, self.lineControllerIP2, self.lineControllerIP3, self.lineControllerIP4])

        if self.perspective_method == 'Rectangle':
            para = {'Width': self.para.pixel_per_mm[0], 'Height': self.para.pixel_per_mm[1]}
        else:
            para = {'Point1': [self.lineQuad1x.text(), self.lineQuad1y.text()],
                    'Point2': [self.lineQuad2x.text(), self.lineQuad2y.text()],
                    'Point3': [self.lineQuad3x.text(), self.lineQuad3y.text()],
                    'Point4': [self.lineQuad4x.text(), self.lineQuad4y.text()],
                    }

        perspective_para = {"OriginalPoint":self.original_points,
                            "Parameter":para}

        roi_slider = [[self.sliderX0.value(), self.sliderY0.value()], [self.sliderWidth.value(), self.sliderHeight.value()]]

        fout = open(fname, 'w')
        fout.write(textwrap.dedent(f"""\
            Auto: {str(last)}
            CameraSDK: "{self.camera_sdk}"
            CameraURL: "{camera_url}"
            ControllerUse: {str(self.checkUseControlServer.isChecked())}
            ControllerIP: {controller_ip}
            ControllerPort: {self.lineControllerIP5.text()}
            Gain: {self.gain}
            ExposureTime: {self.para.exp_time}
            ROI: {str(self.para.roi)}
            ROISlider: {str(roi_slider)}
            FilterType: "{self.comboFilter.currentText()}"
            FilterParameter: {str(self.para.filter_para)}
            CalibrationImage: "{str(self.calibration_image_name)}"
            Rotation: {self.lineRotationAngle.text()}
            PerspectiveMatrixMethod: {str(self.perspective_method)}
            PerspectiveMatrixParameters: {str(perspective_para)}
            """))
        fout.close()

    def load(self, fname=''):
        if fname == '':
            extension = ["Yaml file (*.yaml *.yml)"]
            fname = QFileDialog.getOpenFileName(self, "Select Setup file", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            with open(fname, 'r') as f:
                cfg = yaml.load(f, Loader=yaml.FullLoader)
                
                self.lineCameraAddr.setText(str(cfg['CameraURL']))
                self.camera_sdk = str(cfg['CameraSDK'])
                for idx in range(self.comboSDKType.count()):
                    if self.comboSDKType.itemText(idx) == self.camera_sdk:
                        self.comboSDKType.setCurrentIndex(idx)
                        break
                
                self.connect_camera()

                if cfg['ControllerUse']:
                    self.checkUseControlServer.setChecked(True)
                    controller_ip = str(cfg['ControllerIP']).split('.')
                    if len(controller_ip):
                        self.lineControllerIP1.setText(controller_ip[0]) 
                        self.lineControllerIP2.setText(controller_ip[1])
                        self.lineControllerIP3.setText(controller_ip[2])
                        self.lineControllerIP4.setText(controller_ip[3])
                    if str(cfg['ControllerPort']) != 'None':
                        self.lineControllerIP5.setText(str(cfg['ControllerPort']))
                    self.connect_server()

                self.gain = int(cfg['Gain'])
                self.sliderGain.setValue(self.gain)
                self.para.exp_time = int(cfg['ExposureTime'])
                self.sliderExposureTime.setValue(self.para.exp_time)


                for idx in range(self.comboFilter.count()):
                    if self.comboFilter.itemText(idx) == cfg['FilterType']:
                        self.comboFilter.setCurrentIndex(idx)
                        self.load_filter_parameters()
                        break
                self.para.filter_para = cfg['FilterParameter']
                for idx in range(self.listParameters.count()):
                    widget = self.listParameters.itemWidget(self.listParameters.item(idx))
                    for key, value in self.para.filter_para.items():
                        if widget.label.text() == key:
                            widget.linevalue.setText(str(value))

                self.calibration_image_name = str(cfg['CalibrationImage'])
                self.lineRotationAngle.setText(str(cfg['Rotation']))
                self.perspective_method = str(cfg['PerspectiveMatrixMethod'])
                self.original_points = cfg['PerspectiveMatrixParameters']['OriginalPoint']
                if self.perspective_method == 'Rectangle':
                    self.tabWidget_2.setCurrentIndex(0)
                    self.linePixelPerMM_x.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Width']))
                    self.linePixelPerMM_y.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Height']))
                elif self.perspective_method == 'Point':
                    self.tabWidget_2.setCurrentIndex(1)
                    self.lineQuad1x.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point1'][0]))
                    self.lineQuad2x.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point2'][0]))
                    self.lineQuad3x.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point3'][0]))
                    self.lineQuad4x.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point4'][0]))
                    self.lineQuad1y.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point1'][1]))
                    self.lineQuad2y.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point2'][1]))
                    self.lineQuad3y.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point3'][1]))
                    self.lineQuad4y.setText(str(cfg['PerspectiveMatrixParameters']['Parameter']['Point4'][1]))

                self.load_calibration_image()
                self.lineGain.setText(str(cfg['Gain']))
                self.set_photo_para(CAMERA_GAIN, False)
                self.lineExposureTime.setText(str(cfg['ExposureTime']))
                self.set_photo_para(CAMERA_EXPOSURE_TIME, False)

                self.take_a_picture()

                roi_slider = cfg['ROISlider']
                self.sliderX0.setValue(roi_slider[0][0])
                self.sliderY0.setValue(roi_slider[0][1])
                self.sliderWidth.setValue(roi_slider[1][0])
                self.sliderHeight.setValue(roi_slider[1][1])
                self.para.roi = cfg['ROI']
                if self.para.roi != [[0, 0], [0, 0]]:
                    self.apply_roi()

    def click_ok(self):
        base_path = os.path.abspath(os.path.dirname(__file__))

        if self.checkSaveLast.isChecked():
            self.save(last=True)
        else:
            if os.path.exists(os.path.join(base_path,'setup','last.yaml')):
                os.remove(os.path.join(base_path, 'setup', 'last.yaml'))
        if self.checkCameraConnected.isChecked():
            self.camera_connected = True
        if self.checkControllerConnected.isChecked():
            self.controller_connected = True

        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            #self.initialize_parameters(True)
            #self.reset_all = True
            self.reject()
            return True
        else:
            return False

    def return_para(self):
        return super().exec_()

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
