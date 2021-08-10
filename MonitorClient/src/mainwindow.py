import os, sys
import logging
import numpy as np
import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

from src.variables import *
from src.blackberry import Blackberry
from src.blueberry import Blueberry
from src.ui_mainwindow import Ui_MainWindow
from src.hiddenwindow import HiddenWindow
from src.emittancewindow import EmittanceWindow
from src.calibrationwindow import CalibrationWindow
from src.filterwindow import FilterWindow
from src.logger import LogStringHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    parameter_signal = Signal(int, int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.__password = "NCCproton"
        self.blackberry = Blackberry()
        self.blueberry = Blueberry(parent=self)
        
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textLog)
        self.logger.addHandler(handler)

        self.images_names = []
        self.original_images = []
        self.filtered_images = []

        self.image_size = [None,None]
        self.profile_size = [None,None]
        self.beamx_size = [None, None]
        self.beamy_size = [None, None]

        self.profile = None
        self.beamx = None
        self.beamy = None

        self.set_action()

        self.initialize()
        self.showMaximized()

    def set_action(self):
        # Signal connection
        self.parameter_signal.connect(self.blueberry.receive_signal)
        #self.blueberry.thread_signal.connect(self.receive_signal)
        #self.blueberry.thread_logger_signal.connect(self.receive_log)

        # Hidden window - Closing Controller
        self.keyHidden = QShortcut(QKeySequence('Ctrl+F10'), self)
        self.keyHidden.activated.connect(self.close_server)
        # Network connection
        self.checkConnectController.clicked.connect(lambda: self.set_checked(self.checkConnectController, self.blackberry.connected))
        self.checkConnectCamera.clicked.connect(lambda: self.set_checked(self.checkConnectCamera, self.blueberry.connected))
        self.pushReconnect.clicked.connect(self.initialize)

        # Camera Capture
        self.pushCapture.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_CAPTURE, self.sliderRepeat.value()))
        self.pushStop.clicked.connect(lambda: self.parameter_signal.emit(CAMERA_STOP, -999))
        # Camera Controll
        self.sliderGain.valueChanged.connect(lambda: self.lineGain.setText(str(self.sliderGain.value())))
        self.sliderGain.sliderReleased.connect(lambda: self.parameter_signal.emit(CAMERA_GAIN, self.sliderGain.value()))
        self.sliderFrameRate.valueChanged.connect(lambda: self.lineFrameRate.setText(str(self.sliderFrameRate.value())))
        self.sliderFrameRate.sliderReleased.connect(lambda: self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value()))
        self.sliderExposureTime.valueChanged.connect(lambda: self.lineExposureTime.setText(str(self.sliderExposureTime.value())))
        self.sliderExposureTime.sliderReleased.connect(lambda: self.parameter_signal.emit(CAMERA_EXPOSURE_TIME, self.sliderExposureTime.value()))
        self.sliderRepeat.valueChanged.connect(lambda: self.lineRepeat.setText(str(self.sliderRepeat.value())))
        self.sliderRepeat.sliderReleased.connect(lambda: self.parameter_signal.emit(CAMERA_REPEAT, self.sliderRepeat.value()))
        self.sliderX0.valueChanged.connect(lambda: self.lineX0.setText(str(self.sliderX0.value())))
        self.sliderY0.valueChanged.connect(lambda: self.lineY0.setText(str(self.sliderY0.value())))
        self.sliderDX.valueChanged.connect(lambda: self.lineDX.setText(str(self.sliderDX.value())))
        self.sliderDY.valueChanged.connect(lambda: self.lineDY.setText(str(self.sliderDY.value())))
        # Screen Control
        self.sliderScreenSpace.valueChanged.connect(lambda: self.lineScreenSpace.setText(str(self.sliderScreenSpace.value())))
        # Emittance Measurement
        self.pushCalibration.clicked.connect(self.calibrate_image)
        self.pushFilter.clicked.connect(self.filter_image)
        #self.pushCalculate.clicked.connect()

    def set_checked(self, checkbox, checked):
        if checked:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def initialize(self):
        self.connect_network(self.blackberry, self.checkConnectController)
        self.connect_network(self.blueberry, self.checkConnectCamera)

        self.parameter_signal.emit(CAMERA_GAIN, self.sliderGain.value())
        self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value())
        self.parameter_signal.emit(CAMERA_EXPOSURE_TIME, self.sliderExposureTime.value())
        self.parameter_signal.emit(CAMERA_REPEAT, self.sliderRepeat.value())

        self.blueberry.start()

    def connect_network(self, berry, checkbox):
        if berry.connected: return
        berry.initialize()
        self.logger.info(f"Try to connect to {berry.name}...")
        if berry.connected:
            self.logger.info("Connection is succeed")
        else:
            self.logger.error(f"Connection is failed. Please, reconnect to {berry.name}...")
        self.set_checked(checkbox, berry.connected)

    def calibrate_image(self):
        calibration = CalibrationWindow()
        r = calibration.return_para()
        if r:
            self.blueberry.transform_points = calibration.original_points

    def filter_image(self):
        #filtering = FilterWindow(self, self.original_images[-1])
        filtering = FilterWindow(self, cv2.imread("/home/seohyeon/work/BeamMonitor/SCFC/data/raw_data/500ms_6db.bmp"))
        r = filtering.return_para()
        if r:
            self.blueberry.filter_code = filtering.code
            self.blueberry.filter_para = filtering.parameters
    
    def measure_emittance(self):
        emittance = EmittanceWindow()
        r = emittance.return_para()
        if r:
            pass

    def close_server(self):
        hidden = HiddenWindow()
        r = hidden.return_para()
        if r and hidden.password == self.__password:
            self.blackberry.send_command('quit')

    def resizeEvent(self, event):
        self.image_size = [self.wViewer.width(), self.wViewer.height()]
        self.profile_size = [self.wProfile.width(), self.wProfile.height()]
        self.beamx_size = [self.wBeamSizeX.width(), self.wBeamSizeX.height()]
        self.beamy_size = [self.wBeamSizeY.width(), self.wBeamSizeY.height()]

        if self.labelViewer is not None:
            self.labelViewer.resize(self.image_size[0], self.image_size[1])
        if self.profile is not None:
            self.profile.resize(self.profile_size[0], self.profile_size[1])
        if self.beamx is not None:
            self.beamx.resize(self.beamx_size[0], self.beamx_size[1])
        if self.beamy is not None:
            self.beamy.resize(self.beamy_size[0], self.beamy_size[1])

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.blueberry.working = False
            self.blueberry.stop()
            event.accept()
        else:
            event.ignore()

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

    @Slot(int, list, list)
    @Slot(int, QPixmap)
    def update_screen(self, target, graphics, additional_curves=None):
        gara_pen = pg.mkPen(color=(255,255,255), width=0)

        if target == PICTURE_SCREEN:
            graphics = graphics.scaled(self.image_size[0], self.image_size[1])
            self.labelViewer.resize(graphics.width(), graphics.height())
            self.labelViewer.setPixmap(graphics)
        elif target == PROFILE_SCREEN:
            # Example Image...
            
            from colour import Color
            blue, red = Color(hex="#dedeff"), Color('red')
            colors = blue.range_to(red, 255)
            colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
            look_up_table = colors_array.astype(np.uint8)
            
            image = pg.ImageItem()
            #image.setImage(graphics)
            image.setLookupTable(look_up_table)
            image.setImage(np.array(graphics))
            scale = self.blueberry.pixel_to_mm
            image.setTransform(QTransform().scale(scale, scale).translate(-400,-400))
            #image.setTransform(QTransform().translate(-40, -40))

            if self.profile is not None:
                self.gridProfile.removeWidget(self.profile)
            gview = pg.GraphicsView()
            glayout = pg.GraphicsLayout(border=(255,255,255))
            gview.setCentralItem(glayout)
            plot = glayout.addPlot(title="Beam Profile")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Vertical', 'mm')
            plot.setLabel('bottom', 'Horizontal', 'mm')
            plot.setXRange(-20, 20)
            plot.setYRange(-20, 20)
            plot.addItem(image)

            self.profile = gview
            self.profile.setBackground('w')
            self.profile.resize(self.profile_size[0], self.profile_size[1])
            self.gridProfile.addWidget(self.profile)
            self.wProfile.resize(self.profile_size[0], self.profile_size[1])

            #self.original_images.append(np.array(additional_curves))
            self.filtered_images.append(np.array(graphics))

        elif target == XSIZE_SCREEN:
            if self.beamx is not None:
                self.gridBeamSizeX.removeWidget(self.beamx)
            plot = pg.PlotWidget(title="Vertical axis intensity")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Intensity', '%')
            plot.setLabel('bottom', 'Vertical', 'mm')
            x1 = []
            y1 = []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            #plot.resize(self.blueberry.xsize_width, self.blueberry.xsize_height)
            #plot.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            plot.setXRange(min(x1),max(x1))
            plot.setYRange(min(y1), max(y1)+5)


            plot.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            if additional_curves is not None:
                if len(additional_curves) > 0:
                    x2, y2 = [], []
                    for value in additional_curves:
                        x2.append(value[0])
                        y2.append(value[1])
                    plot.plot(x2, y2, pen=pg.mkPen(color=(227, 28, 14), width=2))
            plot.setBackground('w')

            self.beamx = plot
            self.beamx.resize(self.beamx_size[0], self.beamx_size[1])
            self.gridBeamSizeX.addWidget(self.beamx)
            self.wBeamSizeX.resize(self.beamx_size[0], self.beamx_size[1])
        elif target == YSIZE_SCREEN:
            if self.beamy is not None:
                self.gridBeamSizeY.removeWidget(self.beamy)
            plot = pg.PlotWidget(title="Horizontal axis intensity")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Intensity', '%')
            plot.setLabel('bottom', 'Horizontal', 'mm')
            plot.setYRange(0, 100)
            x1, y1 = [], []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            plot.setXRange(min(x1),max(x1))
            plot.setYRange(min(y1), max(y1)+5)
            #plot.resize(self.blueberry.ysize_width, self.blueberry.ysize_height)
            #plot.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

            plot.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            if additional_curves is not None:
                if len(additional_curves) > 0:
                    x2, y2 = [], []
                    for value in additional_curves:
                        x2.append(value[0])
                        y2.append(value[1])
                    plot.plot(x2, y2, pen=pg.mkPen(color=(227, 28, 14), width=2))

            plot.setBackground('w')

            self.beamy = plot
            self.beamy.resize(self.beamy_size[0], self.beamy_size[1])
            self.gridBeamSizeY.addWidget(self.beamy)
            self.wBeamSizeY.resize(self.beamy_size[0], self.beamy_size[1])
        else:
            return
        
        self.wViewer.resize(self.image_size[0], self.image_size[1])

    def set_layout(self, widget, xrange=None, yrange=None, zrange=None):
        widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widget.showGrid(x=True, y=True)
        widget.setBackground('w')
        if xrange is not None:
            widget.setXRange(xrange[0],xrange[1])