import os, sys
import logging
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.variables import *
from src.blackberry import Blackberry
from src.blueberry import Blueberry
from src.ui_mainwindow import Ui_MainWindow
from src.hiddenwindow import HiddenWindow
from src.logger import LogStringHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    main_signal = Signal(int, int)
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

        self.initialize()
        self.set_action()
        self.show()

    def set_action(self):
        # Hidden window - Closing Controller
        self.keyHidden = QShortcut(QKeySequence('Ctrl+F10'), self)
        self.keyHidden.activated.connect(self.close_server)
        # Network connection
        self.checkConnectController.clicked.connect(lambda: self.set_checked(self.checkConnectController, self.blackberry.connected))
        self.checkConnectCamera.clicked.connect(lambda: self.set_checked(self.checkConnectCamera, self.blueberry.connected))
        self.pushReconnect.clicked.connect(self.initialize)


        self.main_signal.connect(self.blueberry.receive_signal)
        #self.blueberry.thread_signal.connect(self.receive_signal)
        self.blueberry.thread_logger_signal.connect(self.receive_log)
        # Camera Capture
        self.pushCapture.clicked.connect(lambda: self.main_signal.emit(CAMERA_CAPTURE, self.sliderRepeat.value()))
        self.pushStop.clicked.connect(lambda: self.main_signal.emit(CAMERA_STOP, -999))
        # Camera Controll
        self.sliderGain.valueChanged.connect(lambda: self.lineGain.setText(str(self.sliderGain.value())))
        self.sliderGain.sliderReleased.connect(lambda: self.control_camera())
        self.sliderFrameRate.valueChanged.connect(lambda: self.lineFrameRate.setText(str(self.sliderFrameRate.value())))
        self.sliderExposureTime.valueChanged.connect(lambda: self.lineExposureTime.setText(str(self.sliderExposureTime.value())))
        self.sliderRepeat.valueChanged.connect(lambda: self.lineRepeat.setText(str(self.sliderRepeat.value())))
        self.sliderX0.valueChanged.connect(lambda: self.lineX0.setText(str(self.sliderX0.value())))
        self.sliderY0.valueChanged.connect(lambda: self.lineY0.setText(str(self.sliderY0.value())))
        self.sliderDX.valueChanged.connect(lambda: self.lineDX.setText(str(self.sliderDX.value())))
        self.sliderDY.valueChanged.connect(lambda: self.lineDY.setText(str(self.sliderDY.value())))
        # Screen Control
        self.sliderScreenSpace.valueChanged.connect(lambda: self.lineScreenSpace.setText(str(self.sliderScreenSpace.value())))
        # Emittance Measurement

    def set_checked(self, checkbox, checked):
        if checked:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def initialize(self):
        self.connect_network(self.blackberry, self.checkConnectController)
        self.connect_network(self.blueberry, self.checkConnectCamera)
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

    def close_server(self):
        hidden = HiddenWindow()
        r = hidden.return_para()
        if r and hidden.password == self.__password:
            self.blackberry.send_command('quit')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply:
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
