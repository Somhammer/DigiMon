import os, sys
import logging
import numpy as np

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
    resize_signal = Signal(int, int, int)

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

        self.profile = None
        self.beamx = None
        self.beamy = None

        self.set_action()

        self.initialize()
        self.showMaximized()

    def set_action(self):
        # Signal connection
        self.parameter_signal.connect(self.blueberry.receive_signal)
        self.resize_signal.connect(self.blueberry.resize_image)
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

        self.resize_signal.emit(PICTURE_SCREEN, self.wViewer.width(), self.wViewer.height())
        self.resize_signal.emit(PROFILE_SCREEN, self.wProfile.width(), self.wProfile.height())
        self.resize_signal.emit(XSIZE_SCREEN, self.wBeamSizeX.width(), self.wBeamSizeX.height())
        self.resize_signal.emit(YSIZE_SCREEN, self.wBeamSizeY.width(), self.wBeamSizeY.height())

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
            pass

    def filter_image(self):
        filtering = FilterWindow(self, self.original_images[-1])
        r = filtering.return_para()
        if r:
            filter_code = filtering.code
            filter_para = filtering.parameters
            self.parameter_signal(filter_code, None)
    
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
        self.resize_signal.emit(PICTURE_SCREEN, self.wViewer.width(), self.wViewer.height())
        self.resize_signal.emit(PROFILE_SCREEN, self.wProfile.width(), self.wProfile.height())
        self.resize_signal.emit(XSIZE_SCREEN, self.wBeamSizeX.width(), self.wBeamSizeX.height())
        self.resize_signal.emit(YSIZE_SCREEN, self.wBeamSizeY.width(), self.wBeamSizeY.height())

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
            self.labelViewer.resize(graphics.width(), graphics.height())
            self.labelViewer.setPixmap(graphics)
        elif target == PROFILE_SCREEN:
            # Example Image...
            from colour import Color
            blue, red = Color('blue'), Color('red')
            colors = blue.range_to(red, 256)
            colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
            look_up_table = colors_array.astype(np.uint8)

            image = pg.ImageItem()
            image.setLookupTable(look_up_table)
            image.setImage(np.array(graphics))

            self.gridProfile.removeWidget(self.profile)
            gview = pg.GraphicsView()
            glayout = pg.GraphicsLayout(border=(255,255,255))
            gview.setCentralItem(glayout)
            plot = glayout.addPlot(title="Beam Profile")
            plot.setLabel('left', 'Vertical', 'mm')
            plot.setLabel('bottom', 'Horizontal', 'mm')
            plot.setXRange(0, 200)
            plot.setYRange(0, 200)
            plot.addItem(image)

            self.profile = gview
            self.profile.setBackground('w')
            self.gridProfile.addWidget(self.profile)

            self.original_images.append(np.array(additional_curves))
            self.filtered_images.append(np.array(graphics))

        elif target == XSIZE_SCREEN:
            self.gridBeamSizeX.removeWidget(self.beamx)
            plot = pg.PlotWidget(title="Vertical axis intensity")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Intensity', '%')
            plot.setLabel('bottom', 'Vertical', 'mm')
            plot.setXRange(0, len(graphics))
            plot.setYRange(0, 100)
            x1 = []
            y1 = []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            plot.resize(self.blueberry.xsize_width, self.blueberry.xsize_height)
            plot.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

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
            self.gridBeamSizeX.addWidget(self.beamx)
        elif target == YSIZE_SCREEN:
            self.gridBeamSizeY.removeWidget(self.beamy)
            plot = pg.PlotWidget(title="Horizontal axis intensity")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Intensity', '%')
            plot.setLabel('bottom', 'Horizontal', 'mm')
            plot.setXRange(0, len(graphics))
            plot.setYRange(0, 100)
            x1, y1 = [], []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            plot.resize(self.blueberry.ysize_width, self.blueberry.ysize_height)
            plot.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

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
            self.gridBeamSizeY.addWidget(self.beamy)
        else:
            return

    def set_layout(self, widget, xrange=None, yrange=None, zrange=None):
        widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widget.showGrid(x=True, y=True)
        widget.setBackground('w')
        if xrange is not None:
            widget.setXRange(xrange[0],xrange[1])