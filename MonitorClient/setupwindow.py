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
from custom_classes import DigiLabel
from ui_setupwindow import Ui_SetupWindow

class SetupWindow(QDialog, Ui_SetupWindow):
    send_signal_to_blueberry = Signal(int, int)
    def __init__(self, parent):
        super(SetupWindow, self).__init__()
        self.parent = parent
        self.reset_all = False
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

        #self.initialize_parameter(reset=False)
        self.set_action()

        #self.show()

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
                if any(i == event.key() for i in [Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down]):
                    self.move_circle(event.key())

    def keyReleaseEvent(self, event):
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

    # Common Methods
    def initialize_parameter(self, reset):
        if reset:
            self.camera_connected = self.controller_connected = self.select_ROI = self.calibrated = self.draw_square = False

            self.camera_sdk = self.comboSDKType.currentText()
            self.monitor_number = self.comboMonitor.currentText()

            self.captured_image = None
            self.captured_image_aratio = None
            self.captured_image_screen_size = (550, 550)

            self.calibration_image = None
            self.calibration_image_aratio = None
            self.calibration_image_name = ""
            self.calibration_image_screen_size = (450, 450)
            self.calibration_image_backup = None

            self.labelImage.resize(self.captured_image_screen_size[0], self.captured_image_screen_size[1])
            self.labelOrigin.resize(self.calibration_image_screen_size[0], self.calibration_image_screen_size[1])
            self.labelTrans.resize(self.calibration_image_screen_size[0], self.calibration_image_screen_size[1])

            self.perspective_method = None

            self.gain = 50
            self.exposure_time = 30000
            self.ROI = [[0,0], [0,0]] # [(StartPoint), (width, height)]
            self.image_for_ROI = None

            self.filter_code = self.filter_para = None
            self.calibration_angle = 0

            self.original_points = self.destination_points = self.resized_points = self.pixel_per_mm = []
        else:
            self.connect_network(self.parent.blueberry, self.checkCameraConnected)
            if self.checkUseControlServer.isChecked():
                self.connect_network(self.parent.blackberry, self.checkControllerConnected)
            self.sliderGain.setValue(self.gain)
            self.sliderExposureTime.setValue(self.exposure_time)
            self.sliderX0.setValue(self.ROI[0][0])
            self.sliderY0.setValue(self.ROI[0][1])
            self.sliderWidth.setValue(self.ROI[1][0])
            self.sliderHeight.setValue(self.ROI[1][1])
            if not self.ROI == [[0,0], [0,0]]:
                self.select_ROI = True
            else:
                self.select_ROI = False
            if self.filter_code is not None:
                self.comboFilter.setCurrentIndex(self.filter_code - 60000 + 1)
                self.load_filter_parameters(reset=False)
                for idx in range(self.listParameters.count()):
                    widget = self.listParameters.itemWidget(self.listParameters.item(idx))
                    for key, value in self.filter_para.items():
                        if widget.label.text() == key:
                            widget.linevalue.setText(str(value))
            if self.perspective_method == 'Rectangle':
                self.tabWidget_2.setCurrentIndex(0)
                self.linePixelPerMM_x.setText(str(self.pixel_per_mm[0]))
                self.linePixelPerMM_y.setText(str(self.pixel_per_mm[1]))
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

    def set_checked(self, checkbox, state):
        if state:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)
    
    def set_action(self):
        # Signal
        self.send_signal_to_blueberry.connect(self.parent.blueberry.receive_signal)
        # Outside tab widgets
        self.pushSave.clicked.connect(self.save)
        self.pushLoad.clicked.connect(lambda: self.load())
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

        self.checkCameraConnected.clicked.connect(lambda: self.set_checked(self.checkCameraConnected, self.parent.blueberry.connected))
        self.checkControllerConnected.clicked.connect(lambda: self.set_checked(self.checkControllerConnected, self.parent.blackberry.connected))

        self.pushConnectCamera.clicked.connect(lambda: self.connect_network(self.parent.blueberry, self.checkCameraConnected))
        self.pushConnectController.clicked.connect(lambda: self.connect_network(self.parent.blackberry, self.checkControllerConnected))

        self.comboSDKType.currentTextChanged.connect(self.set_sdk)

        self.comboMonitor.addItem('')
        for i in range(NUMBER_OF_MONITORS):
            self.comboMonitor.addItem(f"{PV_NAME_RANK1}{i}")

        self.comboMonitor.currentTextChanged.connect(self.set_monitor)

        # Photo
        self.labelImage.move.connect(self.set_ROI)
        self.labelImage.ldclicked.connect(self.apply_ROI)
        self.labelImage.rdclicked.connect(lambda: self.apply_ROI(True))

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

        self.pushFilterApply.clicked.connect(lambda: self.draw_image(self.captured_image, self.labelImage, self.captured_image_screen_size, self.captured_image_aratio))

        # Calibration
        ### Basic button & image
        self.labelOrigin.clicked.connect(self.draw_circle)
        self.pushOpenImage.clicked.connect(self.open_calibration_image)
        self.pushCalCapture.clicked.connect(self.capture_calibration_image)
        self.pushConvert.clicked.connect(self.convert_image)
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
            para = {'Width': self.pixel_per_mm[0], 'Height': self.pixel_per_mm[1]}
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
            ExposureTime: {self.exposure_time}
            ROI: {str(self.ROI)}
            ROISlider: {str(roi_slider)}
            FilterType: "{self.comboFilter.currentText()}"
            FilterParameter: {str(self.filter_para)}
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
                
                self.connect_network(self.parent.blueberry, self.checkCameraConnected)

                if cfg['ControllerUse']:
                    self.checkUseControlServer.setChecked(True)
                    controller_ip = str(cfg['ControllerIP']).split('.')
                    if len(controller_ip):
                        self.lineControllerIP1.setText(controller_ip[0]) 
                        self.lineControllerIP2.setText(controller_ip[1])
                        self.lineControllerIP3.setText(controller_ip[2])
                        self.lineControllerIP4.setText(controller_ip[3])
                    self.lineControllerIP5.setText(str(cfg['ControllerPort']))
                    self.connect_network(self.parent.blackberry, self.checkControllerConnected)

                self.gain = int(cfg['Gain'])
                self.sliderGain.setValue(self.gain)
                self.exposure_time = int(cfg['ExposureTime'])
                self.sliderExposureTime.setValue(self.exposure_time)


                for idx in range(self.comboFilter.count()):
                    if self.comboFilter.itemText(idx) == cfg['FilterType']:
                        self.comboFilter.setCurrentIndex(idx)
                        self.load_filter_parameters()
                        break
                self.filter_para = cfg['FilterParameter']
                for idx in range(self.listParameters.count()):
                    widget = self.listParameters.itemWidget(self.listParameters.item(idx))
                    for key, value in self.filter_para.items():
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

                self.load_calibrated_image()
                self.take_a_picture()

                roi_slider = cfg['ROISlider']
                self.sliderX0.setValue(roi_slider[0][0])
                self.sliderY0.setValue(roi_slider[0][1])
                self.sliderWidth.setValue(roi_slider[1][0])
                self.sliderHeight.setValue(roi_slider[1][1])
                self.ROI = cfg['ROI']
                self.apply_ROI()

    ### Methods for Connection
    def set_sdk(self):
        self.camera_sdk = self.comboSDKType.currentText()

    def set_monitor(self):
        if self.parent.blackberry is not None:
            self.parent.blackberry.set_monitor(self.comboMonitor.currentText())

    def connect_network(self, berry, checkbox):
        if berry.name == "Network Camera":
            url = self.lineCameraAddr.text()
            self.parent.blueberry.sdk = self.camera_sdk
            self.logger.info(f"Set SDK as {self.camera_sdk}.")
        else:
            if not self.checkUseControlServer.isChecked():
                self.logger.warning(f"Please, check 'Use Network Camera Controller Server' first.")
                return
            ip1, ip2, ip3, ip4, port = self.lineControllerIP1, self.lineControllerIP2, self.lineControllerIP3, self.lineControllerIP4, self.lineControllerIP5
            if any(i.text() == '' for i in [ip1, ip2, ip3, ip4]):
                return
            url = '.'.join(i.text() for i in [ip1, ip2, ip3, ip4])+':'+port.text()

        if berry.connected:
            self.logger.info(f"{berry.name} is already connected.")
            self.set_checked(checkbox, berry.connected)
            if berry.name == 'Network Camera':
                self.camera_connected = True
            else:
                self.controller_connected = True
        else:
            self.logger.info(f"Try to connect to {berry.name}...")
            message = berry.connection(url)
            self.set_checked(checkbox, berry.connected)

            if berry.name == 'Network Camera':
                self.camera_connected = berry.connected
            else:
                self.controller_connected = berry.connected

            if 'ERROR ' in message:
                message = message.replace('ERROR ','')
                self.logger.error(message)
            elif 'INFO ' in message:
                message  = message.replace('INFO ','')
                self.logger.info(message)

        if berry.name == 'Network Camera':
            self.take_a_picture()
        
        if self.camera_connected:
            self.set_checked(self.checkConnection, True)

    ### Methods for Photo
    def set_photo_para(self, idx, slider=True):
        if self.camera_connected:
            if idx == CAMERA_GAIN:
                if slider:
                    self.gain = self.sliderGain.value()
                    self.lineGain.setText(str(self.sliderGain.value()))
                else:
                    if self.lineGain.text() == '': return
                    self.gain = int(self.lineGain.text())
                    self.sliderGain.setValue(self.gain)
                self.send_signal_to_blueberry.emit(idx, self.gain)
            elif idx == CAMERA_EXPOSURE_TIME:
                if slider:
                    self.exposure_time = self.sliderExposureTime.value()
                    self.lineExposureTime.setText(str(self.sliderExposureTime.value()))
                else:
                    if self.lineExposureTime.text() == '': return
                    self.exposure_time = int(self.lineExposureTime.text())
                    self.sliderExposureTime.setValue(self.exposure_time)
                self.send_signal_to_blueberry.emit(idx, self.exposure_time)
            elif idx == CAMERA_ROI_X0:
                self.ROI[0][0] = round(self.captured_image.shape[1] * self.sliderX0.value() / 1000.0)
                self.lineX0.setText(str(self.sliderX0.value()/10))
                self.labelSPPixel.setText(f"({self.ROI[0][0]}, {self.ROI[0][1]}) pixel")
                self.draw_rectangle()
            elif idx == CAMERA_ROI_Y0:
                self.ROI[0][1] = round(self.captured_image.shape[0] * self.sliderY0.value() / 1000.0)
                self.lineY0.setText(str(self.sliderY0.value()/10))
                self.labelSPPixel.setText(f"({self.ROI[0][0]}, {self.ROI[0][1]}) pixel")
                self.draw_rectangle()
            elif idx == CAMERA_ROI_WIDTH:
                self.ROI[1][0] = round(self.captured_image.shape[1] * self.sliderWidth.value() / 1000.0)
                self.lineWidth.setText(str(self.sliderWidth.value()/10))
                self.labelSizePixel.setText(f"({self.ROI[1][0]}, {self.ROI[1][1]}) pixel")
                self.draw_rectangle()
            elif idx == CAMERA_ROI_HEIGHT:
                self.ROI[1][1] = round(self.captured_image.shape[0] * self.sliderHeight.value() / 1000.0)
                self.lineHeight.setText(str(self.sliderHeight.value()/10))
                self.labelSizePixel.setText(f"({self.ROI[1][0]}, {self.ROI[1][1]}) pixel")
                self.draw_rectangle()

        if (idx == i for i in [CAMERA_GAIN, CAMERA_EXPOSURE_TIME, CAMERA_ROI_X0, CAMERA_ROI_Y0, CAMERA_ROI_WIDTH, CAMERA_ROI_HEIGHT]):
            if self.camera_connected and self.captured_image is None:
                self.take_a_picture()

    def take_a_picture(self, calibration=False):
        if not self.camera_connected: return
        self.send_signal_to_blueberry.emit(CAMERA_GAIN, self.gain)
        self.send_signal_to_blueberry.emit(CAMERA_EXPOSURE_TIME, self.exposure_time)
        if not calibration:
            self.captured_image = self.parent.blueberry.take_a_picture(True)
            if self.captured_image_aratio is None:
                self.captured_image_aratio = float(self.captured_image.shape[1]) / float(self.captured_image.shape[0])
            
            self.draw_image(self.captured_image, self.labelImage, self.captured_image_screen_size, self.captured_image_aratio)
        else:
            self.calibration_image = self.parent.blueberry.take_a_picture(True)
            if self.calibration_image_aratio is None:
                self.calibration_image_aratio = float(self.calibration_image.shape[1]) / float(self.calibration_image.shape[0])
            
            self.calibration_image_backup = self.calibration_image.copy()
            self.draw_image(self.calibration_image, self.labelOrigin, self.calibration_image_screen_size, self.calibration_image_aratio, image_processing=False)

    def draw_image(self, image, label, screen_size, aspect_ratio, image_processing=True):
        image_copy = copy.deepcopy(image)
        if image_processing:
            if self.calibrated:
                image_copy = ut.transform_image(image_copy, self.original_points, self.destination_points)
            image_copy = ut.filter_image(image_copy, self.filter_code, self.filter_para)
            image_copy = ut.slice_image(image_copy, self.ROI)
            dsize = (screen_size[0], screen_size[1])
        else:
            if aspect_ratio > 1:
                dsize = (screen_size[0], round(screen_size[0] / aspect_ratio))
            elif aspect_ratio < 1:
                dsize = (round(screen_size[1] * aspect_ratio), screen_size[1])
            else:
                dsize = (screen_size[0], screen_size[1])

        height, width = image_copy.shape[0], image_copy.shape[1]

        if 0.99 < width / height < 1.01:
            dsize = (screen_size[0], screen_size[1])

        resized_image = cv2.resize(image_copy, dsize=dsize, interpolation=cv2.INTER_LINEAR)
        self.image_for_ROI = copy.deepcopy(resized_image)

        if len(resized_image.shape) == 3:
            height, width, channel = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(qImg)

        label.resize(width, height)
        label.setPixmap(pixmap)

    def draw_rectangle(self):
        if self.select_ROI or self.image_for_ROI is None: return
        resized_image = copy.deepcopy(self.image_for_ROI)
        
        if len(resized_image.shape) == 3:
            height, width, channel = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = resized_image.shape
            qImg = QImage(resized_image.data, width, height, width, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qImg)
        painter = QPainter(pixmap)
        painter.setPen(QPen(QColor(3, 252, 127), 1.5, Qt.DashLine))

        x = pixmap.width() * self.sliderX0.value() / 1000.0
        y = pixmap.height() * self.sliderY0.value() / 1000.0
        width = pixmap.width() * self.sliderWidth.value() / 1000.0
        height = pixmap.height() * self.sliderHeight.value() / 1000.0

        painter.drawRect(x, y, width, height)
        painter.end()
        self.labelImage.setPixmap(pixmap)

    def set_ROI(self):
        if not self.camera_connected or self.select_ROI or not self.labelImage.left: return

        if self.labelImage.x < self.labelImage.x_end and self.labelImage.y < self.labelImage.y_end:
            x = self.labelImage.x
            y = self.labelImage.y
        elif self.labelImage.x > self.labelImage.x_end and self.labelImage.y < self.labelImage.y_end:
            x = self.labelImage.x_end
            y = self.labelImage.y
        elif self.labelImage.x > self.labelImage.x_end and self.labelImage.y > self.labelImage.y_end:
            x = self.labelImage.x_end
            y = self.labelImage.y_end
        else:
            x = self.labelImage.x
            y = self.labelImage.y_end
        width = abs(self.labelImage.x - self.labelImage.x_end)
        height = abs(self.labelImage.y - self.labelImage.y_end)

        if self.draw_square:
            height = width

        self.sliderX0.setValue(x / self.labelImage.width() * 1000)
        self.sliderY0.setValue(y / self.labelImage.height() * 1000)
        self.sliderWidth.setValue(width / self.labelImage.width() * 1000)
        self.sliderHeight.setValue(height / self.labelImage.height() * 1000)

    def apply_ROI(self, reset=False):
        if reset:
            self.ROI = [[0,0],[0,0]]

            self.sliderX0.setValue(0)
            self.sliderY0.setValue(0)
            self.sliderWidth.setValue(0)
            self.sliderHeight.setValue(0)

            self.select_ROI = False
        else:
            self.select_ROI = True

        self.draw_image(self.captured_image, self.labelImage, self.captured_image_screen_size, self.captured_image_aratio)

    def load_filter_parameters(self, reset=True):
        class Item(QWidget):
            def __init__(self):
                QWidget.__init__(self)
                self.layout = QBoxLayout(QBoxLayout.LeftToRight)

            def add_lineedit(self, name, makebtn=False):
                self.label = QLabel(name)
                self.linevalue = QLineEdit()
                self.layout.addWidget(self.label)
                self.layout.addWidget(self.linevalue)
                if makebtn:
                    def click_open(line):
                        fname = QFileDialog.getExistingDirectory(self, "Select Background Image File")
                        line.setText(fname)
                    self.pushbtn = QPushButton("Open")
                    self.pushbtn.clicked.connect(lambda: click_open(self.linevalue))
                    self.layout.addWidget(self.pushbtn)
                self.layout.setSizeConstraint(QBoxLayout.SetFixedSize)
                self.setLayout(self.layout)

        def set_value(name, value):
            if value == '': return
            if name == 'background file':
                value = str(value)
            else:
                value = int(value)
            self.filter_para[name] = value

        if reset:
            if self.comboFilter.currentText() == 'No Filter':
                self.filter_code = None
                self.filter_para = None
            elif self.comboFilter.currentText() == 'Background Substraction':
                self.filter_code = BKG_SUBSTRACTION
                self.filter_para = {'background file':''}
            elif self.comboFilter.currentText() == 'Gaussian':
                self.filter_code = GAUSSIAN_FILTER
                self.filter_para = {'x kernal size':0, 'y kernal size':0, 'sigmaX':0}
            elif self.comboFilter.currentText() == 'Median':
                self.filter_code = MEDIAN_FILTER
                self.filter_para = {'kernal size':0}
            elif self.comboFilter.currentText() == 'Bilateral':
                self.filter_code = BILATERAL_FILTER
                self.filter_para = {'kernal size':0, 'sigma color':0, 'sigma space':0}
            else:
                return

        self.listParameters.clear()
        if self.filter_para is not None:
            for name in self.filter_para.keys():
                flag = False
                if name == 'background file': flag = True
                witem = QListWidgetItem(self.listParameters)
                item = Item()
                item.add_lineedit(name, makebtn=flag)
                item.linevalue.textChanged.connect(lambda: set_value(item.label.text(), item.linevalue.text()))
                item.linevalue.returnPressed.connect(lambda: set_value(item.label.text(), item.linevalue.text()))
                self.listParameters.setItemWidget(witem, item)
                self.listParameters.addItem(witem)
                witem.setSizeHint(item.sizeHint())

    ### Methods for Calibration
    def open_calibration_image(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            self.calibration_image_name = fname
            self.original_points = []
            self.destination_points = []
            self.resized_points = []
            self.load_calibrated_image()
    
    ############################ 20211115 ############################
    def draw_calibration_image(self, image, origin=True):
        if image is None: return
        #resized_image = cv2.resize(image, dsize=self.calibration_image_screen_size, interpolation=cv2.INTER_LINEAR)
        #height, width, channel = resized_image.shape
        #qImg = QImage(resized_image.data, width, height, width*channel, QImage.Format_BGR888)
        #pixmap = QPixmap.fromImage(qImg)
        if origin:
            angle = float(self.lineRotationAngle.text())
            image = ut.rotate_image(image, angle)
            self.draw_image(image, self.labelOrigin, self.calibration_image_screen_size, self.calibration_image_aratio, image_processing=False)
            pixmap = self.labelOrigin.pixmap()
            halflength = 100
            painter = QPainter(pixmap)
            for point in self.resized_points:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])
            painter.end()
            self.labelOrigin.resize(pixmap.width(), pixmap.height())
            self.labelOrigin.setPixmap(pixmap)
        else:
            self.draw_image(image, self.labelTrans, self.calibration_image_screen_size, self.calibration_image_aratio, image_processing=False)
            pixmap = self.labelTrans.pixmap()
            painter = QPainter(pixmap)
            if self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()) == "Rectangle":
                painter.setPen(QPen(QColor(178, 54, 245), 4, Qt.DashLine))
                start_point = (self.destination_points[0][0] / self.ratio_width, self.destination_points[0][1] / self.ratio_height)
                end_point = (self.destination_points[3][0] / self.ratio_width, self.destination_points[3][1] / self.ratio_height)
                width = end_point[0] - start_point[0]
                height = end_point[1] - start_point[1]
                painter.drawRect(start_point[0], start_point[1], width, height)
            else:
                painter.setPen(QPen(QColor(90, 94, 99), 2 , Qt.SolidLine))
                halflength = 100
                for point in self.destination_points:
                    x, y = point[0] / self.ratio_width, point[1] / self.ratio_height
                    painter.drawLine(x - halflength, y, x + halflength, y)
                    painter.drawLine(x, y - halflength, x, y + halflength)
            painter.end()
            self.labelTrans.resize(pixmap.width(), pixmap.height())
            self.labelTrans.setPixmap(pixmap)

    def load_calibrated_image(self):
        self.calibration_image = cv2.imread(self.calibration_image_name)
        self.calibration_image_backup = self.calibration_image.copy()
        if self.calibration_image_aratio is None:
            self.calibration_image_aratio = float(self.calibration_image.shape[1]) / float(self.calibration_image.shape[0])

        if self.calibration_image_aratio > 1:
            self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
            self.ratio_height = float(self.calibration_image.shape[0] / (self.calibration_image_screen_size[0] / self.calibration_image_aratio))
        elif self.calibration_image_aratio < 1:
            self.ratio_width = float(self.calibration_image.shape[1] / (self.calibration_image_screen_size[0] * self.calibration_image_aratio))
            self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
        else:
            self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
            self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])

        if len(self.original_points) > 0:
            for point in self.original_points:
                x, y = point[0]/self.ratio_width, point[1]/self.ratio_height
                self.resized_points.append([round(x), round(y)])
        
        self.convert_image()
        self.draw_calibration_image(self.calibration_image)

    def capture_calibration_image(self):
        self.take_a_picture(True)

        if self.calibration_image_aratio > 1:
            self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
            self.ratio_height = float(self.calibration_image.shape[0] / (self.calibration_image_screen_size[0] / self.calibration_image_aratio))
        elif self.calibration_image_aratio < 1:
            self.ratio_width = float(self.calibration_image.shape[1] / (self.calibration_image_screen_size[0] * self.calibration_image_aratio))
            self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
        else:
            self.ratio_width = float(self.calibration_image.shape[1] / self.calibration_image_screen_size[0])
            self.ratio_height = float(self.calibration_image.shape[0] / self.calibration_image_screen_size[1])
            
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.calibration_image_name = os.path.join(base_path, 'setup', f"Calibration_{datetime.datetime.today().strftime('%H-%M-%S_%f')}.png").replace('\\', '/')
        cv2.imwrite(self.calibration_image_name, self.calibration_image)

    def set_rotation_angle(self, up=True):
        if self.sliderAngle.value() == 0: unit = 0.01
        elif self.sliderAngle.value() == 1: unit = 0.1
        elif self.sliderAngle.value() == 2: unit = 1
        elif self.sliderAngle.value() == 3: unit = 10
        else: unit = 100

        value = float(self.lineRotationAngle.text())
        if up: value = value + unit
        else: value = value - unit
        value = round(value, 2)
        
        if value < 0.0: value = 360.0 + value
        elif value > 360.0: value = value - 360.0
        if up:
            self.lineRotationAngle.setText(str(value))
        else:
            self.lineRotationAngle.setText(str(value))
        self.draw_calibration_image(self.calibration_image)
 
    def draw_circle(self):
        self.labelPosition.setText(f"Position: {self.labelOrigin.x}, {self.labelOrigin.y} ({int(self.labelOrigin.x*self.ratio_width)}, {int(self.labelOrigin.y*self.ratio_height)})")
        if self.labelOrigin.left:
            if len(self.resized_points) == 4: return
            self.resized_points.append([self.labelOrigin.x, self.labelOrigin.y])
        else:
            x,y = 999, 999
            radius = 40
            for point in self.resized_points:
                distance = math.sqrt(pow((point[0] - self.labelOrigin.x),2) + pow((point[1] - self.labelOrigin.y), 2))
                if distance < radius:
                    x = point[0]
                    y = point[1]

            if x != 999 and y != 999:
                self.resized_points.remove([x,y])

        self.draw_calibration_image(self.calibration_image)
        
    def move_circle(self, key):
        if len(self.resized_points) < 1: return

        x, y = self.resized_points[-1][0], self.resized_points[-1][1]

        if key == Qt.Key_Right:
            x = x + 1
        elif key == Qt.Key_Left:
            x = x - 1
        elif key == Qt.Key_Up:
            y = y - 1
        elif key == Qt.Key_Down:
            y = y + 1

        self.resized_points.pop(-1)
        self.resized_points.append([x, y])

        self.labelPosition.setText(f"Position: {self.resized_points[-1][0]}, {self.resized_points[-1][1]} ({int(self.resized_points[-1][0]*self.ratio_width)}, {int(self.resized_points[-1][1]*self.ratio_height)})")
        self.draw_calibration_image(self.calibration_image)

    def convert_image(self):
        if len(self.resized_points) != 4: return

        for point in self.resized_points:
            x, y = point[0], point[1]
            x *= self.ratio_width
            y *= self.ratio_height
            if len(self.original_points) == 4:
                self.original_points = []
            self.original_points.append([int(x), int(y)])

        half_width = self.calibration_image.shape[1] / 2
        half_height = self.calibration_image.shape[0] / 2

        upper_left, lower_left, upper_right, lower_right = [0,0], [0,0], [0,0], [0,0]
        for point in self.original_points:
            if point[0] < half_width and point[1] < half_height:
                upper_left = point
            elif point[0] < half_width and point[1] > half_height:
                lower_left = point
            elif point[0] > half_width and point[1] < half_height:
                upper_right = point
            else:
                lower_right = point

        self.original_points = [upper_left, lower_left, upper_right, lower_right]

        if self.tabWidget_2.tabText(self.tabWidget_2.currentIndex()) == "Rectangle":
            w, h = -9999, -9999
            for coordinate in self.original_points:
                w_tmp = round(abs(half_width - coordinate[0]))
                h_tmp = round(abs(half_height - coordinate[1]))
                if w < w_tmp: w = w_tmp
                if h < h_tmp: h = h_tmp
            
            self.destination_points = [
                [round(half_width - w), round(half_height - h)],
                [round(half_width - w), round(half_height + h)],
                [round(half_width + w), round(half_height - h)],
                [round(half_width + w), round(half_height + h)]
            ]

            self.pixel_per_mm = [float(self.linePixelPerMM_x.text()), float(self.linePixelPerMM_y.text())]
        else:
            x1, y1, x2, y2 = float(self.lineQuad1x.text()), float(self.lineQuad1y.text()), float(self.lineQuad2x.text()), float(self.lineQuad4y.text())
            self.pixel_per_mm = [abs(upper_right[0] - upper_left[0])/abs(x2 - x1), abs(upper_right[1] - lower_right[1])/abs(y2 - y1)]

            self.points = [self.lineQuad1x.text(), self.lineQuad2x.text(), self.lineQuad3x.text(), self.lineQuad4x.text(),
                           self.lineQuad1y.text(), self.lineQuad2y.text(), self.lineQuad3y.text(), self.lineQuad4y.text()]

            self.destination_points = [
                [half_width - abs(float(self.lineQuad2x.text()))*self.pixel_per_mm[0], half_height - abs(float(self.lineQuad2y.text()))*self.pixel_per_mm[1]],
                [half_width - abs(float(self.lineQuad3x.text()))*self.pixel_per_mm[0], half_height + abs(float(self.lineQuad3y.text()))*self.pixel_per_mm[1]],
                [half_width + abs(float(self.lineQuad1x.text()))*self.pixel_per_mm[0], half_height - abs(float(self.lineQuad1y.text()))*self.pixel_per_mm[1]],
                [half_width + abs(float(self.lineQuad4x.text()))*self.pixel_per_mm[0], half_height + abs(float(self.lineQuad4y.text()))*self.pixel_per_mm[1]]
            ]

            x1, y1, x2, y2 = float(self.lineQuad1x.text()), float(self.lineQuad1y.text()), float(self.lineQuad3x.text()), float(self.lineQuad3y.text())
            self.pixel_per_mm = [
                abs(self.destination_points[2][0] - self.destination_points[1][0])/abs(x2 - x1),
                abs(self.destination_points[2][1] - self.destination_points[1][1])/abs(y2 - y1)
            ]
        self.transform_matrix = cv2.getPerspectiveTransform(np.float32(self.original_points), np.float32(self.destination_points))
        self.calibration_angle = float(self.lineRotationAngle.text())
        image = ut.rotate_image(self.calibration_image, self.calibration_angle)

        self.transformed_image = cv2.warpPerspective(image, self.transform_matrix, (image.shape[1], image.shape[0]))

        self.draw_calibration_image(self.transformed_image, False)
        self.calibrated = True
        self.set_checked(self.checkCalibration, True)
        self.perspective_method = self.tabWidget_2.tabText(self.tabWidget_2.currentIndex())

    ### Methods for close
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
            self.initialize_parameter(True)
            self.reset_all = True
            self.reject()
            return True
        else:
            return False

    def return_para(self):
        return super().exec_()