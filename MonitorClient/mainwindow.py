# -------------------------------------------------------
# MainWindow
# Author: Seohyeon An
# Date: 2022-04-21
#
# -------------------------------------------------------

import platform
import os, sys
import logging
import datetime
import yaml
import asyncio

import numpy as np
import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from variables import *
from blackberry import Blackberry
from blueberry import Blueberry
from strawberry import Strawberry
from ui_mainwindow import Ui_MainWindow
from setupwindow import SetupWindow
from hiddenwindow import HiddenWindow
from emittancewindow import EmittanceWindow
from logger import LogStringHandler
from digilabel import DigiLabel
from DigiMon import mutex

class MainWindow(QMainWindow, Ui_MainWindow):
    redraw_signal = Signal(str)

    def __init__(self, para, stream_queue, analysis_queue, return_queue):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.para = para

        self.dialog = False

        self.layoutMargin = 3
        self.layoutSpacing = 3

        base_path = os.path.abspath(os.path.dirname(__file__))
        self.iconRedLight = QIcon(os.path.join(base_path, 'icons', 'redlight.png'))
        self.iconGreenLight = QIcon(os.path.join(base_path, 'icons', 'greenlight.png'))
        self.iconSize = QSize(20,20)

        self.timer = QTimer()
        self.starttime = None

        self.labelCamera = DigiLabel(self.labelCamera)
        self.gridLayout.addWidget(self.labelCamera, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.__password = "profile"
        self.blackberry = Blackberry(para, self)
        self.blueberry = Blueberry(para, self, stream_queue, analysis_queue, return_queue)
        self.strawberry = Strawberry(para, self, return_queue)
        self.strawberry.working = True
        self.strawberry.start()

        self.setup = SetupWindow(para = self.para, blueberry=self.blueberry, blackberry=self.blackberry)
        
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textLog)
        self.logger.addHandler(handler)

        self.images_names = []
        self.names_for_saving = []
        self.names_for_table = []
        self.original_images = []

        self.livex = None
        self.livey = None

        self.last_picture = None
        self.profile = None
        self.beamx = None
        self.beamy = None

        self.beamx_size = []
        self.beamy_size = []

        self.set_action()
        
        self.main_size = [self.width(), self.height()]
        self.showMaximized()
        self.initialize()
        self.main_size = [self.width(), self.height()]
        self.plot_livex_size = [self.frameLiveXProfile.width(), self.frameLiveXProfile.height()]
        self.plot_livey_size = [self.frameLiveYProfile.width(), self.frameLiveYProfile.height()]
        self.plot_profile_size = [self.frameProfile.width(), self.frameProfile.height()]
        self.plot_beamx_size = [self.frameProfileX.width(), self.frameProfileX.height()]
        self.plot_beamy_size = [self.frameProfileY.width(), self.frameProfileY.height()]

        self.para.stream_size = [self.frameCamera.width(), self.frameCamera.height()]


    def set_action(self):
        # Signal connection
        self.redraw_signal.connect(self.blueberry.redraw_signal)

        # Hidden window - Closing Controller
        self.keyHidden = QShortcut(QKeySequence('Ctrl+F10'), self)
        self.keyHidden.activated.connect(self.close_server)

        # Image Screen
        self.labelCamera.clicked.connect(self.set_focused_line)
        self.labelCamera.move.connect(self.set_focused_line)

        # Camera Setup
        self.pushSetup.clicked.connect(self.setup_module)
        self.sliderFrameRate.valueChanged.connect(lambda: self.lineFrameRate.setText(str(self.sliderFrameRate.value())))
        self.sliderFrameRate.sliderReleased.connect(lambda: self.para.set_parameter(CAMERA_FPS, self.sliderFrameRate.value()))
        self.sliderRepeat.valueChanged.connect(lambda: self.lineRepeat.setText(str(self.sliderRepeat.value())))
        self.sliderRepeat.sliderReleased.connect(lambda: self.para.set_parameter(CAMERA_REPEAT, self.sliderRepeat.value()))

        # Camera Capture
        self.pushCapture.clicked.connect(lambda: self.para.set_parameter.emit(CAMERA_REQUEST_CAPTURE, self.sliderRepeat.value()))
        self.pushStop.clicked.connect(lambda: self.para.set_parameter.emit(CAMERA_REQUEST_STOP, -999))

        # Image rotation
        self.pushRotateLeft.clicked.connect(lambda: self.para.set_parameter(CAMERA_ROTATION_LEFT, 1))
        self.pushRotateRight.clicked.connect(lambda: self.para.set_parameter(CAMERA_ROTATION_RIGHT, 1))
        self.pushFlipUpDown.clicked.connect(lambda: self.para.set_parameter(CAMERA_FLIP_UP_DOWN, 1))
        self.pushFilpRightLeft.clicked.connect(lambda: self.para.set_parameter(CAMERA_FLIP_RIGHT_LEFT, 1))

        # Screen Zoom
        self.pushScreenDown.clicked.connect(lambda: self.blackberry.receive_request(ACTUATOR_REQUEST_GO_DOWN))
        self.pushScreenUp.clicked.connect(lambda: self.blackberry.receive_request(ACTUATOR_REQUEST_GO_UP))

        # Emittance Measurement
        self.pushEmittance.clicked.connect(self.measure_emittance)
        self.pushOpenImage.clicked.connect(self.open_image)

        def set_current(current):
            self.blueberry.current = current

        self.lineFieldGradient.textChanged.connect(lambda: set_current(self.lineFieldGradient.text()))
        self.tableProfiles.doubleClicked.connect(lambda: self.redraw_signal.emit(self.images_names[self.tableProfiles.currentIndex().row()]))

        self.timer.timeout.connect(self.timeout)

    def set_checked(self, checkbox, checked):
        if checked:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def initialize(self):
        self.labelCameraPixmap.setPixmap(self.iconRedLight.pixmap(self.iconSize))
        self.labelControllerPixmap.setPixmap(self.iconRedLight.pixmap(self.iconSize))
        self.labelCalibrationPixmap.setPixmap(self.iconRedLight.pixmap(self.iconSize))

        bluePen = pg.mkPen(color=(0,0,255), width=1)

        self.plotLiveX = pg.PlotWidget()
        self.plotLiveX.setBackground('w')
        self.plotLiveX.showGrid(x=True, y=True)
        self.plotLiveX.hideAxis('left')
        self.plotLiveX.hideAxis('bottom')
        #self.plotLiveX.setLabel('bottom', 'Horizontal')
        self.plotLiveX.setLabel('top', 'Horizontal', 'mm')
        #self.plotLiveX.setMaximumSize(9999, 120)
        #self.plotLiveX.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.liveXCurve = self.plotLiveX.plot(pen=bluePen)
        self.gridLiveXProfile.addWidget(self.plotLiveX)
        #self.plotLiveX.resize(self.frameLiveXProfile.width()-self.layoutMargin, self.frameLiveXProfile.height()-self.layoutMargin)

        self.plotLiveY = pg.PlotWidget()
        self.plotLiveY.setBackground('w')
        self.plotLiveY.showGrid(x=True, y=True)
        self.plotLiveY.hideAxis('bottom')
        self.plotLiveY.hideAxis('left')
        self.plotLiveY.setLabel('right', 'Vertical', 'mm')
        #self.plotLiveY.setLabel('bottom', 'Vertical')
        self.liveYCurve = self.plotLiveY.plot(pen=bluePen)
        self.gridLiveYProfile.addWidget(self.plotLiveY)
        self.plotLiveY.resize(self.frameLiveYProfile.width()-self.layoutMargin, self.frameLiveYProfile.height()-self.layoutMargin)

        self.plotProfile = pg.PlotWidget(size=(self.frameProfile.width()-self.layoutMargin, self.frameProfile.height()-self.layoutMargin))
        self.plotProfile.setBackground('w')
        self.plotProfile.showGrid(x=True, y=True)
        self.plotProfile.setLabel('left', 'Vertical', 'mm')
        self.plotProfile.setLabel('bottom', 'Horizontal', 'mm')
        self.gridProfile.addWidget(self.plotProfile)
        self.plotProfile.setMinimumSize(self.frameProfile.width()-self.layoutMargin, self.frameProfile.height()-self.layoutMargin)
        #self.plotProfile.setMaximumSize(self.frameProfile.width()-self.layoutMargin, self.frameProfile.height()-self.layoutMargin)
        #self.plotProfile.resize(self.frameProfile.width()-self.layoutMargin, self.frameProfile.height()-self.layoutMargin)

        self.plotProfileX = pg.PlotWidget()
        self.plotProfileX.setBackground('w')
        self.plotProfileX.showGrid(x=True, y=True)
        self.plotProfileX.setLabel('left', 'Intensity', 'A.U')
        self.plotProfileX.hideAxis('bottom')
        #self.plotProfileX.setLabel('bottom', 'Horizontal', 'mm')
        self.gridBeamSizeX.addWidget(self.plotProfileX)
        self.plotProfileX.resize(self.frameProfileX.width()-self.layoutMargin, self.frameProfileX.height()-self.layoutMargin)

        self.plotProfileY = pg.PlotWidget()
        self.plotProfileY.setBackground('w')
        self.plotProfileY.showGrid(x=True, y=True)
        #self.plotProfileY.setLabel('left', 'Intensity', '%')
        #self.plotProfileY.setLabel('bottom', 'Vertical', 'mm')
        self.plotProfileY.setLabel('bottom', 'Intensity', 'A.U')
        self.plotProfileY.hideAxis('left')
        self.gridBeamSizeY.addWidget(self.plotProfileY)
        self.plotProfileY.resize(self.frameProfileY.width()-self.layoutMargin, self.frameProfileY.height()-self.layoutMargin)

        self.plotPVHist = pg.PlotWidget()
        self.plotPVHist.setBackground('w')
        self.plotPVHist.setLabel('bottom', 'Pixel Value')
        self.plotPVHist.hideAxis('left')       
        self.gridPVHist.addWidget(self.plotPVHist)
        self.plotPVHist.resize(self.framePVHist.width()-self.layoutMargin, self.framePVHist.height()-self.layoutMargin)
        self.plotPVHist.setXRange(-1,256)
        #self.plotPVHist.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.lcdTimer.display("00:00.000")
    
        self.labelCamera.resize(self.frameCamera.width()-self.layoutMargin, self.frameCamera.height()-self.layoutMargin)
        self.para.intensity_line = [round(self.labelCamera.width()/2), round(self.labelCamera.height()/2)]

    def set_variable(self, idx, value):
        if idx == CAMERA_FPS:
            if value != self.para.fps:
                mutex.acquire()
                while not self.queue_for_analyze.empty():
                    self.queue_for_analyze.get()
                mutex.release()
        self.para.set_variable(idx, value)

    def setup_module(self):
        if self.dialog: return

        self.blueberry.working = False
        self.blueberry.stop()

        self.blackberry.working = False
        self.blackberry.stop()
        
        self.setup.show()
        self.dialog = True
        r = self.setup.return_para()
        if r:
            if self.para.cam_conn:
                self.labelCameraPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
            if self.para.ctl_conn:
                self.labelControllerPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
            if self.para.calibrated:
                self.labelCalibrationPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))

            if self.para.cam_conn:
                self.blueberry.working = True
                self.blueberry.start()
            
            if self.para.ctl_conn:
                self.blackberry.working = True
                self.blackberry.start()
                self.blackberry.setPriority(QThread.IdlePriority)

        self.dialog = False

    def measure_emittance(self):
        if self.dialog: return
        self.dialog = True
        emittance = EmittanceWindow(self)
        r = emittance.return_para()
        self.dialog = False

    def update_table(self, gradient, beamx, beamy, image):
        if any(image.split('/')[-1] == self.tableProfiles.item(i, 3).text() for i in range(self.tableProfiles.rowCount())):
            return
        self.tableProfiles.setRowCount(self.tableProfiles.rowCount() + 1)
        twidget = QTableWidgetItem(str(gradient))
        self.tableProfiles.setItem(self.tableProfiles.rowCount()-1, 0, twidget)

        for idx, value in enumerate([f'{beamx:.2f}', f'{beamy:.2f}', image.split('/')[-1]]):
            twidget = QTableWidgetItem(str(value))
            twidget.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableProfiles.setItem(self.tableProfiles.rowCount()-1, idx + 1, twidget)

    def close_server(self):
        hidden = HiddenWindow()
        r = hidden.return_para()
        if r and hidden.password == self.__password:
            self.logger.info("Close Controller Server")
            self.blackberry.send_command('quit')

    def open_image(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        if fname != '':
            if 'Window' in platform.system():
                fname = fname.replace("/", "\\")
            self.images_names.append(fname)
            self.redraw_signal.emit(fname)

    def set_focused_line(self):
        if not self.labelCamera.left: return
        self.para.intensity_line = [self.labelCamera.x, self.labelCamera.y]
        if self.labelCamera.x_end is not None:
            if self.labelCamera.x_end < self.labelCamera.width():
                self.para.intensity_line[0] = self.labelCamera.x_end
            else:
                self.para.intensity_line[0] = self.labelCamera.width() - 1
        if self.labelCamera.y_end is not None:
            if self.labelCamera.y_end < self.labelCamera.height():
                self.para.intensity_line[1] = self.labelCamera.y_end
            else:
                self.para.intensity_line[1] = self.labelCamera.height() - 1

    def resizeEvent(self, event):
        self.previous = self.main_size
        self.main_size = [self.width(), self.height()]
        self.plot_livex_size = [self.frameLiveXProfile.width(), self.frameLiveXProfile.height()]
        self.plot_livey_size = [self.frameLiveYProfile.width(), self.frameLiveYProfile.height()]
        self.plot_profile_size = [self.frameProfile.width(), self.frameProfile.height()]
        self.plot_beamx_size = [self.frameProfileX.width(), self.frameProfileX.height()]
        self.plot_beamy_size = [self.frameProfileY.width(), self.frameProfileY.height()]
        
        self.para.stream_size = [self.frameCamera.width(), self.frameCamera.height()]

        if self.labelCamera is not None:
            self.labelCamera.resize(self.para.stream_size[0], self.para.stream_size[1])
            self.blueberry.resized_pixel = [self.labelCamera.width(), self.labelCamera.height()]
        if self.profile is not None:
            self.profile.resize(self.plot_profile_size[0], self.plot_profile_size[1])
        if self.beamx is not None:
            self.beamx.resize(self.plot_beamx_size[0], self.plot_beamx_size[1])
        if self.beamy is not None:
            self.beamy.resize(self.plot_beamy_size[0], self.plot_beamy_size[1])

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.blueberry.stop()
            self.blackberry.stop()
            self.strawberry.stop()
            event.accept()
        else:
            event.ignore()

    @Slot(str)
    def actuator_status(self, message):
        self.labelScreenStatus.setText(f"Status: {message}")

    @Slot(bool)
    def stopwatch(self, start=False):
        if start:
            self.starttime = QTime.currentTime()
            self.lcdTimer.display("00:00.000")
            self.timer.start()
        else:
            self.timer.stop()

    def timeout(self):
        current = QTime.currentTime()
        difference = self.starttime.msecsTo(current)
        
        quo = difference / 1000
        rem = difference % 1000
        msec = round(rem)
        quo2 = quo / 60
        rem2 = quo % 60
        second = round(rem2)
        minute = round(quo2)
        time = QTime(0, minute, s=second, ms=msec).toString("mm:ss.zzz")
        self.lcdTimer.display(time)

    @Slot(str, str)
    def receive_log(self, level, message):
        if level == 'DEBUG':
            self.logger.debug(message)
        elif level == 'INFO':
            self.logger.info(message)
        elif level == 'WARNING':
            self.logger.warning(message)
        elif level == 'ERROR':
            self.logger.error(message)
        elif level == 'CRITICAL':
            self.logger.critical(message)

    @Slot(str)
    def save_image(self, image):
        self.images_names.append(str(image))
        self.names_for_table.append(str(image))
        self.names_for_saving.append(str(image))

    @Slot(list)
    def image_stream(self, element):
        image, xbin, ybin, xhist, yhist = element

        if len(image.shape) == 3:
            height, width, channel = image.shape
            qImg = QImage(image.data, width, height, width*channel, QImage.Format_BGR888)
        else:
            height, width = image.shape
            qImg = QImage(image.data, width, height, width, QImage.Format_Grayscale8)
        
        pixmap = QPixmap.fromImage(qImg)
            
        painter = QPainter(pixmap)
        painter.setPen(QPen(QColor(3, 252, 127), 1.5, Qt.DashLine))
        if self.para.intensity_line != [-1,-1]:
            x, y = self.para.intensity_line[0], self.para.intensity_line[1]
        else:
            x = round(self.labelCamera.width()/2) - 1
            y = round(self.labelCamera.height()/2)- 1
        painter.drawLine(0, y, self.labelCamera.width(), y)
        painter.drawLine(x, 0, x, self.labelCamera.height())
        painter.end()
        
        self.labelCamera.setPixmap(pixmap)

        self.liveXCurve.setData(xbin, xhist)
        self.liveYCurve.setData(-np.array(yhist).tolist(), ybin)

        self.plotLiveX.setLimits(xMin=min(xbin), xMax=max(xbin))
        self.plotLiveY.setLimits(yMin=min(ybin), yMax=max(ybin))

        arr = image.reshape(-1)
        hist, bin = np.histogram(arr, np.arange(0,257))
        histogram = pg.BarGraphItem(x=bin[:-1], height=hist, width = 1, brush=(107,200,224))
        self.plotPVHist.addItem(histogram)
        self.plotPVHist.setLogMode(False, True)
        self.plotPVHist.setXRange(-1,256)

    @Slot(list)
    def image_analysis(self, element):
        para, image, xbin, ybin, xhist, yhist, xfitvalue, yfitvalue, center_pixel, center_real, xwidth, ywidth = element
        self.para = para
        gara_pen = pg.mkPen(color=(255,255,255), width=0)
        self.plotProfile.clear()

        from colour import Color
        blue, red = Color(hex="#dedeff"), Color('red')
        colors = blue.range_to(red, 255)
        colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
        look_up_table = colors_array.astype(np.uint8)

        # PyqtGraph에서 90도 돌아져서 그림이 그려져서 돌림...
        image = cv2.flip(image, 0)
        image = np.transpose(image)

        #graphics = np.array(graphics)
        #graphics = cv2.rotate(graphics, cv2.ROTATE_90_CLOCKWISE)
        #if not graphics.shape != 2:
        #    grayimage = cv2.cvtColor(graphics, cv2.COLOR_BGR2GRAY)
        if self.para.calibrated:
            self.plotProfile.setLabel('left', 'Vertical', 'mm')
            self.plotProfile.setLabel('bottom', 'Horizontal', 'mm')
        else:
            self.plotProfile.setLabel('left', 'Vertical', 'pixel')
            self.plotProfile.setLabel('bottom', 'Horizontal', 'pixel')

        image_item = pg.ImageItem()
        image_item.setLookupTable(look_up_table)
        image_item.setImage(image)

        image_item.setTransform(QTransform().scale(1.0/self.para.pixel_per_mm[0], 1.0/self.para.pixel_per_mm[1]).translate(
                -self.para.coordinate_center[0]/self.para.pixel_per_mm[0], -self.para.coordinate_center[1]/self.para.pixel_per_mm[1]))

        self.plotProfile.addItem(image_item)
        self.plotProfile.addLine(x=center_real[0], y=None, pen=pg.mkPen(color=(29, 36, 229), width=2))
        self.plotProfile.addLine(x=None, y=center_real[1], pen=pg.mkPen(color=(29, 36, 229), width=2))
        self.plotProfile.addLine(x=0, y=None, pen=pg.mkPen(color=(40, 246, 60), width=2))
        self.plotProfile.addLine(x=None, y=0, pen=pg.mkPen(color=(40, 246, 60), width=2))
        self.plotProfile.setXRange(min(xbin), max(xbin))
        self.plotProfile.setYRange(min(ybin), max(ybin))

        txt_pos = f"Center: ({center_real[1]:.2f}, {center_real[0]:.2f}) mm  Size: ({xwidth[0]:.2f} ± {xwidth[1]:.2f}, {ywidth[0]:.2f} ± {ywidth[1]:.2f}) mm"
        self.labelPosition.setText(txt_pos)

        name = self.names_for_table[0]
        self.names_for_table.pop(0)
        self.update_table(self.lineFieldGradient.text(), xwidth[0], ywidth[0], name)

        self.plotProfileX.clear()
        self.plotProfileX.setXRange(min(xbin), max(xbin))
        self.plotProfileX.setYRange(min(xhist), max(xhist)+5)
        self.plotProfileX.plot(xbin, xhist, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
        self.plotProfileX.plot(xbin, xfitvalue, pen=pg.mkPen(color=(227, 28, 14), width=2))
        self.plotProfileX.addLine(x=center_real[0], y=None, pen=pg.mkPen(color=(29, 36, 229), width=2))

        self.plotProfileY.clear()
        self.plotProfileY.setXRange(min(yhist),max(yhist)+5)
        self.plotProfileY.setYRange(min(ybin), max(ybin))
        self.plotProfileY.plot(yhist, ybin, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
        self.plotProfileY.plot(yfitvalue, ybin, pen=pg.mkPen(color=(227, 28, 14), width=2))
        self.plotProfileY.addLine(x=None, y=center_real[1], pen=pg.mkPen(color=(29, 36, 229), width=2))
        #self.plotProfileY.plot([center_real[1] for i in range(len(ybin))], ybin, pen=pg.mkPen(color=(29, 36, 229), width=2))

        arr = image.reshape(-1)
        hist, bin = np.histogram(arr, np.arange(0,257))
        histogram = pg.BarGraphItem(x=bin[:-1], height=hist, width = 1, brush=(107,200,224))
        self.plotPVHist.addItem(histogram)
        self.plotPVHist.setLogMode(False, True)
        self.plotPVHist.setXRange(-1,256)

        self.save_pretty_plot(element)

    # UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
    def save_pretty_plot(self, element):
        para, image, xbin, ybin, xhist, yhist, xfitvalue, yfitvalue, center_pixel, center_real, xwidth, ywidth = element
        #transformed_image = cv2.rotate(transformed_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #image = np.transpose(image)
        #transformed_image = cv2.resize(transformed_image, dsize=(400,400), interpolation=cv2.INTER_LINEAR)
        gridspec = GridSpec(nrows=2, ncols=2, width_ratios=[4,1], height_ratios=[1,4], wspace=0.025, hspace=0.025)

        #plt.rcParams['figure.figsize'] = (4.687, 4.687)
        plt.rcParams['figure.figsize'] = (6, 6)

        plt.subplot(gridspec[1,0])
        plt.tick_params(axis='both', direction='in')
        plt.xlabel(r"Horizontal Axis [mm]")
        plt.ylabel(r"Vertical Axis [mm]")
        
        plt.imshow(image, extent=(min(xbin), max(xbin), min(ybin), max(ybin)), interpolation='nearest', aspect='auto', cmap=plt.cm.jet)
        #plt.xlim(min(xbin), max(xbin))
        #yplt.ylim(min(ybin), max(ybin))
        #plt.hist(xhist_percent, bins=transformed_image.shape[0])
        #plt.hist2d(xhist_percent, yhist_percent, bins=[transformed_image.shape[0], transformed_image.shape[1]])
        plt.axvline(x=0, color='#0ffc03', linestyle=(0, (3.5, 2.5)), linewidth=0.6, zorder=3)
        plt.axhline(y=0, color='#0ffc03', linestyle=(0, (3.5, 2.5)), linewidth=0.6, zorder=2)
        plt.axvline(x=center_real[0], color='#d703fc', linestyle='solid', linewidth=0.6, zorder=4)
        plt.axhline(y=center_real[1], color='#d703fc', linestyle='solid', linewidth=0.6, zorder=5)
        txt_pos = f"Center: {center_real[0]:.2f}, {center_real[1]:.2f} mm\nSize(2w): {xwidth[0]:.2f} ± {xwidth[1]:.2f}, {ywidth[0]:.2f} ± {ywidth[1]:.2f} mm"
        plt.text(min(xbin)+abs(min(xbin))*0.15, max(ybin)-max(ybin)*0.3, txt_pos, color='#ffff14')

        plt.subplot(gridspec[0,0])
        plt.xlim(min(xbin), max(xbin))
        plt.tick_params(axis='both', direction='in')
        plt.gca().axes.xaxis.set_ticklabels([])
        plt.gca().axes.yaxis.set_ticklabels([])

        plt.axvline(x=0, color='#0ffc03', linestyle='dashed', linewidth=0.6, zorder=1)
        plt.axvline(x=center_real[0], color='#d703fc', linestyle='solid', linewidth=0.6, zorder=2)
        plt.plot(xbin, xhist, color='#000000', zorder=3)
        plt.plot(xbin, xfitvalue, color='#ff0000', zorder=4)

        plt.subplot(gridspec[1,1])
        plt.ylim(min(ybin), max(ybin))
        plt.tick_params(axis='both', direction='in')
        plt.gca().axes.xaxis.set_ticklabels([])
        plt.gca().axes.yaxis.set_ticklabels([])

        plt.axhline(y=0, color='#0ffc03', linestyle='dashed', linewidth=0.6, zorder=1)
        plt.axhline(y=center_real[1], color='#d703fc', linestyle='solid', linewidth=0.6, zorder=2)
        plt.plot(yhist, ybin, color='#000000', zorder=3)
        plt.plot(yfitvalue, ybin, color='#ff0000', zorder=4)
        #plt.hist(yhist_percent, bins=transformed_image.shape[1], orientation=u'vertical')
        
        outdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if 'Windows' in platform.system():
            name = self.names_for_saving[0].split('\\')[-1]
        elif 'Linux' in platform.system():
            name = self.names_for_saving[0].split('/')[-1]
        if '.' in name:
            name = name.split('.')[0]
        self.names_for_saving.pop(0)
        plt.savefig(os.path.join(outdir, 'profile', f'BeamProfile_{name}.pdf'))
        plt.close()