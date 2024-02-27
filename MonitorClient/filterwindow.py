import copy
import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from logger import LogStringHandler
from variables import *
import utilities as ut
from digilabel import DigiLabel
from ui_filterwindow import Ui_FilterWindow

class FilterWindow(QDialog, Ui_FilterWindow):
    def __init__(self, para, blueberry):
        super(FilterWindow, self).__init__()
        self.setupUi(self)

        self.para = para
        self.blueberry = blueberry

        self.filter_code = None
        self.filter_para = {}

        self.captured_image = None
        self.captured_image_aratio = None
        self.captured_image_screen_size = (300, 300)

        self.set_action()

    def return_para(self):
        sender = self.sender()
        if sender == self.buttonBox:
            button = self.buttonBox.standardButton(sender.button(sender.clickedButton()))
            if button == QDialogButtonBox.Ok:
                self.accept()
            else:
                self.reject()
        return super().exec_()

    def set_action(self):
        self.comboFilter.currentTextChanged.connect(lambda: self.load_filter_parameters(reset=True))
        self.pushApplyFilter.clicked.connect(self.apply_filter_parameters)

    def take_a_picture(self):
        if not self.para.cam_conn: return

        self.captured_image = self.blueberry.take_a_picture(True)
        if self.captured_image is None: return
        if self.captured_image_aratio is None:
            self.captured_image_aratio = float(self.captured_image.shape[1]) / float(self.captured_image.shape[0])
        
        self.draw_image(self.captured_image, self.labelImage, self.captured_image_screen_size, self.captured_image_aratio)
        
    def draw_image(self, image, label, screen_size, aspect_ratio):
        if image is None: return
        
        image_copy = copy.deepcopy(image)
        dsize = (screen_size[0], screen_size[1])

        height, width = image_copy.shape[0], image_copy.shape[1]


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

    def load_filter_parameters(self, reset=False):
        class Item(QWidget):
            def __init__(self):
                QWidget.__init__(self)
                self.layout = QBoxLayout(QBoxLayout.LeftToRight)

            def add_lineedit(self, name):
                self.label = QLabel(name)
                self.linevalue = QLineEdit()
                self.layout.addWidget(self.label)
                self.layout.addWidget(self.linevalue)

                self.layout.setSizeConstraint(QBoxLayout.SetFixedSize)
                self.setLayout(self.layout)

        def set_value(fpara, lst):
            for i in range(lst.count()):
                item = lst.itemWidget(lst.item(i))
                name = item.label.text()
                value = int(item.linevalue.text())

                fpara[name] = value

        if reset:
            if self.comboFilter.currentText() == '':
                self.filter_code = NO_FILTER
                self.filter_para = {}
            elif self.comboFilter.currentText() == 'No Filter':
                self.filter_code = NO_FILTER
                self.filter_para = {}
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
        if self.para.filter_para is not None:
            for name, value in self.filter_para.items():
                flag = False
                witem = QListWidgetItem(self.listParameters)
                item = Item()
                item.add_lineedit(name)
                item.linevalue.textChanged.connect(lambda: set_value(self.filter_para, self.listParameters))
                item.linevalue.returnPressed.connect(lambda: set_value(self.filter_para, self.listParameters))
                self.listParameters.setItemWidget(witem, item)
                self.listParameters.addItem(witem)
                witem.setSizeHint(item.sizeHint())

                item.linevalue.setText(str(value))

    def apply_filter_parameters(self):
        self.para.filter_code = self.filter_code
        self.para.filter_para = self.filter_para
        self.draw_image(self.captured_image, self.labelImage, self.captured_image_screen_size, self.captured_image_aratio)