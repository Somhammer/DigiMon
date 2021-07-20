# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 769)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/ncc.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.mainFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupCamera = QGroupBox(self.mainFrame)
        self.groupCamera.setObjectName(u"groupCamera")
        font = QFont()
        font.setFamilies([u"Nimbus Sans [urw]"])
        font.setPointSize(14)
        font.setBold(True)
        self.groupCamera.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupCamera)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelFrameRate = QLabel(self.groupCamera)
        self.labelFrameRate.setObjectName(u"labelFrameRate")
        font1 = QFont()
        font1.setFamilies([u"Nimbus Sans [urw]"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.labelFrameRate.setFont(font1)

        self.gridLayout_3.addWidget(self.labelFrameRate, 4, 0, 1, 1)

        self.labelFrameRange = QLabel(self.groupCamera)
        self.labelFrameRange.setObjectName(u"labelFrameRange")
        self.labelFrameRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelFrameRange, 4, 4, 1, 1)

        self.sliderExposureTime = QSlider(self.groupCamera)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy1)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderExposureTime, 5, 2, 1, 2)

        self.lineGain = QLineEdit(self.groupCamera)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineGain.sizePolicy().hasHeightForWidth())
        self.lineGain.setSizePolicy(sizePolicy2)
        self.lineGain.setMaximumSize(QSize(50, 16777215))
        self.lineGain.setFont(font1)
        self.lineGain.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineGain, 3, 1, 1, 1)

        self.lineFrameRate = QLineEdit(self.groupCamera)
        self.lineFrameRate.setObjectName(u"lineFrameRate")
        sizePolicy1.setHeightForWidth(self.lineFrameRate.sizePolicy().hasHeightForWidth())
        self.lineFrameRate.setSizePolicy(sizePolicy1)
        self.lineFrameRate.setMaximumSize(QSize(50, 16777215))
        self.lineFrameRate.setFont(font1)
        self.lineFrameRate.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineFrameRate, 4, 1, 1, 1)

        self.pushConnect = QPushButton(self.groupCamera)
        self.pushConnect.setObjectName(u"pushConnect")
        sizePolicy1.setHeightForWidth(self.pushConnect.sizePolicy().hasHeightForWidth())
        self.pushConnect.setSizePolicy(sizePolicy1)
        self.pushConnect.setMaximumSize(QSize(80, 16777215))
        self.pushConnect.setFont(font1)

        self.gridLayout_3.addWidget(self.pushConnect, 0, 4, 1, 1)

        self.labelIP = QLabel(self.groupCamera)
        self.labelIP.setObjectName(u"labelIP")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelIP.sizePolicy().hasHeightForWidth())
        self.labelIP.setSizePolicy(sizePolicy3)
        self.labelIP.setFont(font1)

        self.gridLayout_3.addWidget(self.labelIP, 1, 0, 1, 1)

        self.labelGainRange = QLabel(self.groupCamera)
        self.labelGainRange.setObjectName(u"labelGainRange")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelGainRange.sizePolicy().hasHeightForWidth())
        self.labelGainRange.setSizePolicy(sizePolicy4)
        self.labelGainRange.setMaximumSize(QSize(100, 16777215))
        self.labelGainRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelGainRange, 3, 4, 1, 1)

        self.silderGain = QSlider(self.groupCamera)
        self.silderGain.setObjectName(u"silderGain")
        sizePolicy1.setHeightForWidth(self.silderGain.sizePolicy().hasHeightForWidth())
        self.silderGain.setSizePolicy(sizePolicy1)
        self.silderGain.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.silderGain, 3, 2, 1, 2)

        self.sliderFrameRate = QSlider(self.groupCamera)
        self.sliderFrameRate.setObjectName(u"sliderFrameRate")
        sizePolicy1.setHeightForWidth(self.sliderFrameRate.sizePolicy().hasHeightForWidth())
        self.sliderFrameRate.setSizePolicy(sizePolicy1)
        self.sliderFrameRate.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderFrameRate, 4, 2, 1, 2)

        self.labelGain = QLabel(self.groupCamera)
        self.labelGain.setObjectName(u"labelGain")
        self.labelGain.setFont(font1)

        self.gridLayout_3.addWidget(self.labelGain, 3, 0, 1, 1)

        self.labelInterest = QLabel(self.groupCamera)
        self.labelInterest.setObjectName(u"labelInterest")
        font2 = QFont()
        font2.setFamilies([u"Nimbus Sans [urw]"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.labelInterest.setFont(font2)

        self.gridLayout_3.addWidget(self.labelInterest, 6, 0, 1, 1)

        self.labelConfig = QLabel(self.groupCamera)
        self.labelConfig.setObjectName(u"labelConfig")
        self.labelConfig.setFont(font2)

        self.gridLayout_3.addWidget(self.labelConfig, 2, 0, 1, 5)

        self.labelExposureTimeRange = QLabel(self.groupCamera)
        self.labelExposureTimeRange.setObjectName(u"labelExposureTimeRange")
        self.labelExposureTimeRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelExposureTimeRange, 5, 4, 1, 1)

        self.gridInterest = QGridLayout()
        self.gridInterest.setObjectName(u"gridInterest")
        self.lineDX = QLineEdit(self.groupCamera)
        self.lineDX.setObjectName(u"lineDX")
        sizePolicy2.setHeightForWidth(self.lineDX.sizePolicy().hasHeightForWidth())
        self.lineDX.setSizePolicy(sizePolicy2)
        self.lineDX.setMaximumSize(QSize(30, 16777215))
        self.lineDX.setFont(font1)
        self.lineDX.setReadOnly(True)

        self.gridInterest.addWidget(self.lineDX, 0, 4, 1, 1)

        self.lineDY = QLineEdit(self.groupCamera)
        self.lineDY.setObjectName(u"lineDY")
        sizePolicy2.setHeightForWidth(self.lineDY.sizePolicy().hasHeightForWidth())
        self.lineDY.setSizePolicy(sizePolicy2)
        self.lineDY.setMaximumSize(QSize(30, 16777215))
        self.lineDY.setFont(font1)
        self.lineDY.setReadOnly(True)

        self.gridInterest.addWidget(self.lineDY, 1, 4, 1, 1)

        self.lineY0 = QLineEdit(self.groupCamera)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy2.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy2)
        self.lineY0.setMaximumSize(QSize(30, 16777215))
        self.lineY0.setFont(font1)
        self.lineY0.setReadOnly(True)

        self.gridInterest.addWidget(self.lineY0, 1, 1, 1, 1)

        self.silderY0 = QSlider(self.groupCamera)
        self.silderY0.setObjectName(u"silderY0")
        sizePolicy1.setHeightForWidth(self.silderY0.sizePolicy().hasHeightForWidth())
        self.silderY0.setSizePolicy(sizePolicy1)
        self.silderY0.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.silderY0, 1, 2, 1, 1)

        self.labelDY = QLabel(self.groupCamera)
        self.labelDY.setObjectName(u"labelDY")
        self.labelDY.setMaximumSize(QSize(20, 16777215))
        self.labelDY.setFont(font1)

        self.gridInterest.addWidget(self.labelDY, 1, 3, 1, 1)

        self.silderX0 = QSlider(self.groupCamera)
        self.silderX0.setObjectName(u"silderX0")
        sizePolicy1.setHeightForWidth(self.silderX0.sizePolicy().hasHeightForWidth())
        self.silderX0.setSizePolicy(sizePolicy1)
        self.silderX0.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.silderX0, 0, 2, 1, 1)

        self.labelY0 = QLabel(self.groupCamera)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setFont(font1)

        self.gridInterest.addWidget(self.labelY0, 1, 0, 1, 1)

        self.lineX0 = QLineEdit(self.groupCamera)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy2.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy2)
        self.lineX0.setMaximumSize(QSize(30, 16777215))
        self.lineX0.setFont(font1)
        self.lineX0.setReadOnly(True)

        self.gridInterest.addWidget(self.lineX0, 0, 1, 1, 1)

        self.labelX0 = QLabel(self.groupCamera)
        self.labelX0.setObjectName(u"labelX0")
        self.labelX0.setMaximumSize(QSize(20, 16777215))
        self.labelX0.setFont(font1)

        self.gridInterest.addWidget(self.labelX0, 0, 0, 1, 1)

        self.labelDX = QLabel(self.groupCamera)
        self.labelDX.setObjectName(u"labelDX")
        self.labelDX.setMaximumSize(QSize(20, 16777215))
        self.labelDX.setFont(font1)

        self.gridInterest.addWidget(self.labelDX, 0, 3, 1, 1)

        self.silderDX = QSlider(self.groupCamera)
        self.silderDX.setObjectName(u"silderDX")
        sizePolicy1.setHeightForWidth(self.silderDX.sizePolicy().hasHeightForWidth())
        self.silderDX.setSizePolicy(sizePolicy1)
        self.silderDX.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.silderDX, 0, 5, 1, 1)

        self.silderDY = QSlider(self.groupCamera)
        self.silderDY.setObjectName(u"silderDY")
        sizePolicy1.setHeightForWidth(self.silderDY.sizePolicy().hasHeightForWidth())
        self.silderDY.setSizePolicy(sizePolicy1)
        self.silderDY.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.silderDY, 1, 5, 1, 1)


        self.gridLayout_3.addLayout(self.gridInterest, 8, 0, 1, 5)

        self.lineName = QLineEdit(self.groupCamera)
        self.lineName.setObjectName(u"lineName")
        sizePolicy1.setHeightForWidth(self.lineName.sizePolicy().hasHeightForWidth())
        self.lineName.setSizePolicy(sizePolicy1)
        self.lineName.setFont(font1)
        self.lineName.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineName, 0, 1, 1, 3)

        self.labelName = QLabel(self.groupCamera)
        self.labelName.setObjectName(u"labelName")
        sizePolicy3.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy3)
        self.labelName.setFont(font1)

        self.gridLayout_3.addWidget(self.labelName, 0, 0, 1, 1)

        self.lineExposureTime = QLineEdit(self.groupCamera)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        sizePolicy2.setHeightForWidth(self.lineExposureTime.sizePolicy().hasHeightForWidth())
        self.lineExposureTime.setSizePolicy(sizePolicy2)
        self.lineExposureTime.setMaximumSize(QSize(50, 16777215))
        self.lineExposureTime.setFont(font1)
        self.lineExposureTime.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineExposureTime, 5, 1, 1, 1)

        self.labelExposureTime = QLabel(self.groupCamera)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        self.labelExposureTime.setFont(font1)

        self.gridLayout_3.addWidget(self.labelExposureTime, 5, 0, 1, 1)

        self.gridRotation = QGridLayout()
        self.gridRotation.setObjectName(u"gridRotation")
        self.pushRotateRight = QPushButton(self.groupCamera)
        self.pushRotateRight.setObjectName(u"pushRotateRight")
        self.pushRotateRight.setMaximumSize(QSize(30, 16777215))
        self.pushRotateRight.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"icons/right_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateRight.setIcon(icon1)
        self.pushRotateRight.setIconSize(QSize(20, 20))
        self.pushRotateRight.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateRight, 0, 2, 1, 1)

        self.pushFilpRightLeft = QPushButton(self.groupCamera)
        self.pushFilpRightLeft.setObjectName(u"pushFilpRightLeft")
        icon2 = QIcon()
        icon2.addFile(u"icons/vertical_flip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushFilpRightLeft.setIcon(icon2)
        self.pushFilpRightLeft.setIconSize(QSize(20, 20))
        self.pushFilpRightLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushFilpRightLeft, 0, 3, 1, 1)

        self.pushFlipUpDown = QPushButton(self.groupCamera)
        self.pushFlipUpDown.setObjectName(u"pushFlipUpDown")
        self.pushFlipUpDown.setMaximumSize(QSize(30, 16777215))
        self.pushFlipUpDown.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icons/horizontal_flip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushFlipUpDown.setIcon(icon3)
        self.pushFlipUpDown.setIconSize(QSize(20, 20))
        self.pushFlipUpDown.setFlat(False)

        self.gridRotation.addWidget(self.pushFlipUpDown, 0, 4, 1, 1)

        self.pushRotateLeft = QPushButton(self.groupCamera)
        self.pushRotateLeft.setObjectName(u"pushRotateLeft")
        icon4 = QIcon()
        icon4.addFile(u"icons/left_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateLeft.setIcon(icon4)
        self.pushRotateLeft.setIconSize(QSize(20, 20))
        self.pushRotateLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateLeft, 0, 1, 1, 1)

        self.labelRotation = QLabel(self.groupCamera)
        self.labelRotation.setObjectName(u"labelRotation")
        self.labelRotation.setFont(font2)

        self.gridRotation.addWidget(self.labelRotation, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridRotation, 9, 0, 1, 2)

        self.lineIP = QLineEdit(self.groupCamera)
        self.lineIP.setObjectName(u"lineIP")
        sizePolicy1.setHeightForWidth(self.lineIP.sizePolicy().hasHeightForWidth())
        self.lineIP.setSizePolicy(sizePolicy1)
        self.lineIP.setFont(font1)
        self.lineIP.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineIP, 1, 1, 1, 4)


        self.gridLayout_2.addWidget(self.groupCamera, 1, 1, 2, 1)

        self.textLog = QPlainTextEdit(self.mainFrame)
        self.textLog.setObjectName(u"textLog")
        sizePolicy4.setHeightForWidth(self.textLog.sizePolicy().hasHeightForWidth())
        self.textLog.setSizePolicy(sizePolicy4)
        self.textLog.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textLog, 5, 1, 1, 1)

        self.gridCapture = QGridLayout()
        self.gridCapture.setObjectName(u"gridCapture")
        self.pushStop = QPushButton(self.mainFrame)
        self.pushStop.setObjectName(u"pushStop")

        self.gridCapture.addWidget(self.pushStop, 0, 1, 1, 1)

        self.pushCapture = QPushButton(self.mainFrame)
        self.pushCapture.setObjectName(u"pushCapture")

        self.gridCapture.addWidget(self.pushCapture, 0, 0, 1, 1)

        self.lcdTimer = QLCDNumber(self.mainFrame)
        self.lcdTimer.setObjectName(u"lcdTimer")
        self.lcdTimer.setFrameShape(QFrame.StyledPanel)
        self.lcdTimer.setFrameShadow(QFrame.Plain)
        self.lcdTimer.setSmallDecimalPoint(False)
        self.lcdTimer.setDigitCount(5)
        self.lcdTimer.setMode(QLCDNumber.Dec)
        self.lcdTimer.setSegmentStyle(QLCDNumber.Flat)
        self.lcdTimer.setProperty("value", 0.000000000000000)
        self.lcdTimer.setProperty("intValue", 0)

        self.gridCapture.addWidget(self.lcdTimer, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridCapture, 0, 1, 1, 1)

        self.groupEmittance = QGroupBox(self.mainFrame)
        self.groupEmittance.setObjectName(u"groupEmittance")
        self.groupEmittance.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupEmittance)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelXemittance = QLabel(self.groupEmittance)
        self.labelXemittance.setObjectName(u"labelXemittance")
        self.labelXemittance.setMaximumSize(QSize(10, 16777215))
        self.labelXemittance.setFont(font1)

        self.gridLayout_4.addWidget(self.labelXemittance, 0, 0, 1, 1)

        self.labelYemittanceUnit = QLabel(self.groupEmittance)
        self.labelYemittanceUnit.setObjectName(u"labelYemittanceUnit")
        self.labelYemittanceUnit.setMaximumSize(QSize(60, 16777215))
        self.labelYemittanceUnit.setFont(font1)

        self.gridLayout_4.addWidget(self.labelYemittanceUnit, 1, 2, 1, 1)

        self.labelYemittance = QLabel(self.groupEmittance)
        self.labelYemittance.setObjectName(u"labelYemittance")
        self.labelYemittance.setMaximumSize(QSize(10, 16777215))
        self.labelYemittance.setFont(font1)

        self.gridLayout_4.addWidget(self.labelYemittance, 1, 0, 1, 1)

        self.lineXemittance = QLineEdit(self.groupEmittance)
        self.lineXemittance.setObjectName(u"lineXemittance")
        sizePolicy1.setHeightForWidth(self.lineXemittance.sizePolicy().hasHeightForWidth())
        self.lineXemittance.setSizePolicy(sizePolicy1)
        self.lineXemittance.setMaximumSize(QSize(100, 16777215))
        self.lineXemittance.setFont(font1)
        self.lineXemittance.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineXemittance, 0, 1, 1, 1)

        self.lineYemittance = QLineEdit(self.groupEmittance)
        self.lineYemittance.setObjectName(u"lineYemittance")
        sizePolicy1.setHeightForWidth(self.lineYemittance.sizePolicy().hasHeightForWidth())
        self.lineYemittance.setSizePolicy(sizePolicy1)
        self.lineYemittance.setMaximumSize(QSize(100, 16777215))
        self.lineYemittance.setFont(font1)
        self.lineYemittance.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineYemittance, 1, 1, 1, 1)

        self.labelXemittanceUnit = QLabel(self.groupEmittance)
        self.labelXemittanceUnit.setObjectName(u"labelXemittanceUnit")
        self.labelXemittanceUnit.setMaximumSize(QSize(60, 16777215))
        self.labelXemittanceUnit.setFont(font1)

        self.gridLayout_4.addWidget(self.labelXemittanceUnit, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.groupEmittance)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton, 2, 0, 1, 3)

        self.twissFrame = QFrame(self.groupEmittance)
        self.twissFrame.setObjectName(u"twissFrame")
        self.twissFrame.setFrameShape(QFrame.StyledPanel)
        self.twissFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.twissFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineBeta = QLineEdit(self.twissFrame)
        self.lineBeta.setObjectName(u"lineBeta")
        sizePolicy1.setHeightForWidth(self.lineBeta.sizePolicy().hasHeightForWidth())
        self.lineBeta.setSizePolicy(sizePolicy1)
        self.lineBeta.setFont(font1)
        self.lineBeta.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineBeta, 1, 1, 1, 1)

        self.lineGamma = QLineEdit(self.twissFrame)
        self.lineGamma.setObjectName(u"lineGamma")
        sizePolicy1.setHeightForWidth(self.lineGamma.sizePolicy().hasHeightForWidth())
        self.lineGamma.setSizePolicy(sizePolicy1)
        self.lineGamma.setFont(font1)
        self.lineGamma.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineGamma, 2, 1, 1, 1)

        self.labelGamma = QLabel(self.twissFrame)
        self.labelGamma.setObjectName(u"labelGamma")
        self.labelGamma.setMaximumSize(QSize(45, 16777215))
        self.labelGamma.setFont(font1)

        self.gridLayout_5.addWidget(self.labelGamma, 2, 0, 1, 1)

        self.labelAlpha = QLabel(self.twissFrame)
        self.labelAlpha.setObjectName(u"labelAlpha")
        self.labelAlpha.setMaximumSize(QSize(45, 16777215))
        self.labelAlpha.setFont(font1)

        self.gridLayout_5.addWidget(self.labelAlpha, 0, 0, 1, 1)

        self.labelBeta = QLabel(self.twissFrame)
        self.labelBeta.setObjectName(u"labelBeta")
        self.labelBeta.setMaximumSize(QSize(45, 16777215))
        self.labelBeta.setFont(font1)

        self.gridLayout_5.addWidget(self.labelBeta, 1, 0, 1, 1)

        self.lineAlpha = QLineEdit(self.twissFrame)
        self.lineAlpha.setObjectName(u"lineAlpha")
        sizePolicy1.setHeightForWidth(self.lineAlpha.sizePolicy().hasHeightForWidth())
        self.lineAlpha.setSizePolicy(sizePolicy1)
        self.lineAlpha.setFont(font1)
        self.lineAlpha.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineAlpha, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.twissFrame, 0, 3, 3, 1)


        self.gridLayout_2.addWidget(self.groupEmittance, 3, 1, 2, 1)

        self.gridViewer = QGridLayout()
        self.gridViewer.setObjectName(u"gridViewer")
        self.wIntensity = QFrame(self.mainFrame)
        self.wIntensity.setObjectName(u"wIntensity")
        self.wIntensity.setFrameShape(QFrame.Panel)

        self.gridViewer.addWidget(self.wIntensity, 2, 0, 1, 2)

        self.wProfile = QFrame(self.mainFrame)
        self.wProfile.setObjectName(u"wProfile")
        self.wProfile.setFrameShape(QFrame.Panel)
        self.wProfile.setFrameShadow(QFrame.Plain)

        self.gridViewer.addWidget(self.wProfile, 3, 0, 2, 1)

        self.wBeamSize = QFrame(self.mainFrame)
        self.wBeamSize.setObjectName(u"wBeamSize")
        self.wBeamSize.setFrameShape(QFrame.Panel)

        self.gridViewer.addWidget(self.wBeamSize, 3, 1, 2, 1)

        self.wViewer = QFrame(self.mainFrame)
        self.wViewer.setObjectName(u"wViewer")
        self.wViewer.setFrameShape(QFrame.Panel)

        self.gridViewer.addWidget(self.wViewer, 0, 0, 2, 2)


        self.gridLayout_2.addLayout(self.gridViewer, 0, 0, 6, 1)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        font3 = QFont()
        font3.setBold(True)
        self.toolBar.setFont(font3)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.pushFlipUpDown.setDefault(False)
        self.pushRotateLeft.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DigiMon", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupCamera.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.labelFrameRate.setText(QCoreApplication.translate("MainWindow", u"Frame Rate (FPS)", None))
        self.labelFrameRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 60)", None))
        self.pushConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labelIP.setText(QCoreApplication.translate("MainWindow", u"IP Addr.", None))
        self.labelGainRange.setText(QCoreApplication.translate("MainWindow", u"(0 - 100)", None))
        self.labelGain.setText(QCoreApplication.translate("MainWindow", u"Gain (%)", None))
        self.labelInterest.setText(QCoreApplication.translate("MainWindow", u"Region of Interest", None))
        self.labelConfig.setText(QCoreApplication.translate("MainWindow", u"Basic Config", None))
        self.labelExposureTimeRange.setText(QCoreApplication.translate("MainWindow", u"(0 - 100)", None))
        self.labelDY.setText(QCoreApplication.translate("MainWindow", u"dy", None))
        self.labelY0.setText(QCoreApplication.translate("MainWindow", u"y0", None))
        self.labelX0.setText(QCoreApplication.translate("MainWindow", u"x0", None))
        self.labelDX.setText(QCoreApplication.translate("MainWindow", u"dx", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.labelExposureTime.setText(QCoreApplication.translate("MainWindow", u"Exposure Time (s)", None))
        self.pushRotateRight.setText("")
        self.pushFilpRightLeft.setText("")
        self.pushFlipUpDown.setText("")
        self.pushRotateLeft.setText("")
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.pushStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.groupEmittance.setTitle(QCoreApplication.translate("MainWindow", u"Emittance", None))
        self.labelXemittance.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.labelYemittanceUnit.setText(QCoreApplication.translate("MainWindow", u"mrad mm", None))
        self.labelYemittance.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.labelXemittanceUnit.setText(QCoreApplication.translate("MainWindow", u"mrad mm", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.labelGamma.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.labelAlpha.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.labelBeta.setText(QCoreApplication.translate("MainWindow", u"Beta", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

