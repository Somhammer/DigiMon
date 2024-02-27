# -------------------------------------------------------
# MainWindow
# Author: Seohyeon An
# Date: 2022-04-21
#
# -------------------------------------------------------

import platform
import os
import logging
import datetime

import numpy as np
import cv2

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.gridspec import GridSpec

from qled import QLed
from variables import *
from blackberry import Blackberry
from blueberry import Blueberry
from strawberry import Strawberry
from ui_mainwindow import Ui_MainWindow
from connectionwindow import ConnectionWindow
from calibrationwindow import CalibrationWindow
from roiwindow import ROIWindow
from filterwindow import FilterWindow
from hiddenwindow import HiddenWindow
from logger import LogStringHandler
from digilabel import DigiLabel
from DigiMon import mutex

class MainWindow(QMainWindow, Ui_MainWindow):
    set_camera_parameter = Signal(int, int)
    control_signal = Signal(int)
    current_signal = Signal(str)
    def __init__(self, para, stream_input_queue, analysis_input_queue, stream_output_queue, analysis_output_queue):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.para = para
        self.stream_input_queue = stream_input_queue
        self.analysis_input_queue = analysis_input_queue
        self.stream_output_queue = stream_output_queue
        self.analysis_output_queue = analysis_output_queue

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textLog)
        self.logger.addHandler(handler)

        self.dialog = False

        self.layoutMargin = 3
        self.layoutSpacing = 3

        self.ledCameraStatus = QLed(self.labelCameraPixmap, onColour=QLed.Red, shape=QLed.Circle)
        self.ledCameraStatus.value = True
        self.labelCameraPixmap.setFixedSize(30,30)
        self.ledCameraStatus.setFixedSize(self.labelCameraPixmap.sizeHint())

        self.ledControllerStatus = QLed(self.labelControllerPixmap, onColour=QLed.Red, shape=QLed.Circle)
        self.ledControllerStatus.value = True
        self.labelControllerPixmap.setFixedSize(30,30)
        self.ledControllerStatus.setFixedSize(self.labelControllerPixmap.sizeHint())

        self.ledCalibrationStatus = QLed(self.labelCalibrationPixmap, onColour=QLed.Red, shape=QLed.Circle)
        self.ledCalibrationStatus.value = True
        self.labelCalibrationPixmap.setFixedSize(30,30)
        self.ledCalibrationStatus.setFixedSize(self.labelCalibrationPixmap.sizeHint())

        self.labelCamera = DigiLabel(self.labelCamera)
        self.gridLayout.addWidget(self.labelCamera, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.__password = "profile"
        self.blackberry = Blackberry(para, self)
        self.blueberry = Blueberry(para, self, stream_input_queue, analysis_input_queue)
        self.strawberry = Strawberry(para, self.image_stream, stream_output_queue)
        self.strawberry.working = True
        self.strawberry.start()
        self.strawberry2 = Strawberry(para, self.image_analysis, analysis_output_queue)
        self.strawberry2.working = True
        self.strawberry2.start()

        self.connection = ConnectionWindow(para = self.para, logger=self.logger, blueberry=self.blueberry, blackberry=self.blackberry)
        self.calibration = CalibrationWindow(para = self.para, blueberry=self.blueberry)
        self.roi = ROIWindow(para = self.para, blueberry=self.blueberry)
        self.filter = FilterWindow(para = self.para, blueberry=self.blueberry)

        self.image_paths = []
        self.image_names = []
        self.analyzed_images = []
        self.redraw = False

        self.livex = None
        self.livey = None

        self.last_picture = None
        self.profile = None
        self.beamx = None
        self.beamy = None

        self.beamx_size = []
        self.beamy_size = []

        self.outdir = None
        self.previous = self.main_size = []
        self.set_directories()
        self.set_action()

        self.showMaximized()
        self.initialize()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.sliderGain.setSingleStep(10)
            self.sliderExposureTime.setSingleStep(10)
        elif event.key() == Qt.Key_Shift:
            self.sliderGain.setSingleStep(100)
            self.sliderExposureTime.setSingleStep(100)

    def keyReleaseEvent(self, event):
        if any(event.key() == i for i in [Qt.Key_Control, Qt.Key_Shift]):
            self.sliderGain.setSingleStep(1)
            self.sliderExposureTime.setSingleStep(1)

    def set_directories(self):
        self.outdir = os.path.join(os.getcwd(), 'output', datetime.datetime.today().strftime('%y%m%d'))
        for subdir in ['raw', 'analyzed', 'plot']:
            os.makedirs(os.path.join(self.outdir, subdir), exist_ok=True)

    def set_action(self):
        # Signal connection
        self.set_camera_parameter.connect(self.blueberry.set_camera_parameter)
        self.control_signal.connect(self.blackberry.receive_request)
        self.current_signal.connect(self.blueberry.set_current)

        # Hidden window - Closing Controller
        self.keyHidden = QShortcut(QKeySequence('Ctrl+F10'), self)
        self.keyHidden.activated.connect(self.close_server)

        # Image Screen
        self.labelCamera.clicked.connect(self.set_focused_line)
        self.labelCamera.move.connect(self.set_focused_line)

        # Setup
        self.pushConnection.clicked.connect(self.setup_connection)
        self.pushCalibration.clicked.connect(self.setup_calibration)
        self.pushROI.clicked.connect(self.setup_ROI)
        self.pushFilter.clicked.connect(self.setup_filter)

        # Camera Setup
        #self.pushSetup.clicked.connect(self.setup_module)

        self.sliderFrameRate.valueChanged.connect(lambda: self.lineFrameRate.setText(str(self.sliderFrameRate.value())))
        self.sliderFrameRate.sliderReleased.connect(lambda: self.set_camera_parameter.emit(CAMERA_FPS, self.sliderFrameRate.value()))
        self.sliderRepeat.valueChanged.connect(lambda: self.lineRepeat.setText(str(self.sliderRepeat.value())))
        self.sliderRepeat.sliderReleased.connect(lambda: self.set_camera_parameter.emit(CAMERA_REPEAT, self.sliderRepeat.value()))

        self.lineGain.setValidator(QIntValidator(self))
        self.lineExposureTime.setValidator(QIntValidator(self))
        self.sliderGain.valueChanged.connect(lambda: self.lineGain.setText(str(self.sliderGain.value())))
        self.sliderGain.sliderReleased.connect(lambda: self.set_camera_parameter.emit(CAMERA_GAIN, self.sliderGain.value()))
        self.sliderExposureTime.valueChanged.connect(lambda: self.lineExposureTime.setText(str(self.sliderExposureTime.value())))
        self.sliderExposureTime.sliderReleased.connect(lambda: self.set_camera_parameter.emit(CAMERA_EXPOSURE_TIME, self.sliderExposureTime.value()))
        # Camera Capture
        def set_value(slider, line):
            if not line.text() == '':
                slider.setValue(int(line.text()))
        self.lineGain.textEdited.connect(lambda: set_value(self.sliderGain, self.lineGain))
        self.lineGain.returnPressed.connect(lambda: self.set_camera_parameter.emit(CAMERA_GAIN, int(self.lineGain.text())))
        self.lineExposureTime.textEdited.connect(lambda: set_value(self.sliderExposureTime, self.lineExposureTime))
        self.lineExposureTime.returnPressed.connect(lambda: self.set_camera_parameter.emit(CAMERA_EXPOSURE_TIME, int(self.lineExposureTime.text())))

        self.pushCapture.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_REQUEST_CAPTURE, self.sliderRepeat.value()))
        self.pushStop.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_REQUEST_STOP, -999))

        # Image rotation
        self.pushRotateLeft.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_ROTATION_LEFT, 1))
        self.pushRotateRight.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_ROTATION_RIGHT, 1))
        self.pushFlipUpDown.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_FLIP_UP_DOWN, 1))
        self.pushFilpRightLeft.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_FLIP_RIGHT_LEFT, 1))
        self.pushAngleUp.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_ROTATION_CUSTOM_RIGHT, float(self.lineRotationAngle.text())))
        self.pushAngleDown.clicked.connect(lambda: self.set_camera_parameter.emit(CAMERA_ROTATION_CUSTOM_LEFT, float(self.lineRotationAngle.text())))

        # Screen Zoom
        ### -> signal <-> slot 형식으로 바꿔야 함
        self.pushScreenDown.clicked.connect(lambda: self.control_signal.emit(ACTUATOR_REQUEST_GO_DOWN))
        self.pushScreenUp.clicked.connect(lambda: self.control_signal.emit(ACTUATOR_REQUEST_GO_UP))

        self.pushOpenImage.clicked.connect(self.open_image)

        #self.lineFieldGradient.textChanged.connect(lambda: self.current_signal.emit(self.lineFieldGradient.text()))
        self.tableProfiles.doubleClicked.connect(lambda: self.redraw_image(self.tableProfiles.currentIndex().row()))

    def set_checked(self, checkbox, checked):
        if checked:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def initialize(self):
        self.ledCameraStatus.m_onColour = QLed.Red
        self.ledControllerStatus.m_onColour = QLed.Red
        self.ledCalibrationStatus.m_onColour = QLed.Red

        bluePen = pg.mkPen(color=(0,0,255), width=1)

        self.plotLiveX = pg.PlotWidget()
        self.plotLiveX.setBackground('w')
        self.plotLiveX.showGrid(x=True, y=True)
        self.plotLiveX.hideAxis('left')
        self.plotLiveX.hideAxis('bottom')
        #self.plotLiveX.setLabel('bottom', 'Horizontal')
        self.plotLiveX.setLabel('top', 'Horizontal')
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
        self.plotLiveY.setLabel('right', 'Vertical')
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
    
        self.labelCamera.resize(self.frameCamera.width()-self.layoutMargin, self.frameCamera.height()-self.layoutMargin)
        self.para.intensity_line = [round(self.labelCamera.width()/2), round(self.labelCamera.height()/2)]

    def set_parameter(self, idx, value):
        mutex.acquire()
        while not self.stream_output_queue.empty():
            self.stream_output_queue.get()
        while not self.analysis_output_queue.empty():
            self.analysis_output_queue.get()
        self.para.set_parameter(idx, value)
        mutex.release()

    def setup_connection(self):
        if self.dialog: return

        self.dialog = True

        self.connection.show()
        r = self.connection.return_para()
        if r:
            if self.para.cam_conn:
                self.ledCameraStatus.m_onColour = QLed.Green
                self.set_camera_parameter.emit(CAMERA_REQUEST_STREAM, 1)
                self.lineGain.setText(str(self.para.gain))
                self.lineExposureTime.setText(str(self.para.exp_time))
                self.blueberry.working = True
                self.blueberry.start()
            else:
                self.ledCameraStatus.m_onColour = QLed.Red

            if self.para.ctl_conn:
                self.ledControllerStatus.m_onColour = QLed.Green
                self.blackberry.start()
                self.blackberry.setPriority(QThread.IdlePriority)
                self.control_signal.emit(ACTUATOR_REQUEST_STATUS)
            else:
                self.ledControllerStatus.m_onColour = QLed.Red
        
        self.dialog =  False
                
    def setup_calibration(self):
        if self.dialog: return

        self.dialog = True

        self.calibration.show()
        r = self.calibration.return_para()
        if r:
            if self.para.calibrated:
                self.ledCalibrationStatus.m_onColour = QLed.Green
            else:
                self.ledCalibrationStatus.m_onColour = QLed.Red
        
        self.dialog = False

    def setup_ROI(self):
        if self.dialog: return

        self.dialog = True

        self.roi.show()
        self.roi.take_a_picture()

        r = self.roi.return_para()
        if r:
            self.para.roi = self.roi.roi
        self.roi.apply_roi(reset=True)
        self.dialog = False

    def setup_filter(self):
        if self.dialog: return

        self.dialog = True

        self.filter.show()
        self.filter.take_a_picture()
        r = self.filter.return_para()
        if r:
            pass
        else:
            self.para.filter_code = NO_FILTER
            self.para.filter_para = {}
        
        self.dialog = False

    def update_table(self, beamx, beamy, fname):
        if self.redraw: return
        if any(fname == self.tableProfiles.item(i, 2).text() for i in range(self.tableProfiles.rowCount())): return
        
        count = self.tableProfiles.rowCount()
        self.tableProfiles.setRowCount(self.tableProfiles.rowCount() + 1)
        twidget = QTableWidgetItem(count)
        self.tableProfiles.setItem(self.tableProfiles.rowCount()-1, 0, twidget)

        for idx, value in enumerate([f'{beamx:.2f}', f'{beamy:.2f}', fname]):
            twidget = QTableWidgetItem(str(value))
            twidget.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableProfiles.setItem(self.tableProfiles.rowCount()-1, idx, twidget)

    def close_server(self):
        hidden = HiddenWindow()
        r = hidden.return_para()
        if r and hidden.password == self.__password:
            self.logger.info("Close Controller Server")
            self.blackberry.send_command('quit')

    def open_image(self):
        extension = ["Image file (*.bmp *.jpg *jpeg *png *tiff *tif)"]
        fname = QFileDialog.getOpenFileName(self, "Select Image", selectedFilter=extension[0], filter='\n'.join(i for i in extension))[0]
        if fname != '':
            if 'Window' in platform.system():
                fname = fname.replace("/", "\\")
            image = cv2.imread(fname)
            self.image_paths.append(fname)
            dirname, fname = os.path.split(fname)
            self.image_names.append(fname)
            self.analysis_input_queue.put([image, self.para])

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

        if len(self.previous) > 0:
            if self.previous != self.main_size and abs(self.previous[0] - self.main_size[0]) > 10:
                self.labelCamera.resize(self.para.stream_size[0], self.para.stream_size[1])
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.blueberry.stop()
            self.blackberry.stop()
            self.strawberry.stop()
            self.strawberry2.stop()
            event.accept()
            super().closeEvent(event)
        else:
            event.ignore()

    @Slot(str)
    def actuator_status(self, message):
        self.labelScreenStatus.setText(f"{message}")

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

    @Slot(list, int)
    def save_image(self, image, itype):
        try:
            outdir = ""
            fname = f"{datetime.datetime.today().strftime('%H-%M-%S-%f')[:-3]}_Exp{self.para.exp_time}_Gain{self.para.gain}.png"
            if itype == RAW_IMAGE:
                outdir = os.path.join(self.outdir, 'raw')
            elif itype == ANALYZED_IMAGE:
                outdir = os.path.join(self.outdir, 'analyzed')
            full_path = os.path.join(outdir, fname)
            cv2.imwrite(full_path, np.array(image))
            self.logger.info(f"Save Image: {full_path}")
            self.image_paths.append(full_path)
            self.image_names.append(fname)
        except:
            return

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
        pixmap = pixmap.scaled(self.labelCamera.width(), self.labelCamera.height())
            
        painter = QPainter(pixmap)
        painter.setPen(QPen(QColor(3, 252, 127), 1.5, Qt.DashLine))
        if self.para.intensity_line != [-1,-1]:
            x, y = self.para.intensity_line[0], self.para.intensity_line[1]
        else:
            x = round(self.labelCamera.width()/2) - 1
            y = round(self.labelCamera.height()/2) - 1
        painter.drawLine(0, y, self.labelCamera.width(), y)
        painter.drawLine(x, 0, x, self.labelCamera.height())
        painter.end()
        
        self.labelCamera.setPixmap(pixmap)

        self.liveXCurve.setData(xbin, xhist)
        ybin.reverse()
        self.liveYCurve.setData((np.array(yhist)).tolist(), ybin)

        self.plotLiveX.setLimits(xMin=min(xbin), xMax=max(xbin))
        self.plotLiveY.setLimits(yMin=min(ybin), yMax=max(ybin))

        arr = image.reshape(-1)
        hist, bin = np.histogram(arr, np.arange(0,257))
        histogram = pg.BarGraphItem(x=bin[:-1], height=hist, width = 1, brush=(107,200,224))
        self.plotPVHist.clear()
        self.plotPVHist.addItem(histogram)
        self.plotPVHist.setLogMode(False, True)
        self.plotPVHist.setXRange(-1,256)

    @Slot(list)
    def image_analysis(self, element):
        if element == False:
            self.logger.error(f"Image analysis is failed.")
            return
        para, image, xbin, ybin, xhist, yhist, xfitvalue, yfitvalue, center_pixel, center_real, xwidth, ywidth, rms_size = element
        gara_pen = pg.mkPen(color=(255,255,255), width=0)
        self.plotProfile.clear()

        from colour import Color
        blue, red = Color(hex="#dedeff"), Color('red')
        colors = blue.range_to(red, 255)
        colors_array = np.array([np.array(color.get_rgb()) * 255 for color in colors])
        look_up_table = colors_array.astype(np.uint8)

        # PyqtGraph에서 90도 돌아져서 그림이 그려져서 돌림...
        if not self.redraw:
            self.save_image(image, itype=ANALYZED_IMAGE)
            self.update_table(xwidth[0], ywidth[0], self.image_names[-1])
            self.analyzed_images.append(element)

        image = cv2.flip(image, 0)
        image = np.transpose(image)

        #graphics = np.array(graphics)
        #graphics = cv2.rotate(graphics, cv2.ROTATE_90_CLOCKWISE)
        #if not graphics.shape != 2:
        #    grayimage = cv2.cvtColor(graphics, cv2.COLOR_BGR2GRAY)
        if para.calibrated:
            self.plotProfile.setLabel('left', 'Vertical', 'mm')
            self.plotProfile.setLabel('bottom', 'Horizontal', 'mm')
        else:
            self.plotProfile.setLabel('left', 'Vertical', 'pixel')
            self.plotProfile.setLabel('bottom', 'Horizontal', 'pixel')

        image_item = pg.ImageItem()
        image_item.setLookupTable(look_up_table)
        image_item.setImage(image)

        if para.calibrated:
            image_item.setTransform(QTransform().scale(1.0/para.pixel_per_mm[0], 1.0/para.pixel_per_mm[1]).translate(
                    -para.coordinate_center[0]/para.pixel_per_mm[0], -para.coordinate_center[1]/para.pixel_per_mm[1]))
        else:
            image_item.setTransform(QTransform().translate(-round(image.shape[0]/2), -round(image.shape[1]/2)))

        self.plotProfile.addItem(image_item)
        self.plotProfile.setLimits(xMin=min(xbin), xMax=max(xbin), yMin=min(ybin), yMax=max(ybin))

        self.plotProfile.addLine(x=center_real[0], y=None, pen=pg.mkPen(color=(29, 36, 229), width=1))
        self.plotProfile.addLine(x=None, y=center_real[1], pen=pg.mkPen(color=(29, 36, 229), width=1))
        self.plotProfile.addLine(x=0, y=None, pen=pg.mkPen(color=(40, 246, 60), width=1))
        self.plotProfile.addLine(x=None, y=0, pen=pg.mkPen(color=(40, 246, 60), width=1))

        self.plotProfile.setXRange(min(xbin), max(xbin))
        self.plotProfile.setYRange(min(ybin), max(ybin))

        if para.calibrated: unit = "mm"
        else: unit = "pixel"
        txt_pos = f"Center: ({center_real[1]:.2f}, {center_real[0]:.2f}) {unit} RMS Size: ({rms_size[0]:.2f}, {rms_size[1]:.2f}) {unit} Gaussian Size: ({xwidth[0]:.2f} ± {xwidth[1]:.2f}, {ywidth[0]:.2f} ± {ywidth[1]:.2f}) {unit}"
        self.labelPosition.setText(txt_pos)

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

        if not self.redraw:
            self.logger.info("Anlaysis is done.")
            self.save_pretty_plot(element)
        else:
            self.redraw = False

    def redraw_image(self, idx):
        self.redraw = True
        self.analysis_output_queue.put(self.analyzed_images[idx])

    # UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
    def save_pretty_plot(self, element):
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 12
        plt.rcParams['mathtext.fontset'] = 'dejavuserif'
        plt.rcParams['legend.fontsize'] = 5
        plt.rcParams['axes.titlesize'] = 6
        #plt.rcParams['figure.dpi'] = 200
        #plt.rcParams['savefig.dpi'] = 300
        #plt.rcParams['patch.linewidth'] = 0.5
        plt.rcParams["legend.frameon"] = False
        plt.rcParams['figure.figsize'] = (6, 6)
        plt.tight_layout()

        cmap = plt.get_cmap("jet").copy()
        newcolors = cmap(np.linspace(0, 1, 128))
        newcolors[0, :] = np.array([1,1,1,1])
        newcmap = ListedColormap(newcolors)

        para, image, xbin, ybin, xhist, yhist, xfitvalue, yfitvalue, center_pixel, center_real, xwidth, ywidth, rms_beam_size = element
        gridspec = GridSpec(nrows=2, ncols=2, width_ratios=[4,1], height_ratios=[1,4], wspace=0.025, hspace=0.025)

        plt.subplot(gridspec[1,0])
        plt.tick_params(axis='both', direction='in')
        plt.xlabel(r"Horizontal Axis [mm]")
        plt.ylabel(r"Vertical Axis [mm]")
        
        plt.imshow(image, extent=(min(xbin), max(xbin), min(ybin), max(ybin)), interpolation='nearest', aspect='auto', cmap=newcmap)
        plt.axvline(x=0, color='#0ffc03', linestyle=(0, (3.5, 2.5)), linewidth=1, zorder=3)
        plt.axhline(y=0, color='#0ffc03', linestyle=(0, (3.5, 2.5)), linewidth=1, zorder=2)
        plt.axvline(x=center_real[0], color='#d703fc', linestyle='solid', linewidth=1, zorder=4)
        plt.axhline(y=center_real[1], color='#d703fc', linestyle='solid', linewidth=1, zorder=5)
        txt_pos = f"Center: {center_real[0]:.2f}, {center_real[1]:.2f} mm\n\RMS: {rms_beam_size[0]:.2f}, {rms_beam_size[1]:.2f} mm\n\Fit(1$\sigma$): {xwidth[0]:.2f} ± {xwidth[1]:.2f}, {ywidth[0]:.2f} ± {ywidth[1]:.2f} mm"
        plt.text(min(xbin)+abs(min(xbin))*0.10, max(ybin)-max(ybin)*1.95, txt_pos, color='black', fontsize=12)

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

        plt.savefig(os.path.join(self.outdir, 'plot', f"BeamProfile_{self.image_names[-1].split('.')[0]}.pdf"))
        plt.savefig(os.path.join(self.outdir, 'plot', f"BeamProfile_{self.image_names[-1].split('.')[0]}.png"), dpi=450)
        plt.close()