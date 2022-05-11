import copy
import cv2

from PySide6.QtWidgets import *
from PySide6.QtGui import *

from variables import *
import utilities as ut

def set_photo_para(self, idx, slider=True):
    if self.camera_connected:
        if idx == CAMERA_GAIN:
            if slider:
                self.para.gain = self.sliderGain.value()
                self.lineGain.setText(str(self.sliderGain.value()))
            else:
                if self.lineGain.text() == '': return
                self.para.gain = int(self.lineGain.text())
                self.sliderGain.setValue(self.para.gain)
        elif idx == CAMERA_EXPOSURE_TIME:
            if slider:
                self.para.exp_time = self.sliderExposureTime.value()
                self.lineExposureTime.setText(str(self.sliderExposureTime.value()))
            else:
                if self.lineExposureTime.text() == '': return
                self.para.exp_time = int(self.lineExposureTime.text())
                self.sliderExposureTime.setValue(self.para.exp_time)
        elif idx == CAMERA_ROI_X0:
            self.para.roi[0][0] = round(self.captured_image.shape[1] * self.sliderX0.value() / 1000.0)
            self.lineX0.setText(str(self.sliderX0.value()/10))
            self.labelSPPixel.setText(f"({self.para.roi[0][0]}, {self.para.roi[0][1]}) pixel")
            self.draw_roi_rectangle()
        elif idx == CAMERA_ROI_Y0:
            self.para.roi[0][1] = round(self.captured_image.shape[0] * self.sliderY0.value() / 1000.0)
            self.lineY0.setText(str(self.sliderY0.value()/10))
            self.labelSPPixel.setText(f"({self.para.roi[0][0]}, {self.para.roi[0][1]}) pixel")
            self.draw_roi_rectangle()
        elif idx == CAMERA_ROI_WIDTH:
            self.para.roi[1][0] = round(self.captured_image.shape[1] * self.sliderWidth.value() / 1000.0)
            self.lineWidth.setText(str(self.sliderWidth.value()/10))
            self.labelSizePixel.setText(f"({self.para.roi[1][0]}, {self.para.roi[1][1]}) pixel")
            self.draw_roi_rectangle()
        elif idx == CAMERA_ROI_HEIGHT:
            self.para.roi[1][1] = round(self.captured_image.shape[0] * self.sliderHeight.value() / 1000.0)
            self.lineHeight.setText(str(self.sliderHeight.value()/10))
            self.labelSizePixel.setText(f"({self.para.roi[1][0]}, {self.para.roi[1][1]}) pixel")
            self.draw_roi_rectangle()

def take_a_picture(self, calibration=False):
    if not self.para.cam_conn: return
    if not calibration:
        self.captured_image = self.blueberry.take_a_picture(True)
        if self.captured_image_aratio is None:
            self.captured_image_aratio = float(self.captured_image.shape[1]) / float(self.captured_image.shape[0])
        
        self.draw_image(self.captured_image, self.labelImage, self.captured_image_screen_size, self.captured_image_aratio)
    else:
        self.calibration_image = self.blueberry.take_a_picture(True)
        if self.calibration_image_aratio is None:
            self.calibration_image_aratio = float(self.calibration_image.shape[1]) / float(self.calibration_image.shape[0])
        
        self.calibration_image_backup = self.calibration_image.copy()
        self.draw_image(self.calibration_image, self.labelOrigin, self.calibration_image_screen_size, self.calibration_image_aratio, image_processing=False)

def draw_image(self, image, label, screen_size, aspect_ratio, image_processing=True):
    image_copy = copy.deepcopy(image)
    if image_processing:
        if self.para.calibrated:
            image_copy = ut.transform_image(image_copy)
        image_copy = ut.filter_image(image_copy)
        image_copy = ut.slice_image(image_copy)
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

def draw_roi_rectangle(self):
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

def set_roi(self):
    if not self.para.cam_conn or self.select_roi or not self.labelImage.left: return

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

def apply_roi(self, reset=False):
    if reset:
        self.para.ROI = [[0,0],[0,0]]

        self.sliderX0.setValue(0)
        self.sliderY0.setValue(0)
        self.sliderWidth.setValue(0)
        self.sliderHeight.setValue(0)

        self.select_roi = False
    else:
        self.select_roi = True

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
                    extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
                    fname = QFileDialog.getOpenFileName(self, "Select Background Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
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
        self.para.filter_para[name] = value

    if reset:
        if self.comboFilter.currentText() == 'No Filter':
            self.para.filter_code = None
            self.para.filter_para = None
        elif self.comboFilter.currentText() == 'Background Substraction':
            self.para.filter_code = BKG_SUBSTRACTION
            self.para.filter_para = {'background file':''}
        elif self.comboFilter.currentText() == 'Gaussian':
            self.para.filter_code = GAUSSIAN_FILTER
            self.para.filter_para = {'x kernal size':0, 'y kernal size':0, 'sigmaX':0}
        elif self.comboFilter.currentText() == 'Median':
            self.para.filter_code = MEDIAN_FILTER
            self.para.filter_para = {'kernal size':0}
        elif self.comboFilter.currentText() == 'Bilateral':
            self.para.filter_code = BILATERAL_FILTER
            self.para.filter_para = {'kernal size':0, 'sigma color':0, 'sigma space':0}
        else:
            return

    self.listParameters.clear()
    if self.para.filter_para is not None:
        for name in self.para.filter_para.keys():
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

def apply_filter_parameters(self):
    pass