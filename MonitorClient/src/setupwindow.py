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

from src.logger import LogStringHandler
from src.variables import *
from src.ui_setupwindow import Ui_SetupWindow

class DigiLabel(QLabel):
    clicked = Signal()
    move = Signal()
    dclicked = Signal()
    def __init__(self, parent):
        super(DigiLabel, self).__init__(parent)
        #self.setMouseTracking(True)
        self.x = None
        self.y = None
        self.left = None

        self.x_end = None
        self.y_end = None

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        self.x_end = event.x()
        self.y_end = event.y()

        if event.button() == Qt.RightButton:
            self.left = False
        elif event.button() == Qt.LeftButton:
            self.left = True

    def mouseMoveEvent(self, event):
        self.x_end = event.x()
        self.y_end = event.y()
        self.move.emit()
        
    def mouseReleaseEvent(self, event):
        self.clicked.emit()

    def mouseDoubleClickEvent(self, event):
        self.dclicked.emit()
        
class SetupWindow(QDialog, Ui_SetupWindow):
    send_signal_to_blueberry = Signal(int, int)
    logger_signal = Signal(str, str)
    def __init__(self, parent):
        super(SetupWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)

        self.changed = False

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textConnectionLog)
        self.logger.addHandler(handler)

        self.labelOrigin = DigiLabel(self.labelOrigin)
        self.labelImage = DigiLabel(self.labelImage)

        self.ratio_width = self.ratio_height = 1

        self.initialize_parameter()
        self.set_action()
        self.show()

    def keyPressEvent(self, event):
        if self.tabWidget.currentIndex() == 1:
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
        elif self.tabWidget.currentIndex() == 2:
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
    
    # Common Methods
    def initialize_parameter(self):
        self.camera_connected = self.controller_connected = self.photo_setup = self.select_ROI = self.calibrated = False

        self.camera_sdk = None

        self.backup_image = None

        self.captured_image = None
        self.calibration_image = None
        self.calibration_image_name = ""

        self.resized_capimage = None
        self.resized_calimage = None

        self.gain = 100
        self.exposure_time = 500
        self.ROI = [[0,0], [0,0]] # [(StartPoint), (width, height)]

        self.filter_code = self.filter_para = None

        self.original_points = self.destination_points = self.resized_points = self.mm_per_pixel = []

    def set_checked(self, checkbox, state):
        if state:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)
    
    def set_action(self):
        self.send_signal_to_blueberry.connect(self.parent.blueberry.receive_signal)

        # Setup
        base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        self.comboSetup.addItem('')
        for item in os.listdir(os.path.join(base_path, 'setup')):
            if any(item.endswith(i) for i in ['yaml','yml']):
                self.comboSetup.addItem(os.path.join(base_path, 'setup', item))
        self.comboSetup.currentTextChanged.connect(lambda: self.load(self.comboSetup.currentText()))

        self.pushSave.clicked.connect(self.save)
        self.pushLoad.clicked.connect(lambda: self.load())
        self.pushOk.clicked.connect(self.click_ok)
        self.pushCancel.clicked.connect(self.click_cancel)

        # Connection
        # ui_setupwindow가 안정화 되면 그 쪽으로 옮기기
        self.lineCameraIP1.setValidator(QIntValidator(self))
        self.lineCameraIP2.setValidator(QIntValidator(self))
        self.lineCameraIP3.setValidator(QIntValidator(self))
        self.lineCameraIP4.setValidator(QIntValidator(self))
        self.lineCameraIP5.setValidator(QIntValidator(self))

        self.lineControllerIP1.setValidator(QIntValidator(self))
        self.lineControllerIP2.setValidator(QIntValidator(self))
        self.lineControllerIP3.setValidator(QIntValidator(self))
        self.lineControllerIP3.setValidator(QIntValidator(self))
        self.lineControllerIP5.setValidator(QIntValidator(self))

        self.checkCameraConnected.clicked.connect(lambda: self.set_checked(self.checkCameraConnected, self.parent.blueberry.connected))
        self.checkControllerConnected.clicked.connect(lambda: self.set_checked(self.checkControllerConnected, self.parent.blackberry.connected))

        self.pushConnectCamera.clicked.connect(lambda: self.connect_network(self.parent.blueberry, self.checkCameraConnected))
        self.pushConnectController.clicked.connect(lambda: self.connect_network(self.parent.blackberry, self.checkControllerConnected))

        # Photo
        self.labelImage.move.connect(self.set_ROI)
        self.labelImage.dclicked.connect(self.draw_ROI)

        self.sliderGain.valueChanged.connect(lambda: self.set_photo_para(CAMERA_GAIN))
        self.sliderExposureTime.valueChanged.connect(lambda: self.set_photo_para(CAMERA_EXPOSURE_TIME))

        self.sliderX0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_X0))
        self.sliderY0.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_Y0))
        self.sliderWidth.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_WIDTH))
        self.sliderHeight.valueChanged.connect(lambda: self.set_photo_para(CAMERA_ROI_HEIGHT))

        self.comboFilter.currentTextChanged.connect(self.load_filter_parameters)

        self.pushFilterApply.clicked.connect(self.draw_image)

        # Calibration
        self.labelOrigin.clicked.connect(self.draw_circle)

        def set_linevalue(width, height):
            if width == '': width = 1.0
            if height == '': height = 1.0
            self.mm_per_pixel = [float(width), float(height)]

        self.linePixelWidth.editingFinished.connect(lambda: set_linevalue(self.linePixelWidth.text(), self.linePixelHeight.text()))
        self.linePixelHeight.editingFinished.connect(lambda: set_linevalue(self.linePixelWidth.text(), self.linePixelHeight.text()))

        #self.pushSave.clicked.connect(self.save)
        self.pushOpenImage.clicked.connect(lambda: self.open())
        self.pushConvert.clicked.connect(self.convert_image)

    def save(self, last=False):
        base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        if not last:
            fname = QFileDialog.getSaveFileName(self, 'Save', os.path.join(base_path, 'data'), filter="Yaml file (*.yaml *.yml)")[0]
            if not (fname.endswith('.yaml') or fname.endswith('.yml')):
                fname = fname + '.yaml'
        else:
            fname = os.path.join(base_path, 'setup', 'last.yaml')

        camera_ip = '.'.join(i.text() for i in[self.lineCameraIP1, self.lineCameraIP2, self.lineCameraIP3, self.lineCameraIP4])
        controller_ip = '.'.join(i.text() for i in[self.lineControllerIP1, self.lineControllerIP2, self.lineControllerIP3, self.lineControllerIP4])

        fout = open(fname, 'w')
        fout.write(textwrap.dedent(f"""\
            Auto: {str(last)}
            CameraIP: "{camera_ip}"
            CameraPort: {self.lineCameraIP5.text()}
            CameraSDK: "{self.camera_sdk}"
            ControllerUse: {str(self.checkUseControlServer.isChecked())}
            ControllerIP: {controller_ip}
            ControllerPort: {self.lineControllerIP5.text()}
            Gain: {self.gain}
            ExposureTime: {self.exposure_time}
            ROI: {str(self.ROI)}            
            FilterType: "{self.comboFilter.currentText()}"
            FilterParameter: {str(self.filter_para)}
            Image: "{self.calibration_image_name}"
            Original: {str(self.original_points)}
            Destination: {str(self.destination_points)}
            PixelLength: {str(self.mm_per_pixel)}
            """))
        fout.close()

    def load(self, fname=''):
        if fname == '':
            extension = ["Yaml file (*.yaml *.yml)"]
            fname = QFileDialog.getOpenFileName(self, "Select Setup file", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            with open(fname, 'r') as f:
                cfg = yaml.load(f, Loader=yaml.FullLoader)
                
                camera_ip = str(cfg['CameraIP']).split('.')
                if len(camera_ip) == 4:
                    self.lineCameraIP1.setText(camera_ip[0])
                    self.lineCameraIP2.setText(camera_ip[1])
                    self.lineCameraIP3.setText(camera_ip[2])
                    self.lineCameraIP4.setText(camera_ip[3])
                self.lineCameraIP5.setText(str(cfg['CameraPort']))
                self.camera_sdk = str(cfg['CameraSDK'])
                for idx in range(self.comboSDKType.count()):
                    if self.comboSDKType.itemText(idx) == self.camera_sdk:
                        self.comboSDKType.setCurrentIndex(idx)
                        break

                if cfg['ControllerUse']:
                    self.checkUseControlServer.setChecked(True)
                controller_ip = str(cfg['ControllerIP']).split('.')
                if len(controller_ip):
                    self.lineControllerIP1.setText(controller_ip[0]) 
                    self.lineControllerIP2.setText(controller_ip[1])
                    self.lineControllerIP3.setText(controller_ip[2])
                    self.lineControllerIP4.setText(controller_ip[3])
                self.lineControllerIP5.setText(str(cfg['ControllerPort']))

                self.connect_network(self.parent.blueberry, self.checkCameraConnected)
                self.connect_network(self.parent.blackberry, self.checkControllerConnected)
                
                self.gain = int(cfg['Gain'])
                self.sliderGain.setValue(self.gain)
                self.exposure_time = int(cfg['ExposureTime'])
                self.sliderExposureTime.setValue(self.exposure_time)

                self.ROI = cfg['ROI']
                self.sliderX0.setValue(self.ROI[0][0])
                self.sliderY0.setValue(self.ROI[0][1])
                self.sliderWidth.setValue(self.ROI[1][0])
                self.sliderHeight.setValue(self.ROI[1][1])

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
                self.draw_image()

                self.calibration_image_name = str(cfg['Image'])
                self.original_points = cfg['Original']
                self.destination_points = cfg['Destination']
                self.mm_per_pixel = cfg['PixelLength']
                self.load_calibrated_image()

    ### Methods for Connection
    def connect_network(self, berry, checkbox):
        if berry.name == "Network Camera":
            ip1, ip2, ip3, ip4, port = self.lineCameraIP1, self.lineCameraIP2, self.lineCameraIP3, self.lineCameraIP4, self.lineCameraIP5
            if self.camera_sdk is None:
                self.camera_sdk = self.comboSDKType.currentText()
            self.parent.blueberry.sdk = self.camera_sdk
            self.logger.info(f"Set SDK as {self.camera_sdk}.")
        else:
            if not self.checkUseControlServer.isChecked():
                self.logger.warning(f"Please, check 'Use Network Camera Controller Server' first.")
                return
            ip1, ip2, ip3, ip4, port = self.lineControllerIP1, self.lineControllerIP2, self.lineControllerIP3, self.lineControllerIP4, self.lineControllerIP5

        if any(i.text() == '' for i in [ip1, ip2, ip3, ip4]):
            return
        url = '.'.join(i.text() for i in [ip1, ip2, ip3, ip4])
        if berry.connected:
            if berry.address == url and berry.port == port.text():
                self.set_checked(checkbox, berry.connected)
                if berry.name == "Network Camera":
                    self.captured_image = self.parent.blueberry.camera.take_a_picture()

                    height, width, channel = self.captured_image.shape
                    qImg = QImage(self.captured_image.data, width, height, width*channel, QImage.Format_BGR888)
                    pixmap = QPixmap.fromImage(qImg)
                    pixmap = pixmap.scaled(self.labelImage.width(), self.labelImage.height())
                    self.labelImage.setPixmap(pixmap)
                return

        if port.text() != '':
            berry.initialize(url, port.text())

        self.logger.info(f"Try to connect to {berry.name}...")
        if berry.connected:
            self.logger.info("Connection is succeed")
        else:
            self.parent.blueberry.sdk = None
            self.camera_sdk = None
            self.logger.error(f"Connection is failed. Please, reconnect to {berry.name}...")
        self.set_checked(checkbox, berry.connected)

        if berry.name == "Network Camera":
            self.captured_image = self.parent.blueberry.camera.take_a_picture()
            self.backup_image = self.captured_image.copy()

            height, width, channel = self.captured_image.shape
            qImg = QImage(self.captured_image.data, width, height, width*channel, QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.labelImage.width(), self.labelImage.height())
            self.labelImage.setPixmap(pixmap)

    ### Methods for Photo
    def set_photo_para(self, idx):
            self.changed = True
            if idx == CAMERA_GAIN:
                self.gain = self.sliderGain.value()
                self.lineGain.setText(str(self.sliderGain.value()))
                self.send_signal_to_blueberry.emit(idx, self.gain)
            elif idx == CAMERA_EXPOSURE_TIME:
                self.exposure_time = self.sliderExposureTime.value()
                self.lineExposureTime.setText(str(self.sliderExposureTime.value()))
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

            if (idx == i for i in [CAMERA_GAIN, CAMERA_ROI_X0, CAMERA_ROI_Y0, CAMERA_ROI_WIDTH, CAMERA_ROI_HEIGHT]):
                if self.camera_connected:
                    self.captured_image = self.parent.blueberry.camera.take_a_picture()
                    self.draw_image()

    def draw_image(self):
        image = copy.deepcopy(self.captured_image)

        if self.filter_code == BKG_SUBSTRACTION:
            background = cv2.imread(self.filter_para['background file'])
            image = cv2.subtract(image, background)
        if self.filter_code == GAUSSIAN_FILTER:
            ksize = (self.filter_para['x kernal size'], self.filter_para['y kernal size'])
            sigmaX = self.filter_para['sigmaX']
            image = cv2.GaussianBlur(image, ksize=ksize, sigmaX=sigmaX)
        elif self.filter_code == MEDIAN_FILTER:
            ksize = self.filter_para['kernal size']
            image = cv2.medianBlur(image, ksize=ksize)
        elif self.filter_code == BILATERAL_FILTER:
            ksize = self.filter_para['kernal size']
            scolor = self.filter_para['sigma color']
            sspace = self.filter_para['sigma space']
            image = cv2.bilateralFilter(image, d=ksize, sigmaColor=scolor, sigmaSpace=sspace)
        
        self.resized_capimage = cv2.resize(image, dsize=(550,550), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.resized_capimage.shape
        qImg = QImage(self.resized_capimage.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)

        self.labelImage.resize(width, height)
        self.labelImage.setPixmap(pixmap)

    def draw_rectangle(self):
        if self.select_ROI:
            self.captured_image = self.backup_image.copy()
            self.draw_image()
            self.select_ROI = False
        if self.resized_capimage is None: return
        height, width, channel = self.resized_capimage.shape
        qImg = QImage(self.resized_capimage.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        painter = QPainter(pixmap)
        painter.setPen(QPen(QColor(3, 252, 127), 1.5, Qt.DashLine))

        x = self.resized_capimage.shape[1] * self.sliderX0.value() / 1000.0
        y = self.resized_capimage.shape[0] * self.sliderY0.value() / 1000.0
        width = self.resized_capimage.shape[1] * self.sliderWidth.value() / 1000.0
        height = self.resized_capimage.shape[0] * self.sliderHeight.value() / 1000.0

        painter.drawRect(x, y, width, height)
        painter.end()
        self.labelImage.setPixmap(pixmap)

    def set_ROI(self):
        if not self.labelImage.left: return
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

        self.sliderX0.setValue(x / self.labelImage.width() * 1000)
        self.sliderY0.setValue(y / self.labelImage.height() * 1000)
        self.sliderWidth.setValue(width / self.labelImage.width() * 1000)
        self.sliderHeight.setValue(height / self.labelImage.height() * 1000)

    def draw_ROI(self):
        x, y, width, height = self.ROI[0][0], self.ROI[0][1], self.ROI[1][0], self.ROI[1][1]

        src = self.captured_image.copy()
        roi = src[y:y+height, x:x+width]
        self.captured_image = roi
        roi = cv2.resize(roi, dsize=(550,550), interpolation=cv2.INTER_LINEAR)
        self.resized_capimage = roi
        self.draw_image()
        self.select_ROI = True

    def load_filter_parameters(self):
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
    def open(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            self.set_image(fname)
            self.original_points = []
            self.destination_points = []
            self.resized_points = []

    def load_calibrated_image(self):
        self.set_image(self.calibration_image_name)
        if len(self.original_points) > 0:
            for point in self.original_points:
                x, y = point[0]/self.ratio_width, point[1]/self.ratio_height
                self.resized_points.append([round(x), round(y)])

            halflength = 100
            pixmap = self.labelOrigin.pixmap()
            painter = QPainter(pixmap)
            for point in self.resized_points:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])

            painter.end()
            self.labelOrigin.setPixmap(pixmap)

        if len(self.destination_points) > 1:
            w = round(self.destination_points[2][0] - self.destination_points[0][0])
            h = round(self.destination_points[1][1] - self.destination_points[0][1])
            self.lineTransWidth.setText(str(w))
            self.lineTransHeight.setText(str(h))

        if len(self.mm_per_pixel) > 1:
            self.linePixelWidth.setText(str(self.mm_per_pixel[0]))
            self.linePixelHeight.setText(str(self.mm_per_pixel[1]))
        
        self.convert_image()
                
    def set_image(self, name):
        if name == "": return
        self.calibration_image_name = name
        self.calibration_image = cv2.imread(name)
        self.resized_calimage = cv2.resize(self.calibration_image, dsize=(450,450), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.resized_calimage.shape
        self.ratio_width = self.calibration_image.shape[1] / width
        self.ratio_height = self.calibration_image.shape[0] / height
        qImg = QImage(self.resized_calimage.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        self.labelOrigin.resize(pixmap.width(), pixmap.height())
        self.labelOrigin.setPixmap(pixmap)

    def draw_circle(self):
        self.labelPosition.setText(f"Position: {self.labelOrigin.x}, {self.labelOrigin.y} ({int(self.labelOrigin.x*self.ratio_width)}, {int(self.labelOrigin.y*self.ratio_height)})")
        halflength = 100
        pixmap = self.labelOrigin.pixmap()
        if self.labelOrigin.left:
            if len(self.resized_points) == 4: return
            self.resized_points.append([self.labelOrigin.x, self.labelOrigin.y])
            painter = QPainter(pixmap)
            painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
            painter.drawLine(self.labelOrigin.x - halflength, self.labelOrigin.y, self.labelOrigin.x + halflength, self.labelOrigin.y)
            painter.drawLine(self.labelOrigin.x, self.labelOrigin.y - halflength, self.labelOrigin.x, self.labelOrigin.y + halflength)
            painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
            painter.drawPoint(self.labelOrigin.x, self.labelOrigin.y)

            painter.end()
            self.labelOrigin.setPixmap(pixmap)
        else:
            height, width, channel = self.resized_calimage.shape
            qImg = QImage(self.resized_calimage.data, width, height, width*channel, QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(qImg)
            painter = QPainter(pixmap)
            x,y = 999, 999
            radius = 40
            for point in self.resized_points:
                distance = math.sqrt(pow((point[0] - self.labelOrigin.x),2) + pow((point[1] - self.labelOrigin.y), 2))
                if distance < radius:
                    x = point[0]
                    y = point[1]

            if x != 999 and y != 999:
                self.resized_points.remove([x,y])

            for point in self.resized_points:
                painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
                painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
                painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
                painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
                painter.drawPoint(point[0], point[1])
            
            painter.end()
            self.labelOrigin.setPixmap(pixmap)
        
    def move_circle(self, key):
        if len(self.resized_points) < 1:
            return

        halflength = 100
        x, y = self.resized_points[-1][0], self.resized_points[-1][1]
        height, width, channel = self.resized_calimage.shape
        qImg = QImage(self.resized_calimage.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        painter = QPainter(pixmap)

        last_point = self.resized_points[-1]
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

        for point in self.resized_points:
            painter.setPen(QPen(QColor(90, 94, 99), 2, Qt.SolidLine))
            painter.drawLine(point[0]- halflength, point[1], point[0] + halflength, point[1])
            painter.drawLine(point[0], point[1] - halflength, point[0], point[1] + halflength)
            painter.setPen(QPen(QColor(5, 79, 181), 10, Qt.SolidLine, Qt.RoundCap))
            painter.drawPoint(point[0], point[1])
            
        painter.end()
        self.labelOrigin.setPixmap(pixmap)
        self.labelPosition.setText(f"Position: {self.resized_points[-1][0]}, {self.resized_points[-1][1]} ({int(self.resized_points[-1][0]*self.ratio_width)}, {int(self.resized_points[-1][1]*self.ratio_height)})")

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
        w = int(max(math.sqrt((upper_left[0] - upper_right[0])**2 + (upper_left[1] - upper_right[1])**2), math.sqrt((lower_left[0] - lower_right[0])**2 + (lower_left[1] - lower_right[1])**2)))
        h = int(max(math.sqrt((upper_left[0] - lower_left[0])**2 + (upper_left[1] - lower_left[0])**2), math.sqrt((upper_right[0] - lower_right[0])**2 + (upper_right[1] - lower_right[0])**2)))
        if not (self.lineTransWidth.text() == '' and self.lineTransHeight.text() == ''):
            w = int(self.lineTransWidth.text())
            h = int(self.lineTransHeight.text())
        self.destination_points = [upper_left, [upper_left[0], upper_left[1]+h], [upper_left[0]+w, upper_left[1]], [upper_left[0]+w, upper_left[1]+h]]

        # 좌표: 좌상, 좌하, 우상, 우하
        transform_matrix = cv2.getPerspectiveTransform(np.float32(self.original_points), np.float32(self.destination_points))
        self.transformed_image = cv2.warpPerspective(self.calibration_image, transform_matrix, (self.calibration_image.shape[1], self.calibration_image.shape[0]))

        self.transformed_image2 = cv2.resize(self.transformed_image, dsize=(450,450), interpolation=cv2.INTER_LINEAR)
        height, width, channel = self.transformed_image2.shape
        qImg = QImage(self.transformed_image2.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)

        painter = QPainter(pixmap)
        painter.setPen(QPen(QColor(178, 54, 245), 4, Qt.DashLine))
        start_point = (self.destination_points[0][0] / self.ratio_width, self.destination_points[0][1] / self.ratio_height)
        width = w / self.ratio_width
        height = h / self.ratio_height
        painter.drawRect(start_point[0], start_point[1], width, height)
        painter.end()

        self.labelTrans.resize(pixmap.width(), pixmap.height())
        self.labelTrans.setPixmap(pixmap)
        self.calibrated = True

    ### Methods for close
    def click_ok(self):
        base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

        if self.checkSaveLast.isChecked():
            self.save(last=True)
        else:
            if os.path.exists(os.path.join(base_path,'setup','last.yaml')):
                os.remove(os.path.join(base_path, 'setup', 'last.yaml'))
        if self.checkCameraConnected.isChecked():
            self.camera_connected = True
        if self.checkControllerConnected.isChecked():
            self.controller_connected = True
        if len(self.mm_per_pixel) < 1:
            self.calibrated = False
            msg = "Please, complite calibration. write mm per pixel."
            relpy = QMessageBox.warning(self, 'Message', msg)
            return

        #if self.changed:
        #    msg = "Camera Parameter was changed. Please, calibrate again."
        #    reply = QMessageBox.warning(self, 'Message', msg)
        #    return
        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.initialize_parameter()
            self.reject()
        else:
            return

    def return_para(self):
        return super().exec_()

