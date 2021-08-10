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
        MainWindow.resize(1397, 1052)
        icon = QIcon()
        icon.addFile(u"../icons/ncc.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.mainFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameControl = QFrame(self.mainFrame)
        self.frameControl.setObjectName(u"frameControl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameControl.sizePolicy().hasHeightForWidth())
        self.frameControl.setSizePolicy(sizePolicy)
        self.frameControl.setFrameShape(QFrame.NoFrame)
        self.frameControl.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameControl)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupEmittance = QGroupBox(self.frameControl)
        self.groupEmittance.setObjectName(u"groupEmittance")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupEmittance.setFont(font)
        self.gridEmittance = QGridLayout(self.groupEmittance)
        self.gridEmittance.setObjectName(u"gridEmittance")
        self.labelYemittance = QLabel(self.groupEmittance)
        self.labelYemittance.setObjectName(u"labelYemittance")
        self.labelYemittance.setMaximumSize(QSize(10, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.labelYemittance.setFont(font1)

        self.gridEmittance.addWidget(self.labelYemittance, 1, 0, 1, 1)

        self.labelXemittanceUnit = QLabel(self.groupEmittance)
        self.labelXemittanceUnit.setObjectName(u"labelXemittanceUnit")
        self.labelXemittanceUnit.setMaximumSize(QSize(70, 16777215))
        self.labelXemittanceUnit.setFont(font1)

        self.gridEmittance.addWidget(self.labelXemittanceUnit, 0, 2, 1, 1)

        self.pushCalculate = QPushButton(self.groupEmittance)
        self.pushCalculate.setObjectName(u"pushCalculate")
        self.pushCalculate.setFont(font1)

        self.gridEmittance.addWidget(self.pushCalculate, 2, 0, 1, 3)

        self.twissFrame = QFrame(self.groupEmittance)
        self.twissFrame.setObjectName(u"twissFrame")
        self.twissFrame.setFrameShape(QFrame.StyledPanel)
        self.twissFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.twissFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.twissFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_5.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(self.twissFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)

        self.lineGammaY = QLineEdit(self.twissFrame)
        self.lineGammaY.setObjectName(u"lineGammaY")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineGammaY.sizePolicy().hasHeightForWidth())
        self.lineGammaY.setSizePolicy(sizePolicy1)
        self.lineGammaY.setMaximumSize(QSize(16777210, 16777215))
        self.lineGammaY.setFont(font1)

        self.gridLayout_5.addWidget(self.lineGammaY, 3, 2, 1, 1)

        self.lineBetaX = QLineEdit(self.twissFrame)
        self.lineBetaX.setObjectName(u"lineBetaX")
        sizePolicy1.setHeightForWidth(self.lineBetaX.sizePolicy().hasHeightForWidth())
        self.lineBetaX.setSizePolicy(sizePolicy1)
        self.lineBetaX.setMaximumSize(QSize(16777210, 16777215))
        self.lineBetaX.setFont(font1)
        self.lineBetaX.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineBetaX, 2, 1, 1, 1)

        self.lineAlphaX = QLineEdit(self.twissFrame)
        self.lineAlphaX.setObjectName(u"lineAlphaX")
        sizePolicy1.setHeightForWidth(self.lineAlphaX.sizePolicy().hasHeightForWidth())
        self.lineAlphaX.setSizePolicy(sizePolicy1)
        self.lineAlphaX.setMaximumSize(QSize(16777210, 16777210))
        self.lineAlphaX.setFont(font1)
        self.lineAlphaX.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineAlphaX, 1, 1, 1, 1)

        self.labelBeta = QLabel(self.twissFrame)
        self.labelBeta.setObjectName(u"labelBeta")
        self.labelBeta.setMaximumSize(QSize(16777215, 16777215))
        self.labelBeta.setFont(font1)

        self.gridLayout_5.addWidget(self.labelBeta, 2, 0, 1, 1)

        self.lineAlphaY = QLineEdit(self.twissFrame)
        self.lineAlphaY.setObjectName(u"lineAlphaY")
        sizePolicy1.setHeightForWidth(self.lineAlphaY.sizePolicy().hasHeightForWidth())
        self.lineAlphaY.setSizePolicy(sizePolicy1)
        self.lineAlphaY.setMaximumSize(QSize(16777210, 16777215))
        self.lineAlphaY.setFont(font1)

        self.gridLayout_5.addWidget(self.lineAlphaY, 1, 2, 1, 1)

        self.labelGamma = QLabel(self.twissFrame)
        self.labelGamma.setObjectName(u"labelGamma")
        self.labelGamma.setMaximumSize(QSize(16777215, 16777215))
        self.labelGamma.setFont(font1)

        self.gridLayout_5.addWidget(self.labelGamma, 3, 0, 1, 1)

        self.lineGammaX = QLineEdit(self.twissFrame)
        self.lineGammaX.setObjectName(u"lineGammaX")
        sizePolicy1.setHeightForWidth(self.lineGammaX.sizePolicy().hasHeightForWidth())
        self.lineGammaX.setSizePolicy(sizePolicy1)
        self.lineGammaX.setMaximumSize(QSize(16777210, 16777215))
        self.lineGammaX.setFont(font1)
        self.lineGammaX.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineGammaX, 3, 1, 1, 1)

        self.labelAlpha = QLabel(self.twissFrame)
        self.labelAlpha.setObjectName(u"labelAlpha")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelAlpha.sizePolicy().hasHeightForWidth())
        self.labelAlpha.setSizePolicy(sizePolicy2)
        self.labelAlpha.setMaximumSize(QSize(16777215, 16777215))
        self.labelAlpha.setFont(font1)

        self.gridLayout_5.addWidget(self.labelAlpha, 1, 0, 1, 1)

        self.lineBetaY = QLineEdit(self.twissFrame)
        self.lineBetaY.setObjectName(u"lineBetaY")
        sizePolicy1.setHeightForWidth(self.lineBetaY.sizePolicy().hasHeightForWidth())
        self.lineBetaY.setSizePolicy(sizePolicy1)
        self.lineBetaY.setMaximumSize(QSize(16777210, 16777215))
        self.lineBetaY.setFont(font1)

        self.gridLayout_5.addWidget(self.lineBetaY, 2, 2, 1, 1)


        self.gridEmittance.addWidget(self.twissFrame, 0, 3, 3, 1)

        self.labelYemittanceUnit = QLabel(self.groupEmittance)
        self.labelYemittanceUnit.setObjectName(u"labelYemittanceUnit")
        self.labelYemittanceUnit.setMaximumSize(QSize(70, 16777215))
        self.labelYemittanceUnit.setFont(font1)

        self.gridEmittance.addWidget(self.labelYemittanceUnit, 1, 2, 1, 1)

        self.labelXemittance = QLabel(self.groupEmittance)
        self.labelXemittance.setObjectName(u"labelXemittance")
        self.labelXemittance.setMaximumSize(QSize(10, 16777215))
        self.labelXemittance.setFont(font1)

        self.gridEmittance.addWidget(self.labelXemittance, 0, 0, 1, 1)

        self.lineYemittance = QLineEdit(self.groupEmittance)
        self.lineYemittance.setObjectName(u"lineYemittance")
        sizePolicy1.setHeightForWidth(self.lineYemittance.sizePolicy().hasHeightForWidth())
        self.lineYemittance.setSizePolicy(sizePolicy1)
        self.lineYemittance.setMaximumSize(QSize(100, 16777215))
        self.lineYemittance.setFont(font1)
        self.lineYemittance.setReadOnly(True)

        self.gridEmittance.addWidget(self.lineYemittance, 1, 1, 1, 1)

        self.lineXemittance = QLineEdit(self.groupEmittance)
        self.lineXemittance.setObjectName(u"lineXemittance")
        sizePolicy1.setHeightForWidth(self.lineXemittance.sizePolicy().hasHeightForWidth())
        self.lineXemittance.setSizePolicy(sizePolicy1)
        self.lineXemittance.setMaximumSize(QSize(100, 16777215))
        self.lineXemittance.setFont(font1)
        self.lineXemittance.setReadOnly(True)

        self.gridEmittance.addWidget(self.lineXemittance, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupEmittance, 4, 0, 1, 1)

        self.groupProfile = QGroupBox(self.frameControl)
        self.groupProfile.setObjectName(u"groupProfile")
        self.groupProfile.setFont(font)
        self.gridProfile_2 = QGridLayout(self.groupProfile)
        self.gridProfile_2.setObjectName(u"gridProfile_2")
        self.pushCalibration = QPushButton(self.groupProfile)
        self.pushCalibration.setObjectName(u"pushCalibration")
        self.pushCalibration.setFont(font1)

        self.gridProfile_2.addWidget(self.pushCalibration, 0, 0, 1, 1)

        self.listProfiles = QListWidget(self.groupProfile)
        self.listProfiles.setObjectName(u"listProfiles")

        self.gridProfile_2.addWidget(self.listProfiles, 2, 0, 1, 4)

        self.pushFilter = QPushButton(self.groupProfile)
        self.pushFilter.setObjectName(u"pushFilter")
        self.pushFilter.setFont(font1)

        self.gridProfile_2.addWidget(self.pushFilter, 0, 1, 1, 1)

        self.labelSaveImages = QLabel(self.groupProfile)
        self.labelSaveImages.setObjectName(u"labelSaveImages")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.labelSaveImages.setFont(font2)

        self.gridProfile_2.addWidget(self.labelSaveImages, 0, 2, 1, 1)

        self.pushExportProfiles = QPushButton(self.groupProfile)
        self.pushExportProfiles.setObjectName(u"pushExportProfiles")
        self.pushExportProfiles.setFont(font1)

        self.gridProfile_2.addWidget(self.pushExportProfiles, 0, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupProfile, 5, 0, 1, 1)

        self.groupCamera = QGroupBox(self.frameControl)
        self.groupCamera.setObjectName(u"groupCamera")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupCamera.sizePolicy().hasHeightForWidth())
        self.groupCamera.setSizePolicy(sizePolicy3)
        self.groupCamera.setFont(font)
        self.gridCamera = QGridLayout(self.groupCamera)
        self.gridCamera.setObjectName(u"gridCamera")
        self.labelGain = QLabel(self.groupCamera)
        self.labelGain.setObjectName(u"labelGain")
        self.labelGain.setFont(font1)

        self.gridCamera.addWidget(self.labelGain, 0, 0, 1, 1)

        self.labelGainRange = QLabel(self.groupCamera)
        self.labelGainRange.setObjectName(u"labelGainRange")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelGainRange.sizePolicy().hasHeightForWidth())
        self.labelGainRange.setSizePolicy(sizePolicy4)
        self.labelGainRange.setMaximumSize(QSize(100, 16777215))
        self.labelGainRange.setFont(font1)

        self.gridCamera.addWidget(self.labelGainRange, 0, 4, 1, 1)

        self.lineGain = QLineEdit(self.groupCamera)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineGain.sizePolicy().hasHeightForWidth())
        self.lineGain.setSizePolicy(sizePolicy5)
        self.lineGain.setMaximumSize(QSize(50, 16777215))
        self.lineGain.setFont(font1)
        self.lineGain.setReadOnly(True)

        self.gridCamera.addWidget(self.lineGain, 0, 1, 1, 1)

        self.lineFrameRate = QLineEdit(self.groupCamera)
        self.lineFrameRate.setObjectName(u"lineFrameRate")
        sizePolicy1.setHeightForWidth(self.lineFrameRate.sizePolicy().hasHeightForWidth())
        self.lineFrameRate.setSizePolicy(sizePolicy1)
        self.lineFrameRate.setMaximumSize(QSize(50, 16777215))
        self.lineFrameRate.setFont(font1)
        self.lineFrameRate.setReadOnly(True)

        self.gridCamera.addWidget(self.lineFrameRate, 1, 1, 1, 1)

        self.labelFrameRange = QLabel(self.groupCamera)
        self.labelFrameRange.setObjectName(u"labelFrameRange")
        self.labelFrameRange.setFont(font1)

        self.gridCamera.addWidget(self.labelFrameRange, 1, 4, 1, 1)

        self.labelExposureTimeRange = QLabel(self.groupCamera)
        self.labelExposureTimeRange.setObjectName(u"labelExposureTimeRange")
        self.labelExposureTimeRange.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTimeRange, 2, 4, 1, 1)

        self.gridRotation = QGridLayout()
        self.gridRotation.setObjectName(u"gridRotation")
        self.pushRotateRight = QPushButton(self.groupCamera)
        self.pushRotateRight.setObjectName(u"pushRotateRight")
        self.pushRotateRight.setMaximumSize(QSize(30, 16777215))
        self.pushRotateRight.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"../icons/right_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateRight.setIcon(icon1)
        self.pushRotateRight.setIconSize(QSize(20, 20))
        self.pushRotateRight.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateRight, 0, 2, 1, 1)

        self.pushFilpRightLeft = QPushButton(self.groupCamera)
        self.pushFilpRightLeft.setObjectName(u"pushFilpRightLeft")
        self.pushFilpRightLeft.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"../icons/vertical_flip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushFilpRightLeft.setIcon(icon2)
        self.pushFilpRightLeft.setIconSize(QSize(20, 20))
        self.pushFilpRightLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushFilpRightLeft, 0, 3, 1, 1)

        self.pushFlipUpDown = QPushButton(self.groupCamera)
        self.pushFlipUpDown.setObjectName(u"pushFlipUpDown")
        self.pushFlipUpDown.setMaximumSize(QSize(30, 16777215))
        self.pushFlipUpDown.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"../icons/horizontal_flip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushFlipUpDown.setIcon(icon3)
        self.pushFlipUpDown.setIconSize(QSize(20, 20))
        self.pushFlipUpDown.setFlat(False)

        self.gridRotation.addWidget(self.pushFlipUpDown, 0, 4, 1, 1)

        self.pushRotateLeft = QPushButton(self.groupCamera)
        self.pushRotateLeft.setObjectName(u"pushRotateLeft")
        self.pushRotateLeft.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"../icons/left_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateLeft.setIcon(icon4)
        self.pushRotateLeft.setIconSize(QSize(20, 20))
        self.pushRotateLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateLeft, 0, 1, 1, 1)

        self.labelRotation = QLabel(self.groupCamera)
        self.labelRotation.setObjectName(u"labelRotation")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.labelRotation.setFont(font3)

        self.gridRotation.addWidget(self.labelRotation, 0, 0, 1, 1)


        self.gridCamera.addLayout(self.gridRotation, 7, 0, 1, 2)

        self.labelExposureTime = QLabel(self.groupCamera)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        self.labelExposureTime.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTime, 2, 0, 1, 1)

        self.sliderGain = QSlider(self.groupCamera)
        self.sliderGain.setObjectName(u"sliderGain")
        sizePolicy1.setHeightForWidth(self.sliderGain.sizePolicy().hasHeightForWidth())
        self.sliderGain.setSizePolicy(sizePolicy1)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setValue(100)
        self.sliderGain.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderGain, 0, 2, 1, 2)

        self.sliderExposureTime = QSlider(self.groupCamera)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy1.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy1)
        self.sliderExposureTime.setMinimum(1)
        self.sliderExposureTime.setMaximum(1000)
        self.sliderExposureTime.setValue(500)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderExposureTime, 2, 2, 1, 2)

        self.lineExposureTime = QLineEdit(self.groupCamera)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        sizePolicy5.setHeightForWidth(self.lineExposureTime.sizePolicy().hasHeightForWidth())
        self.lineExposureTime.setSizePolicy(sizePolicy5)
        self.lineExposureTime.setMaximumSize(QSize(50, 16777215))
        self.lineExposureTime.setFont(font1)
        self.lineExposureTime.setReadOnly(True)

        self.gridCamera.addWidget(self.lineExposureTime, 2, 1, 1, 1)

        self.gridInterest = QGridLayout()
        self.gridInterest.setObjectName(u"gridInterest")
        self.lineDX = QLineEdit(self.groupCamera)
        self.lineDX.setObjectName(u"lineDX")
        sizePolicy5.setHeightForWidth(self.lineDX.sizePolicy().hasHeightForWidth())
        self.lineDX.setSizePolicy(sizePolicy5)
        self.lineDX.setMaximumSize(QSize(30, 16777215))
        self.lineDX.setFont(font1)
        self.lineDX.setReadOnly(True)

        self.gridInterest.addWidget(self.lineDX, 0, 4, 1, 1)

        self.lineDY = QLineEdit(self.groupCamera)
        self.lineDY.setObjectName(u"lineDY")
        sizePolicy5.setHeightForWidth(self.lineDY.sizePolicy().hasHeightForWidth())
        self.lineDY.setSizePolicy(sizePolicy5)
        self.lineDY.setMaximumSize(QSize(30, 16777215))
        self.lineDY.setFont(font1)
        self.lineDY.setReadOnly(True)

        self.gridInterest.addWidget(self.lineDY, 1, 4, 1, 1)

        self.lineY0 = QLineEdit(self.groupCamera)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy5.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy5)
        self.lineY0.setMaximumSize(QSize(30, 16777215))
        self.lineY0.setFont(font1)
        self.lineY0.setReadOnly(True)

        self.gridInterest.addWidget(self.lineY0, 1, 1, 1, 1)

        self.sliderY0 = QSlider(self.groupCamera)
        self.sliderY0.setObjectName(u"sliderY0")
        sizePolicy1.setHeightForWidth(self.sliderY0.sizePolicy().hasHeightForWidth())
        self.sliderY0.setSizePolicy(sizePolicy1)
        self.sliderY0.setMaximum(100)
        self.sliderY0.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderY0, 1, 2, 1, 1)

        self.labelDY = QLabel(self.groupCamera)
        self.labelDY.setObjectName(u"labelDY")
        self.labelDY.setMaximumSize(QSize(20, 16777215))
        self.labelDY.setFont(font1)

        self.gridInterest.addWidget(self.labelDY, 1, 3, 1, 1)

        self.sliderX0 = QSlider(self.groupCamera)
        self.sliderX0.setObjectName(u"sliderX0")
        sizePolicy1.setHeightForWidth(self.sliderX0.sizePolicy().hasHeightForWidth())
        self.sliderX0.setSizePolicy(sizePolicy1)
        self.sliderX0.setMaximum(100)
        self.sliderX0.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderX0, 0, 2, 1, 1)

        self.labelY0 = QLabel(self.groupCamera)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setFont(font1)

        self.gridInterest.addWidget(self.labelY0, 1, 0, 1, 1)

        self.lineX0 = QLineEdit(self.groupCamera)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy5.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy5)
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

        self.sliderDX = QSlider(self.groupCamera)
        self.sliderDX.setObjectName(u"sliderDX")
        sizePolicy1.setHeightForWidth(self.sliderDX.sizePolicy().hasHeightForWidth())
        self.sliderDX.setSizePolicy(sizePolicy1)
        self.sliderDX.setMaximum(100)
        self.sliderDX.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderDX, 0, 5, 1, 1)

        self.sliderDY = QSlider(self.groupCamera)
        self.sliderDY.setObjectName(u"sliderDY")
        sizePolicy1.setHeightForWidth(self.sliderDY.sizePolicy().hasHeightForWidth())
        self.sliderDY.setSizePolicy(sizePolicy1)
        self.sliderDY.setMaximum(100)
        self.sliderDY.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderDY, 1, 5, 1, 1)


        self.gridCamera.addLayout(self.gridInterest, 6, 0, 1, 5)

        self.sliderFrameRate = QSlider(self.groupCamera)
        self.sliderFrameRate.setObjectName(u"sliderFrameRate")
        sizePolicy1.setHeightForWidth(self.sliderFrameRate.sizePolicy().hasHeightForWidth())
        self.sliderFrameRate.setSizePolicy(sizePolicy1)
        self.sliderFrameRate.setMinimum(1)
        self.sliderFrameRate.setMaximum(30)
        self.sliderFrameRate.setValue(30)
        self.sliderFrameRate.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderFrameRate, 1, 2, 1, 2)

        self.labelInterest = QLabel(self.groupCamera)
        self.labelInterest.setObjectName(u"labelInterest")
        self.labelInterest.setFont(font3)

        self.gridCamera.addWidget(self.labelInterest, 4, 0, 1, 1)

        self.labelFrameRate = QLabel(self.groupCamera)
        self.labelFrameRate.setObjectName(u"labelFrameRate")
        self.labelFrameRate.setFont(font1)

        self.gridCamera.addWidget(self.labelFrameRate, 1, 0, 1, 1)

        self.labelRepeat = QLabel(self.groupCamera)
        self.labelRepeat.setObjectName(u"labelRepeat")
        self.labelRepeat.setFont(font1)

        self.gridCamera.addWidget(self.labelRepeat, 3, 0, 1, 1)

        self.lineRepeat = QLineEdit(self.groupCamera)
        self.lineRepeat.setObjectName(u"lineRepeat")
        sizePolicy1.setHeightForWidth(self.lineRepeat.sizePolicy().hasHeightForWidth())
        self.lineRepeat.setSizePolicy(sizePolicy1)
        self.lineRepeat.setMaximumSize(QSize(50, 16777215))
        self.lineRepeat.setFont(font1)
        self.lineRepeat.setReadOnly(True)

        self.gridCamera.addWidget(self.lineRepeat, 3, 1, 1, 1)

        self.labelRepeatRange = QLabel(self.groupCamera)
        self.labelRepeatRange.setObjectName(u"labelRepeatRange")
        self.labelRepeatRange.setFont(font1)

        self.gridCamera.addWidget(self.labelRepeatRange, 3, 4, 1, 1)

        self.sliderRepeat = QSlider(self.groupCamera)
        self.sliderRepeat.setObjectName(u"sliderRepeat")
        sizePolicy1.setHeightForWidth(self.sliderRepeat.sizePolicy().hasHeightForWidth())
        self.sliderRepeat.setSizePolicy(sizePolicy1)
        self.sliderRepeat.setMinimum(1)
        self.sliderRepeat.setMaximum(30)
        self.sliderRepeat.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderRepeat, 3, 2, 1, 2)


        self.gridLayout_3.addWidget(self.groupCamera, 2, 0, 1, 1)

        self.groupScreen = QGroupBox(self.frameControl)
        self.groupScreen.setObjectName(u"groupScreen")
        self.groupScreen.setFont(font)
        self.gridScreenControl = QGridLayout(self.groupScreen)
        self.gridScreenControl.setObjectName(u"gridScreenControl")
        self.gridScreenControl.setContentsMargins(6, 6, 6, 6)
        self.sliderScreenSpace = QSlider(self.groupScreen)
        self.sliderScreenSpace.setObjectName(u"sliderScreenSpace")
        sizePolicy4.setHeightForWidth(self.sliderScreenSpace.sizePolicy().hasHeightForWidth())
        self.sliderScreenSpace.setSizePolicy(sizePolicy4)
        self.sliderScreenSpace.setMinimum(1)
        self.sliderScreenSpace.setMaximum(3)
        self.sliderScreenSpace.setOrientation(Qt.Horizontal)
        self.sliderScreenSpace.setTickPosition(QSlider.TicksBelow)
        self.sliderScreenSpace.setTickInterval(1)

        self.gridScreenControl.addWidget(self.sliderScreenSpace, 0, 2, 2, 1)

        self.lineScreenSpace = QLineEdit(self.groupScreen)
        self.lineScreenSpace.setObjectName(u"lineScreenSpace")
        sizePolicy1.setHeightForWidth(self.lineScreenSpace.sizePolicy().hasHeightForWidth())
        self.lineScreenSpace.setSizePolicy(sizePolicy1)
        self.lineScreenSpace.setMaximumSize(QSize(30, 16777215))
        self.lineScreenSpace.setFont(font1)
        self.lineScreenSpace.setReadOnly(True)

        self.gridScreenControl.addWidget(self.lineScreenSpace, 0, 0, 2, 1)

        self.labelScreenUnit = QLabel(self.groupScreen)
        self.labelScreenUnit.setObjectName(u"labelScreenUnit")
        self.labelScreenUnit.setMaximumSize(QSize(30, 16777215))
        self.labelScreenUnit.setFont(font1)

        self.gridScreenControl.addWidget(self.labelScreenUnit, 0, 1, 2, 1)


        self.gridLayout_3.addWidget(self.groupScreen, 3, 0, 1, 1)

        self.gridCapture = QGridLayout()
        self.gridCapture.setObjectName(u"gridCapture")
        self.pushStop = QPushButton(self.frameControl)
        self.pushStop.setObjectName(u"pushStop")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushStop.sizePolicy().hasHeightForWidth())
        self.pushStop.setSizePolicy(sizePolicy6)

        self.gridCapture.addWidget(self.pushStop, 0, 1, 1, 1)

        self.pushCapture = QPushButton(self.frameControl)
        self.pushCapture.setObjectName(u"pushCapture")
        sizePolicy6.setHeightForWidth(self.pushCapture.sizePolicy().hasHeightForWidth())
        self.pushCapture.setSizePolicy(sizePolicy6)

        self.gridCapture.addWidget(self.pushCapture, 0, 0, 1, 1)

        self.lcdTimer = QLCDNumber(self.frameControl)
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


        self.gridLayout_3.addLayout(self.gridCapture, 1, 0, 1, 1)

        self.gridConnection = QGridLayout()
        self.gridConnection.setObjectName(u"gridConnection")
        self.pushReconnect = QPushButton(self.frameControl)
        self.pushReconnect.setObjectName(u"pushReconnect")

        self.gridConnection.addWidget(self.pushReconnect, 0, 2, 1, 1)

        self.checkConnectCamera = QCheckBox(self.frameControl)
        self.checkConnectCamera.setObjectName(u"checkConnectCamera")
        sizePolicy1.setHeightForWidth(self.checkConnectCamera.sizePolicy().hasHeightForWidth())
        self.checkConnectCamera.setSizePolicy(sizePolicy1)
        self.checkConnectCamera.setFont(font1)
        self.checkConnectCamera.setCheckable(False)

        self.gridConnection.addWidget(self.checkConnectCamera, 0, 1, 1, 1)

        self.checkConnectController = QCheckBox(self.frameControl)
        self.checkConnectController.setObjectName(u"checkConnectController")
        sizePolicy1.setHeightForWidth(self.checkConnectController.sizePolicy().hasHeightForWidth())
        self.checkConnectController.setSizePolicy(sizePolicy1)
        self.checkConnectController.setFont(font1)
        self.checkConnectController.setCheckable(False)

        self.gridConnection.addWidget(self.checkConnectController, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridConnection, 0, 0, 1, 1)

        self.textLog = QTextBrowser(self.frameControl)
        self.textLog.setObjectName(u"textLog")
        sizePolicy.setHeightForWidth(self.textLog.sizePolicy().hasHeightForWidth())
        self.textLog.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.textLog, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameControl, 0, 1, 11, 1)

        self.frameViewer = QFrame(self.mainFrame)
        self.frameViewer.setObjectName(u"frameViewer")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frameViewer.sizePolicy().hasHeightForWidth())
        self.frameViewer.setSizePolicy(sizePolicy7)
        self.gridViewer = QGridLayout(self.frameViewer)
        self.gridViewer.setSpacing(3)
        self.gridViewer.setObjectName(u"gridViewer")
        self.wProfile = QFrame(self.frameViewer)
        self.wProfile.setObjectName(u"wProfile")
        sizePolicy4.setHeightForWidth(self.wProfile.sizePolicy().hasHeightForWidth())
        self.wProfile.setSizePolicy(sizePolicy4)
        self.wProfile.setMaximumSize(QSize(16777215, 16777215))
        self.wProfile.setFrameShape(QFrame.StyledPanel)
        self.wProfile.setFrameShadow(QFrame.Plain)
        self.gridProfile = QGridLayout(self.wProfile)
        self.gridProfile.setSpacing(0)
        self.gridProfile.setObjectName(u"gridProfile")
        self.gridProfile.setContentsMargins(0, 0, 0, 0)

        self.gridViewer.addWidget(self.wProfile, 2, 0, 4, 1)

        self.wViewer = QFrame(self.frameViewer)
        self.wViewer.setObjectName(u"wViewer")
        sizePolicy4.setHeightForWidth(self.wViewer.sizePolicy().hasHeightForWidth())
        self.wViewer.setSizePolicy(sizePolicy4)
        self.wViewer.setMinimumSize(QSize(576, 529))
        self.wViewer.setFrameShape(QFrame.StyledPanel)
        self.gridScreen = QGridLayout(self.wViewer)
        self.gridScreen.setSpacing(0)
        self.gridScreen.setObjectName(u"gridScreen")
        self.gridScreen.setContentsMargins(0, 0, 0, 0)
        self.labelViewer = QLabel(self.wViewer)
        self.labelViewer.setObjectName(u"labelViewer")
        sizePolicy4.setHeightForWidth(self.labelViewer.sizePolicy().hasHeightForWidth())
        self.labelViewer.setSizePolicy(sizePolicy4)

        self.gridScreen.addWidget(self.labelViewer, 0, 0, 1, 1)


        self.gridViewer.addWidget(self.wViewer, 0, 0, 2, 2)

        self.wBeamSizeX = QFrame(self.frameViewer)
        self.wBeamSizeX.setObjectName(u"wBeamSizeX")
        sizePolicy4.setHeightForWidth(self.wBeamSizeX.sizePolicy().hasHeightForWidth())
        self.wBeamSizeX.setSizePolicy(sizePolicy4)
        self.wBeamSizeX.setMaximumSize(QSize(16777215, 16777215))
        self.wBeamSizeX.setFrameShape(QFrame.StyledPanel)
        self.gridBeamSizeX = QGridLayout(self.wBeamSizeX)
        self.gridBeamSizeX.setSpacing(0)
        self.gridBeamSizeX.setObjectName(u"gridBeamSizeX")
        self.gridBeamSizeX.setContentsMargins(0, 0, 0, 0)

        self.gridViewer.addWidget(self.wBeamSizeX, 2, 1, 2, 1)

        self.wBeamSizeY = QFrame(self.frameViewer)
        self.wBeamSizeY.setObjectName(u"wBeamSizeY")
        sizePolicy4.setHeightForWidth(self.wBeamSizeY.sizePolicy().hasHeightForWidth())
        self.wBeamSizeY.setSizePolicy(sizePolicy4)
        self.wBeamSizeY.setMaximumSize(QSize(16777215, 16777215))
        self.wBeamSizeY.setFrameShape(QFrame.StyledPanel)
        self.wBeamSizeY.setFrameShadow(QFrame.Plain)
        self.gridBeamSizeY = QGridLayout(self.wBeamSizeY)
        self.gridBeamSizeY.setSpacing(0)
        self.gridBeamSizeY.setObjectName(u"gridBeamSizeY")
        self.gridBeamSizeY.setContentsMargins(0, 0, 0, 0)

        self.gridViewer.addWidget(self.wBeamSizeY, 4, 1, 2, 1)


        self.gridLayout_2.addWidget(self.frameViewer, 0, 0, 11, 1)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1397, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.groupEmittance.setTitle(QCoreApplication.translate("MainWindow", u"Emittance", None))
        self.labelYemittance.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.labelXemittanceUnit.setText(QCoreApplication.translate("MainWindow", u"mrad mm", None))
        self.pushCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.lineGammaY.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineBetaX.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineAlphaX.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelBeta.setText(QCoreApplication.translate("MainWindow", u"Beta", None))
        self.lineAlphaY.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelGamma.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.lineGammaX.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelAlpha.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.lineBetaY.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelYemittanceUnit.setText(QCoreApplication.translate("MainWindow", u"mrad mm", None))
        self.labelXemittance.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.lineYemittance.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineXemittance.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.groupProfile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushCalibration.setText(QCoreApplication.translate("MainWindow", u"Callibration", None))
        self.pushFilter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.labelSaveImages.setText("")
        self.pushExportProfiles.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.groupCamera.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.labelGain.setText(QCoreApplication.translate("MainWindow", u"Gain (%)", None))
        self.labelGainRange.setText(QCoreApplication.translate("MainWindow", u"(0 - 100)", None))
        self.lineGain.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineFrameRate.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.labelFrameRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
        self.labelExposureTimeRange.setText(QCoreApplication.translate("MainWindow", u"(1- 1000)", None))
        self.pushRotateRight.setText("")
        self.pushFilpRightLeft.setText("")
        self.pushFlipUpDown.setText("")
        self.pushRotateLeft.setText("")
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.labelExposureTime.setText(QCoreApplication.translate("MainWindow", u"Exposure Time (ms)", None))
        self.lineExposureTime.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.lineDX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineDY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineY0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelDY.setText(QCoreApplication.translate("MainWindow", u"dy", None))
        self.labelY0.setText(QCoreApplication.translate("MainWindow", u"y0", None))
        self.lineX0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelX0.setText(QCoreApplication.translate("MainWindow", u"x0", None))
        self.labelDX.setText(QCoreApplication.translate("MainWindow", u"dx", None))
        self.labelInterest.setText(QCoreApplication.translate("MainWindow", u"Region of Interest", None))
        self.labelFrameRate.setText(QCoreApplication.translate("MainWindow", u"Frame Rate (FPS)", None))
        self.labelRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.lineRepeat.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.labelRepeatRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
        self.groupScreen.setTitle(QCoreApplication.translate("MainWindow", u"Screen", None))
        self.lineScreenSpace.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.labelScreenUnit.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.pushStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushReconnect.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.checkConnectCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.checkConnectController.setText(QCoreApplication.translate("MainWindow", u"Controller", None))
        self.labelViewer.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

