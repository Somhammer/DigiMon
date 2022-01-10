# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        base_path = os.path.abspath(os.path.dirname(__file__))
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1507, 839)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(os.path.join(base_path, 'icons', 'ncc.png'), QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionController = QAction(MainWindow)
        self.actionController.setObjectName(u"actionController")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridCentral = QGridLayout(self.centralwidget)
        self.gridCentral.setSpacing(6)
        self.gridCentral.setObjectName(u"gridCentral")
        self.gridCentral.setContentsMargins(-1, 9, 9, 9)
        self.groupProfile = QGroupBox(self.centralwidget)
        self.groupProfile.setObjectName(u"groupProfile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupProfile.sizePolicy().hasHeightForWidth())
        self.groupProfile.setSizePolicy(sizePolicy1)
        self.groupProfile.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupProfile.setFont(font)
        self.gridLayout_6 = QGridLayout(self.groupProfile)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horiProfileButtons = QHBoxLayout()
        self.horiProfileButtons.setObjectName(u"horiProfileButtons")
        self.pushOpenImage = QPushButton(self.groupProfile)
        self.pushOpenImage.setObjectName(u"pushOpenImage")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.pushOpenImage.setFont(font1)

        self.horiProfileButtons.addWidget(self.pushOpenImage)

        self.pushEmittance = QPushButton(self.groupProfile)
        self.pushEmittance.setObjectName(u"pushEmittance")
        self.pushEmittance.setFont(font1)

        self.horiProfileButtons.addWidget(self.pushEmittance)

        self.horiSpacerProfileButtons = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horiProfileButtons.addItem(self.horiSpacerProfileButtons)


        self.gridLayout_6.addLayout(self.horiProfileButtons, 0, 0, 1, 1)

        self.tableProfiles = QTableWidget(self.groupProfile)
        if (self.tableProfiles.columnCount() < 4):
            self.tableProfiles.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1)
        self.tableProfiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1)
        self.tableProfiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1)
        self.tableProfiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1)
        self.tableProfiles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableProfiles.setObjectName(u"tableProfiles")
        sizePolicy1.setHeightForWidth(self.tableProfiles.sizePolicy().hasHeightForWidth())
        self.tableProfiles.setSizePolicy(sizePolicy1)
        self.tableProfiles.setFont(font1)
        self.tableProfiles.horizontalHeader().setCascadingSectionResizes(False)
        self.tableProfiles.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableProfiles, 2, 0, 1, 1)

        self.horiCurrent = QHBoxLayout()
        self.horiCurrent.setObjectName(u"horiCurrent")
        self.labelCurrent = QLabel(self.groupProfile)
        self.labelCurrent.setObjectName(u"labelCurrent")
        self.labelCurrent.setMaximumSize(QSize(100, 16777215))
        self.labelCurrent.setFont(font1)

        self.horiCurrent.addWidget(self.labelCurrent)

        self.lineFieldGradient = QLineEdit(self.groupProfile)
        self.lineFieldGradient.setObjectName(u"lineFieldGradient")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineFieldGradient.sizePolicy().hasHeightForWidth())
        self.lineFieldGradient.setSizePolicy(sizePolicy2)
        self.lineFieldGradient.setMinimumSize(QSize(100, 0))
        self.lineFieldGradient.setMaximumSize(QSize(100, 16777215))
        self.lineFieldGradient.setFont(font1)

        self.horiCurrent.addWidget(self.lineFieldGradient)

        self.horiSpacerCurrent = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horiCurrent.addItem(self.horiSpacerCurrent)


        self.gridLayout_6.addLayout(self.horiCurrent, 1, 0, 1, 1)


        self.gridCentral.addWidget(self.groupProfile, 2, 2, 1, 1)

        self.frameProfileViewer = QFrame(self.centralwidget)
        self.frameProfileViewer.setObjectName(u"frameProfileViewer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frameProfileViewer.sizePolicy().hasHeightForWidth())
        self.frameProfileViewer.setSizePolicy(sizePolicy3)
        self.frameProfileViewer.setFrameShape(QFrame.StyledPanel)
        self.frameProfileViewer.setFrameShadow(QFrame.Raised)
        self.gridProfileViewer = QGridLayout(self.frameProfileViewer)
        self.gridProfileViewer.setObjectName(u"gridProfileViewer")
        self.frameProfile = QFrame(self.frameProfileViewer)
        self.frameProfile.setObjectName(u"frameProfile")
        sizePolicy.setHeightForWidth(self.frameProfile.sizePolicy().hasHeightForWidth())
        self.frameProfile.setSizePolicy(sizePolicy)
        self.frameProfile.setMaximumSize(QSize(16777215, 16777215))
        self.frameProfile.setFrameShape(QFrame.StyledPanel)
        self.frameProfile.setFrameShadow(QFrame.Plain)
        self.gridProfile = QGridLayout(self.frameProfile)
        self.gridProfile.setSpacing(0)
        self.gridProfile.setObjectName(u"gridProfile")
        self.gridProfile.setContentsMargins(0, 0, 0, 0)

        self.gridProfileViewer.addWidget(self.frameProfile, 1, 0, 3, 3)

        self.frameProfileY = QFrame(self.frameProfileViewer)
        self.frameProfileY.setObjectName(u"frameProfileY")
        sizePolicy.setHeightForWidth(self.frameProfileY.sizePolicy().hasHeightForWidth())
        self.frameProfileY.setSizePolicy(sizePolicy)
        self.frameProfileY.setMaximumSize(QSize(150, 16777215))
        self.frameProfileY.setFrameShape(QFrame.StyledPanel)
        self.gridBeamSizeY = QGridLayout(self.frameProfileY)
        self.gridBeamSizeY.setSpacing(0)
        self.gridBeamSizeY.setObjectName(u"gridBeamSizeY")
        self.gridBeamSizeY.setContentsMargins(0, 0, 0, 0)

        self.gridProfileViewer.addWidget(self.frameProfileY, 1, 3, 3, 1)

        self.frameProfileX = QFrame(self.frameProfileViewer)
        self.frameProfileX.setObjectName(u"frameProfileX")
        sizePolicy.setHeightForWidth(self.frameProfileX.sizePolicy().hasHeightForWidth())
        self.frameProfileX.setSizePolicy(sizePolicy)
        self.frameProfileX.setMaximumSize(QSize(16777215, 150))
        self.frameProfileX.setFrameShape(QFrame.StyledPanel)
        self.frameProfileX.setFrameShadow(QFrame.Plain)
        self.gridBeamSizeX = QGridLayout(self.frameProfileX)
        self.gridBeamSizeX.setSpacing(0)
        self.gridBeamSizeX.setObjectName(u"gridBeamSizeX")
        self.gridBeamSizeX.setContentsMargins(0, 0, 0, 0)

        self.gridProfileViewer.addWidget(self.frameProfileX, 0, 0, 1, 3)


        self.gridCentral.addWidget(self.frameProfileViewer, 1, 1, 2, 1)

        self.frameLog = QFrame(self.centralwidget)
        self.frameLog.setObjectName(u"frameLog")
        self.frameLog.setFrameShape(QFrame.StyledPanel)
        self.frameLog.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frameLog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textLog = QTextBrowser(self.frameLog)
        self.textLog.setObjectName(u"textLog")
        sizePolicy.setHeightForWidth(self.textLog.sizePolicy().hasHeightForWidth())
        self.textLog.setSizePolicy(sizePolicy)
        self.textLog.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_4.addWidget(self.textLog, 1, 0, 1, 2)

        self.horiSpacerLog = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horiSpacerLog, 0, 0, 1, 1)

        self.labelPosition = QLabel(self.frameLog)
        self.labelPosition.setObjectName(u"labelPosition")

        self.gridLayout_4.addWidget(self.labelPosition, 0, 1, 1, 1)


        self.gridCentral.addWidget(self.frameLog, 3, 0, 1, 2)

        self.groupControl = QGroupBox(self.centralwidget)
        self.groupControl.setObjectName(u"groupControl")
        sizePolicy.setHeightForWidth(self.groupControl.sizePolicy().hasHeightForWidth())
        self.groupControl.setSizePolicy(sizePolicy)
        self.groupControl.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupControl)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridScreen = QGridLayout()
        self.gridScreen.setObjectName(u"gridScreen")
        self.pushScreenUp = QPushButton(self.groupControl)
        self.pushScreenUp.setObjectName(u"pushScreenUp")
        self.pushScreenUp.setFont(font1)

        self.gridScreen.addWidget(self.pushScreenUp, 0, 2, 1, 1)

        self.horiSpacerScreen = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridScreen.addItem(self.horiSpacerScreen, 0, 3, 1, 1)

        self.labelScreen = QLabel(self.groupControl)
        self.labelScreen.setObjectName(u"labelScreen")
        self.labelScreen.setFont(font1)

        self.gridScreen.addWidget(self.labelScreen, 0, 0, 1, 1)

        self.pushScreenDown = QPushButton(self.groupControl)
        self.pushScreenDown.setObjectName(u"pushScreenDown")
        self.pushScreenDown.setFont(font1)

        self.gridScreen.addWidget(self.pushScreenDown, 0, 1, 1, 1)

        self.labelScreenStatus = QLabel(self.groupControl)
        self.labelScreenStatus.setObjectName(u"labelScreenStatus")
        self.labelScreenStatus.setMinimumSize(QSize(0, 26))
        self.labelScreenStatus.setFont(font1)

        self.gridScreen.addWidget(self.labelScreenStatus, 1, 0, 1, 4)


        self.gridLayout_5.addLayout(self.gridScreen, 3, 0, 1, 1)

        self.gridCapture = QGridLayout()
        self.gridCapture.setObjectName(u"gridCapture")
        self.pushCapture = QPushButton(self.groupControl)
        self.pushCapture.setObjectName(u"pushCapture")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushCapture.sizePolicy().hasHeightForWidth())
        self.pushCapture.setSizePolicy(sizePolicy4)
        self.pushCapture.setFont(font1)

        self.gridCapture.addWidget(self.pushCapture, 0, 0, 1, 1)

        self.pushStop = QPushButton(self.groupControl)
        self.pushStop.setObjectName(u"pushStop")
        sizePolicy4.setHeightForWidth(self.pushStop.sizePolicy().hasHeightForWidth())
        self.pushStop.setSizePolicy(sizePolicy4)
        self.pushStop.setFont(font1)

        self.gridCapture.addWidget(self.pushStop, 0, 1, 1, 1)

        self.lcdTimer = QLCDNumber(self.groupControl)
        self.lcdTimer.setObjectName(u"lcdTimer")
        self.lcdTimer.setFont(font1)
        self.lcdTimer.setFrameShape(QFrame.StyledPanel)
        self.lcdTimer.setFrameShadow(QFrame.Plain)
        self.lcdTimer.setSmallDecimalPoint(False)
        self.lcdTimer.setDigitCount(5)
        self.lcdTimer.setMode(QLCDNumber.Dec)
        self.lcdTimer.setSegmentStyle(QLCDNumber.Flat)
        self.lcdTimer.setProperty("value", 0.000000000000000)
        self.lcdTimer.setProperty("intValue", 0)

        self.gridCapture.addWidget(self.lcdTimer, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridCapture, 5, 0, 1, 1)

        self.gridSubControl = QGridLayout()
        self.gridSubControl.setObjectName(u"gridSubControl")
        self.labelRepeat = QLabel(self.groupControl)
        self.labelRepeat.setObjectName(u"labelRepeat")
        self.labelRepeat.setMaximumSize(QSize(60, 16777215))
        self.labelRepeat.setFont(font1)

        self.gridSubControl.addWidget(self.labelRepeat, 1, 0, 1, 1)

        self.lineRepeat = QLineEdit(self.groupControl)
        self.lineRepeat.setObjectName(u"lineRepeat")
        sizePolicy2.setHeightForWidth(self.lineRepeat.sizePolicy().hasHeightForWidth())
        self.lineRepeat.setSizePolicy(sizePolicy2)
        self.lineRepeat.setMaximumSize(QSize(50, 16777215))
        self.lineRepeat.setFont(font1)
        self.lineRepeat.setReadOnly(True)

        self.gridSubControl.addWidget(self.lineRepeat, 1, 1, 1, 1)

        self.sliderRepeat = QSlider(self.groupControl)
        self.sliderRepeat.setObjectName(u"sliderRepeat")
        sizePolicy2.setHeightForWidth(self.sliderRepeat.sizePolicy().hasHeightForWidth())
        self.sliderRepeat.setSizePolicy(sizePolicy2)
        self.sliderRepeat.setMinimum(1)
        self.sliderRepeat.setMaximum(30)
        self.sliderRepeat.setOrientation(Qt.Horizontal)

        self.gridSubControl.addWidget(self.sliderRepeat, 1, 2, 1, 1)

        self.labelRepeatRange = QLabel(self.groupControl)
        self.labelRepeatRange.setObjectName(u"labelRepeatRange")
        self.labelRepeatRange.setFont(font1)

        self.gridSubControl.addWidget(self.labelRepeatRange, 1, 3, 1, 1)

        self.labelFrameRate = QLabel(self.groupControl)
        self.labelFrameRate.setObjectName(u"labelFrameRate")
        self.labelFrameRate.setFont(font1)

        self.gridSubControl.addWidget(self.labelFrameRate, 0, 0, 1, 1)

        self.lineFrameRate = QLineEdit(self.groupControl)
        self.lineFrameRate.setObjectName(u"lineFrameRate")
        sizePolicy2.setHeightForWidth(self.lineFrameRate.sizePolicy().hasHeightForWidth())
        self.lineFrameRate.setSizePolicy(sizePolicy2)
        self.lineFrameRate.setMaximumSize(QSize(50, 16777215))
        self.lineFrameRate.setFont(font1)
        self.lineFrameRate.setReadOnly(True)

        self.gridSubControl.addWidget(self.lineFrameRate, 0, 1, 1, 1)

        self.sliderFrameRate = QSlider(self.groupControl)
        self.sliderFrameRate.setObjectName(u"sliderFrameRate")
        sizePolicy2.setHeightForWidth(self.sliderFrameRate.sizePolicy().hasHeightForWidth())
        self.sliderFrameRate.setSizePolicy(sizePolicy2)
        self.sliderFrameRate.setMinimumSize(QSize(150, 0))
        self.sliderFrameRate.setMinimum(1)
        self.sliderFrameRate.setMaximum(30)
        self.sliderFrameRate.setValue(30)
        self.sliderFrameRate.setOrientation(Qt.Horizontal)

        self.gridSubControl.addWidget(self.sliderFrameRate, 0, 2, 1, 1)

        self.labelFrameRange = QLabel(self.groupControl)
        self.labelFrameRange.setObjectName(u"labelFrameRange")
        self.labelFrameRange.setFont(font1)

        self.gridSubControl.addWidget(self.labelFrameRange, 0, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridSubControl, 1, 0, 1, 1)

        self.horiRotation = QHBoxLayout()
        self.horiRotation.setObjectName(u"horiRotation")
        self.labelRotation = QLabel(self.groupControl)
        self.labelRotation.setObjectName(u"labelRotation")
        self.labelRotation.setFont(font1)

        self.horiRotation.addWidget(self.labelRotation)

        self.pushRotateLeft = QPushButton(self.groupControl)
        self.pushRotateLeft.setObjectName(u"pushRotateLeft")
        self.pushRotateLeft.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(os.path.join(base_path, 'icons', 'left_rotation.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateLeft.setIcon(icon1)
        self.pushRotateLeft.setIconSize(QSize(20, 20))
        self.pushRotateLeft.setFlat(False)

        self.horiRotation.addWidget(self.pushRotateLeft)

        self.pushRotateRight = QPushButton(self.groupControl)
        self.pushRotateRight.setObjectName(u"pushRotateRight")
        self.pushRotateRight.setMaximumSize(QSize(30, 16777215))
        self.pushRotateRight.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(os.path.join(base_path, 'icons', 'right_rotation.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateRight.setIcon(icon2)
        self.pushRotateRight.setIconSize(QSize(20, 20))
        self.pushRotateRight.setFlat(False)

        self.horiRotation.addWidget(self.pushRotateRight)

        self.pushFilpRightLeft = QPushButton(self.groupControl)
        self.pushFilpRightLeft.setObjectName(u"pushFilpRightLeft")
        self.pushFilpRightLeft.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(os.path.join(base_path, 'icons', 'vertical_flip.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushFilpRightLeft.setIcon(icon3)
        self.pushFilpRightLeft.setIconSize(QSize(20, 20))
        self.pushFilpRightLeft.setFlat(False)

        self.horiRotation.addWidget(self.pushFilpRightLeft)

        self.pushFlipUpDown = QPushButton(self.groupControl)
        self.pushFlipUpDown.setObjectName(u"pushFlipUpDown")
        self.pushFlipUpDown.setMaximumSize(QSize(30, 16777215))
        self.pushFlipUpDown.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(os.path.join(base_path, 'icons', 'horizontal_flip.png'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushFlipUpDown.setIcon(icon4)
        self.pushFlipUpDown.setIconSize(QSize(20, 20))
        self.pushFlipUpDown.setFlat(False)

        self.horiRotation.addWidget(self.pushFlipUpDown)

        self.horiSpacerRotation = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horiRotation.addItem(self.horiSpacerRotation)


        self.gridLayout_5.addLayout(self.horiRotation, 2, 0, 1, 1)


        self.gridCentral.addWidget(self.groupControl, 1, 2, 1, 1)

        self.frameCameraViewer = QFrame(self.centralwidget)
        self.frameCameraViewer.setObjectName(u"frameCameraViewer")
        sizePolicy3.setHeightForWidth(self.frameCameraViewer.sizePolicy().hasHeightForWidth())
        self.frameCameraViewer.setSizePolicy(sizePolicy3)
        self.gridCameraViewer = QGridLayout(self.frameCameraViewer)
        self.gridCameraViewer.setObjectName(u"gridCameraViewer")
        self.frameLiveYProfile = QFrame(self.frameCameraViewer)
        self.frameLiveYProfile.setObjectName(u"frameLiveYProfile")
        self.frameLiveYProfile.setMaximumSize(QSize(150, 16777215))
        self.frameLiveYProfile.setFrameShape(QFrame.StyledPanel)
        self.frameLiveYProfile.setFrameShadow(QFrame.Plain)
        self.gridLiveYProfile = QGridLayout(self.frameLiveYProfile)
        self.gridLiveYProfile.setObjectName(u"gridLiveYProfile")
        self.gridLiveYProfile.setHorizontalSpacing(0)
        self.gridLiveYProfile.setContentsMargins(0, 0, 0, 0)

        self.gridCameraViewer.addWidget(self.frameLiveYProfile, 1, 3, 3, 1)

        self.frameCamera = QFrame(self.frameCameraViewer)
        self.frameCamera.setObjectName(u"frameCamera")
        sizePolicy.setHeightForWidth(self.frameCamera.sizePolicy().hasHeightForWidth())
        self.frameCamera.setSizePolicy(sizePolicy)
        self.frameCamera.setMinimumSize(QSize(0, 0))
        self.frameCamera.setFrameShape(QFrame.StyledPanel)
        self.gridLayout = QGridLayout(self.frameCamera)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCamera = QLabel(self.frameCamera)
        self.labelCamera.setObjectName(u"labelCamera")
        sizePolicy.setHeightForWidth(self.labelCamera.sizePolicy().hasHeightForWidth())
        self.labelCamera.setSizePolicy(sizePolicy)

        self.gridCameraViewer.addWidget(self.frameCamera, 1, 0, 3, 3)

        self.frameLiveXProfile = QFrame(self.frameCameraViewer)
        self.frameLiveXProfile.setObjectName(u"frameLiveXProfile")
        self.frameLiveXProfile.setMaximumSize(QSize(16777215, 150))
        self.frameLiveXProfile.setFrameShape(QFrame.StyledPanel)
        self.frameLiveXProfile.setFrameShadow(QFrame.Plain)
        self.gridLiveXProfile = QGridLayout(self.frameLiveXProfile)
        self.gridLiveXProfile.setSpacing(0)
        self.gridLiveXProfile.setObjectName(u"gridLiveXProfile")
        self.gridLiveXProfile.setContentsMargins(0, 0, 0, 0)

        self.gridCameraViewer.addWidget(self.frameLiveXProfile, 0, 0, 1, 3)


        self.gridCentral.addWidget(self.frameCameraViewer, 1, 0, 2, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushSetup = QPushButton(self.centralwidget)
        self.pushSetup.setObjectName(u"pushSetup")
        self.pushSetup.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushSetup)

        self.labelCameraPixmap = QLabel(self.centralwidget)
        self.labelCameraPixmap.setObjectName(u"labelCameraPixmap")
        self.labelCameraPixmap.setMinimumSize(QSize(30, 30))
        self.labelCameraPixmap.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.labelCameraPixmap)

        self.labelStatusCamera = QLabel(self.centralwidget)
        self.labelStatusCamera.setObjectName(u"labelStatusCamera")

        self.horizontalLayout_2.addWidget(self.labelStatusCamera)

        self.labelControllerPixmap = QLabel(self.centralwidget)
        self.labelControllerPixmap.setObjectName(u"labelControllerPixmap")
        self.labelControllerPixmap.setMinimumSize(QSize(30, 30))
        self.labelControllerPixmap.setMaximumSize(QSize(30, 30))
        self.labelControllerPixmap.setBaseSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.labelControllerPixmap)

        self.labelStatusController = QLabel(self.centralwidget)
        self.labelStatusController.setObjectName(u"labelStatusController")

        self.horizontalLayout_2.addWidget(self.labelStatusController)

        self.labelCalibrationPixmap = QLabel(self.centralwidget)
        self.labelCalibrationPixmap.setObjectName(u"labelCalibrationPixmap")
        self.labelCalibrationPixmap.setMinimumSize(QSize(30, 30))
        self.labelCalibrationPixmap.setMaximumSize(QSize(30, 30))
        self.labelCalibrationPixmap.setBaseSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.labelCalibrationPixmap)

        self.labelStatusCalibration = QLabel(self.centralwidget)
        self.labelStatusCalibration.setObjectName(u"labelStatusCalibration")

        self.horizontalLayout_2.addWidget(self.labelStatusCalibration)


        self.gridCentral.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridCentral.addItem(self.horizontalSpacer, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushRotateLeft.setDefault(False)
        self.pushFlipUpDown.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DigiMon", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"Camera IP", None))
        self.actionController.setText(QCoreApplication.translate("MainWindow", u"Controller IP", None))
        self.groupProfile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushOpenImage.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushEmittance.setText(QCoreApplication.translate("MainWindow", u"Emittance", None))
        ___qtablewidgetitem = self.tableProfiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem1 = self.tableProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Beam Size(x)", None));
        ___qtablewidgetitem2 = self.tableProfiles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Beam Size(y)", None));
        ___qtablewidgetitem3 = self.tableProfiles.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        self.labelCurrent.setText(QCoreApplication.translate("MainWindow", u"Current (A)", None))
        self.lineFieldGradient.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelPosition.setText(QCoreApplication.translate("MainWindow", u"Center: (0.00, 0.00) mm Size: (0.00, 0.00) mm", None))
        self.groupControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushScreenUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.labelScreen.setText(QCoreApplication.translate("MainWindow", u"Screen", None))
        self.pushScreenDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.labelScreenStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.pushCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.labelRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.lineRepeat.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.labelRepeatRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
        self.labelFrameRate.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.lineFrameRate.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.labelFrameRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.pushRotateLeft.setText("")
        self.pushRotateRight.setText("")
        self.pushFilpRightLeft.setText("")
        self.pushFlipUpDown.setText("")
        self.labelCamera.setText("")
        self.pushSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.labelCameraPixmap.setText("")
        self.labelStatusCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.labelControllerPixmap.setText("")
        self.labelStatusController.setText(QCoreApplication.translate("MainWindow", u"Controller", None))
        self.labelCalibrationPixmap.setText("")
        self.labelStatusCalibration.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
    # retranslateUi

