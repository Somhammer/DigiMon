# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SetupWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1084, 706)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(Dialog)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pushSave = QPushButton(Dialog)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushSave, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.comboSetup = QComboBox(Dialog)
        self.comboSetup.setObjectName(u"comboSetup")
        self.comboSetup.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.comboSetup, 0, 2, 1, 1)

        self.checkSaveLast = QCheckBox(Dialog)
        self.checkSaveLast.setObjectName(u"checkSaveLast")
        self.checkSaveLast.setChecked(True)

        self.gridLayout_13.addWidget(self.checkSaveLast, 2, 3, 1, 1)

        self.pushOk = QPushButton(Dialog)
        self.pushOk.setObjectName(u"pushOk")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushOk.sizePolicy().hasHeightForWidth())
        self.pushOk.setSizePolicy(sizePolicy1)
        self.pushOk.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushOk, 2, 4, 1, 1)

        self.pushLoad = QPushButton(Dialog)
        self.pushLoad.setObjectName(u"pushLoad")
        self.pushLoad.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushLoad, 0, 1, 1, 1)

        self.pushCancel = QPushButton(Dialog)
        self.pushCancel.setObjectName(u"pushCancel")
        sizePolicy1.setHeightForWidth(self.pushCancel.sizePolicy().hasHeightForWidth())
        self.pushCancel.setSizePolicy(sizePolicy1)
        self.pushCancel.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_13.addWidget(self.pushCancel, 2, 5, 1, 1)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabConnection = QWidget()
        self.tabConnection.setObjectName(u"tabConnection")
        self.gridLayout_8 = QGridLayout(self.tabConnection)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupCameraConnection = QGroupBox(self.tabConnection)
        self.groupCameraConnection.setObjectName(u"groupCameraConnection")
        sizePolicy2.setHeightForWidth(self.groupCameraConnection.sizePolicy().hasHeightForWidth())
        self.groupCameraConnection.setSizePolicy(sizePolicy2)
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

        self.comboSDKType = QComboBox(self.groupCameraConnection)
        self.comboSDKType.addItem("")
        self.comboSDKType.addItem("")
        self.comboSDKType.addItem("")
        self.comboSDKType.setObjectName(u"comboSDKType")
        self.comboSDKType.setFont(font1)

        self.gridLayout_3.addWidget(self.comboSDKType, 0, 1, 1, 1)

        self.labelIP = QLabel(self.groupCameraConnection)
        self.labelIP.setObjectName(u"labelIP")
        self.labelIP.setFont(font1)

        self.gridLayout_3.addWidget(self.labelIP, 1, 0, 1, 1)

        self.lineCameraAddr = QLineEdit(self.groupCameraConnection)
        self.lineCameraAddr.setObjectName(u"lineCameraAddr")
        self.lineCameraAddr.setFont(font1)

        self.gridLayout_3.addWidget(self.lineCameraAddr, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.pushConnectCamera = QPushButton(self.groupCameraConnection)
        self.pushConnectCamera.setObjectName(u"pushConnectCamera")
        self.pushConnectCamera.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushConnectCamera)

        self.checkCameraConnected = QCheckBox(self.groupCameraConnection)
        self.checkCameraConnected.setObjectName(u"checkCameraConnected")
        self.checkCameraConnected.setFont(font1)
        self.checkCameraConnected.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.checkCameraConnected)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)


        self.gridLayout_8.addWidget(self.groupCameraConnection, 0, 0, 1, 1)

        self.groupControllerConnection = QGroupBox(self.tabConnection)
        self.groupControllerConnection.setObjectName(u"groupControllerConnection")
        sizePolicy2.setHeightForWidth(self.groupControllerConnection.sizePolicy().hasHeightForWidth())
        self.groupControllerConnection.setSizePolicy(sizePolicy2)
        self.groupControllerConnection.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupControllerConnection)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkUseControlServer = QCheckBox(self.groupControllerConnection)
        self.checkUseControlServer.setObjectName(u"checkUseControlServer")
        self.checkUseControlServer.setFont(font1)

        self.gridLayout_5.addWidget(self.checkUseControlServer, 0, 0, 1, 2)

        self.labelControllerIP1 = QLabel(self.groupControllerConnection)
        self.labelControllerIP1.setObjectName(u"labelControllerIP1")
        self.labelControllerIP1.setFont(font1)

        self.gridLayout_5.addWidget(self.labelControllerIP1, 1, 0, 1, 1)

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

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.pushConnectController = QPushButton(self.groupControllerConnection)
        self.pushConnectController.setObjectName(u"pushConnectController")
        self.pushConnectController.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushConnectController)

        self.checkControllerConnected = QCheckBox(self.groupControllerConnection)
        self.checkControllerConnected.setObjectName(u"checkControllerConnected")
        self.checkControllerConnected.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkControllerConnected)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)


        self.gridLayout_8.addWidget(self.groupControllerConnection, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(751, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.textConnectionLog = QTextBrowser(self.tabConnection)
        self.textConnectionLog.setObjectName(u"textConnectionLog")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textConnectionLog.sizePolicy().hasHeightForWidth())
        self.textConnectionLog.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.textConnectionLog, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabConnection, "")
        self.tabPhoto = QWidget()
        self.tabPhoto.setObjectName(u"tabPhoto")
        self.gridLayout_6 = QGridLayout(self.tabPhoto)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frameImage = QFrame(self.tabPhoto)
        self.frameImage.setObjectName(u"frameImage")
        sizePolicy2.setHeightForWidth(self.frameImage.sizePolicy().hasHeightForWidth())
        self.frameImage.setSizePolicy(sizePolicy2)
        self.frameImage.setMinimumSize(QSize(550, 550))
        self.frameImage.setMaximumSize(QSize(550, 550))
        self.frameImage.setFrameShape(QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameImage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImage = QLabel(self.frameImage)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setMinimumSize(QSize(550, 550))
        self.labelImage.setMaximumSize(QSize(9999, 9999))
        self.labelImage.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.labelImage, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameImage, 0, 0, 3, 1)

        self.groupCamera = QGroupBox(self.tabPhoto)
        self.groupCamera.setObjectName(u"groupCamera")
        sizePolicy2.setHeightForWidth(self.groupCamera.sizePolicy().hasHeightForWidth())
        self.groupCamera.setSizePolicy(sizePolicy2)
        self.groupCamera.setFont(font)
        self.gridCamera = QGridLayout(self.groupCamera)
        self.gridCamera.setObjectName(u"gridCamera")
        self.lineGain = QLineEdit(self.groupCamera)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineGain.sizePolicy().hasHeightForWidth())
        self.lineGain.setSizePolicy(sizePolicy4)
        self.lineGain.setMaximumSize(QSize(50, 16777215))
        self.lineGain.setFont(font1)
        self.lineGain.setFocusPolicy(Qt.NoFocus)
        self.lineGain.setReadOnly(True)

        self.gridCamera.addWidget(self.lineGain, 0, 1, 1, 1)

        self.lineExposureTime = QLineEdit(self.groupCamera)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        sizePolicy4.setHeightForWidth(self.lineExposureTime.sizePolicy().hasHeightForWidth())
        self.lineExposureTime.setSizePolicy(sizePolicy4)
        self.lineExposureTime.setMaximumSize(QSize(50, 16777215))
        self.lineExposureTime.setFont(font1)
        self.lineExposureTime.setFocusPolicy(Qt.NoFocus)
        self.lineExposureTime.setReadOnly(True)

        self.gridCamera.addWidget(self.lineExposureTime, 1, 1, 1, 1)

        self.labelExposureTimeRange = QLabel(self.groupCamera)
        self.labelExposureTimeRange.setObjectName(u"labelExposureTimeRange")
        self.labelExposureTimeRange.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTimeRange, 1, 4, 1, 1)

        self.labelGainRange = QLabel(self.groupCamera)
        self.labelGainRange.setObjectName(u"labelGainRange")
        sizePolicy2.setHeightForWidth(self.labelGainRange.sizePolicy().hasHeightForWidth())
        self.labelGainRange.setSizePolicy(sizePolicy2)
        self.labelGainRange.setMaximumSize(QSize(100, 16777215))
        self.labelGainRange.setFont(font1)

        self.gridCamera.addWidget(self.labelGainRange, 0, 4, 1, 1)

        self.labelGain = QLabel(self.groupCamera)
        self.labelGain.setObjectName(u"labelGain")
        self.labelGain.setFont(font1)

        self.gridCamera.addWidget(self.labelGain, 0, 0, 1, 1)

        self.sliderGain = QSlider(self.groupCamera)
        self.sliderGain.setObjectName(u"sliderGain")
        sizePolicy1.setHeightForWidth(self.sliderGain.sizePolicy().hasHeightForWidth())
        self.sliderGain.setSizePolicy(sizePolicy1)
        self.sliderGain.setFocusPolicy(Qt.TabFocus)
        self.sliderGain.setMaximum(200)
        self.sliderGain.setValue(100)
        self.sliderGain.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderGain, 0, 2, 1, 2)

        self.labelExposureTime = QLabel(self.groupCamera)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        self.labelExposureTime.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTime, 1, 0, 1, 1)

        self.sliderExposureTime = QSlider(self.groupCamera)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy1.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy1)
        self.sliderExposureTime.setFocusPolicy(Qt.TabFocus)
        self.sliderExposureTime.setMinimum(1)
        self.sliderExposureTime.setMaximum(1000)
        self.sliderExposureTime.setValue(500)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderExposureTime, 1, 2, 1, 2)


        self.gridLayout_6.addWidget(self.groupCamera, 0, 1, 1, 1)

        self.groupROI = QGroupBox(self.tabPhoto)
        self.groupROI.setObjectName(u"groupROI")
        self.groupROI.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupROI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelX0 = QLabel(self.groupROI)
        self.labelX0.setObjectName(u"labelX0")
        self.labelX0.setMaximumSize(QSize(50, 16777215))
        self.labelX0.setFont(font1)

        self.gridLayout_2.addWidget(self.labelX0, 1, 0, 1, 1)

        self.sliderX0 = QSlider(self.groupROI)
        self.sliderX0.setObjectName(u"sliderX0")
        sizePolicy1.setHeightForWidth(self.sliderX0.sizePolicy().hasHeightForWidth())
        self.sliderX0.setSizePolicy(sizePolicy1)
        self.sliderX0.setFocusPolicy(Qt.StrongFocus)
        self.sliderX0.setMaximum(1000)
        self.sliderX0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderX0, 1, 2, 1, 1)

        self.labelY0 = QLabel(self.groupROI)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setMaximumSize(QSize(50, 16777215))
        self.labelY0.setFont(font1)

        self.gridLayout_2.addWidget(self.labelY0, 2, 0, 1, 1)

        self.sliderY0 = QSlider(self.groupROI)
        self.sliderY0.setObjectName(u"sliderY0")
        sizePolicy1.setHeightForWidth(self.sliderY0.sizePolicy().hasHeightForWidth())
        self.sliderY0.setSizePolicy(sizePolicy1)
        self.sliderY0.setMaximum(1000)
        self.sliderY0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderY0, 2, 2, 1, 1)

        self.labelWidth = QLabel(self.groupROI)
        self.labelWidth.setObjectName(u"labelWidth")
        self.labelWidth.setMaximumSize(QSize(1000, 16777215))
        self.labelWidth.setFont(font1)

        self.gridLayout_2.addWidget(self.labelWidth, 4, 0, 1, 1)

        self.labelSize = QLabel(self.groupROI)
        self.labelSize.setObjectName(u"labelSize")
        self.labelSize.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSize, 3, 0, 1, 2)

        self.labelSP = QLabel(self.groupROI)
        self.labelSP.setObjectName(u"labelSP")
        self.labelSP.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSP, 0, 0, 1, 2)

        self.labelHeight = QLabel(self.groupROI)
        self.labelHeight.setObjectName(u"labelHeight")
        self.labelHeight.setMaximumSize(QSize(100, 16777215))
        self.labelHeight.setFont(font1)

        self.gridLayout_2.addWidget(self.labelHeight, 5, 0, 1, 1)

        self.lineWidth = QLineEdit(self.groupROI)
        self.lineWidth.setObjectName(u"lineWidth")
        sizePolicy4.setHeightForWidth(self.lineWidth.sizePolicy().hasHeightForWidth())
        self.lineWidth.setSizePolicy(sizePolicy4)
        self.lineWidth.setMaximumSize(QSize(50, 16777215))
        self.lineWidth.setFont(font1)
        self.lineWidth.setFocusPolicy(Qt.NoFocus)
        self.lineWidth.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineWidth, 4, 1, 1, 1)

        self.labelSizePixel = QLabel(self.groupROI)
        self.labelSizePixel.setObjectName(u"labelSizePixel")
        self.labelSizePixel.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSizePixel, 3, 2, 1, 1)

        self.lineX0 = QLineEdit(self.groupROI)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy4.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy4)
        self.lineX0.setMaximumSize(QSize(50, 16777215))
        self.lineX0.setFont(font1)
        self.lineX0.setFocusPolicy(Qt.NoFocus)
        self.lineX0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineX0, 1, 1, 1, 1)

        self.sliderWidth = QSlider(self.groupROI)
        self.sliderWidth.setObjectName(u"sliderWidth")
        sizePolicy1.setHeightForWidth(self.sliderWidth.sizePolicy().hasHeightForWidth())
        self.sliderWidth.setSizePolicy(sizePolicy1)
        self.sliderWidth.setMaximum(1000)
        self.sliderWidth.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderWidth, 4, 2, 1, 1)

        self.lineY0 = QLineEdit(self.groupROI)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy4.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy4)
        self.lineY0.setMaximumSize(QSize(50, 16777215))
        self.lineY0.setFont(font1)
        self.lineY0.setFocusPolicy(Qt.NoFocus)
        self.lineY0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineY0, 2, 1, 1, 1)

        self.sliderHeight = QSlider(self.groupROI)
        self.sliderHeight.setObjectName(u"sliderHeight")
        sizePolicy1.setHeightForWidth(self.sliderHeight.sizePolicy().hasHeightForWidth())
        self.sliderHeight.setSizePolicy(sizePolicy1)
        self.sliderHeight.setMaximum(1000)
        self.sliderHeight.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderHeight, 5, 2, 1, 1)

        self.lineHeight = QLineEdit(self.groupROI)
        self.lineHeight.setObjectName(u"lineHeight")
        sizePolicy4.setHeightForWidth(self.lineHeight.sizePolicy().hasHeightForWidth())
        self.lineHeight.setSizePolicy(sizePolicy4)
        self.lineHeight.setMaximumSize(QSize(50, 16777215))
        self.lineHeight.setFont(font1)
        self.lineHeight.setFocusPolicy(Qt.NoFocus)
        self.lineHeight.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineHeight, 5, 1, 1, 1)

        self.labelSPPixel = QLabel(self.groupROI)
        self.labelSPPixel.setObjectName(u"labelSPPixel")
        self.labelSPPixel.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSPPixel, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupROI, 1, 1, 1, 1)

        self.label = QLabel(self.tabPhoto)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 3, 0, 1, 1)

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

        self.pushFilterApply = QPushButton(self.groupFilter)
        self.pushFilterApply.setObjectName(u"pushFilterApply")
        sizePolicy1.setHeightForWidth(self.pushFilterApply.sizePolicy().hasHeightForWidth())
        self.pushFilterApply.setSizePolicy(sizePolicy1)
        self.pushFilterApply.setFont(font1)

        self.gridLayout_4.addWidget(self.pushFilterApply, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 1, 1, 1)

        self.comboFilter = QComboBox(self.groupFilter)
        self.comboFilter.addItem("")
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


        self.gridLayout_6.addWidget(self.groupFilter, 2, 1, 2, 1)

        self.tabWidget.addTab(self.tabPhoto, "")
        self.tabCalibration = QWidget()
        self.tabCalibration.setObjectName(u"tabCalibration")
        self.gridLayout_7 = QGridLayout(self.tabCalibration)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushOpenImage = QPushButton(self.tabCalibration)
        self.pushOpenImage.setObjectName(u"pushOpenImage")
        self.pushOpenImage.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_7.addWidget(self.pushOpenImage, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.pushConvert = QPushButton(self.tabCalibration)
        self.pushConvert.setObjectName(u"pushConvert")
        self.pushConvert.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_7.addWidget(self.pushConvert, 0, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frameOrigin = QFrame(self.tabCalibration)
        self.frameOrigin.setObjectName(u"frameOrigin")
        self.frameOrigin.setMinimumSize(QSize(450, 450))
        self.frameOrigin.setMaximumSize(QSize(450, 450))
        self.frameOrigin.setFrameShape(QFrame.StyledPanel)
        self.frameOrigin.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frameOrigin)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.labelOrigin = QLabel(self.frameOrigin)
        self.labelOrigin.setObjectName(u"labelOrigin")
        self.labelOrigin.setMinimumSize(QSize(450, 450))
        self.labelOrigin.setMaximumSize(QSize(450, 450))
        self.labelOrigin.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_9.addWidget(self.labelOrigin, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frameOrigin, 1, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.frameTrans = QFrame(self.tabCalibration)
        self.frameTrans.setObjectName(u"frameTrans")
        self.frameTrans.setMinimumSize(QSize(450, 450))
        self.frameTrans.setMaximumSize(QSize(450, 450))
        self.frameTrans.setFrameShape(QFrame.StyledPanel)
        self.frameTrans.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frameTrans)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.labelTrans = QLabel(self.frameTrans)
        self.labelTrans.setObjectName(u"labelTrans")
        self.labelTrans.setMinimumSize(QSize(450, 450))
        self.labelTrans.setMaximumSize(QSize(450, 450))

        self.gridLayout_10.addWidget(self.labelTrans, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frameTrans, 1, 4, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 1, 6, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_17 = QLabel(self.tabCalibration)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 0, 0, 1, 2)

        self.labelExplain = QLabel(self.tabCalibration)
        self.labelExplain.setObjectName(u"labelExplain")

        self.gridLayout_11.addWidget(self.labelExplain, 1, 0, 1, 2)

        self.labelPosition = QLabel(self.tabCalibration)
        self.labelPosition.setObjectName(u"labelPosition")

        self.gridLayout_11.addWidget(self.labelPosition, 2, 0, 1, 2)


        self.gridLayout_7.addLayout(self.gridLayout_11, 2, 1, 1, 2)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.linePixelHeight = QLineEdit(self.tabCalibration)
        self.linePixelHeight.setObjectName(u"linePixelHeight")
        sizePolicy1.setHeightForWidth(self.linePixelHeight.sizePolicy().hasHeightForWidth())
        self.linePixelHeight.setSizePolicy(sizePolicy1)
        self.linePixelHeight.setMaximumSize(QSize(80, 16777215))
        self.linePixelHeight.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_12.addWidget(self.linePixelHeight, 4, 2, 1, 1)

        self.label_21 = QLabel(self.tabCalibration)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_21, 0, 0, 1, 2)

        self.linePixelWidth = QLineEdit(self.tabCalibration)
        self.linePixelWidth.setObjectName(u"linePixelWidth")
        sizePolicy1.setHeightForWidth(self.linePixelWidth.sizePolicy().hasHeightForWidth())
        self.linePixelWidth.setSizePolicy(sizePolicy1)
        self.linePixelWidth.setMaximumSize(QSize(80, 16777215))
        self.linePixelWidth.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_12.addWidget(self.linePixelWidth, 3, 2, 1, 1)

        self.lineTransHeight = QLineEdit(self.tabCalibration)
        self.lineTransHeight.setObjectName(u"lineTransHeight")
        sizePolicy1.setHeightForWidth(self.lineTransHeight.sizePolicy().hasHeightForWidth())
        self.lineTransHeight.setSizePolicy(sizePolicy1)
        self.lineTransHeight.setMaximumSize(QSize(80, 16777215))
        self.lineTransHeight.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_12.addWidget(self.lineTransHeight, 0, 4, 1, 1)

        self.label_19 = QLabel(self.tabCalibration)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(10, 16777215))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_19, 0, 3, 1, 1)

        self.label_24 = QLabel(self.tabCalibration)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_12.addWidget(self.label_24, 4, 4, 1, 1)

        self.label_23 = QLabel(self.tabCalibration)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_12.addWidget(self.label_23, 3, 4, 1, 1)

        self.lineTransWidth = QLineEdit(self.tabCalibration)
        self.lineTransWidth.setObjectName(u"lineTransWidth")
        sizePolicy1.setHeightForWidth(self.lineTransWidth.sizePolicy().hasHeightForWidth())
        self.lineTransWidth.setSizePolicy(sizePolicy1)
        self.lineTransWidth.setMaximumSize(QSize(80, 16777215))
        self.lineTransWidth.setFocusPolicy(Qt.ClickFocus)
        self.lineTransWidth.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.lineTransWidth, 0, 2, 1, 1)

        self.label_18 = QLabel(self.tabCalibration)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_18, 3, 1, 1, 1)

        self.label_20 = QLabel(self.tabCalibration)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_20, 4, 1, 1, 1)

        self.label_22 = QLabel(self.tabCalibration)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_22, 1, 0, 2, 5)


        self.gridLayout_7.addLayout(self.gridLayout_12, 2, 4, 1, 2)

        self.tabWidget.addTab(self.tabCalibration, "")

        self.gridLayout_13.addWidget(self.tabWidget, 1, 0, 1, 6)

        QWidget.setTabOrder(self.pushFilterApply, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.checkCameraConnected)
        QWidget.setTabOrder(self.checkCameraConnected, self.checkUseControlServer)
        QWidget.setTabOrder(self.checkUseControlServer, self.lineControllerIP1)
        QWidget.setTabOrder(self.lineControllerIP1, self.lineControllerIP2)
        QWidget.setTabOrder(self.lineControllerIP2, self.lineControllerIP3)
        QWidget.setTabOrder(self.lineControllerIP3, self.lineControllerIP4)
        QWidget.setTabOrder(self.lineControllerIP4, self.lineControllerIP5)
        QWidget.setTabOrder(self.lineControllerIP5, self.checkControllerConnected)
        QWidget.setTabOrder(self.checkControllerConnected, self.textConnectionLog)
        QWidget.setTabOrder(self.textConnectionLog, self.sliderGain)
        QWidget.setTabOrder(self.sliderGain, self.sliderExposureTime)
        QWidget.setTabOrder(self.sliderExposureTime, self.sliderX0)
        QWidget.setTabOrder(self.sliderX0, self.sliderY0)
        QWidget.setTabOrder(self.sliderY0, self.sliderWidth)
        QWidget.setTabOrder(self.sliderWidth, self.sliderHeight)
        QWidget.setTabOrder(self.sliderHeight, self.comboFilter)
        QWidget.setTabOrder(self.comboFilter, self.listParameters)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Setup", None))
        self.pushSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.checkSaveLast.setText(QCoreApplication.translate("Dialog", u"This settings will be used later.", None))
        self.pushOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pushLoad.setText(QCoreApplication.translate("Dialog", u"Load", None))
        self.pushCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.groupCameraConnection.setTitle(QCoreApplication.translate("Dialog", u"Camera", None))
        self.labelSDKType.setText(QCoreApplication.translate("Dialog", u"SDK Type", None))
        self.comboSDKType.setItemText(0, QCoreApplication.translate("Dialog", u"OpenCV", None))
        self.comboSDKType.setItemText(1, QCoreApplication.translate("Dialog", u"Vimba (Allied Vision)", None))
        self.comboSDKType.setItemText(2, QCoreApplication.translate("Dialog", u"Pylon (Basler)", None))

        self.labelIP.setText(QCoreApplication.translate("Dialog", u"URL or IP", None))
        self.pushConnectCamera.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.checkCameraConnected.setText(QCoreApplication.translate("Dialog", u"Connected", None))
        self.groupControllerConnection.setTitle(QCoreApplication.translate("Dialog", u"Controller", None))
        self.checkUseControlServer.setText(QCoreApplication.translate("Dialog", u"Use Network Camera Control Server", None))
        self.labelControllerIP1.setText(QCoreApplication.translate("Dialog", u"IP Address", None))
        self.labelControllerIP2.setText(QCoreApplication.translate("Dialog", u".", None))
        self.labelControllerIP3.setText(QCoreApplication.translate("Dialog", u".", None))
        self.labelControllerIP4.setText(QCoreApplication.translate("Dialog", u".", None))
        self.labelControllerIP5.setText(QCoreApplication.translate("Dialog", u":", None))
        self.pushConnectController.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.checkControllerConnected.setText(QCoreApplication.translate("Dialog", u"Connected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConnection), QCoreApplication.translate("Dialog", u"Connection", None))
        self.labelImage.setText("")
        self.groupCamera.setTitle(QCoreApplication.translate("Dialog", u"Camera", None))
        self.lineGain.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.lineExposureTime.setText(QCoreApplication.translate("Dialog", u"500", None))
        self.labelExposureTimeRange.setText(QCoreApplication.translate("Dialog", u"(1- 1000)", None))
        self.labelGainRange.setText(QCoreApplication.translate("Dialog", u"(0 - 200)", None))
        self.labelGain.setText(QCoreApplication.translate("Dialog", u"Gain (%)", None))
        self.labelExposureTime.setText(QCoreApplication.translate("Dialog", u"Exposure Time (ms)", None))
        self.groupROI.setTitle(QCoreApplication.translate("Dialog", u"Region of Interest", None))
        self.labelX0.setText(QCoreApplication.translate("Dialog", u"  x (%)", None))
        self.labelY0.setText(QCoreApplication.translate("Dialog", u"  y (%)", None))
        self.labelWidth.setText(QCoreApplication.translate("Dialog", u"  width (%)", None))
        self.labelSize.setText(QCoreApplication.translate("Dialog", u"ROI Size", None))
        self.labelSP.setText(QCoreApplication.translate("Dialog", u"Start Point", None))
        self.labelHeight.setText(QCoreApplication.translate("Dialog", u"  height (%)", None))
        self.lineWidth.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.labelSizePixel.setText(QCoreApplication.translate("Dialog", u"(0,0) pixel", None))
        self.lineX0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lineY0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lineHeight.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.labelSPPixel.setText(QCoreApplication.translate("Dialog", u"(0,0) pixel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Drag: draw ROI range, Left double click: set ROI, Right double click: reset ROI", None))
        self.groupFilter.setTitle(QCoreApplication.translate("Dialog", u"Filter", None))
        self.pushFilterApply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Dialog", u"No Filter", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Dialog", u"Background Substraction", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("Dialog", u"Gaussian", None))
        self.comboFilter.setItemText(4, QCoreApplication.translate("Dialog", u"Median", None))
        self.comboFilter.setItemText(5, QCoreApplication.translate("Dialog", u"Bilateral", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPhoto), QCoreApplication.translate("Dialog", u"Photo", None))
        self.pushOpenImage.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.pushConvert.setText(QCoreApplication.translate("Dialog", u"Convert", None))
        self.labelOrigin.setText("")
        self.labelTrans.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Ctrl + arrow keys: Move last point", None))
        self.labelExplain.setText(QCoreApplication.translate("Dialog", u"Left click: Add point,  Right click: Erase point", None))
        self.labelPosition.setText(QCoreApplication.translate("Dialog", u"Position:", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Transformed image size:", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"mm/pixel", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"mm/pixel", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Horizontal:", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Vertical:", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Pixel to actual length of original image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalibration), QCoreApplication.translate("Dialog", u"Calibration", None))
    # retranslateUi

