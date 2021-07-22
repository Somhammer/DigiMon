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
        MainWindow.resize(1200, 880)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.mainFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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


        self.gridLayout_2.addLayout(self.gridViewer, 0, 0, 10, 1)

        self.groupCamera = QGroupBox(self.mainFrame)
        self.groupCamera.setObjectName(u"groupCamera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupCamera.sizePolicy().hasHeightForWidth())
        self.groupCamera.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupCamera.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupCamera)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelGain = QLabel(self.groupCamera)
        self.labelGain.setObjectName(u"labelGain")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.labelGain.setFont(font1)

        self.gridLayout_3.addWidget(self.labelGain, 0, 0, 1, 1)

        self.labelGainRange = QLabel(self.groupCamera)
        self.labelGainRange.setObjectName(u"labelGainRange")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelGainRange.sizePolicy().hasHeightForWidth())
        self.labelGainRange.setSizePolicy(sizePolicy2)
        self.labelGainRange.setMaximumSize(QSize(100, 16777215))
        self.labelGainRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelGainRange, 0, 4, 1, 1)

        self.lineGain = QLineEdit(self.groupCamera)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineGain.sizePolicy().hasHeightForWidth())
        self.lineGain.setSizePolicy(sizePolicy3)
        self.lineGain.setMaximumSize(QSize(50, 16777215))
        self.lineGain.setFont(font1)
        self.lineGain.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineGain, 0, 1, 1, 1)

        self.lineFrameRate = QLineEdit(self.groupCamera)
        self.lineFrameRate.setObjectName(u"lineFrameRate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineFrameRate.sizePolicy().hasHeightForWidth())
        self.lineFrameRate.setSizePolicy(sizePolicy4)
        self.lineFrameRate.setMaximumSize(QSize(50, 16777215))
        self.lineFrameRate.setFont(font1)
        self.lineFrameRate.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineFrameRate, 1, 1, 1, 1)

        self.labelFrameRange = QLabel(self.groupCamera)
        self.labelFrameRange.setObjectName(u"labelFrameRange")
        self.labelFrameRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelFrameRange, 1, 4, 1, 1)

        self.labelExposureTimeRange = QLabel(self.groupCamera)
        self.labelExposureTimeRange.setObjectName(u"labelExposureTimeRange")
        self.labelExposureTimeRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelExposureTimeRange, 2, 4, 1, 1)

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
        icon4 = QIcon()
        icon4.addFile(u"../icons/left_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateLeft.setIcon(icon4)
        self.pushRotateLeft.setIconSize(QSize(20, 20))
        self.pushRotateLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateLeft, 0, 1, 1, 1)

        self.labelRotation = QLabel(self.groupCamera)
        self.labelRotation.setObjectName(u"labelRotation")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.labelRotation.setFont(font2)

        self.gridRotation.addWidget(self.labelRotation, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridRotation, 7, 0, 1, 2)

        self.labelExposureTime = QLabel(self.groupCamera)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        self.labelExposureTime.setFont(font1)

        self.gridLayout_3.addWidget(self.labelExposureTime, 2, 0, 1, 1)

        self.sliderGain = QSlider(self.groupCamera)
        self.sliderGain.setObjectName(u"sliderGain")
        sizePolicy4.setHeightForWidth(self.sliderGain.sizePolicy().hasHeightForWidth())
        self.sliderGain.setSizePolicy(sizePolicy4)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setValue(100)
        self.sliderGain.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderGain, 0, 2, 1, 2)

        self.sliderExposureTime = QSlider(self.groupCamera)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy4.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy4)
        self.sliderExposureTime.setMinimum(1)
        self.sliderExposureTime.setMaximum(2000)
        self.sliderExposureTime.setValue(2000)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderExposureTime, 2, 2, 1, 2)

        self.lineExposureTime = QLineEdit(self.groupCamera)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        sizePolicy3.setHeightForWidth(self.lineExposureTime.sizePolicy().hasHeightForWidth())
        self.lineExposureTime.setSizePolicy(sizePolicy3)
        self.lineExposureTime.setMaximumSize(QSize(50, 16777215))
        self.lineExposureTime.setFont(font1)
        self.lineExposureTime.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineExposureTime, 2, 1, 1, 1)

        self.gridInterest = QGridLayout()
        self.gridInterest.setObjectName(u"gridInterest")
        self.lineDX = QLineEdit(self.groupCamera)
        self.lineDX.setObjectName(u"lineDX")
        sizePolicy3.setHeightForWidth(self.lineDX.sizePolicy().hasHeightForWidth())
        self.lineDX.setSizePolicy(sizePolicy3)
        self.lineDX.setMaximumSize(QSize(30, 16777215))
        self.lineDX.setFont(font1)
        self.lineDX.setReadOnly(True)

        self.gridInterest.addWidget(self.lineDX, 0, 4, 1, 1)

        self.lineDY = QLineEdit(self.groupCamera)
        self.lineDY.setObjectName(u"lineDY")
        sizePolicy3.setHeightForWidth(self.lineDY.sizePolicy().hasHeightForWidth())
        self.lineDY.setSizePolicy(sizePolicy3)
        self.lineDY.setMaximumSize(QSize(30, 16777215))
        self.lineDY.setFont(font1)
        self.lineDY.setReadOnly(True)

        self.gridInterest.addWidget(self.lineDY, 1, 4, 1, 1)

        self.lineY0 = QLineEdit(self.groupCamera)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy3.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy3)
        self.lineY0.setMaximumSize(QSize(30, 16777215))
        self.lineY0.setFont(font1)
        self.lineY0.setReadOnly(True)

        self.gridInterest.addWidget(self.lineY0, 1, 1, 1, 1)

        self.sliderY0 = QSlider(self.groupCamera)
        self.sliderY0.setObjectName(u"sliderY0")
        sizePolicy4.setHeightForWidth(self.sliderY0.sizePolicy().hasHeightForWidth())
        self.sliderY0.setSizePolicy(sizePolicy4)
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
        sizePolicy4.setHeightForWidth(self.sliderX0.sizePolicy().hasHeightForWidth())
        self.sliderX0.setSizePolicy(sizePolicy4)
        self.sliderX0.setMaximum(100)
        self.sliderX0.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderX0, 0, 2, 1, 1)

        self.labelY0 = QLabel(self.groupCamera)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setFont(font1)

        self.gridInterest.addWidget(self.labelY0, 1, 0, 1, 1)

        self.lineX0 = QLineEdit(self.groupCamera)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy3.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy3)
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
        sizePolicy4.setHeightForWidth(self.sliderDX.sizePolicy().hasHeightForWidth())
        self.sliderDX.setSizePolicy(sizePolicy4)
        self.sliderDX.setMaximum(100)
        self.sliderDX.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderDX, 0, 5, 1, 1)

        self.sliderDY = QSlider(self.groupCamera)
        self.sliderDY.setObjectName(u"sliderDY")
        sizePolicy4.setHeightForWidth(self.sliderDY.sizePolicy().hasHeightForWidth())
        self.sliderDY.setSizePolicy(sizePolicy4)
        self.sliderDY.setMaximum(100)
        self.sliderDY.setOrientation(Qt.Horizontal)

        self.gridInterest.addWidget(self.sliderDY, 1, 5, 1, 1)


        self.gridLayout_3.addLayout(self.gridInterest, 6, 0, 1, 5)

        self.sliderFrameRate = QSlider(self.groupCamera)
        self.sliderFrameRate.setObjectName(u"sliderFrameRate")
        sizePolicy4.setHeightForWidth(self.sliderFrameRate.sizePolicy().hasHeightForWidth())
        self.sliderFrameRate.setSizePolicy(sizePolicy4)
        self.sliderFrameRate.setMinimum(1)
        self.sliderFrameRate.setMaximum(60)
        self.sliderFrameRate.setValue(30)
        self.sliderFrameRate.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderFrameRate, 1, 2, 1, 2)

        self.labelInterest = QLabel(self.groupCamera)
        self.labelInterest.setObjectName(u"labelInterest")
        self.labelInterest.setFont(font2)

        self.gridLayout_3.addWidget(self.labelInterest, 4, 0, 1, 1)

        self.labelFrameRate = QLabel(self.groupCamera)
        self.labelFrameRate.setObjectName(u"labelFrameRate")
        self.labelFrameRate.setFont(font1)

        self.gridLayout_3.addWidget(self.labelFrameRate, 1, 0, 1, 1)

        self.labelRepeat = QLabel(self.groupCamera)
        self.labelRepeat.setObjectName(u"labelRepeat")
        font3 = QFont()
        font3.setFamilies([u"Nimbus Sans [urw]"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.labelRepeat.setFont(font3)

        self.gridLayout_3.addWidget(self.labelRepeat, 3, 0, 1, 1)

        self.lineRepeat = QLineEdit(self.groupCamera)
        self.lineRepeat.setObjectName(u"lineRepeat")
        sizePolicy4.setHeightForWidth(self.lineRepeat.sizePolicy().hasHeightForWidth())
        self.lineRepeat.setSizePolicy(sizePolicy4)
        self.lineRepeat.setMaximumSize(QSize(50, 16777215))
        self.lineRepeat.setFont(font3)
        self.lineRepeat.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineRepeat, 3, 1, 1, 1)

        self.labelRepeatRange = QLabel(self.groupCamera)
        self.labelRepeatRange.setObjectName(u"labelRepeatRange")
        self.labelRepeatRange.setFont(font3)

        self.gridLayout_3.addWidget(self.labelRepeatRange, 3, 4, 1, 1)

        self.sliderRepeat = QSlider(self.groupCamera)
        self.sliderRepeat.setObjectName(u"sliderRepeat")
        sizePolicy4.setHeightForWidth(self.sliderRepeat.sizePolicy().hasHeightForWidth())
        self.sliderRepeat.setSizePolicy(sizePolicy4)
        self.sliderRepeat.setMinimum(1)
        self.sliderRepeat.setMaximum(30)
        self.sliderRepeat.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderRepeat, 3, 2, 1, 2)


        self.gridLayout_2.addWidget(self.groupCamera, 4, 1, 2, 1)

        self.gridConnection = QGridLayout()
        self.gridConnection.setObjectName(u"gridConnection")
        self.checkConnectController = QCheckBox(self.mainFrame)
        self.checkConnectController.setObjectName(u"checkConnectController")
        sizePolicy4.setHeightForWidth(self.checkConnectController.sizePolicy().hasHeightForWidth())
        self.checkConnectController.setSizePolicy(sizePolicy4)
        self.checkConnectController.setFont(font1)
        self.checkConnectController.setCheckable(False)

        self.gridConnection.addWidget(self.checkConnectController, 0, 0, 1, 1)

        self.checkConnectCamera = QCheckBox(self.mainFrame)
        self.checkConnectCamera.setObjectName(u"checkConnectCamera")
        sizePolicy4.setHeightForWidth(self.checkConnectCamera.sizePolicy().hasHeightForWidth())
        self.checkConnectCamera.setSizePolicy(sizePolicy4)
        self.checkConnectCamera.setFont(font1)
        self.checkConnectCamera.setCheckable(False)

        self.gridConnection.addWidget(self.checkConnectCamera, 0, 1, 1, 1)

        self.pushReconnect = QPushButton(self.mainFrame)
        self.pushReconnect.setObjectName(u"pushReconnect")

        self.gridConnection.addWidget(self.pushReconnect, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridConnection, 1, 1, 1, 1)

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
        self.labelYemittanceUnit.setMaximumSize(QSize(70, 16777215))
        self.labelYemittanceUnit.setFont(font1)

        self.gridLayout_4.addWidget(self.labelYemittanceUnit, 1, 2, 1, 1)

        self.labelYemittance = QLabel(self.groupEmittance)
        self.labelYemittance.setObjectName(u"labelYemittance")
        self.labelYemittance.setMaximumSize(QSize(10, 16777215))
        self.labelYemittance.setFont(font1)

        self.gridLayout_4.addWidget(self.labelYemittance, 1, 0, 1, 1)

        self.lineXemittance = QLineEdit(self.groupEmittance)
        self.lineXemittance.setObjectName(u"lineXemittance")
        sizePolicy4.setHeightForWidth(self.lineXemittance.sizePolicy().hasHeightForWidth())
        self.lineXemittance.setSizePolicy(sizePolicy4)
        self.lineXemittance.setMaximumSize(QSize(100, 16777215))
        self.lineXemittance.setFont(font1)
        self.lineXemittance.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineXemittance, 0, 1, 1, 1)

        self.lineYemittance = QLineEdit(self.groupEmittance)
        self.lineYemittance.setObjectName(u"lineYemittance")
        sizePolicy4.setHeightForWidth(self.lineYemittance.sizePolicy().hasHeightForWidth())
        self.lineYemittance.setSizePolicy(sizePolicy4)
        self.lineYemittance.setMaximumSize(QSize(100, 16777215))
        self.lineYemittance.setFont(font1)
        self.lineYemittance.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineYemittance, 1, 1, 1, 1)

        self.labelXemittanceUnit = QLabel(self.groupEmittance)
        self.labelXemittanceUnit.setObjectName(u"labelXemittanceUnit")
        self.labelXemittanceUnit.setMaximumSize(QSize(70, 16777215))
        self.labelXemittanceUnit.setFont(font1)

        self.gridLayout_4.addWidget(self.labelXemittanceUnit, 0, 2, 1, 1)

        self.pushFit = QPushButton(self.groupEmittance)
        self.pushFit.setObjectName(u"pushFit")
        self.pushFit.setFont(font1)

        self.gridLayout_4.addWidget(self.pushFit, 2, 0, 1, 3)

        self.twissFrame = QFrame(self.groupEmittance)
        self.twissFrame.setObjectName(u"twissFrame")
        self.twissFrame.setFrameShape(QFrame.StyledPanel)
        self.twissFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.twissFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineBeta = QLineEdit(self.twissFrame)
        self.lineBeta.setObjectName(u"lineBeta")
        sizePolicy4.setHeightForWidth(self.lineBeta.sizePolicy().hasHeightForWidth())
        self.lineBeta.setSizePolicy(sizePolicy4)
        self.lineBeta.setFont(font1)
        self.lineBeta.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineBeta, 1, 1, 1, 1)

        self.lineGamma = QLineEdit(self.twissFrame)
        self.lineGamma.setObjectName(u"lineGamma")
        sizePolicy4.setHeightForWidth(self.lineGamma.sizePolicy().hasHeightForWidth())
        self.lineGamma.setSizePolicy(sizePolicy4)
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
        sizePolicy4.setHeightForWidth(self.lineAlpha.sizePolicy().hasHeightForWidth())
        self.lineAlpha.setSizePolicy(sizePolicy4)
        self.lineAlpha.setFont(font1)
        self.lineAlpha.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineAlpha, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.twissFrame, 0, 3, 3, 1)


        self.gridLayout_2.addWidget(self.groupEmittance, 7, 1, 2, 1)

        self.gridCapture = QGridLayout()
        self.gridCapture.setObjectName(u"gridCapture")
        self.pushStop = QPushButton(self.mainFrame)
        self.pushStop.setObjectName(u"pushStop")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushStop.sizePolicy().hasHeightForWidth())
        self.pushStop.setSizePolicy(sizePolicy5)

        self.gridCapture.addWidget(self.pushStop, 0, 1, 1, 1)

        self.pushCapture = QPushButton(self.mainFrame)
        self.pushCapture.setObjectName(u"pushCapture")
        sizePolicy5.setHeightForWidth(self.pushCapture.sizePolicy().hasHeightForWidth())
        self.pushCapture.setSizePolicy(sizePolicy5)

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


        self.gridLayout_2.addLayout(self.gridCapture, 2, 1, 1, 1)

        self.groupScreen = QGroupBox(self.mainFrame)
        self.groupScreen.setObjectName(u"groupScreen")
        self.groupScreen.setFont(font)
        self.gridLayout_7 = QGridLayout(self.groupScreen)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(6, 6, 6, 6)
        self.sliderScreenSpace = QSlider(self.groupScreen)
        self.sliderScreenSpace.setObjectName(u"sliderScreenSpace")
        sizePolicy2.setHeightForWidth(self.sliderScreenSpace.sizePolicy().hasHeightForWidth())
        self.sliderScreenSpace.setSizePolicy(sizePolicy2)
        self.sliderScreenSpace.setMinimum(1)
        self.sliderScreenSpace.setMaximum(3)
        self.sliderScreenSpace.setOrientation(Qt.Horizontal)
        self.sliderScreenSpace.setTickPosition(QSlider.TicksBelow)
        self.sliderScreenSpace.setTickInterval(1)

        self.gridLayout_7.addWidget(self.sliderScreenSpace, 0, 2, 2, 1)

        self.lineScreenSpace = QLineEdit(self.groupScreen)
        self.lineScreenSpace.setObjectName(u"lineScreenSpace")
        sizePolicy4.setHeightForWidth(self.lineScreenSpace.sizePolicy().hasHeightForWidth())
        self.lineScreenSpace.setSizePolicy(sizePolicy4)
        self.lineScreenSpace.setMaximumSize(QSize(30, 16777215))
        self.lineScreenSpace.setFont(font1)
        self.lineScreenSpace.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineScreenSpace, 0, 0, 2, 1)

        self.labelScreenUnit = QLabel(self.groupScreen)
        self.labelScreenUnit.setObjectName(u"labelScreenUnit")
        self.labelScreenUnit.setMaximumSize(QSize(30, 16777215))
        self.labelScreenUnit.setFont(font1)

        self.gridLayout_7.addWidget(self.labelScreenUnit, 0, 1, 2, 1)


        self.gridLayout_2.addWidget(self.groupScreen, 6, 1, 1, 1)

        self.textLog = QTextBrowser(self.mainFrame)
        self.textLog.setObjectName(u"textLog")
        sizePolicy.setHeightForWidth(self.textLog.sizePolicy().hasHeightForWidth())
        self.textLog.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.textLog, 9, 1, 1, 1)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        font4 = QFont()
        font4.setBold(True)
        self.toolBar.setFont(font4)
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
        self.labelGain.setText(QCoreApplication.translate("MainWindow", u"Gain (%)", None))
        self.labelGainRange.setText(QCoreApplication.translate("MainWindow", u"(0 - 100)", None))
        self.lineGain.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineFrameRate.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.labelFrameRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 60)", None))
        self.labelExposureTimeRange.setText(QCoreApplication.translate("MainWindow", u"(1- 2000)", None))
        self.pushRotateRight.setText("")
        self.pushFilpRightLeft.setText("")
        self.pushFlipUpDown.setText("")
        self.pushRotateLeft.setText("")
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.labelExposureTime.setText(QCoreApplication.translate("MainWindow", u"Exposure Time (ms)", None))
        self.lineExposureTime.setText(QCoreApplication.translate("MainWindow", u"2000", None))
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
        self.checkConnectController.setText(QCoreApplication.translate("MainWindow", u"Controller", None))
        self.checkConnectCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.pushReconnect.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.groupEmittance.setTitle(QCoreApplication.translate("MainWindow", u"Emittance", None))
        self.labelXemittance.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.labelYemittanceUnit.setText(QCoreApplication.translate("MainWindow", u"mrad mm", None))
        self.labelYemittance.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.lineXemittance.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineYemittance.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelXemittanceUnit.setText(QCoreApplication.translate("MainWindow", u"mrad mm", None))
        self.pushFit.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.lineBeta.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineGamma.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelGamma.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.labelAlpha.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.labelBeta.setText(QCoreApplication.translate("MainWindow", u"Beta", None))
        self.lineAlpha.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.pushStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.groupScreen.setTitle(QCoreApplication.translate("MainWindow", u"Screen", None))
        self.lineScreenSpace.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.labelScreenUnit.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

