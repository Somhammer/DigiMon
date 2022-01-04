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
from ui_mainwindow import Ui_MainWindow
from setupwindow import SetupWindow
from hiddenwindow import HiddenWindow
from emittancewindow import EmittanceWindow
from logger import LogStringHandler
from custom_classes import DigiLabel

class MainWindow(QMainWindow, Ui_MainWindow):
    parameter_signal = Signal(int, int)
    redraw_signal = Signal(str)

    def __init__(self, queue_for_analyze, return_queue):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.queue_for_analyze = queue_for_analyze
        self.return_queue = return_queue

        self.dialog = False

        self.layoutMargin = 3
        self.layoutSpacing = 3

        base_path = os.path.abspath(os.path.dirname(__file__))
        self.iconRedLight = QIcon(os.path.join(base_path, 'icons', 'redlight.png'))
        self.iconGreenLight = QIcon(os.path.join(base_path, 'icons', 'greenlight.png'))
        self.iconSize = QSize(20,20)

        self.timer = QTimer()
        self.starttime = None

        self.camera_connected = False
        self.controller_connected = False
        self.calibrated = False

        self.labelCamera = DigiLabel(self.labelCamera)
        self.gridLayout.addWidget(self.labelCamera, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.__password = "profile"
        self.blackberry = Blackberry(parent=self)
        self.blueberry = Blueberry(queue_for_analyze=self.queue_for_analyze, return_queue=self.return_queue, parent=self)
        self.setup = SetupWindow(parent=self)
        
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textLog)
        self.logger.addHandler(handler)

        self.images_names = []
        self.original_images = []
        self.filtered_images = []

        self.livex = None
        self.livey = None

        self.last_picture = None
        self.profile = None
        self.beamx = None
        self.beamy = None

        self.beamx_size = []
        self.beamy_size = []
        self.intensity_line = [-1,-1]

        self.set_action()

        #self.initialize()
        self.main_size = [self.width(), self.height()]
        self.showMaximized()
        #self.show()
        self.initialize()
        self.main_size = [self.width(), self.height()]
        self.image_size = [self.frameCamera.width(), self.frameCamera.height()]
        self.plot_livex_size = [self.frameLiveXProfile.width(), self.frameLiveXProfile.height()]
        self.plot_livey_size = [self.frameLiveYProfile.width(), self.frameLiveYProfile.height()]
        self.plot_profile_size = [self.frameProfile.width(), self.frameProfile.height()]
        self.plot_beamx_size = [self.frameProfileX.width(), self.frameProfileX.height()]
        self.plot_beamy_size = [self.frameProfileY.width(), self.frameProfileY.height()]

    def set_action(self):
        # Signal connection
        self.parameter_signal.connect(self.blueberry.receive_signal)
        self.redraw_signal.connect(self.blueberry.redraw_signal)

        # Hidden window - Closing Controller
        self.keyHidden = QShortcut(QKeySequence('Ctrl+F10'), self)
        self.keyHidden.activated.connect(self.close_server)
        # Network connection
        #self.checkConnectController.clicked.connect(lambda: self.set_checked(self.checkConnectController, self.blackberry.connected))
        #self.checkConnectCamera.clicked.connect(lambda: self.set_checked(self.checkConnectCamera, self.blueberry.connected))

        # Image Screen
        self.labelCamera.clicked.connect(self.set_line)
        self.labelCamera.move.connect(self.set_line)

        # Camera Setup
        self.pushSetup.clicked.connect(self.setup_module)
        self.sliderFrameRate.valueChanged.connect(lambda: self.lineFrameRate.setText(str(self.sliderFrameRate.value())))
        self.sliderFrameRate.sliderReleased.connect(lambda: self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value()))
        self.sliderRepeat.valueChanged.connect(lambda: self.lineRepeat.setText(str(self.sliderRepeat.value())))
        self.sliderRepeat.sliderReleased.connect(lambda: self.parameter_signal.emit(CAMERA_REPEAT, self.sliderRepeat.value()))

        # Camera Capture
        self.pushCapture.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_CAPTURE, self.sliderRepeat.value()))
        self.pushStop.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_STOP, -999))

        # Image rotation
        self.pushRotateLeft.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_ROTATION_LEFT, 1))
        self.pushRotateRight.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_ROTATION_RIGHT, 1))
        self.pushFlipUpDown.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_FLIP_UP_DOWN, 1))
        self.pushFilpRightLeft.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_FLIP_RIGHT_LEFT, 1))

        # Screen Zoom
        self.pushScreenDown.clicked.connect(lambda: self.blackberry.receive_request(REQUEST_GO_DOWN))
        self.pushScreenUp.clicked.connect(lambda: self.blackberry.receive_request(REQUEST_GO_UP))

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
        self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value())
        self.parameter_signal.emit(CAMERA_REPEAT, self.sliderRepeat.value())
        self.parameter_signal.emit(CAMERA_GAIN, 100)
        self.parameter_signal.emit(CAMERA_EXPOSURE_TIME, 500)
        
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
        self.plotProfileX.setLabel('left', 'Intensity', '%')
        self.plotProfileX.hideAxis('bottom')
        #self.plotProfileX.setLabel('bottom', 'Horizontal', 'mm')
        self.gridBeamSizeX.addWidget(self.plotProfileX)
        self.plotProfileX.resize(self.frameProfileX.width()-self.layoutMargin, self.frameProfileX.height()-self.layoutMargin)

        self.plotProfileY = pg.PlotWidget()
        self.plotProfileY.setBackground('w')
        self.plotProfileY.showGrid(x=True, y=True)
        #self.plotProfileY.setLabel('left', 'Intensity', '%')
        #self.plotProfileY.setLabel('bottom', 'Vertical', 'mm')
        self.plotProfileY.setLabel('bottom', 'Intensity', '%')
        self.plotProfileY.hideAxis('left')
        self.gridBeamSizeY.addWidget(self.plotProfileY)
        self.plotProfileY.resize(self.frameProfileY.width()-self.layoutMargin, self.frameProfileY.height()-self.layoutMargin)

        self.lcdTimer.display("00:00.000")
    
        self.labelCamera.resize(self.frameCamera.width()-self.layoutMargin, self.frameCamera.height()-self.layoutMargin)

    def setup_module(self):
        if self.dialog: return
        self.blueberry.working = False
        self.blueberry.stop()
        #self.blueberry.initialize()

        self.blackberry.working = False
        self.blackberry.stop()
        self.blackberry.initialize()

        self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value())
        self.parameter_signal.emit(CAMERA_REPEAT, self.sliderRepeat.value())
        self.parameter_signal.emit(CAMERA_GAIN, 100)
        self.parameter_signal.emit(CAMERA_EXPOSURE_TIME, 500)
        self.blackberry.initialize()
        if self.camera_connected or self.controller_connected or self.calibrated:
            reset = False
        else:
            reset = True
        if self.setup.reset_all: 
            reset = True
        
        self.setup.initialize_parameter(reset)
        self.setup.show()
        #setup = SetupWindow(self, reset)
        self.dialog = True
        r = self.setup.return_para()
        if r:
            if self.setup.camera_connected:
                self.camera_connected = True
                self.labelCameraPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
            if self.setup.controller_connected:
                self.controller_connected = True
                self.labelControllerPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
            if self.setup.calibrated:
                self.calibrated = True
                self.labelCalibrationPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
                self.blueberry.do_transformation = True
                self.blueberry.transform_points = self.setup.original_points
                self.blueberry.destination_points = self.setup.destination_points
                self.blueberry.pixel_per_mm = self.setup.pixel_per_mm
                self.blueberry.rotate_angle = float(self.setup.lineRotationAngle.text())

            self.blueberry.gain = self.setup.gain
            self.blueberry.exposure_time = self.setup.exposure_time
            self.blueberry.ROI = self.setup.ROI
            self.blueberry.filter_code = self.setup.filter_code
            self.blueberry.filter_para = self.setup.filter_para
            self.blueberry.calibration_angle = self.setup.calibration_angle

            if self.blueberry.connected:
                self.blueberry.working = True
                self.blueberry.start()
            
            if self.blackberry.connected:
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

    def set_line(self):
        if not self.labelCamera.left: return
        self.intensity_line = [self.labelCamera.x, self.labelCamera.y]
        if self.labelCamera.x_end is not None:
            self.intensity_line[0] = self.labelCamera.x_end
        if self.labelCamera.y_end is not None:
            self.intensity_line[1] = self.labelCamera.y_end
        self.blueberry.intensity_line = self.intensity_line

    def resizeEvent(self, event):
        self.previous = self.main_size
        self.main_size = [self.width(), self.height()]
        self.image_size = [self.frameCamera.width(), self.frameCamera.height()]
        self.plot_livex_size = [self.frameLiveXProfile.width(), self.frameLiveXProfile.height()]
        self.plot_livey_size = [self.frameLiveYProfile.width(), self.frameLiveYProfile.height()]
        self.plot_profile_size = [self.frameProfile.width(), self.frameProfile.height()]
        self.plot_beamx_size = [self.frameProfileX.width(), self.frameProfileX.height()]
        self.plot_beamy_size = [self.frameProfileY.width(), self.frameProfileY.height()]

        if self.labelCamera is not None:
            self.labelCamera.resize(self.image_size[0], self.image_size[1])
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

    @Slot(int, list, list)
    @Slot(int, np.ndarray)
    def update_screen(self, target, graphics, additional_curves=None):
        gara_pen = pg.mkPen(color=(255,255,255), width=0)

        if target == PICTURE_SCREEN:
            self.last_picture = graphics
            if len(graphics.shape) == 3:
                height, width, channel = graphics.shape
                qImg = QImage(graphics.data, width, height, width*channel, QImage.Format_BGR888)
            else:
                height, width = graphics.shape
                qImg = QImage(graphics.data, width, height, width, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.labelCamera.width(), self.labelCamera.height())

            painter = QPainter(pixmap)
            painter.setPen(QPen(QColor(3, 252, 127), 1.5, Qt.DashLine))
            if self.intensity_line != [-1,-1]:
                x, y = self.intensity_line[0], self.intensity_line[1]
            else:
                x, y = round(self.labelCamera.width()/2), round(self.labelCamera.height()/2)
            painter.drawLine(0, y, self.labelCamera.width(), y)
            painter.drawLine(x, 0, x, self.labelCamera.height())
            painter.end()
            self.labelCamera.setPixmap(pixmap)
        elif any(target == i for i in [LIVE_XPROFILE_SCREEN, LIVE_YPROFILE_SCREEN]):
            if target == LIVE_XPROFILE_SCREEN:
                curve = self.liveXCurve
            else:
                curve = self.liveYCurve
            x1 = []
            y1 = []
            for value in graphics:
                if target == LIVE_XPROFILE_SCREEN:
                    x1.append(value[0])
                else:
                    x1.append(-value[0])
                y1.append(value[1])
            if target == LIVE_XPROFILE_SCREEN:
                curve.setData(x1, y1)
            else:
                curve.setData(y1, x1)
            #plot.setXRange(min(x1),max(x1))
            #plot.setYRange(min(y1), max(y1)+5)

            #plot.plot(x1, y1, pen=gara_pen)#, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            #txt_pos = f"Center: ({additional_curves[0]:.2f}, {additional_curves[1]:.2f}) mm\nSize: ({additional_curves[2]:.2f}, {additional_curves[3]:.2f}) mm"
            #text = pg.TextItem(text=txt_pos, color=(0,0,0))
            #text.setPos(-15,15)
            #plot.addItem(text)
        elif target == PROFILE_SCREEN:
            self.plotProfile.clear()

            from colour import Color
            blue, red = Color(hex="#dedeff"), Color('red')
            colors = blue.range_to(red, 255)
            colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
            look_up_table = colors_array.astype(np.uint8)

            # PyqtGraph에서 90도 돌아져서 그림이 그려져서 돌림...

            graphics = np.array(graphics)
            graphics = cv2.rotate(graphics, cv2.ROTATE_90_CLOCKWISE)
            if not graphics.shape != 2:
                grayimage = cv2.cvtColor(graphics, cv2.COLOR_BGR2GRAY)
            
            image = pg.ImageItem()
            image.setLookupTable(look_up_table)
            image.setImage(np.array(graphics))
            scale_x = 1.0/self.blueberry.pixel_per_mm[0]
            scale_y = 1.0/self.blueberry.pixel_per_mm[1]
            image.setTransform(QTransform().scale(scale_x, scale_y).translate(-graphics.shape[0]/2.0,-graphics.shape[1]/2.0))

            self.plotProfile.addItem(image)
            txt_pos = f"Center: ({additional_curves[0]:.2f}, {additional_curves[2]:.2f}) mm  Size: ({additional_curves[1]:.2f}, {additional_curves[3]:.2f}) mm"
            self.labelPosition.setText(txt_pos)

            self.filtered_images.append(np.array(graphics))
            self.update_table(self.lineFieldGradient.text(), additional_curves[1], additional_curves[3], self.images_names[-1])
        elif target == XSIZE_SCREEN:
            self.plotProfileX.clear()
            x1, y1 = [], []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            self.plotProfileX.setXRange(min(x1),max(x1))
            self.plotProfileX.setYRange(min(y1), max(y1)+5)
            self.plotProfileX.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            if additional_curves is not None:
                if len(additional_curves) > 0:
                    x2, y2 = [], []
                    for value in additional_curves:
                        x2.append(value[0])
                        y2.append(value[1])
                    self.plotProfileX.plot(x2, y2, pen=pg.mkPen(color=(227, 28, 14), width=2))
        elif target == YSIZE_SCREEN:
            self.plotProfileY.clear()
            x1, y1 = [], []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            self.plotProfileY.setXRange(min(y1),max(y1))
            self.plotProfileY.setYRange(min(x1), max(x1)+5)

            self.plotProfileY.plot(y1, x1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            if additional_curves is not None:
                if len(additional_curves) > 0:
                    x2, y2 = [], []
                    for value in additional_curves:
                        x2.append(value[0])
                        y2.append(value[1])
                    self.plotProfileY.plot(y2, x2, pen=pg.mkPen(color=(227, 28, 14), width=2))
        else:
            return

        if any(target == i for i in [XSIZE_SCREEN, YSIZE_SCREEN, PROFILE_SCREEN]):
            self.image_size = [self.frameCamera.width(), self.frameCamera.height()]

    @Slot(np.ndarray, list, list, np.ndarray, np.ndarray, list, list)
    def save_pretty_plot(self, transformed_image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline):
        transformed_image = cv2.rotate(transformed_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        mm_per_pixel = [1.0/self.blueberry.pixel_per_mm[0], 1.0/self.blueberry.pixel_per_mm[1]]
        #transformed_image = cv2.resize(transformed_image, dsize=(400,400), interpolation=cv2.INTER_LINEAR)
        gridspec = GridSpec(nrows=2, ncols=2, width_ratios=[4,1], height_ratios=[1,4], wspace=0.025, hspace=0.025)

        plt.rcParams['figure.figsize'] = (4.687, 4.687)

        plt.subplot(gridspec[1,0])
        plt.tick_params(axis='both', direction='in')
        plt.xlabel(r"Horizontal Axis [mm]")
        plt.ylabel(r"Vertical Axis [mm]")
        
        xmax, ymax = np.argmax(xhist_percent), np.argmax(yhist_percent)
        xcenter, ycenter = xbin[xmax], ybin[ymax]
        xlength, ylength = len(np.where(xhist_percent > 32)[0]) * mm_per_pixel[0], len(np.where(yhist_percent > 32)[0]) * mm_per_pixel[1]
        
        plt.xlim(min(xbin), max(xbin))
        plt.ylim(min(ybin), max(ybin))
        #plt.hist(xhist_percent, bins=transformed_image.shape[0])
        #plt.hist2d(xhist_percent, yhist_percent, bins=[transformed_image.shape[0], transformed_image.shape[1]])
        plt.axvline(x=0, color='#0ffc03', linestyle=(0, (3.5, 2.5)), linewidth=0.6, zorder=3)
        plt.axhline(y=0, color='#0ffc03', linestyle=(0, (3.5, 2.5)), linewidth=0.6, zorder=2)
        plt.axvline(x=xcenter, color='#d703fc', linestyle='solid', linewidth=0.6, zorder=4)
        plt.axhline(y=ycenter, color='#d703fc', linestyle='solid', linewidth=0.6, zorder=5)
        #plt.imshow(transformed_image, extent=(min()), interpolation='nearest', aspect='auto', zorder=1, cmap='gray')
        plt.imshow(transformed_image, extent=(min(xbin), max(xbin), min(ybin), max(ybin)), interpolation='nearest', aspect='auto', cmap=plt.cm.jet)
        #plt.hist2d(xbin, ybin, weights=transformed_image.flatten())#, cmap=plt.cm.jet)
        #yplt.imshow(transformed_image)
        txt_pos = f"Center: {xcenter:.2f}, {ycenter:.2f} mm\nSize($1\sigma$): {xlength:.2f}, {ylength:.2f} mm"
        plt.text(min(xbin)+abs(min(xbin))*0.15, max(ybin)-max(ybin)*0.3, txt_pos, color='#ffff14')

        plt.subplot(gridspec[0,0])
        plt.tick_params(axis='both', direction='in')
        plt.gca().axes.xaxis.set_ticklabels([])
        plt.gca().axes.yaxis.set_ticklabels([])

        plt.axvline(x=0, color='#0ffc03', linestyle='dashed', linewidth=0.6, zorder=1)
        plt.axvline(x=xcenter, color='#d703fc', linestyle='solid', linewidth=0.6, zorder=2)
        plt.plot(xbin, xhist_percent, color='#000000', zorder=3)
        plt.plot(xbin, [i[1] for i in xfitline], color='#ff0000', zorder=4)

        plt.subplot(gridspec[1,1])
        plt.tick_params(axis='both', direction='in')
        plt.gca().axes.xaxis.set_ticklabels([])
        plt.gca().axes.yaxis.set_ticklabels([])

        plt.axhline(y=0, color='#0ffc03', linestyle='dashed', linewidth=0.6, zorder=1)
        plt.axhline(y=ycenter, color='#d703fc', linestyle='solid', linewidth=0.6, zorder=2)
        plt.plot(yhist_percent, ybin, color='#000000', zorder=3)
        plt.plot([i[1] for i in yfitline], ybin, color='#ff0000', zorder=4)
        #plt.hist(yhist_percent, bins=transformed_image.shape[1], orientation=u'vertical')
        
        outdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if 'Windows' in platform.system():
            name = self.images_names[-1].split('\\')[-1]
        elif 'Linux' in platform.system():
            name = self.images_names[-1].split('/')[-1]
        if '.' in name:
            name = name.split('.')[0]
        plt.savefig(os.path.join(outdir, 'profile', f'BeamProfile_{name}.pdf'))
        plt.close()