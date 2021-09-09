import os, sys
import logging
import datetime
import yaml

import numpy as np
import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

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

        base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        self.iconRedLight = QIcon(os.path.join(base_path, 'icons', 'redlight.png'))
        self.iconGreenLight = QIcon(os.path.join(base_path, 'icons', 'greenlight.png'))
        self.iconSize = QSize(20,20)

        self.camera_connected = False
        self.controller_connected = False
        self.calibrated = False

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

        self.livex = None
        self.livey = None

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
        self.plot_livex_size = [self.frameLiveXProfile.width(), self.frameLiveXProfile.height()]
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
        #elf.checkConnectController.clicked.connect(lambda: self.set_checked(self.checkConnectController, self.blackberry.connected))
        #self.checkConnectCamera.clicked.connect(lambda: self.set_checked(self.checkConnectCamera, self.blueberry.connected))

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
        self.parameter_signal.emit(CAMERA_FPS, self.sliderFrameRate.value())
        self.parameter_signal.emit(CAMERA_REPEAT, self.sliderRepeat.value())
        self.parameter_signal.emit(CAMERA_GAIN, 100)
        self.parameter_signal.emit(CAMERA_EXPOSURE_TIME, 500)
        
        self.labelCameraPixmap.setPixmap(self.iconRedLight.pixmap(self.iconSize))
        self.labelControllerPixmap.setPixmap(self.iconRedLight.pixmap(self.iconSize))
        self.labelCalibrationPixmap.setPixmap(self.iconRedLight.pixmap(self.iconSize))

        bluePen = pg.mkPen(color=(0,0,255), width=1)

        self.plotLiveX = pg.PlotWidget()
        self.plotLiveX.showGrid(x=True, y=True)
        self.plotLiveX.setLabel('bottom', 'Horizontal')
        self.liveXCurve = self.plotLiveX.plot(pen=bluePen)
        self.gridLiveXProfile.addWidget(self.plotLiveX)

        self.plotLiveY = pg.PlotWidget()
        self.plotLiveY.showGrid(x=True, y=True)
        self.plotLiveY.setLabel('bottom', 'Vertical')
        self.liveYCurve = self.plotLiveY.plot(pen=bluePen)
        self.gridLiveYProfile.addWidget(self.plotLiveY)

        self.plotProfile = pg.PlotWidget(title="Beam Profile")
        self.plotProfile.setBackground('w')
        self.plotProfile.showGrid(x=True, y=True)
        self.plotProfile.setLabel('left', 'Vertical', 'mm')
        self.plotProfile.setLabel('bottom', 'Horizontal', 'mm')
        self.gridProfile.addWidget(self.plotProfile)

        self.plotProfileX = pg.PlotWidget(title="Horizontal axis intensity")
        self.plotProfileX.setBackground('w')
        self.plotProfileX.showGrid(x=True, y=True)
        self.plotProfileX.setLabel('left', 'Intensity', '%')
        self.plotProfileX.setLabel('bottom', 'Horizontal', 'mm')
        self.gridBeamSizeX.addWidget(self.plotProfileX)

        self.plotProfileY = pg.PlotWidget(title="Vertical axis intensity")
        self.plotProfileY.setBackground('w')
        self.plotProfileY.showGrid(x=True, y=True)
        self.plotProfileY.setLabel('left', 'Intensity', '%')
        self.plotProfileY.setLabel('bottom', 'Vertical', 'mm')
        self.gridBeamSizeY.addWidget(self.plotProfileY)

    def setup_camera(self):
        if self.dialog: return
        setup = SetupWindow(self)
        r = setup.return_para()
        if r:
            if setup.camera_connected:
                self.camera_connected = True
                self.labelCameraPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
            if setup.controller_connected:
                self.controller_connected = True
                self.labelControllerPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
            if setup.calibrated:
                self.calibrated = True
                self.labelCalibrationPixmap.setPixmap(self.iconGreenLight.pixmap(self.iconSize))
                self.blueberry.do_transformation = True
                self.blueberry.transform_points = setup.original_points
                self.blueberry.destination_points = setup.destination_points
                self.blueberry.mm_per_pixel = setup.mm_per_pixel

            self.blueberry.gain = setup.gain
            self.blueberry.exposure_time = setup.exposure_time
            self.blueberry.ROI = setup.ROI
            self.blueberry.filter_code = setup.filter_code
            self.blueberry.filter_para = setup.filter_para

            if self.blueberry.connected:
                self.blueberry.start()

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
            if len(graphics.shape) == 3:
                height, width, channel = graphics.shape
                qImg = QImage(graphics.data, width, height, width*channel, QImage.Format_BGR888)
            else:
                height, width = graphics.shape
                qImg = QImage(graphics.data, width, height, width, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.labelViewer.width(), self.labelViewer.height())
            self.labelViewer.setPixmap(pixmap)
        elif any(target == i for i in [LIVE_XPROFILE_SCREEN, LIVE_YPROFILE_SCREEN]):
            if target == LIVE_XPROFILE_SCREEN:
                curve = self.liveXCurve
            else:
                curve = self.liveYCurve
            x1 = []
            y1 = []
            for value in graphics:
                x1.append(value[0])
                y1.append(value[1])
            curve.setData(x1, y1)
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

            graphics = np.array(graphics)
            graphics = cv2.rotate(graphics, cv2.ROTATE_90_CLOCKWISE)
            
            image = pg.ImageItem()
            image.setLookupTable(look_up_table)
            image.setImage(np.array(graphics))
            scale_x = self.blueberry.mm_per_pixel[0]
            scale_y = self.blueberry.mm_per_pixel[1]
            image.setTransform(QTransform().scale(scale_x, scale_y).translate(-400,-400))

            self.plotProfile.addItem(image)
            txt_pos = f"Center: ({additional_curves[0]:.2f}, {additional_curves[1]:.2f}) mm  Size: ({additional_curves[2]:.2f}, {additional_curves[3]:.2f}) mm"
            self.labelPosition.setText(txt_pos)

            self.filtered_images.append(np.array(graphics))
            self.update_table(self.lineFieldGradient.text(), additional_curves[2], additional_curves[3], self.images_names[-1])
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
            self.plotProfileY.setXRange(min(x1),max(x1))
            self.plotProfileY.setYRange(min(y1), max(y1)+5)

            self.plotProfileY.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            if additional_curves is not None:
                if len(additional_curves) > 0:
                    x2, y2 = [], []
                    for value in additional_curves:
                        x2.append(value[0])
                        y2.append(value[1])
                    self.plotProfileY.plot(x2, y2, pen=pg.mkPen(color=(227, 28, 14), width=2))
        else:
            return

        if any(target == i for i in [XSIZE_SCREEN, YSIZE_SCREEN, PROFILE_SCREEN]):
            self.image_size = [self.wViewer.width(), self.wViewer.height()]

    @Slot(np.ndarray, list, list, np.ndarray, np.ndarray, list, list)
    def save_pretty_plot(self, transformed_image, xbin, ybin, xhist_percent, yhist_percent, xfitline, yfitline):
        transformed_image = cv2.rotate(transformed_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        mm_per_pixel = self.blueberry.mm_per_pixel
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
        
        outdir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'output', datetime.datetime.today().strftime('%y%m%d'))
        plt.savefig(os.path.join(outdir, 'profile', f'BeamProfile_{self.images_names[-1].split("/")[-1]}.pdf'))
        plt.close()