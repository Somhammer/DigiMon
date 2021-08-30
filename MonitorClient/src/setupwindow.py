import os, sys
import time
import datetime
import logging
import copy
import yaml

import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.variables import *
from src.ui_setupwindow import Ui_SetupWindow
from src.calibrationwindow import CalibrationWindow

class SetupWindow(QDialog, Ui_SetupWindow):
    logger_signal = Signal(str, str)
    def __init__(self, parent, image):
        super(SetupWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)
        
        self.dialog = False
        self.changed = False

        self.image = image

        self.gain = 100
        self.exposure_time = 500
        self.ROI = [[0,0], [0,0]] # [(StartPoint), (width, height)]

        self.do_transformation = False
        self.calibration_image = ''
        self.original_points = []
        self.destination_points = []
        self.mm_per_pixel = []

        self.filter_code = None
        self.filter_para = None

        self.save_filtered_image = False

        self.set_action()
        self.show()

        height, width, channel = self.image.shape
        qImg = QImage(self.image.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        self.pixmap = pixmap.scaled(self.labelImage.width(), self.labelImage.height())
        self.labelImage.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
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

    def keyReleaseEvent(self, event):
        if any(event.key() == i for i in [Qt.Key_Control, Qt.Key_Shift]):
            self.sliderGain.setSingleStep(1)
            self.sliderExposureTime.setSingleStep(1)
            self.sliderX0.setSingleStep(1)
            self.sliderY0.setSingleStep(1)
            self.sliderWidth.setSingleStep(1)
            self.sliderHeight.setSingleStep(1)

    def set_action(self):
        self.sliderGain.valueChanged.connect(lambda: self.set_value(CAMERA_GAIN))
        self.sliderExposureTime.valueChanged.connect(lambda: self.set_value(CAMERA_EXPOSURE_TIME))

        self.sliderX0.valueChanged.connect(lambda: self.set_value(CAMERA_ROI_X0))
        self.sliderY0.valueChanged.connect(lambda: self.set_value(CAMERA_ROI_Y0))
        self.sliderWidth.valueChanged.connect(lambda: self.set_value(CAMERA_ROI_WIDTH))
        self.sliderHeight.valueChanged.connect(lambda: self.set_value(CAMERA_ROI_HEIGHT))

        base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        self.comboSetup.addItem('')
        for item in os.listdir(os.path.join(base_path, 'setup')):
            if any(item.endswith(i) for i in ['yaml','yml']):
                self.comboSetup.addItem(os.path.join(base_path, 'setup', item))
        self.comboSetup.currentTextChanged.connect(lambda: self.load(os.path.join(base_path, 'setup', self.comboSetup.currentText())))

        self.comboFilter.currentTextChanged.connect(self.load_filter_parameters)

        self.pushSave.clicked.connect(self.save)
        self.pushLoad.clicked.connect(lambda: self.load())
        self.pushCalibration.clicked.connect(self.calibrate_image)
        self.pushFilterApply.clicked.connect(self.draw_image)
        self.pushOk.clicked.connect(self.click_ok)
        self.pushCancel.clicked.connect(self.click_cancel)

    def set_value(self, idx):
            self.changed = True
            if idx == CAMERA_GAIN:
                self.gain = self.sliderGain.value()
                self.lineGain.setText(str(self.sliderGain.value()))
            elif idx == CAMERA_EXPOSURE_TIME:
                self.exposure_time = self.sliderExposureTime.value()
                self.lineExposureTime.setText(str(self.sliderExposureTime.value()))
            elif idx == CAMERA_ROI_X0:
                self.ROI[0][0] = round(self.image.shape[0] * self.sliderX0.value() / 1000.0)
                self.lineX0.setText(str(self.sliderX0.value()/10))
                self.labelSPPixel.setText(f"({self.ROI[0][0]}, {self.ROI[0][1]}) pixel")
            elif idx == CAMERA_ROI_Y0:
                self.ROI[0][1] = round(self.image.shape[1] * self.sliderY0.value() / 1000.0)
                self.lineY0.setText(str(self.sliderY0.value()/10))
                self.labelSPPixel.setText(f"({self.ROI[0][0]}, {self.ROI[0][1]}) pixel")
            elif idx == CAMERA_ROI_WIDTH:
                self.ROI[1][0] = round(self.image.shape[0] * self.sliderWidth.value() / 1000.0)
                self.lineWidth.setText(str(self.sliderWidth.value()/10))
                self.labelSizePixel.setText(f"({self.ROI[1][0]}, {self.ROI[1][1]}) pixel")
            elif idx == CAMERA_ROI_HEIGHT:
                self.ROI[1][1] = round(self.image.shape[1] * self.sliderHeight.value() / 1000.0)
                self.lineHeight.setText(str(self.sliderHeight.value()/10))
                self.labelSizePixel.setText(f"({self.ROI[1][0]}, {self.ROI[1][1]}) pixel")

            if (idx == i for i in [CAMERA_GAIN, CAMERA_ROI_X0, CAMERA_ROI_Y0, CAMERA_ROI_WIDTH, CAMERA_ROI_HEIGHT]):
                self.draw_image()

    def draw_image(self):
        image = copy.deepcopy(self.image)

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
        
        image = cv2.resize(image, dsize=(self.labelImage.width(), self.labelImage.height()), interpolation=cv2.INTER_LINEAR)
        height, width, channel = image.shape
        qImg = QImage(image.data, width, height, width*channel, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)

        self.labelImage.resize(width, height)
        self.labelImage.setPixmap(pixmap)

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

    def calibrate_image(self):
        if self.dialog: return
        self.dialog = True
        calibration = CalibrationWindow(image=self.calibration_image, original_points=self.original_points, destination_points=self.destination_points, mm_per_pixel=self.mm_per_pixel)
        r = calibration.return_para()
        if r:
            print(calibration.original_points)
            self.do_transformation = True
            self.transform_points = calibration.original_points
            self.destination_points = calibration.destination_points
            self.mm_per_pixel = calibration .mm_per_pixel
            self.changed = False

        self.dialog = False

    def save(self):
        base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        fname = QFileDialog.getSaveFileName(self, 'Save', os.path.join(base_path, 'data'), filter="Yaml file (*.yaml *.yml)")[0]
        if not (fname.endswith('.yaml') or fname.endswith('.yml')):
            fname = fname + '.yaml'
        fout = open(fname, 'w')
        fout.write(textwrap.dedent(f"""\
            Gain: {self.gain}
            ExposureTime: {self.exposure_time}
            ROI: {str(self.ROI)}
            Image: "{self.image_name}"
            Original: {str(self.original_points)}
            Destination: {str(self.destination_points)}
            Length: {str(self.mm_per_pixel)}
            """))
        fout.close()

    def load(self, fname=''):
        if fname == '':
            extension = ["Yaml file (*.yaml *.yml)"]
            fname = QFileDialog.getOpenFileName(self, "Select Setup file", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        
        if fname != '':
            with open(fname, 'r') as f:
                cfg = yaml.load(f, Loader=yaml.FullLoader)
                self.gain = int(cfg['Gain'])
                self.exposure_time = int(cfg['ExposureTime'])
                self.calibration_image = str(cfg['Image'])
                self.original_points = cfg['Original']
                self.destination_points = cfg['Destination']
                self.mm_per_pixel = cfg['Length']

    def click_ok(self):
        if self.changed:
            msg = "Camera Parameter was changed. Please, calibrate again."
            reply = QMessageBox.warning(self, 'Message', msg)
            return
        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()
        else:
            return

    def return_para(self):
        return super().exec_()