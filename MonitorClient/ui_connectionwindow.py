# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import os
from variables import BASE_PATH

class Ui_ConnectionWindow(object):
    def setupUi(self, ConnectionWindow):
        if not ConnectionWindow.objectName():
            ConnectionWindow.setObjectName(u"ConnectionWindow")
        ConnectionWindow.resize(539, 333)
        icon = QIcon()
        icon.addFile(os.path.join(BASE_PATH, "icons/ncc.png"), QSize(), QIcon.Normal, QIcon.Off)
        ConnectionWindow.setWindowIcon(icon)

        self.gridLayout = QGridLayout(ConnectionWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupCameraConnection = QGroupBox(ConnectionWindow)
        self.groupCameraConnection.setObjectName(u"groupCameraConnection")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupCameraConnection.sizePolicy().hasHeightForWidth())
        self.groupCameraConnection.setSizePolicy(sizePolicy)
        self.groupCameraConnection.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.groupCameraConnection.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupCameraConnection)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelIP = QLabel(self.groupCameraConnection)
        self.labelIP.setObjectName(u"labelIP")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.labelIP.setFont(font1)

        self.gridLayout_3.addWidget(self.labelIP, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.pushConnectCamera = QPushButton(self.groupCameraConnection)
        self.pushConnectCamera.setObjectName(u"pushConnectCamera")
        self.pushConnectCamera.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushConnectCamera)

        self.pushDisconnectCamera = QPushButton(self.groupCameraConnection)
        self.pushDisconnectCamera.setObjectName(u"pushDisconnectCamera")
        self.pushDisconnectCamera.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushDisconnectCamera)

        self.checkCameraConnected = QCheckBox(self.groupCameraConnection)
        self.checkCameraConnected.setObjectName(u"checkCameraConnected")
        self.checkCameraConnected.setFont(font1)
        self.checkCameraConnected.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.checkCameraConnected)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.lineCameraAddr = QLineEdit(self.groupCameraConnection)
        self.lineCameraAddr.setObjectName(u"lineCameraAddr")
        self.lineCameraAddr.setFont(font1)

        self.gridLayout_3.addWidget(self.lineCameraAddr, 1, 1, 1, 1)

        self.labelSDKType = QLabel(self.groupCameraConnection)
        self.labelSDKType.setObjectName(u"labelSDKType")
        self.labelSDKType.setFont(font1)

        self.gridLayout_3.addWidget(self.labelSDKType, 0, 0, 1, 1)

        self.comboSDKType = QComboBox(self.groupCameraConnection)
        self.comboSDKType.addItem("")
        self.comboSDKType.addItem("")
        self.comboSDKType.setObjectName(u"comboSDKType")
        self.comboSDKType.setFont(font1)

        self.gridLayout_3.addWidget(self.comboSDKType, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupCameraConnection, 0, 0, 1, 2)

        self.groupControllerConnection = QGroupBox(ConnectionWindow)
        self.groupControllerConnection.setObjectName(u"groupControllerConnection")
        sizePolicy.setHeightForWidth(self.groupControllerConnection.sizePolicy().hasHeightForWidth())
        self.groupControllerConnection.setSizePolicy(sizePolicy)
        self.groupControllerConnection.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupControllerConnection)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comboMonitor = QComboBox(self.groupControllerConnection)
        self.comboMonitor.setObjectName(u"comboMonitor")
        self.comboMonitor.setFont(font1)

        self.gridLayout_5.addWidget(self.comboMonitor, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineControllerIP1 = QLineEdit(self.groupControllerConnection)
        self.lineControllerIP1.setObjectName(u"lineControllerIP1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineControllerIP1.sizePolicy().hasHeightForWidth())
        self.lineControllerIP1.setSizePolicy(sizePolicy1)
        self.lineControllerIP1.setFont(font1)
        self.lineControllerIP1.setMaxLength(3)

        self.horizontalLayout.addWidget(self.lineControllerIP1)

        self.labelControllerIP2 = QLabel(self.groupControllerConnection)
        self.labelControllerIP2.setObjectName(u"labelControllerIP2")
        self.labelControllerIP2.setFont(font1)

        self.horizontalLayout.addWidget(self.labelControllerIP2)

        self.lineControllerIP2 = QLineEdit(self.groupControllerConnection)
        self.lineControllerIP2.setObjectName(u"lineControllerIP2")
        sizePolicy1.setHeightForWidth(self.lineControllerIP2.sizePolicy().hasHeightForWidth())
        self.lineControllerIP2.setSizePolicy(sizePolicy1)
        self.lineControllerIP2.setFont(font1)
        self.lineControllerIP2.setMaxLength(3)

        self.horizontalLayout.addWidget(self.lineControllerIP2)

        self.labelControllerIP3 = QLabel(self.groupControllerConnection)
        self.labelControllerIP3.setObjectName(u"labelControllerIP3")
        self.labelControllerIP3.setFont(font1)

        self.horizontalLayout.addWidget(self.labelControllerIP3)

        self.lineControllerIP3 = QLineEdit(self.groupControllerConnection)
        self.lineControllerIP3.setObjectName(u"lineControllerIP3")
        sizePolicy1.setHeightForWidth(self.lineControllerIP3.sizePolicy().hasHeightForWidth())
        self.lineControllerIP3.setSizePolicy(sizePolicy1)
        self.lineControllerIP3.setFont(font1)
        self.lineControllerIP3.setMaxLength(3)

        self.horizontalLayout.addWidget(self.lineControllerIP3)

        self.labelControllerIP4 = QLabel(self.groupControllerConnection)
        self.labelControllerIP4.setObjectName(u"labelControllerIP4")
        self.labelControllerIP4.setFont(font1)

        self.horizontalLayout.addWidget(self.labelControllerIP4)

        self.lineControllerIP4 = QLineEdit(self.groupControllerConnection)
        self.lineControllerIP4.setObjectName(u"lineControllerIP4")
        sizePolicy1.setHeightForWidth(self.lineControllerIP4.sizePolicy().hasHeightForWidth())
        self.lineControllerIP4.setSizePolicy(sizePolicy1)
        self.lineControllerIP4.setFont(font1)
        self.lineControllerIP4.setMaxLength(3)

        self.horizontalLayout.addWidget(self.lineControllerIP4)

        self.labelControllerIP5 = QLabel(self.groupControllerConnection)
        self.labelControllerIP5.setObjectName(u"labelControllerIP5")
        self.labelControllerIP5.setFont(font1)

        self.horizontalLayout.addWidget(self.labelControllerIP5)

        self.lineControllerIP5 = QLineEdit(self.groupControllerConnection)
        self.lineControllerIP5.setObjectName(u"lineControllerIP5")
        sizePolicy1.setHeightForWidth(self.lineControllerIP5.sizePolicy().hasHeightForWidth())
        self.lineControllerIP5.setSizePolicy(sizePolicy1)
        self.lineControllerIP5.setFont(font1)
        self.lineControllerIP5.setMaxLength(10)

        self.horizontalLayout.addWidget(self.lineControllerIP5)


        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.pushConnectController = QPushButton(self.groupControllerConnection)
        self.pushConnectController.setObjectName(u"pushConnectController")
        self.pushConnectController.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushConnectController)

        self.pushDisconnectController = QPushButton(self.groupControllerConnection)
        self.pushDisconnectController.setObjectName(u"pushDisconnectController")
        self.pushDisconnectController.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushDisconnectController)

        self.checkControllerConnected = QCheckBox(self.groupControllerConnection)
        self.checkControllerConnected.setObjectName(u"checkControllerConnected")
        self.checkControllerConnected.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkControllerConnected)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)

        self.labelMonitorNumber = QLabel(self.groupControllerConnection)
        self.labelMonitorNumber.setObjectName(u"labelMonitorNumber")
        self.labelMonitorNumber.setFont(font1)

        self.gridLayout_5.addWidget(self.labelMonitorNumber, 2, 0, 1, 1)

        self.checkUseControlServer = QCheckBox(self.groupControllerConnection)
        self.checkUseControlServer.setObjectName(u"checkUseControlServer")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.checkUseControlServer.setFont(font2)
        self.checkUseControlServer.setChecked(False)

        self.gridLayout_5.addWidget(self.checkUseControlServer, 0, 0, 1, 2)

        self.labelControllerIP1 = QLabel(self.groupControllerConnection)
        self.labelControllerIP1.setObjectName(u"labelControllerIP1")
        self.labelControllerIP1.setFont(font1)

        self.gridLayout_5.addWidget(self.labelControllerIP1, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupControllerConnection, 1, 0, 2, 2)

        self.buttonBox = QDialogButtonBox(ConnectionWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.buttonBox.setFont(font3)
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)


        self.retranslateUi(ConnectionWindow)
        self.buttonBox.accepted.connect(ConnectionWindow.accept)
        self.buttonBox.rejected.connect(ConnectionWindow.reject)

        QMetaObject.connectSlotsByName(ConnectionWindow)
    # setupUi

    def retranslateUi(self, ConnectionWindow):
        ConnectionWindow.setWindowTitle(QCoreApplication.translate("ConnectionWindow", u"Dialog", None))
        self.groupCameraConnection.setTitle(QCoreApplication.translate("ConnectionWindow", u"Camera", None))
        self.labelIP.setText(QCoreApplication.translate("ConnectionWindow", u"URL or IP", None))
        self.pushConnectCamera.setText(QCoreApplication.translate("ConnectionWindow", u"Connect", None))
        self.pushDisconnectCamera.setText(QCoreApplication.translate("ConnectionWindow", u"Disconnect", None))
        self.checkCameraConnected.setText(QCoreApplication.translate("ConnectionWindow", u"Connected", None))
        self.labelSDKType.setText(QCoreApplication.translate("ConnectionWindow", u"SDK Type", None))
        self.comboSDKType.setItemText(0, QCoreApplication.translate("ConnectionWindow", u"OpenCV", None))
        self.comboSDKType.setItemText(1, QCoreApplication.translate("ConnectionWindow", u"Pylon (Basler)", None))

        self.groupControllerConnection.setTitle(QCoreApplication.translate("ConnectionWindow", u"Controller", None))
        self.labelControllerIP2.setText(QCoreApplication.translate("ConnectionWindow", u".", None))
        self.labelControllerIP3.setText(QCoreApplication.translate("ConnectionWindow", u".", None))
        self.labelControllerIP4.setText(QCoreApplication.translate("ConnectionWindow", u".", None))
        self.labelControllerIP5.setText(QCoreApplication.translate("ConnectionWindow", u":", None))
        self.pushConnectController.setText(QCoreApplication.translate("ConnectionWindow", u"Connect", None))
        self.pushDisconnectController.setText(QCoreApplication.translate("ConnectionWindow", u"Disconnect", None))
        self.checkControllerConnected.setText(QCoreApplication.translate("ConnectionWindow", u"Connected", None))
        self.labelMonitorNumber.setText(QCoreApplication.translate("ConnectionWindow", u"Monitor Number", None))
        self.checkUseControlServer.setText(QCoreApplication.translate("ConnectionWindow", u"Use Screen Controller", None))
        self.labelControllerIP1.setText(QCoreApplication.translate("ConnectionWindow", u"IP Address", None))
    # retranslateUi

