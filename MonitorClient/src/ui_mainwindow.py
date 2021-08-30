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
        MainWindow.resize(1228, 871)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(9999, 9999))
        icon = QIcon()
        icon.addFile(u"../../../../.designer/icons/ncc.png", QSize(), QIcon.Normal, QIcon.Off)
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
        sizePolicy.setHeightForWidth(self.frameControl.sizePolicy().hasHeightForWidth())
        self.frameControl.setSizePolicy(sizePolicy)
        self.frameControl.setFrameShape(QFrame.NoFrame)
        self.frameControl.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameControl)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textLog = QTextBrowser(self.frameControl)
        self.textLog.setObjectName(u"textLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textLog.sizePolicy().hasHeightForWidth())
        self.textLog.setSizePolicy(sizePolicy1)
        self.textLog.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_3.addWidget(self.textLog, 9, 0, 1, 2)

        self.wBeamSizeX = QFrame(self.frameControl)
        self.wBeamSizeX.setObjectName(u"wBeamSizeX")
        sizePolicy.setHeightForWidth(self.wBeamSizeX.sizePolicy().hasHeightForWidth())
        self.wBeamSizeX.setSizePolicy(sizePolicy)
        self.wBeamSizeX.setMaximumSize(QSize(16777215, 16777215))
        self.wBeamSizeX.setFrameShape(QFrame.StyledPanel)
        self.gridBeamSizeX = QGridLayout(self.wBeamSizeX)
        self.gridBeamSizeX.setSpacing(0)
        self.gridBeamSizeX.setObjectName(u"gridBeamSizeX")
        self.gridBeamSizeX.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.wBeamSizeX, 3, 1, 1, 1)

        self.groupControl = QGroupBox(self.frameControl)
        self.groupControl.setObjectName(u"groupControl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupControl.sizePolicy().hasHeightForWidth())
        self.groupControl.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupControl.setFont(font)
        self.gridControl = QGridLayout(self.groupControl)
        self.gridControl.setObjectName(u"gridControl")
        self.gridSubControl = QGridLayout()
        self.gridSubControl.setObjectName(u"gridSubControl")
        self.labelRepeat = QLabel(self.groupControl)
        self.labelRepeat.setObjectName(u"labelRepeat")
        self.labelRepeat.setMaximumSize(QSize(60, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.labelRepeat.setFont(font1)

        self.gridSubControl.addWidget(self.labelRepeat, 1, 0, 1, 1)

        self.lineRepeat = QLineEdit(self.groupControl)
        self.lineRepeat.setObjectName(u"lineRepeat")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineRepeat.sizePolicy().hasHeightForWidth())
        self.lineRepeat.setSizePolicy(sizePolicy3)
        self.lineRepeat.setMaximumSize(QSize(50, 16777215))
        self.lineRepeat.setFont(font1)
        self.lineRepeat.setReadOnly(True)

        self.gridSubControl.addWidget(self.lineRepeat, 1, 1, 1, 1)

        self.sliderRepeat = QSlider(self.groupControl)
        self.sliderRepeat.setObjectName(u"sliderRepeat")
        sizePolicy3.setHeightForWidth(self.sliderRepeat.sizePolicy().hasHeightForWidth())
        self.sliderRepeat.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.lineFrameRate.sizePolicy().hasHeightForWidth())
        self.lineFrameRate.setSizePolicy(sizePolicy3)
        self.lineFrameRate.setMaximumSize(QSize(50, 16777215))
        self.lineFrameRate.setFont(font1)
        self.lineFrameRate.setReadOnly(True)

        self.gridSubControl.addWidget(self.lineFrameRate, 0, 1, 1, 1)

        self.sliderFrameRate = QSlider(self.groupControl)
        self.sliderFrameRate.setObjectName(u"sliderFrameRate")
        sizePolicy3.setHeightForWidth(self.sliderFrameRate.sizePolicy().hasHeightForWidth())
        self.sliderFrameRate.setSizePolicy(sizePolicy3)
        self.sliderFrameRate.setMinimum(1)
        self.sliderFrameRate.setMaximum(30)
        self.sliderFrameRate.setValue(30)
        self.sliderFrameRate.setOrientation(Qt.Horizontal)

        self.gridSubControl.addWidget(self.sliderFrameRate, 0, 2, 1, 1)

        self.labelFrameRange = QLabel(self.groupControl)
        self.labelFrameRange.setObjectName(u"labelFrameRange")
        self.labelFrameRange.setFont(font1)

        self.gridSubControl.addWidget(self.labelFrameRange, 0, 3, 1, 1)


        self.gridControl.addLayout(self.gridSubControl, 0, 0, 1, 3)

        self.gridRotation = QGridLayout()
        self.gridRotation.setObjectName(u"gridRotation")
        self.pushRotateRight = QPushButton(self.groupControl)
        self.pushRotateRight.setObjectName(u"pushRotateRight")
        self.pushRotateRight.setMaximumSize(QSize(30, 16777215))
        self.pushRotateRight.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"../../../../.designer/icons/right_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateRight.setIcon(icon1)
        self.pushRotateRight.setIconSize(QSize(20, 20))
        self.pushRotateRight.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateRight, 0, 2, 1, 1)

        self.pushFilpRightLeft = QPushButton(self.groupControl)
        self.pushFilpRightLeft.setObjectName(u"pushFilpRightLeft")
        self.pushFilpRightLeft.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"../../../../.designer/icons/vertical_flip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushFilpRightLeft.setIcon(icon2)
        self.pushFilpRightLeft.setIconSize(QSize(20, 20))
        self.pushFilpRightLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushFilpRightLeft, 0, 3, 1, 1)

        self.labelRotation = QLabel(self.groupControl)
        self.labelRotation.setObjectName(u"labelRotation")
        self.labelRotation.setFont(font1)

        self.gridRotation.addWidget(self.labelRotation, 0, 0, 1, 1)

        self.pushZoomOut = QPushButton(self.groupControl)
        self.pushZoomOut.setObjectName(u"pushZoomOut")
        self.pushZoomOut.setFont(font1)

        self.gridRotation.addWidget(self.pushZoomOut, 0, 6, 1, 1)

        self.pushFlipUpDown = QPushButton(self.groupControl)
        self.pushFlipUpDown.setObjectName(u"pushFlipUpDown")
        self.pushFlipUpDown.setMaximumSize(QSize(30, 16777215))
        self.pushFlipUpDown.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"../../../../.designer/icons/horizontal_flip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushFlipUpDown.setIcon(icon3)
        self.pushFlipUpDown.setIconSize(QSize(20, 20))
        self.pushFlipUpDown.setFlat(False)

        self.gridRotation.addWidget(self.pushFlipUpDown, 0, 4, 1, 1)

        self.pushRotateLeft = QPushButton(self.groupControl)
        self.pushRotateLeft.setObjectName(u"pushRotateLeft")
        self.pushRotateLeft.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"../../../../.designer/icons/left_rotation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateLeft.setIcon(icon4)
        self.pushRotateLeft.setIconSize(QSize(20, 20))
        self.pushRotateLeft.setFlat(False)

        self.gridRotation.addWidget(self.pushRotateLeft, 0, 1, 1, 1)

        self.pushZoomIn = QPushButton(self.groupControl)
        self.pushZoomIn.setObjectName(u"pushZoomIn")
        self.pushZoomIn.setFont(font1)

        self.gridRotation.addWidget(self.pushZoomIn, 0, 5, 1, 1)


        self.gridControl.addLayout(self.gridRotation, 1, 0, 1, 3)


        self.gridLayout_3.addWidget(self.groupControl, 6, 0, 1, 2)

        self.gridConnection = QGridLayout()
        self.gridConnection.setObjectName(u"gridConnection")
        self.checkConnectCamera = QCheckBox(self.frameControl)
        self.checkConnectCamera.setObjectName(u"checkConnectCamera")
        sizePolicy3.setHeightForWidth(self.checkConnectCamera.sizePolicy().hasHeightForWidth())
        self.checkConnectCamera.setSizePolicy(sizePolicy3)
        self.checkConnectCamera.setFont(font1)
        self.checkConnectCamera.setCheckable(False)

        self.gridConnection.addWidget(self.checkConnectCamera, 0, 2, 1, 1)

        self.checkConnectController = QCheckBox(self.frameControl)
        self.checkConnectController.setObjectName(u"checkConnectController")
        sizePolicy3.setHeightForWidth(self.checkConnectController.sizePolicy().hasHeightForWidth())
        self.checkConnectController.setSizePolicy(sizePolicy3)
        self.checkConnectController.setFont(font1)
        self.checkConnectController.setCheckable(False)

        self.gridConnection.addWidget(self.checkConnectController, 0, 1, 1, 1)

        self.pushReconnect = QPushButton(self.frameControl)
        self.pushReconnect.setObjectName(u"pushReconnect")

        self.gridConnection.addWidget(self.pushReconnect, 0, 3, 1, 1)

        self.pushSetup = QPushButton(self.frameControl)
        self.pushSetup.setObjectName(u"pushSetup")
        self.pushSetup.setFont(font1)

        self.gridConnection.addWidget(self.pushSetup, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridConnection, 0, 0, 1, 2)

        self.wBeamSizeY = QFrame(self.frameControl)
        self.wBeamSizeY.setObjectName(u"wBeamSizeY")
        sizePolicy.setHeightForWidth(self.wBeamSizeY.sizePolicy().hasHeightForWidth())
        self.wBeamSizeY.setSizePolicy(sizePolicy)
        self.wBeamSizeY.setMaximumSize(QSize(16777215, 16777215))
        self.wBeamSizeY.setFrameShape(QFrame.StyledPanel)
        self.wBeamSizeY.setFrameShadow(QFrame.Plain)
        self.gridBeamSizeY = QGridLayout(self.wBeamSizeY)
        self.gridBeamSizeY.setSpacing(0)
        self.gridBeamSizeY.setObjectName(u"gridBeamSizeY")
        self.gridBeamSizeY.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.wBeamSizeY, 2, 1, 1, 1)

        self.wProfile = QFrame(self.frameControl)
        self.wProfile.setObjectName(u"wProfile")
        sizePolicy.setHeightForWidth(self.wProfile.sizePolicy().hasHeightForWidth())
        self.wProfile.setSizePolicy(sizePolicy)
        self.wProfile.setMaximumSize(QSize(16777215, 16777215))
        self.wProfile.setFrameShape(QFrame.StyledPanel)
        self.wProfile.setFrameShadow(QFrame.Plain)
        self.gridProfile = QGridLayout(self.wProfile)
        self.gridProfile.setSpacing(0)
        self.gridProfile.setObjectName(u"gridProfile")
        self.gridProfile.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.wProfile, 2, 0, 2, 1)

        self.groupProfile = QGroupBox(self.frameControl)
        self.groupProfile.setObjectName(u"groupProfile")
        self.groupProfile.setMaximumSize(QSize(16777215, 200))
        self.groupProfile.setFont(font)
        self.gridProfile_2 = QGridLayout(self.groupProfile)
        self.gridProfile_2.setObjectName(u"gridProfile_2")
        self.tableProfiles = QTableWidget(self.groupProfile)
        if (self.tableProfiles.columnCount() < 4):
            self.tableProfiles.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableProfiles.setObjectName(u"tableProfiles")
        self.tableProfiles.setFont(font1)
        self.tableProfiles.horizontalHeader().setCascadingSectionResizes(False)
        self.tableProfiles.horizontalHeader().setStretchLastSection(True)

        self.gridProfile_2.addWidget(self.tableProfiles, 2, 0, 1, 4)

        self.horiCurrent = QHBoxLayout()
        self.horiCurrent.setObjectName(u"horiCurrent")
        self.labelCurrent = QLabel(self.groupProfile)
        self.labelCurrent.setObjectName(u"labelCurrent")
        self.labelCurrent.setMaximumSize(QSize(100, 16777215))
        self.labelCurrent.setFont(font1)

        self.horiCurrent.addWidget(self.labelCurrent)

        self.lineFieldGradient = QLineEdit(self.groupProfile)
        self.lineFieldGradient.setObjectName(u"lineFieldGradient")
        sizePolicy3.setHeightForWidth(self.lineFieldGradient.sizePolicy().hasHeightForWidth())
        self.lineFieldGradient.setSizePolicy(sizePolicy3)
        self.lineFieldGradient.setMinimumSize(QSize(100, 0))
        self.lineFieldGradient.setMaximumSize(QSize(100, 16777215))
        self.lineFieldGradient.setFont(font1)

        self.horiCurrent.addWidget(self.lineFieldGradient)

        self.labelCurrentBlank = QLabel(self.groupProfile)
        self.labelCurrentBlank.setObjectName(u"labelCurrentBlank")

        self.horiCurrent.addWidget(self.labelCurrentBlank)


        self.gridProfile_2.addLayout(self.horiCurrent, 1, 0, 1, 4)

        self.pushEmittance = QPushButton(self.groupProfile)
        self.pushEmittance.setObjectName(u"pushEmittance")
        self.pushEmittance.setFont(font1)

        self.gridProfile_2.addWidget(self.pushEmittance, 0, 0, 1, 1)

        self.pushOpenImage = QPushButton(self.groupProfile)
        self.pushOpenImage.setObjectName(u"pushOpenImage")
        self.pushOpenImage.setFont(font1)

        self.gridProfile_2.addWidget(self.pushOpenImage, 0, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupProfile, 7, 0, 1, 2)

        self.gridCapture = QGridLayout()
        self.gridCapture.setObjectName(u"gridCapture")
        self.pushCapture = QPushButton(self.frameControl)
        self.pushCapture.setObjectName(u"pushCapture")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushCapture.sizePolicy().hasHeightForWidth())
        self.pushCapture.setSizePolicy(sizePolicy4)

        self.gridCapture.addWidget(self.pushCapture, 0, 0, 1, 1)

        self.pushStop = QPushButton(self.frameControl)
        self.pushStop.setObjectName(u"pushStop")
        sizePolicy4.setHeightForWidth(self.pushStop.sizePolicy().hasHeightForWidth())
        self.pushStop.setSizePolicy(sizePolicy4)

        self.gridCapture.addWidget(self.pushStop, 0, 1, 1, 1)

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


        self.gridLayout_3.addLayout(self.gridCapture, 5, 0, 1, 2)

        self.labelPosition = QLabel(self.frameControl)
        self.labelPosition.setObjectName(u"labelPosition")

        self.gridLayout_3.addWidget(self.labelPosition, 4, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frameControl, 0, 1, 11, 1)

        self.frameViewer = QFrame(self.mainFrame)
        self.frameViewer.setObjectName(u"frameViewer")
        sizePolicy.setHeightForWidth(self.frameViewer.sizePolicy().hasHeightForWidth())
        self.frameViewer.setSizePolicy(sizePolicy)
        self.gridViewer = QGridLayout(self.frameViewer)
        self.gridViewer.setSpacing(3)
        self.gridViewer.setObjectName(u"gridViewer")
        self.frameLiveXProfile = QFrame(self.frameViewer)
        self.frameLiveXProfile.setObjectName(u"frameLiveXProfile")
        self.frameLiveXProfile.setFrameShape(QFrame.StyledPanel)
        self.frameLiveXProfile.setFrameShadow(QFrame.Raised)
        self.gridLiveXProfile = QGridLayout(self.frameLiveXProfile)
        self.gridLiveXProfile.setSpacing(0)
        self.gridLiveXProfile.setObjectName(u"gridLiveXProfile")
        self.gridLiveXProfile.setContentsMargins(0, 0, 0, 0)

        self.gridViewer.addWidget(self.frameLiveXProfile, 2, 0, 1, 2)

        self.wViewer = QFrame(self.frameViewer)
        self.wViewer.setObjectName(u"wViewer")
        sizePolicy.setHeightForWidth(self.wViewer.sizePolicy().hasHeightForWidth())
        self.wViewer.setSizePolicy(sizePolicy)
        self.wViewer.setMinimumSize(QSize(576, 529))
        self.wViewer.setFrameShape(QFrame.StyledPanel)
        self.gridScreen = QGridLayout(self.wViewer)
        self.gridScreen.setSpacing(0)
        self.gridScreen.setObjectName(u"gridScreen")
        self.gridScreen.setContentsMargins(0, 0, 0, 0)
        self.labelViewer = QLabel(self.wViewer)
        self.labelViewer.setObjectName(u"labelViewer")
        sizePolicy.setHeightForWidth(self.labelViewer.sizePolicy().hasHeightForWidth())
        self.labelViewer.setSizePolicy(sizePolicy)

        self.gridScreen.addWidget(self.labelViewer, 0, 0, 1, 1)


        self.gridViewer.addWidget(self.wViewer, 0, 0, 2, 2)

        self.frameLiveYProfile = QFrame(self.frameViewer)
        self.frameLiveYProfile.setObjectName(u"frameLiveYProfile")
        self.frameLiveYProfile.setFrameShape(QFrame.StyledPanel)
        self.frameLiveYProfile.setFrameShadow(QFrame.Raised)
        self.gridLiveYProfile = QGridLayout(self.frameLiveYProfile)
        self.gridLiveYProfile.setObjectName(u"gridLiveYProfile")
        self.gridLiveYProfile.setHorizontalSpacing(0)
        self.gridLiveYProfile.setContentsMargins(0, 0, 0, 0)

        self.gridViewer.addWidget(self.frameLiveYProfile, 3, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frameViewer, 0, 0, 11, 1)


        self.gridLayout.addWidget(self.mainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1228, 19))
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
        self.groupControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.labelRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.lineRepeat.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.labelRepeatRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
        self.labelFrameRate.setText(QCoreApplication.translate("MainWindow", u"Frame Rate (FPS)", None))
        self.lineFrameRate.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.labelFrameRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
        self.pushRotateRight.setText("")
        self.pushFilpRightLeft.setText("")
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Screen", None))
        self.pushZoomOut.setText(QCoreApplication.translate("MainWindow", u"Zoom out", None))
        self.pushFlipUpDown.setText("")
        self.pushRotateLeft.setText("")
        self.pushZoomIn.setText(QCoreApplication.translate("MainWindow", u"Zoom in", None))
        self.checkConnectCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.checkConnectController.setText(QCoreApplication.translate("MainWindow", u"Controller", None))
        self.pushReconnect.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.pushSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.groupProfile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
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
        self.labelCurrentBlank.setText("")
        self.pushEmittance.setText(QCoreApplication.translate("MainWindow", u"Emittance", None))
        self.pushOpenImage.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.labelPosition.setText(QCoreApplication.translate("MainWindow", u"Center: (0.00, 0.00) mm Size: (0.00, 0.00) mm", None))
        self.labelViewer.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

