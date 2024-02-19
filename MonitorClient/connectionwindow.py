import os, sys
import time
import datetime
import logging
import copy
import yaml
import math
import textwrap
import cv2
import numpy as np

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

from logger import LogStringHandler
from variables import *
import utilities as ut
from digilabel import DigiLabel
from ui_connectionwindow import Ui_ConnectionWindow

class ConnectionWindow(QDialog, Ui_ConnectionWindow):
    def __init__(self, logger, para, blueberry, blackberry):
        super(ConnectionWindow, self).__init__()

        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint)

        self.para = para
        self.blueberry = blueberry
        self.blackberry = blackberry
        self.logger = logger

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
        # Connection
        self.lineControllerIP1.setValidator(QIntValidator(self))
        self.lineControllerIP2.setValidator(QIntValidator(self))
        self.lineControllerIP3.setValidator(QIntValidator(self))
        self.lineControllerIP3.setValidator(QIntValidator(self))
        self.lineControllerIP5.setValidator(QIntValidator(self))

        self.checkCameraConnected.clicked.connect(lambda: self.set_checked(self.checkCameraConnected, self.para.cam_conn))
        self.checkControllerConnected.clicked.connect(lambda: self.set_checked(self.checkControllerConnected, self.para.ctl_conn))

        self.pushConnectCamera.clicked.connect(self.connect_camera)
        self.pushDisconnectCamera.clicked.connect(self.disconnect_camera)
        self.pushConnectController.clicked.connect(self.connect_controller)
        self.pushDisconnectController.clicked.connect(self.disconnect_controller)

        self.comboMonitor.addItem('')
        for i in range(NUMBER_OF_MONITORS):
            self.comboMonitor.addItem(f"{PV_NAME_RANK1}{i}")

    def set_checked(self, checkbox, state):
        if state:
            checkbox.setCheckable(True)
            checkbox.setChecked(True)
        else:
            checkbox.setCheckable(False)

    def connect_camera(self):
        self.para.sdk = self.comboSDKType.currentText()
        self.para.url = self.lineCameraAddr.text()

        if self.para.sdk == '' or self.para.url == '': return
        
        self.logger.info(f"Set SDK as {self.para.sdk}.")
        self.logger.info(f"Try to connect to {self.para.url}.")

        if self.para.cam_conn:
            self.logger.info(f"Network camera is already connected.")
        else:
            message = self.blueberry.connect_device()

            if 'ERROR ' in message:
                message = message.replace('ERROR ','')
                self.logger.error(message)
            elif 'INFO ' in message:
                message  = message.replace('INFO ','')
                self.logger.info(message)

        self.set_checked(self.checkCameraConnected, self.para.cam_conn)

    def disconnect_camera(self):
        if self.para.cam_conn:
            self.blueberry.stop()
            self.blueberry.disconnect_device()
        else: return
        
        if 'ERROR ' in message:
            message = message.replace('ERROR ','')
            self.logger.error(message)
        elif 'INFO ' in message:
            message  = message.replace('INFO ','')
            self.logger.info(message)

        self.set_checked(self.checkCameraConnected, self.para.cam_conn)

    def connect_controller(self):
        ip1, ip2, ip3, ip4, port = self.lineControllerIP1, self.lineControllerIP2, self.lineControllerIP3, self.lineControllerIP4, self.lineControllerIP5
        if any(i.text() == '' for i in [ip1, ip2, ip3, ip4]): return
        self.para.server_ip = '.'.join(i.text() for i in [ip1, ip2, ip3, ip4])+':'+port.text()
        if self.para.server_ip =='': return
        self.logger.info(f"Connect to controller server at {self.para.server_ip}.")
        self.para.monitor_id = self.comboMonitor.currentText()
        if self.para.monitor_id is None or self.para.monitor_id == '':
            self.logger.info(f'Select a profile monitor number.')
            self.para.server_ip = ''
            return

        if self.para.ctl_conn:
            self.logger.info(f"Network camera is already connected.")
            self.set_checked(self.checkControllerConnected, self.para.ctl_conn)
        else:
            message = self.blackberry.connect_device()

            if 'ERROR ' in message:
                message = message.replace('ERROR ','')
                self.logger.error(message)
            elif 'INFO ' in message:
                message  = message.replace('INFO ','')
                self.logger.info(message)
        
        self.set_checked(self.checkControllerConnected, self.para.ctl_conn)

    def disconnect_controller(self):
        if self.para.cam_conn:
            self.blackberry.stop()
            self.blackberry.disconnect_device()
        else: return
