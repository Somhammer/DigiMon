# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        if not SetupWindow.objectName():
            SetupWindow.setObjectName(u"SetupWindow")
        SetupWindow.resize(870, 778)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetupWindow.sizePolicy().hasHeightForWidth())
        SetupWindow.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(SetupWindow)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pushOk = QPushButton(SetupWindow)
        self.pushOk.setObjectName(u"pushOk")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushOk.sizePolicy().hasHeightForWidth())
        self.pushOk.setSizePolicy(sizePolicy1)
        self.pushOk.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushOk, 2, 5, 1, 1)

        self.pushLoad = QPushButton(SetupWindow)
        self.pushLoad.setObjectName(u"pushLoad")
        self.pushLoad.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushLoad, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_4, 2, 3, 1, 1)

        self.tabWidget = QTabWidget(SetupWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabConnection = QWidget()
        self.tabConnection.setObjectName(u"tabConnection")
        self.groupCameraConnection = QGroupBox(self.tabConnection)
        self.groupCameraConnection.setObjectName(u"groupCameraConnection")
        self.groupCameraConnection.setGeometry(QRect(9, 9, 521, 177))
        sizePolicy2.setHeightForWidth(self.groupCameraConnection.sizePolicy().hasHeightForWidth())
        self.groupCameraConnection.setSizePolicy(sizePolicy2)
        self.groupCameraConnection.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupCameraConnection.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupCameraConnection)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelSDKType = QLabel(self.groupCameraConnection)
        self.labelSDKType.setObjectName(u"labelSDKType")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.labelSDKType.setFont(font1)

        self.gridLayout_3.addWidget(self.labelSDKType, 0, 0, 1, 1)

        self.labelIP = QLabel(self.groupCameraConnection)
        self.labelIP.setObjectName(u"labelIP")
        self.labelIP.setFont(font1)

        self.gridLayout_3.addWidget(self.labelIP, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.lineCameraAddr = QLineEdit(self.groupCameraConnection)
        self.lineCameraAddr.setObjectName(u"lineCameraAddr")
        self.lineCameraAddr.setFont(font1)

        self.gridLayout_3.addWidget(self.lineCameraAddr, 1, 1, 1, 1)

        self.comboSDKType = QComboBox(self.groupCameraConnection)
        self.comboSDKType.addItem("")
        self.comboSDKType.addItem("")
        self.comboSDKType.setObjectName(u"comboSDKType")
        self.comboSDKType.setFont(font1)

        self.gridLayout_3.addWidget(self.comboSDKType, 0, 1, 1, 1)

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


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.groupControllerConnection = QGroupBox(self.tabConnection)
        self.groupControllerConnection.setObjectName(u"groupControllerConnection")
        self.groupControllerConnection.setGeometry(QRect(10, 190, 521, 178))
        sizePolicy2.setHeightForWidth(self.groupControllerConnection.sizePolicy().hasHeightForWidth())
        self.groupControllerConnection.setSizePolicy(sizePolicy2)
        self.groupControllerConnection.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupControllerConnection)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkUseControlServer = QCheckBox(self.groupControllerConnection)
        self.checkUseControlServer.setObjectName(u"checkUseControlServer")
        self.checkUseControlServer.setFont(font1)
        self.checkUseControlServer.setChecked(False)

        self.gridLayout_5.addWidget(self.checkUseControlServer, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineControllerIP1 = QLineEdit(self.groupControllerConnection)
        self.lineControllerIP1.setObjectName(u"lineControllerIP1")
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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.labelControllerIP1 = QLabel(self.groupControllerConnection)
        self.labelControllerIP1.setObjectName(u"labelControllerIP1")
        self.labelControllerIP1.setFont(font1)

        self.gridLayout_5.addWidget(self.labelControllerIP1, 1, 0, 1, 1)

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


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)

        self.comboMonitor = QComboBox(self.groupControllerConnection)
        self.comboMonitor.setObjectName(u"comboMonitor")
        self.comboMonitor.setFont(font1)

        self.gridLayout_5.addWidget(self.comboMonitor, 2, 1, 1, 1)

        self.labelMonitorNumber = QLabel(self.groupControllerConnection)
        self.labelMonitorNumber.setObjectName(u"labelMonitorNumber")
        self.labelMonitorNumber.setFont(font1)

        self.gridLayout_5.addWidget(self.labelMonitorNumber, 2, 0, 1, 1)

        self.textConnectionLog = QTextBrowser(self.tabConnection)
        self.textConnectionLog.setObjectName(u"textConnectionLog")
        self.textConnectionLog.setGeometry(QRect(10, 380, 521, 281))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textConnectionLog.sizePolicy().hasHeightForWidth())
        self.textConnectionLog.setSizePolicy(sizePolicy3)
        self.tabWidget.addTab(self.tabConnection, "")
        self.tabCalibration = QWidget()
        self.tabCalibration.setObjectName(u"tabCalibration")
        self.gridLayout_6 = QGridLayout(self.tabCalibration)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelPerspective = QLabel(self.tabCalibration)
        self.labelPerspective.setObjectName(u"labelPerspective")

        self.gridLayout_6.addWidget(self.labelPerspective, 2, 4, 1, 2)

        self.tabWidget_2 = QTabWidget(self.tabCalibration)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabRectangle = QWidget()
        self.tabRectangle.setObjectName(u"tabRectangle")
        self.gridLayout_14 = QGridLayout(self.tabRectangle)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_16 = QLabel(self.tabRectangle)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_14.addWidget(self.label_16, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_3, 1, 0, 1, 4)

        self.linePixelPerMM_y = QLineEdit(self.tabRectangle)
        self.linePixelPerMM_y.setObjectName(u"linePixelPerMM_y")
        self.linePixelPerMM_y.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_14.addWidget(self.linePixelPerMM_y, 0, 3, 1, 1)

        self.label_17 = QLabel(self.tabRectangle)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(20, 16777215))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_17, 0, 2, 1, 1)

        self.linePixelPerMM_x = QLineEdit(self.tabRectangle)
        self.linePixelPerMM_x.setObjectName(u"linePixelPerMM_x")
        self.linePixelPerMM_x.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_14.addWidget(self.linePixelPerMM_x, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tabRectangle, "")
        self.tabPoint = QWidget()
        self.tabPoint.setObjectName(u"tabPoint")
        self.gridLayout_8 = QGridLayout(self.tabPoint)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_14 = QLabel(self.tabPoint)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_14, 5, 0, 1, 1)

        self.lineQuad4y = QLineEdit(self.tabPoint)
        self.lineQuad4y.setObjectName(u"lineQuad4y")
        self.lineQuad4y.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad4y, 5, 2, 1, 1)

        self.lineQuad3y = QLineEdit(self.tabPoint)
        self.lineQuad3y.setObjectName(u"lineQuad3y")
        self.lineQuad3y.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad3y, 4, 2, 1, 1)

        self.lineQuad2y = QLineEdit(self.tabPoint)
        self.lineQuad2y.setObjectName(u"lineQuad2y")
        self.lineQuad2y.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad2y, 3, 2, 1, 1)

        self.label_9 = QLabel(self.tabPoint)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_9, 1, 1, 1, 1)

        self.label_10 = QLabel(self.tabPoint)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_10, 1, 2, 1, 1)

        self.lineQuad2x = QLineEdit(self.tabPoint)
        self.lineQuad2x.setObjectName(u"lineQuad2x")
        self.lineQuad2x.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad2x, 3, 1, 1, 1)

        self.lineQuad4x = QLineEdit(self.tabPoint)
        self.lineQuad4x.setObjectName(u"lineQuad4x")
        self.lineQuad4x.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad4x, 5, 1, 1, 1)

        self.label_7 = QLabel(self.tabPoint)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 4)

        self.label_11 = QLabel(self.tabPoint)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_13 = QLabel(self.tabPoint)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_13, 4, 0, 1, 1)

        self.lineQuad1y = QLineEdit(self.tabPoint)
        self.lineQuad1y.setObjectName(u"lineQuad1y")
        self.lineQuad1y.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad1y, 2, 2, 1, 1)

        self.lineQuad1x = QLineEdit(self.tabPoint)
        self.lineQuad1x.setObjectName(u"lineQuad1x")
        self.lineQuad1x.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad1x, 2, 1, 1, 1)

        self.label_8 = QLabel(self.tabPoint)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_12 = QLabel(self.tabPoint)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_12, 3, 0, 1, 1)

        self.lineQuad3x = QLineEdit(self.tabPoint)
        self.lineQuad3x.setObjectName(u"lineQuad3x")
        self.lineQuad3x.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_8.addWidget(self.lineQuad3x, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.tabWidget_2.addTab(self.tabPoint, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 3, 4, 1, 2)

        self.pushCalCapture = QPushButton(self.tabCalibration)
        self.pushCalCapture.setObjectName(u"pushCalCapture")

        self.gridLayout_6.addWidget(self.pushCalCapture, 0, 1, 1, 1)

        self.frameOrigin = QFrame(self.tabCalibration)
        self.frameOrigin.setObjectName(u"frameOrigin")
        self.frameOrigin.setMinimumSize(QSize(400, 400))
        self.frameOrigin.setMaximumSize(QSize(400, 400))
        self.frameOrigin.setBaseSize(QSize(0, 0))
        self.frameOrigin.setFrameShape(QFrame.StyledPanel)
        self.frameOrigin.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frameOrigin)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.labelOrigin = QLabel(self.frameOrigin)
        self.labelOrigin.setObjectName(u"labelOrigin")
        self.labelOrigin.setMinimumSize(QSize(0, 0))
        self.labelOrigin.setMaximumSize(QSize(16777215, 16777215))
        self.labelOrigin.setBaseSize(QSize(0, 0))
        self.labelOrigin.setFocusPolicy(Qt.ClickFocus)
        self.labelOrigin.setFrameShape(QFrame.NoFrame)
        self.labelOrigin.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.labelOrigin, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameOrigin, 1, 0, 1, 4, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frameTrans = QFrame(self.tabCalibration)
        self.frameTrans.setObjectName(u"frameTrans")
        self.frameTrans.setMinimumSize(QSize(400, 400))
        self.frameTrans.setMaximumSize(QSize(400, 400))
        self.frameTrans.setBaseSize(QSize(0, 0))
        self.frameTrans.setFrameShape(QFrame.StyledPanel)
        self.frameTrans.setFrameShadow(QFrame.Plain)
        self.gridLayout_10 = QGridLayout(self.frameTrans)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.labelTrans = QLabel(self.frameTrans)
        self.labelTrans.setObjectName(u"labelTrans")
        self.labelTrans.setMinimumSize(QSize(0, 0))
        self.labelTrans.setMaximumSize(QSize(16777215, 16777215))
        self.labelTrans.setBaseSize(QSize(0, 0))
        self.labelTrans.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.labelTrans, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_6.addWidget(self.frameTrans, 1, 4, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.pushOpenImage = QPushButton(self.tabCalibration)
        self.pushOpenImage.setObjectName(u"pushOpenImage")
        self.pushOpenImage.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_6.addWidget(self.pushOpenImage, 0, 0, 1, 1)

        self.pushConvert = QPushButton(self.tabCalibration)
        self.pushConvert.setObjectName(u"pushConvert")
        self.pushConvert.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_6.addWidget(self.pushConvert, 0, 2, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lineRotationAngle = QLineEdit(self.tabCalibration)
        self.lineRotationAngle.setObjectName(u"lineRotationAngle")
        sizePolicy1.setHeightForWidth(self.lineRotationAngle.sizePolicy().hasHeightForWidth())
        self.lineRotationAngle.setSizePolicy(sizePolicy1)
        self.lineRotationAngle.setMaximumSize(QSize(55, 55))
        self.lineRotationAngle.setMaxLength(6)
        self.lineRotationAngle.setReadOnly(False)

        self.gridLayout_11.addWidget(self.lineRotationAngle, 0, 1, 1, 1)

        self.labelRotationAngle = QLabel(self.tabCalibration)
        self.labelRotationAngle.setObjectName(u"labelRotationAngle")
        self.labelRotationAngle.setMaximumSize(QSize(115, 16777215))

        self.gridLayout_11.addWidget(self.labelRotationAngle, 0, 0, 1, 1)

        self.pushAngleUp = QPushButton(self.tabCalibration)
        self.pushAngleUp.setObjectName(u"pushAngleUp")
        self.pushAngleUp.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u"../MonitorClient/icons/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushAngleUp.setIcon(icon)

        self.gridLayout_11.addWidget(self.pushAngleUp, 0, 2, 1, 1)

        self.labelPosition = QLabel(self.tabCalibration)
        self.labelPosition.setObjectName(u"labelPosition")

        self.gridLayout_11.addWidget(self.labelPosition, 2, 2, 2, 3)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_5 = QLabel(self.tabCalibration)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_5, 1, 3, 1, 1)

        self.label_2 = QLabel(self.tabCalibration)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tabCalibration)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tabCalibration)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_6 = QLabel(self.tabCalibration)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_6, 1, 4, 1, 1)

        self.sliderAngle = QSlider(self.tabCalibration)
        self.sliderAngle.setObjectName(u"sliderAngle")
        self.sliderAngle.setMaximum(4)
        self.sliderAngle.setPageStep(1)
        self.sliderAngle.setSliderPosition(3)
        self.sliderAngle.setOrientation(Qt.Horizontal)
        self.sliderAngle.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_15.addWidget(self.sliderAngle, 0, 0, 1, 5)


        self.gridLayout_11.addLayout(self.gridLayout_15, 0, 4, 1, 1)

        self.labelExplanation2 = QLabel(self.tabCalibration)
        self.labelExplanation2.setObjectName(u"labelExplanation2")

        self.gridLayout_11.addWidget(self.labelExplanation2, 1, 0, 1, 5)

        self.pushAngleDown = QPushButton(self.tabCalibration)
        self.pushAngleDown.setObjectName(u"pushAngleDown")
        self.pushAngleDown.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"../MonitorClient/icons/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushAngleDown.setIcon(icon1)

        self.gridLayout_11.addWidget(self.pushAngleDown, 0, 3, 1, 1)

        self.labelExplanation = QLabel(self.tabCalibration)
        self.labelExplanation.setObjectName(u"labelExplanation")

        self.gridLayout_11.addWidget(self.labelExplanation, 2, 0, 2, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 4, 0, 1, 5)


        self.gridLayout_6.addLayout(self.gridLayout_11, 2, 0, 2, 4)

        self.tabWidget.addTab(self.tabCalibration, "")
        self.tabPhoto = QWidget()
        self.tabPhoto.setObjectName(u"tabPhoto")
        self.gridLayout_7 = QGridLayout(self.tabPhoto)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBackground = QGroupBox(self.tabPhoto)
        self.groupBackground.setObjectName(u"groupBackground")
        self.groupBackground.setFont(font)
        self.gridLayout_12 = QGridLayout(self.groupBackground)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lineBackground = QLineEdit(self.groupBackground)
        self.lineBackground.setObjectName(u"lineBackground")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.lineBackground.setFont(font2)
        self.lineBackground.setReadOnly(True)

        self.gridLayout_12.addWidget(self.lineBackground, 0, 0, 1, 1)

        self.pushBkgOpen = QPushButton(self.groupBackground)
        self.pushBkgOpen.setObjectName(u"pushBkgOpen")
        self.pushBkgOpen.setFont(font2)

        self.gridLayout_12.addWidget(self.pushBkgOpen, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBackground, 3, 1, 1, 1)

        self.groupFilter = QGroupBox(self.tabPhoto)
        self.groupFilter.setObjectName(u"groupFilter")
        self.groupFilter.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupFilter)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listParameters = QListWidget(self.groupFilter)
        self.listParameters.setObjectName(u"listParameters")
        sizePolicy2.setHeightForWidth(self.listParameters.sizePolicy().hasHeightForWidth())
        self.listParameters.setSizePolicy(sizePolicy2)
        self.listParameters.setFont(font1)

        self.gridLayout_4.addWidget(self.listParameters, 1, 0, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)

        self.pushApplyFilter = QPushButton(self.groupFilter)
        self.pushApplyFilter.setObjectName(u"pushApplyFilter")
        sizePolicy1.setHeightForWidth(self.pushApplyFilter.sizePolicy().hasHeightForWidth())
        self.pushApplyFilter.setSizePolicy(sizePolicy1)
        self.pushApplyFilter.setFont(font1)

        self.gridLayout_4.addWidget(self.pushApplyFilter, 2, 1, 1, 1)

        self.comboFilter = QComboBox(self.groupFilter)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        sizePolicy2.setHeightForWidth(self.comboFilter.sizePolicy().hasHeightForWidth())
        self.comboFilter.setSizePolicy(sizePolicy2)
        self.comboFilter.setFont(font1)

        self.gridLayout_4.addWidget(self.comboFilter, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupFilter, 4, 1, 2, 1)

        self.label = QLabel(self.tabPhoto)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 16777215))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_7.addWidget(self.label, 6, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushCalibrate = QPushButton(self.tabPhoto)
        self.pushCalibrate.setObjectName(u"pushCalibrate")

        self.gridLayout_16.addWidget(self.pushCalibrate, 1, 2, 1, 1)

        self.pushConnectCamera_2 = QPushButton(self.tabPhoto)
        self.pushConnectCamera_2.setObjectName(u"pushConnectCamera_2")

        self.gridLayout_16.addWidget(self.pushConnectCamera_2, 1, 1, 1, 1)

        self.pushCaptureImage = QPushButton(self.tabPhoto)
        self.pushCaptureImage.setObjectName(u"pushCaptureImage")

        self.gridLayout_16.addWidget(self.pushCaptureImage, 1, 3, 1, 1)

        self.checkConnection = QCheckBox(self.tabPhoto)
        self.checkConnection.setObjectName(u"checkConnection")
        self.checkConnection.setMaximumSize(QSize(16777215, 20))
        self.checkConnection.setMouseTracking(False)
        self.checkConnection.setCheckable(False)

        self.gridLayout_16.addWidget(self.checkConnection, 0, 1, 1, 1)

        self.checkCalibration = QCheckBox(self.tabPhoto)
        self.checkCalibration.setObjectName(u"checkCalibration")
        self.checkCalibration.setMaximumSize(QSize(16777215, 20))
        self.checkCalibration.setCheckable(False)

        self.gridLayout_16.addWidget(self.checkCalibration, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer, 0, 3, 1, 2)


        self.gridLayout_7.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.groupCamera = QGroupBox(self.tabPhoto)
        self.groupCamera.setObjectName(u"groupCamera")
        sizePolicy2.setHeightForWidth(self.groupCamera.sizePolicy().hasHeightForWidth())
        self.groupCamera.setSizePolicy(sizePolicy2)
        self.groupCamera.setFont(font)
        self.gridCamera = QGridLayout(self.groupCamera)
        self.gridCamera.setObjectName(u"gridCamera")
        self.labelExposureTime = QLabel(self.groupCamera)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        self.labelExposureTime.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTime, 1, 0, 1, 1)

        self.labelGainRange = QLabel(self.groupCamera)
        self.labelGainRange.setObjectName(u"labelGainRange")
        sizePolicy2.setHeightForWidth(self.labelGainRange.sizePolicy().hasHeightForWidth())
        self.labelGainRange.setSizePolicy(sizePolicy2)
        self.labelGainRange.setMaximumSize(QSize(100, 16777215))
        self.labelGainRange.setFont(font1)

        self.gridCamera.addWidget(self.labelGainRange, 0, 4, 1, 1)

        self.labelExposureTimeRange = QLabel(self.groupCamera)
        self.labelExposureTimeRange.setObjectName(u"labelExposureTimeRange")
        self.labelExposureTimeRange.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTimeRange, 1, 4, 1, 1)

        self.lineGain = QLineEdit(self.groupCamera)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineGain.sizePolicy().hasHeightForWidth())
        self.lineGain.setSizePolicy(sizePolicy4)
        self.lineGain.setMaximumSize(QSize(60, 16777215))
        self.lineGain.setFont(font1)
        self.lineGain.setFocusPolicy(Qt.StrongFocus)
        self.lineGain.setReadOnly(False)

        self.gridCamera.addWidget(self.lineGain, 0, 1, 1, 1)

        self.lineExposureTime = QLineEdit(self.groupCamera)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        sizePolicy4.setHeightForWidth(self.lineExposureTime.sizePolicy().hasHeightForWidth())
        self.lineExposureTime.setSizePolicy(sizePolicy4)
        self.lineExposureTime.setMaximumSize(QSize(60, 16777215))
        self.lineExposureTime.setFont(font1)
        self.lineExposureTime.setFocusPolicy(Qt.StrongFocus)
        self.lineExposureTime.setMaxLength(7)
        self.lineExposureTime.setReadOnly(False)

        self.gridCamera.addWidget(self.lineExposureTime, 1, 1, 1, 1)

        self.pushApplyConf = QPushButton(self.groupCamera)
        self.pushApplyConf.setObjectName(u"pushApplyConf")
        self.pushApplyConf.setFont(font1)

        self.gridCamera.addWidget(self.pushApplyConf, 2, 4, 1, 1)

        self.sliderExposureTime = QSlider(self.groupCamera)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy1.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy1)
        self.sliderExposureTime.setFocusPolicy(Qt.StrongFocus)
        self.sliderExposureTime.setMinimum(25)
        self.sliderExposureTime.setMaximum(1000000)
        self.sliderExposureTime.setValue(5000)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderExposureTime, 1, 2, 1, 2)

        self.labelGain = QLabel(self.groupCamera)
        self.labelGain.setObjectName(u"labelGain")
        self.labelGain.setFont(font1)

        self.gridCamera.addWidget(self.labelGain, 0, 0, 1, 1)

        self.sliderGain = QSlider(self.groupCamera)
        self.sliderGain.setObjectName(u"sliderGain")
        sizePolicy1.setHeightForWidth(self.sliderGain.sizePolicy().hasHeightForWidth())
        self.sliderGain.setSizePolicy(sizePolicy1)
        self.sliderGain.setFocusPolicy(Qt.StrongFocus)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setValue(0)
        self.sliderGain.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderGain, 0, 2, 1, 2)


        self.gridLayout_7.addWidget(self.groupCamera, 0, 1, 2, 1)

        self.frameImage = QFrame(self.tabPhoto)
        self.frameImage.setObjectName(u"frameImage")
        sizePolicy2.setHeightForWidth(self.frameImage.sizePolicy().hasHeightForWidth())
        self.frameImage.setSizePolicy(sizePolicy2)
        self.frameImage.setMinimumSize(QSize(410, 410))
        self.frameImage.setMaximumSize(QSize(410, 410))
        self.frameImage.setBaseSize(QSize(0, 0))
        self.frameImage.setLayoutDirection(Qt.LeftToRight)
        self.frameImage.setFrameShape(QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frameImage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImage = QLabel(self.frameImage)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setMinimumSize(QSize(400, 400))
        self.labelImage.setMaximumSize(QSize(400, 400))
        self.labelImage.setBaseSize(QSize(0, 0))
        self.labelImage.setFocusPolicy(Qt.ClickFocus)
        self.labelImage.setFrameShape(QFrame.NoFrame)
        self.labelImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelImage, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_7.addWidget(self.frameImage, 1, 0, 4, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.groupROI = QGroupBox(self.tabPhoto)
        self.groupROI.setObjectName(u"groupROI")
        self.groupROI.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupROI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelSPPixel = QLabel(self.groupROI)
        self.labelSPPixel.setObjectName(u"labelSPPixel")
        self.labelSPPixel.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSPPixel, 0, 2, 1, 1)

        self.lineHeight = QLineEdit(self.groupROI)
        self.lineHeight.setObjectName(u"lineHeight")
        sizePolicy4.setHeightForWidth(self.lineHeight.sizePolicy().hasHeightForWidth())
        self.lineHeight.setSizePolicy(sizePolicy4)
        self.lineHeight.setMaximumSize(QSize(50, 16777215))
        self.lineHeight.setFont(font1)
        self.lineHeight.setFocusPolicy(Qt.NoFocus)
        self.lineHeight.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineHeight, 5, 1, 1, 1)

        self.labelHeight = QLabel(self.groupROI)
        self.labelHeight.setObjectName(u"labelHeight")
        self.labelHeight.setMaximumSize(QSize(100, 16777215))
        self.labelHeight.setFont(font1)

        self.gridLayout_2.addWidget(self.labelHeight, 5, 0, 1, 1)

        self.labelWidth = QLabel(self.groupROI)
        self.labelWidth.setObjectName(u"labelWidth")
        self.labelWidth.setMaximumSize(QSize(1000, 16777215))
        self.labelWidth.setFont(font1)

        self.gridLayout_2.addWidget(self.labelWidth, 4, 0, 1, 1)

        self.labelSP = QLabel(self.groupROI)
        self.labelSP.setObjectName(u"labelSP")
        self.labelSP.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSP, 0, 0, 1, 2)

        self.labelY0 = QLabel(self.groupROI)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setMaximumSize(QSize(50, 16777215))
        self.labelY0.setFont(font1)

        self.gridLayout_2.addWidget(self.labelY0, 2, 0, 1, 1)

        self.lineY0 = QLineEdit(self.groupROI)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy4.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy4)
        self.lineY0.setMaximumSize(QSize(50, 16777215))
        self.lineY0.setFont(font1)
        self.lineY0.setFocusPolicy(Qt.NoFocus)
        self.lineY0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineY0, 2, 1, 1, 1)

        self.sliderY0 = QSlider(self.groupROI)
        self.sliderY0.setObjectName(u"sliderY0")
        sizePolicy1.setHeightForWidth(self.sliderY0.sizePolicy().hasHeightForWidth())
        self.sliderY0.setSizePolicy(sizePolicy1)
        self.sliderY0.setMaximum(1000)
        self.sliderY0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderY0, 2, 2, 1, 1)

        self.sliderHeight = QSlider(self.groupROI)
        self.sliderHeight.setObjectName(u"sliderHeight")
        sizePolicy1.setHeightForWidth(self.sliderHeight.sizePolicy().hasHeightForWidth())
        self.sliderHeight.setSizePolicy(sizePolicy1)
        self.sliderHeight.setMaximum(1000)
        self.sliderHeight.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderHeight, 5, 2, 1, 1)

        self.labelX0 = QLabel(self.groupROI)
        self.labelX0.setObjectName(u"labelX0")
        self.labelX0.setMaximumSize(QSize(50, 16777215))
        self.labelX0.setFont(font1)

        self.gridLayout_2.addWidget(self.labelX0, 1, 0, 1, 1)

        self.lineWidth = QLineEdit(self.groupROI)
        self.lineWidth.setObjectName(u"lineWidth")
        sizePolicy4.setHeightForWidth(self.lineWidth.sizePolicy().hasHeightForWidth())
        self.lineWidth.setSizePolicy(sizePolicy4)
        self.lineWidth.setMaximumSize(QSize(50, 16777215))
        self.lineWidth.setFont(font1)
        self.lineWidth.setFocusPolicy(Qt.NoFocus)
        self.lineWidth.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineWidth, 4, 1, 1, 1)

        self.lineX0 = QLineEdit(self.groupROI)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy4.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy4)
        self.lineX0.setMaximumSize(QSize(50, 16777215))
        self.lineX0.setFont(font1)
        self.lineX0.setFocusPolicy(Qt.NoFocus)
        self.lineX0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineX0, 1, 1, 1, 1)

        self.labelSizePixel = QLabel(self.groupROI)
        self.labelSizePixel.setObjectName(u"labelSizePixel")
        self.labelSizePixel.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSizePixel, 3, 2, 1, 1)

        self.sliderWidth = QSlider(self.groupROI)
        self.sliderWidth.setObjectName(u"sliderWidth")
        sizePolicy1.setHeightForWidth(self.sliderWidth.sizePolicy().hasHeightForWidth())
        self.sliderWidth.setSizePolicy(sizePolicy1)
        self.sliderWidth.setMaximum(1000)
        self.sliderWidth.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderWidth, 4, 2, 1, 1)

        self.labelSize = QLabel(self.groupROI)
        self.labelSize.setObjectName(u"labelSize")
        self.labelSize.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSize, 3, 0, 1, 2)

        self.sliderX0 = QSlider(self.groupROI)
        self.sliderX0.setObjectName(u"sliderX0")
        sizePolicy1.setHeightForWidth(self.sliderX0.sizePolicy().hasHeightForWidth())
        self.sliderX0.setSizePolicy(sizePolicy1)
        self.sliderX0.setFocusPolicy(Qt.StrongFocus)
        self.sliderX0.setMaximum(1000)
        self.sliderX0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderX0, 1, 2, 1, 1)


        self.gridLayout_7.addWidget(self.groupROI, 2, 1, 1, 1)

        self.framePVHist = QFrame(self.tabPhoto)
        self.framePVHist.setObjectName(u"framePVHist")
        self.framePVHist.setMinimumSize(QSize(410, 135))
        self.framePVHist.setMaximumSize(QSize(410, 135))
        self.framePVHist.setFrameShape(QFrame.StyledPanel)
        self.framePVHist.setFrameShadow(QFrame.Sunken)
        self.gridPVHist = QGridLayout(self.framePVHist)
        self.gridPVHist.setSpacing(0)
        self.gridPVHist.setObjectName(u"gridPVHist")
        self.gridPVHist.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.framePVHist, 5, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.tabWidget.addTab(self.tabPhoto, "")

        self.gridLayout_13.addWidget(self.tabWidget, 1, 0, 1, 7)

        self.checkSaveLast = QCheckBox(SetupWindow)
        self.checkSaveLast.setObjectName(u"checkSaveLast")
        self.checkSaveLast.setChecked(True)

        self.gridLayout_13.addWidget(self.checkSaveLast, 2, 4, 1, 1)

        self.pushCancel = QPushButton(SetupWindow)
        self.pushCancel.setObjectName(u"pushCancel")
        sizePolicy1.setHeightForWidth(self.pushCancel.sizePolicy().hasHeightForWidth())
        self.pushCancel.setSizePolicy(sizePolicy1)
        self.pushCancel.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushCancel, 2, 6, 1, 1)

        self.pushSave = QPushButton(SetupWindow)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushSave, 0, 0, 1, 1)

        self.comboSetup = QComboBox(SetupWindow)
        self.comboSetup.setObjectName(u"comboSetup")
        self.comboSetup.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.comboSetup, 0, 3, 1, 4)

        self.pushReset = QPushButton(SetupWindow)
        self.pushReset.setObjectName(u"pushReset")

        self.gridLayout_13.addWidget(self.pushReset, 0, 2, 1, 1)

        QWidget.setTabOrder(self.tabWidget, self.comboSDKType)
        QWidget.setTabOrder(self.comboSDKType, self.lineCameraAddr)
        QWidget.setTabOrder(self.lineCameraAddr, self.pushConnectCamera)
        QWidget.setTabOrder(self.pushConnectCamera, self.checkCameraConnected)
        QWidget.setTabOrder(self.checkCameraConnected, self.checkUseControlServer)
        QWidget.setTabOrder(self.checkUseControlServer, self.lineControllerIP1)
        QWidget.setTabOrder(self.lineControllerIP1, self.lineControllerIP2)
        QWidget.setTabOrder(self.lineControllerIP2, self.lineControllerIP3)
        QWidget.setTabOrder(self.lineControllerIP3, self.lineControllerIP4)
        QWidget.setTabOrder(self.lineControllerIP4, self.lineControllerIP5)
        QWidget.setTabOrder(self.lineControllerIP5, self.pushConnectController)
        QWidget.setTabOrder(self.pushConnectController, self.checkControllerConnected)
        QWidget.setTabOrder(self.checkControllerConnected, self.lineGain)
        QWidget.setTabOrder(self.lineGain, self.sliderGain)
        QWidget.setTabOrder(self.sliderGain, self.lineExposureTime)
        QWidget.setTabOrder(self.lineExposureTime, self.sliderExposureTime)
        QWidget.setTabOrder(self.sliderExposureTime, self.pushApplyConf)
        QWidget.setTabOrder(self.pushApplyConf, self.sliderX0)
        QWidget.setTabOrder(self.sliderX0, self.sliderY0)
        QWidget.setTabOrder(self.sliderY0, self.sliderWidth)
        QWidget.setTabOrder(self.sliderWidth, self.sliderHeight)
        QWidget.setTabOrder(self.sliderHeight, self.comboFilter)
        QWidget.setTabOrder(self.comboFilter, self.listParameters)
        QWidget.setTabOrder(self.listParameters, self.pushApplyFilter)
        QWidget.setTabOrder(self.pushApplyFilter, self.pushCalCapture)
        QWidget.setTabOrder(self.pushCalCapture, self.lineRotationAngle)
        QWidget.setTabOrder(self.lineRotationAngle, self.pushAngleUp)
        QWidget.setTabOrder(self.pushAngleUp, self.pushAngleDown)
        QWidget.setTabOrder(self.pushAngleDown, self.sliderAngle)
        QWidget.setTabOrder(self.sliderAngle, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.linePixelPerMM_x)
        QWidget.setTabOrder(self.linePixelPerMM_x, self.linePixelPerMM_y)
        QWidget.setTabOrder(self.linePixelPerMM_y, self.lineQuad1x)
        QWidget.setTabOrder(self.lineQuad1x, self.lineQuad1y)
        QWidget.setTabOrder(self.lineQuad1y, self.lineQuad2x)
        QWidget.setTabOrder(self.lineQuad2x, self.lineQuad2y)
        QWidget.setTabOrder(self.lineQuad2y, self.lineQuad3x)
        QWidget.setTabOrder(self.lineQuad3x, self.lineQuad3y)
        QWidget.setTabOrder(self.lineQuad3y, self.lineQuad4x)
        QWidget.setTabOrder(self.lineQuad4x, self.lineQuad4y)
        QWidget.setTabOrder(self.lineQuad4y, self.checkSaveLast)
        QWidget.setTabOrder(self.checkSaveLast, self.textConnectionLog)

        self.retranslateUi(SetupWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SetupWindow)
    # setupUi

    def retranslateUi(self, SetupWindow):
        SetupWindow.setWindowTitle(QCoreApplication.translate("SetupWindow", u"Setup", None))
        self.pushOk.setText(QCoreApplication.translate("SetupWindow", u"Ok", None))
        self.pushLoad.setText(QCoreApplication.translate("SetupWindow", u"Load", None))
        self.groupCameraConnection.setTitle(QCoreApplication.translate("SetupWindow", u"Camera", None))
        self.labelSDKType.setText(QCoreApplication.translate("SetupWindow", u"SDK Type", None))
        self.labelIP.setText(QCoreApplication.translate("SetupWindow", u"URL or IP", None))
        self.comboSDKType.setItemText(0, QCoreApplication.translate("SetupWindow", u"OpenCV", None))
        self.comboSDKType.setItemText(1, QCoreApplication.translate("SetupWindow", u"Pylon (Basler)", None))

        self.pushConnectCamera.setText(QCoreApplication.translate("SetupWindow", u"Connect", None))
        self.pushDisconnectCamera.setText(QCoreApplication.translate("SetupWindow", u"Disconnect", None))
        self.checkCameraConnected.setText(QCoreApplication.translate("SetupWindow", u"Connected", None))
        self.groupControllerConnection.setTitle(QCoreApplication.translate("SetupWindow", u"Controller", None))
        self.checkUseControlServer.setText(QCoreApplication.translate("SetupWindow", u"Use Screen Controller", None))
        self.labelControllerIP2.setText(QCoreApplication.translate("SetupWindow", u".", None))
        self.labelControllerIP3.setText(QCoreApplication.translate("SetupWindow", u".", None))
        self.labelControllerIP4.setText(QCoreApplication.translate("SetupWindow", u".", None))
        self.labelControllerIP5.setText(QCoreApplication.translate("SetupWindow", u":", None))
        self.labelControllerIP1.setText(QCoreApplication.translate("SetupWindow", u"IP Address", None))
        self.pushConnectController.setText(QCoreApplication.translate("SetupWindow", u"Connect", None))
        self.pushDisconnectController.setText(QCoreApplication.translate("SetupWindow", u"Disconnect", None))
        self.checkControllerConnected.setText(QCoreApplication.translate("SetupWindow", u"Connected", None))
        self.labelMonitorNumber.setText(QCoreApplication.translate("SetupWindow", u"Monitor Number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConnection), QCoreApplication.translate("SetupWindow", u"Connection", None))
        self.labelPerspective.setText(QCoreApplication.translate("SetupWindow", u"Perspective Matrix", None))
        self.label_16.setText(QCoreApplication.translate("SetupWindow", u"Pixel per mm", None))
        self.linePixelPerMM_y.setText(QCoreApplication.translate("SetupWindow", u"1.0", None))
        self.label_17.setText(QCoreApplication.translate("SetupWindow", u"x", None))
        self.linePixelPerMM_x.setText(QCoreApplication.translate("SetupWindow", u"1.0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabRectangle), QCoreApplication.translate("SetupWindow", u"Rectangle", None))
        self.label_14.setText(QCoreApplication.translate("SetupWindow", u"4", None))
        self.lineQuad4y.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.lineQuad3y.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.lineQuad2y.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("SetupWindow", u"x (mm)", None))
        self.label_10.setText(QCoreApplication.translate("SetupWindow", u"y (mm)", None))
        self.lineQuad2x.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.lineQuad4x.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.label_7.setText(QCoreApplication.translate("SetupWindow", u"Real space coordinate", None))
        self.label_11.setText(QCoreApplication.translate("SetupWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("SetupWindow", u"3", None))
        self.lineQuad1y.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.lineQuad1x.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.label_8.setText(QCoreApplication.translate("SetupWindow", u"Quadrant", None))
        self.label_12.setText(QCoreApplication.translate("SetupWindow", u"2", None))
        self.lineQuad3x.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabPoint), QCoreApplication.translate("SetupWindow", u"Point", None))
        self.pushCalCapture.setText(QCoreApplication.translate("SetupWindow", u"Capture", None))
        self.labelOrigin.setText("")
        self.labelTrans.setText("")
        self.pushOpenImage.setText(QCoreApplication.translate("SetupWindow", u"Open", None))
        self.pushConvert.setText(QCoreApplication.translate("SetupWindow", u"Convert", None))
        self.lineRotationAngle.setText(QCoreApplication.translate("SetupWindow", u"0.0", None))
        self.labelRotationAngle.setText(QCoreApplication.translate("SetupWindow", u"Rotation angle (deg)", None))
        self.pushAngleUp.setText("")
        self.labelPosition.setText(QCoreApplication.translate("SetupWindow", u"Position:", None))
        self.label_5.setText(QCoreApplication.translate("SetupWindow", u"10 ", None))
        self.label_2.setText(QCoreApplication.translate("SetupWindow", u"0.01", None))
        self.label_3.setText(QCoreApplication.translate("SetupWindow", u" 0.1", None))
        self.label_4.setText(QCoreApplication.translate("SetupWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("SetupWindow", u"100", None))
        self.labelExplanation2.setText(QCoreApplication.translate("SetupWindow", u"Left click: Add transformation point, Right click: Erase transformation point", None))
        self.pushAngleDown.setText("")
        self.labelExplanation.setText(QCoreApplication.translate("SetupWindow", u"Ctrl + arrow keys: Move last point", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalibration), QCoreApplication.translate("SetupWindow", u"Calibration", None))
        self.groupBackground.setTitle(QCoreApplication.translate("SetupWindow", u"Background Substraction", None))
        self.pushBkgOpen.setText(QCoreApplication.translate("SetupWindow", u"Open", None))
        self.groupFilter.setTitle(QCoreApplication.translate("SetupWindow", u"Filter", None))
        self.pushApplyFilter.setText(QCoreApplication.translate("SetupWindow", u"Apply", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("SetupWindow", u"Select", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("SetupWindow", u"No Filter", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("SetupWindow", u"Gaussian", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("SetupWindow", u"Median", None))
        self.comboFilter.setItemText(4, QCoreApplication.translate("SetupWindow", u"Bilateral", None))

        self.label.setText(QCoreApplication.translate("SetupWindow", u"Drag: draw ROI range, Left double click: set ROI, Right double click: reset ROI", None))
        self.pushCalibrate.setText(QCoreApplication.translate("SetupWindow", u"Calibrate", None))
        self.pushConnectCamera_2.setText(QCoreApplication.translate("SetupWindow", u"Connect", None))
        self.pushCaptureImage.setText(QCoreApplication.translate("SetupWindow", u"Capture", None))
        self.checkConnection.setText(QCoreApplication.translate("SetupWindow", u"Connection", None))
        self.checkCalibration.setText(QCoreApplication.translate("SetupWindow", u"Calibration", None))
        self.groupCamera.setTitle(QCoreApplication.translate("SetupWindow", u"Camera", None))
        self.labelExposureTime.setText(QCoreApplication.translate("SetupWindow", u"Exposure Time (\u03bcs)", None))
        self.labelGainRange.setText(QCoreApplication.translate("SetupWindow", u"(0 - 100)", None))
        self.labelExposureTimeRange.setText(QCoreApplication.translate("SetupWindow", u"(25 - 1000000)", None))
        self.lineGain.setText(QCoreApplication.translate("SetupWindow", u"0", None))
        self.lineExposureTime.setText(QCoreApplication.translate("SetupWindow", u"5000", None))
        self.pushApplyConf.setText(QCoreApplication.translate("SetupWindow", u"Apply", None))
        self.labelGain.setText(QCoreApplication.translate("SetupWindow", u"Gain (%)", None))
        self.labelImage.setText("")
        self.groupROI.setTitle(QCoreApplication.translate("SetupWindow", u"Region of Interest", None))
        self.labelSPPixel.setText(QCoreApplication.translate("SetupWindow", u"(0,0) pixel", None))
        self.lineHeight.setText(QCoreApplication.translate("SetupWindow", u"0", None))
        self.labelHeight.setText(QCoreApplication.translate("SetupWindow", u"  height (%)", None))
        self.labelWidth.setText(QCoreApplication.translate("SetupWindow", u"  width (%)", None))
        self.labelSP.setText(QCoreApplication.translate("SetupWindow", u"Start Point", None))
        self.labelY0.setText(QCoreApplication.translate("SetupWindow", u"  y (%)", None))
        self.lineY0.setText(QCoreApplication.translate("SetupWindow", u"0", None))
        self.labelX0.setText(QCoreApplication.translate("SetupWindow", u"  x (%)", None))
        self.lineWidth.setText(QCoreApplication.translate("SetupWindow", u"0", None))
        self.lineX0.setText(QCoreApplication.translate("SetupWindow", u"0", None))
        self.labelSizePixel.setText(QCoreApplication.translate("SetupWindow", u"(0,0) pixel", None))
        self.labelSize.setText(QCoreApplication.translate("SetupWindow", u"ROI Size", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPhoto), QCoreApplication.translate("SetupWindow", u"Photo", None))
        self.checkSaveLast.setText(QCoreApplication.translate("SetupWindow", u"This settings will be used later.", None))
        self.pushCancel.setText(QCoreApplication.translate("SetupWindow", u"Cancel", None))
        self.pushSave.setText(QCoreApplication.translate("SetupWindow", u"Save", None))
        self.pushReset.setText(QCoreApplication.translate("SetupWindow", u"Reset", None))
    # retranslateUi

