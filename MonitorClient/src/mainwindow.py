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
from src.setupwindow import SetupWindow
from src.hiddenwindow import HiddenWindow
from src.emittancewindow import EmittanceWindow
from src.logger import LogStringHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    parameter_signal = Signal(int, int)
    redraw_signal = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.dialog = False

        self.__password = "profile"
        self.blackberry = Blackberry()
        self.blueberry = Blueberry(parent=self)
        
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textLog)
        self.logger.addHandler(handler)

        self.images_names = []
        self.original_images = []
        self.filtered_images = []

        self.last_picture = None
        self.profile = None
        self.beamx = None
        self.beamy = None

        self.beamx_size = []
        self.beamy_size = []

        self.set_action()

        self.initialize()
        self.main_size = [self.width(), self.height()]
        self.show()
        #self.showMaximized()
        self.main_size = [self.width(), self.height()]
        self.image_size = [self.wViewer.width(), self.wViewer.height()]
        self.plot_profile_size = [self.wProfile.width(), self.wProfile.height()]
        self.plot_beamx_size = [self.wBeamSizeX.width(), self.wBeamSizeX.height()]
        self.plot_beamy_size = [self.wBeamSizeY.width(), self.wBeamSizeY.height()]

    def set_action(self):
        # Signal connection
        self.parameter_signal.connect(self.blueberry.receive_signal)
        self.redraw_signal.connect(self.blueberry.redraw_signal)

        # Hidden window - Closing Controller
        self.keyHidden = QShortcut(QKeySequence('Ctrl+F10'), self)
        self.keyHidden.activated.connect(self.close_server)
        # Network connection
        self.checkConnectController.clicked.connect(lambda: self.set_checked(self.checkConnectController, self.blackberry.connected))
        self.checkConnectCamera.clicked.connect(lambda: self.set_checked(self.checkConnectCamera, self.blueberry.connected))
        self.pushReconnect.clicked.connect(self.initialize)

        # Camera Setup
        self.pushSetup.clicked.connect(self.setup_camera)
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
        self.pushZoomIn.clicked.connect(lambda: self.blackberry.send_command('down'))
        self.pushZoomOut.clicked.connect(lambda: self.blackberry.send_command('up'))

        # Emittance Measurement
        self.pushEmittance.clicked.connect(self.measure_emittance)
        self.pushOpenImage.clicked.connect(self.open_image)
        self.tableProfiles.doubleClicked.connect(lambda: self.redraw_signal.emit(self.images_names[self.tableProfiles.currentIndex().row()]))

    def set_checked(self, checkbox, checked):
        if checked:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def initialize(self):
        self.connect_network(self.blackberry, self.checkConnectController)
        self.connect_network(self.blueberry, self.checkConnectCamera)

        self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value())
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

    def setup_camera(self):
        if self.dialog: return
        setup = SetupWindow(self, self.last_picture)
        r = setup.return_para()
        if r:
            self.blueberry.do_transformation = True
            self.blueberry.transform_points = setup.original_points
            self.blueberry.destination_points = setup.destination_points
            self.blueberry.mm_per_pixel = setup.mm_per_pixel
            self.blueberry.filter_code = setup.filter_code
            self.blueberry.filter_para = setup.filter_para
            self.blueberry.save_filtered_image = setup.checkSaveFilteredImage.isChecked()

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
            self.checkConnectController.setCheckable(False)
            self.blackberry.send_command('quit')

    def open_image(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        if fname != '':
            self.images_names.append(fname)
            self.redraw_signal.emit(fname)

    def resizeEvent(self, event):
        self.previous = self.main_size
        self.main_size = [self.width(), self.height()]
        self.image_size = [self.wViewer.width(), self.wViewer.height()]
        self.plot_profile_size = [self.wProfile.width(), self.wProfile.height()]
        self.plot_beamx_size = [self.wBeamSizeX.width(), self.wBeamSizeX.height()]
        self.plot_beamy_size = [self.wBeamSizeY.width(), self.wBeamSizeY.height()]

        if self.labelViewer is not None:
            self.labelViewer.resize(self.image_size[0], self.image_size[1])
        if self.profile is not None:
            self.profile.resize(self.plot_profile_size[0], self.plot_profile_size[1])
        if self.beamx is not None:
            self.beamx.resize(self.plot_beamx_size[0], self.plot_beamx_size[1])
        if self.beamy is not None:
            self.beamy.resize(self.plot_beamy_size[0], self.plot_beamy_size[1])

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

    @Slot(str)
    def save_image(self, image):
        self.images_names.append(str(image))

    @Slot(int, list, list)
    @Slot(int, np.ndarray)
    def update_screen(self, target, graphics, additional_curves=None):
        gara_pen = pg.mkPen(color=(255,255,255), width=0)

        if target == PICTURE_SCREEN:
            #graphics = graphics.scaled(self.image_size[0], self.image_size[1])
            #self.labelViewer.resize(graphics.width(), graphics.height())
            self.last_picture = graphics
            height, width, channel = graphics.shape
            qImg = QImage(graphics.data, width, height, width*channel, QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.labelViewer.width(), self.labelViewer.height())
            self.labelViewer.setPixmap(pixmap)
        elif target == PROFILE_SCREEN:
            from colour import Color
            blue, red = Color(hex="#dedeff"), Color('red')
            colors = blue.range_to(red, 255)
            colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
            look_up_table = colors_array.astype(np.uint8)
            
            image = pg.ImageItem()
            #image.setImage(graphics)
            image.setLookupTable(look_up_table)
            image.setImage(np.array(graphics))
            scale_x = self.blueberry.mm_per_pixel[0]
            scale_y = self.blueberry.mm_per_pixel[1]
            image.setTransform(QTransform().scale(scale_x, scale_y).translate(-400,-400))
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

            txt_pos = f"Center: ({additional_curves[0]:.2f}, {additional_curves[1]:.2f}) mm\nSize: ({additional_curves[2]:.2f}, {additional_curves[3]:.2f}) mm"
            text = pg.TextItem(text=txt_pos, color=(0,0,0))
            text.setPos(-15,15)
            plot.addItem(text)

            self.beamx_size.append(additional_curves[2])
            self.beamy_size.append(additional_curves[3])

            self.profile = gview
            self.profile.setBackground('w')
            self.profile.resize(self.plot_profile_size[0], self.plot_profile_size[1])
            self.gridProfile.addWidget(self.profile)
            #self.wProfile.resize(self.plot_profile_size[0], self.plot_profile_size[1])

            self.filtered_images.append(np.array(graphics))
            self.update_table(self.lineFieldGradient.text(), additional_curves[2], additional_curves[3], self.images_names[-1])

        elif target == XSIZE_SCREEN:
            if self.beamx is not None:
                self.gridBeamSizeX.removeWidget(self.beamx)
            plot = pg.PlotWidget(title="Horizontal axis intensity")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Intensity', '%')
            plot.setLabel('bottom', 'Horizontal', 'mm')
            x1 = []
            y1 = []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
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
            self.beamx.resize(self.plot_beamx_size[0], self.plot_beamx_size[1])
            self.gridBeamSizeX.addWidget(self.beamx)
            #self.wBeamSizeX.resize(self.plot_beamx_size[0], self.plot_beamx_size[1])
        
        elif target == YSIZE_SCREEN:
            if self.beamy is not None:
                self.gridBeamSizeY.removeWidget(self.beamy)
            plot = pg.PlotWidget(title="Vertical axis intensity")
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', 'Intensity', '%')
            plot.setLabel('bottom', 'Vertical', 'mm')
            plot.setYRange(0, 100)
            x1, y1 = [], []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
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

            self.beamy = plot
            #self.beamy.resize(self.plot_beamy_size[0], self.plot_beamy_size[1])
            self.beamy.resize(408, 126)
            self.gridBeamSizeY.addWidget(self.beamy)

            #self.wBeamSizeY.resize(self.plot_beamy_size[0], self.plot_beamy_size[1])
        else:
            return

        if any(target == i for i in [XSIZE_SCREEN, YSIZE_SCREEN, PROFILE_SCREEN]):
            self.image_size = [self.wViewer.width(), self.wViewer.height()]