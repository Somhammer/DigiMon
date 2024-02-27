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

from variables import BASE_PATH

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1427, 875)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(os.path.join(BASE_PATH, "icons/ncc.png"), QSize(), QIcon.Normal, QIcon.Off)
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
        self.frameProfileViewer = QFrame(self.centralwidget)
        self.frameProfileViewer.setObjectName(u"frameProfileViewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameProfileViewer.sizePolicy().hasHeightForWidth())
        self.frameProfileViewer.setSizePolicy(sizePolicy1)
        self.frameProfileViewer.setFrameShape(QFrame.StyledPanel)
        self.frameProfileViewer.setFrameShadow(QFrame.Raised)
        self.gridProfileViewer = QGridLayout(self.frameProfileViewer)
        self.gridProfileViewer.setSpacing(3)
        self.gridProfileViewer.setObjectName(u"gridProfileViewer")
        self.gridProfileViewer.setContentsMargins(0, 0, 0, 0)
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

        self.gridProfileViewer.addWidget(self.frameProfileX, 0, 0, 1, 2)

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

        self.gridProfileViewer.addWidget(self.frameProfileY, 1, 2, 2, 1)

        self.frameProfile = QFrame(self.frameProfileViewer)
        self.frameProfile.setObjectName(u"frameProfile")
        self.frameProfile.setFrameShape(QFrame.StyledPanel)
        self.frameProfile.setFrameShadow(QFrame.Plain)
        self.gridProfile = QGridLayout(self.frameProfile)
        self.gridProfile.setSpacing(0)
        self.gridProfile.setObjectName(u"gridProfile")
        self.gridProfile.setContentsMargins(0, 0, 0, 0)

        self.gridProfileViewer.addWidget(self.frameProfile, 1, 0, 2, 2)


        self.gridCentral.addWidget(self.frameProfileViewer, 2, 1, 4, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridCentral.addItem(self.horizontalSpacer, 0, 0, 1, 2)

        self.horiSpacerLog = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridCentral.addItem(self.horiSpacerLog, 6, 0, 1, 1)

        self.frameCameraViewer = QFrame(self.centralwidget)
        self.frameCameraViewer.setObjectName(u"frameCameraViewer")
        sizePolicy1.setHeightForWidth(self.frameCameraViewer.sizePolicy().hasHeightForWidth())
        self.frameCameraViewer.setSizePolicy(sizePolicy1)
        self.frameCameraViewer.setFrameShadow(QFrame.Sunken)
        self.gridCameraViewer = QGridLayout(self.frameCameraViewer)
        self.gridCameraViewer.setSpacing(3)
        self.gridCameraViewer.setObjectName(u"gridCameraViewer")
        self.gridCameraViewer.setContentsMargins(0, 0, 0, 0)
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

        self.gridLayout.addWidget(self.labelCamera, 0, 0, 1, 1)


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


        self.gridCentral.addWidget(self.frameCameraViewer, 2, 0, 4, 1)

        self.groupImage = QGroupBox(self.centralwidget)
        self.groupImage.setObjectName(u"groupImage")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupImage.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupImage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushFilter = QPushButton(self.groupImage)
        self.pushFilter.setObjectName(u"pushFilter")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.pushFilter.setFont(font1)

        self.gridLayout_2.addWidget(self.pushFilter, 1, 2, 1, 1)

        self.horiRotation = QHBoxLayout()
        self.horiRotation.setObjectName(u"horiRotation")
        self.labelRotation = QLabel(self.groupImage)
        self.labelRotation.setObjectName(u"labelRotation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelRotation.sizePolicy().hasHeightForWidth())
        self.labelRotation.setSizePolicy(sizePolicy2)
        self.labelRotation.setMinimumSize(QSize(85, 0))
        self.labelRotation.setMaximumSize(QSize(85, 16777215))
        self.labelRotation.setFont(font1)
        self.labelRotation.setAlignment(Qt.AlignCenter)

        self.horiRotation.addWidget(self.labelRotation)

        self.pushRotateLeft = QPushButton(self.groupImage)
        self.pushRotateLeft.setObjectName(u"pushRotateLeft")
        self.pushRotateLeft.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(os.path.join(BASE_PATH, "icons/left_rotation.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateLeft.setIcon(icon1)
        self.pushRotateLeft.setIconSize(QSize(20, 20))
        self.pushRotateLeft.setFlat(False)

        self.horiRotation.addWidget(self.pushRotateLeft)

        self.pushRotateRight = QPushButton(self.groupImage)
        self.pushRotateRight.setObjectName(u"pushRotateRight")
        self.pushRotateRight.setMaximumSize(QSize(30, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.pushRotateRight.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(os.path.join(BASE_PATH, "icons/right_rotation.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushRotateRight.setIcon(icon2)
        self.pushRotateRight.setIconSize(QSize(20, 20))
        self.pushRotateRight.setFlat(False)

        self.horiRotation.addWidget(self.pushRotateRight)

        self.pushFilpRightLeft = QPushButton(self.groupImage)
        self.pushFilpRightLeft.setObjectName(u"pushFilpRightLeft")
        self.pushFilpRightLeft.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(os.path.join(BASE_PATH, "icons/vertical_flip.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushFilpRightLeft.setIcon(icon3)
        self.pushFilpRightLeft.setIconSize(QSize(20, 20))
        self.pushFilpRightLeft.setFlat(False)

        self.horiRotation.addWidget(self.pushFilpRightLeft)

        self.pushFlipUpDown = QPushButton(self.groupImage)
        self.pushFlipUpDown.setObjectName(u"pushFlipUpDown")
        self.pushFlipUpDown.setMaximumSize(QSize(30, 16777215))
        self.pushFlipUpDown.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(os.path.join(BASE_PATH, "icons/horizontal_flip.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushFlipUpDown.setIcon(icon4)
        self.pushFlipUpDown.setIconSize(QSize(20, 20))
        self.pushFlipUpDown.setFlat(False)

        self.horiRotation.addWidget(self.pushFlipUpDown)

        self.labelRotationAngle = QLabel(self.groupImage)
        self.labelRotationAngle.setObjectName(u"labelRotationAngle")
        self.labelRotationAngle.setMaximumSize(QSize(115, 16777215))
        self.labelRotationAngle.setFont(font1)
        self.labelRotationAngle.setAlignment(Qt.AlignCenter)

        self.horiRotation.addWidget(self.labelRotationAngle)

        self.lineRotationAngle = QLineEdit(self.groupImage)
        self.lineRotationAngle.setObjectName(u"lineRotationAngle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineRotationAngle.sizePolicy().hasHeightForWidth())
        self.lineRotationAngle.setSizePolicy(sizePolicy3)
        self.lineRotationAngle.setMaximumSize(QSize(55, 55))
        self.lineRotationAngle.setFont(font1)
        self.lineRotationAngle.setMaxLength(6)
        self.lineRotationAngle.setReadOnly(False)

        self.horiRotation.addWidget(self.lineRotationAngle)

        self.pushAngleUp = QPushButton(self.groupImage)
        self.pushAngleUp.setObjectName(u"pushAngleUp")
        self.pushAngleUp.setMaximumSize(QSize(30, 16777215))
        self.pushAngleUp.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(os.path.join(BASE_PATH, "icons/up.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushAngleUp.setIcon(icon5)

        self.horiRotation.addWidget(self.pushAngleUp)

        self.pushAngleDown = QPushButton(self.groupImage)
        self.pushAngleDown.setObjectName(u"pushAngleDown")
        self.pushAngleDown.setMaximumSize(QSize(30, 16777215))
        self.pushAngleDown.setFont(font1)
        self.pushAngleDown.setAcceptDrops(True)
        icon6 = QIcon()
        icon6.addFile(os.path.join(BASE_PATH, "icons/down.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushAngleDown.setIcon(icon6)

        self.horiRotation.addWidget(self.pushAngleDown)


        self.gridLayout_2.addLayout(self.horiRotation, 0, 0, 1, 3)

        self.pushCalibration = QPushButton(self.groupImage)
        self.pushCalibration.setObjectName(u"pushCalibration")
        self.pushCalibration.setFont(font1)

        self.gridLayout_2.addWidget(self.pushCalibration, 1, 0, 1, 1)

        self.pushROI = QPushButton(self.groupImage)
        self.pushROI.setObjectName(u"pushROI")
        self.pushROI.setFont(font1)

        self.gridLayout_2.addWidget(self.pushROI, 1, 1, 1, 1)


        self.gridCentral.addWidget(self.groupImage, 4, 2, 1, 1)

        self.framePVHist = QFrame(self.centralwidget)
        self.framePVHist.setObjectName(u"framePVHist")
        sizePolicy.setHeightForWidth(self.framePVHist.sizePolicy().hasHeightForWidth())
        self.framePVHist.setSizePolicy(sizePolicy)
        self.framePVHist.setMaximumSize(QSize(16777215, 200))
        self.framePVHist.setFrameShape(QFrame.StyledPanel)
        self.framePVHist.setFrameShadow(QFrame.Plain)
        self.gridPVHist = QGridLayout(self.framePVHist)
        self.gridPVHist.setSpacing(0)
        self.gridPVHist.setObjectName(u"gridPVHist")
        self.gridPVHist.setContentsMargins(0, 0, 0, 0)

        self.gridCentral.addWidget(self.framePVHist, 7, 0, 1, 2)

        self.groupProfile = QGroupBox(self.centralwidget)
        self.groupProfile.setObjectName(u"groupProfile")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupProfile.sizePolicy().hasHeightForWidth())
        self.groupProfile.setSizePolicy(sizePolicy4)
        self.groupProfile.setMaximumSize(QSize(16777215, 16777215))
        self.groupProfile.setFont(font)
        self.gridLayout_6 = QGridLayout(self.groupProfile)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableProfiles = QTableWidget(self.groupProfile)
        if (self.tableProfiles.columnCount() < 3):
            self.tableProfiles.setColumnCount(3)
        font3 = QFont()
        font3.setPointSize(11)
        font3.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableProfiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableProfiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableProfiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableProfiles.setObjectName(u"tableProfiles")
        sizePolicy4.setHeightForWidth(self.tableProfiles.sizePolicy().hasHeightForWidth())
        self.tableProfiles.setSizePolicy(sizePolicy4)
        self.tableProfiles.setFont(font1)
        self.tableProfiles.horizontalHeader().setCascadingSectionResizes(False)
        self.tableProfiles.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableProfiles, 1, 0, 1, 1)

        self.horiProfileButtons = QHBoxLayout()
        self.horiProfileButtons.setObjectName(u"horiProfileButtons")
        self.pushOpenImage = QPushButton(self.groupProfile)
        self.pushOpenImage.setObjectName(u"pushOpenImage")
        self.pushOpenImage.setMaximumSize(QSize(16777215, 16777215))
        self.pushOpenImage.setFont(font1)

        self.horiProfileButtons.addWidget(self.pushOpenImage)

        self.horiSpacerProfileButtons = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horiProfileButtons.addItem(self.horiSpacerProfileButtons)


        self.gridLayout_6.addLayout(self.horiProfileButtons, 0, 0, 1, 1)


        self.gridCentral.addWidget(self.groupProfile, 5, 2, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineExposureTime = QLineEdit(self.groupBox)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        self.lineExposureTime.setMinimumSize(QSize(100, 0))
        self.lineExposureTime.setMaximumSize(QSize(100, 16777215))
        self.lineExposureTime.setFont(font1)

        self.gridLayout_3.addWidget(self.lineExposureTime, 1, 1, 1, 1)

        self.sliderExposureTime = QSlider(self.groupBox)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy3.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy3)
        self.sliderExposureTime.setMaximumSize(QSize(200, 16777215))
        self.sliderExposureTime.setMinimum(25)
        self.sliderExposureTime.setMaximum(1000000)
        self.sliderExposureTime.setValue(5000)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderExposureTime, 1, 2, 1, 1)

        self.labelGain = QLabel(self.groupBox)
        self.labelGain.setObjectName(u"labelGain")
        sizePolicy2.setHeightForWidth(self.labelGain.sizePolicy().hasHeightForWidth())
        self.labelGain.setSizePolicy(sizePolicy2)
        self.labelGain.setMinimumSize(QSize(120, 0))
        self.labelGain.setMaximumSize(QSize(120, 16777215))
        self.labelGain.setFont(font1)

        self.gridLayout_3.addWidget(self.labelGain, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 1, 3, 1, 1)

        self.labelFrameRate = QLabel(self.groupBox)
        self.labelFrameRate.setObjectName(u"labelFrameRate")
        sizePolicy2.setHeightForWidth(self.labelFrameRate.sizePolicy().hasHeightForWidth())
        self.labelFrameRate.setSizePolicy(sizePolicy2)
        self.labelFrameRate.setMinimumSize(QSize(120, 0))
        self.labelFrameRate.setMaximumSize(QSize(120, 16777215))
        self.labelFrameRate.setFont(font1)

        self.gridLayout_3.addWidget(self.labelFrameRate, 2, 0, 1, 1)

        self.sliderGain = QSlider(self.groupBox)
        self.sliderGain.setObjectName(u"sliderGain")
        sizePolicy3.setHeightForWidth(self.sliderGain.sizePolicy().hasHeightForWidth())
        self.sliderGain.setSizePolicy(sizePolicy3)
        self.sliderGain.setMaximumSize(QSize(200, 16777215))
        self.sliderGain.setMaximum(100)
        self.sliderGain.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderGain, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 3, 1, 1)

        self.labelExposureTime = QLabel(self.groupBox)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        sizePolicy2.setHeightForWidth(self.labelExposureTime.sizePolicy().hasHeightForWidth())
        self.labelExposureTime.setSizePolicy(sizePolicy2)
        self.labelExposureTime.setMinimumSize(QSize(120, 0))
        self.labelExposureTime.setMaximumSize(QSize(120, 16777215))
        self.labelExposureTime.setFont(font1)

        self.gridLayout_3.addWidget(self.labelExposureTime, 1, 0, 1, 1)

        self.lineFrameRate = QLineEdit(self.groupBox)
        self.lineFrameRate.setObjectName(u"lineFrameRate")
        sizePolicy3.setHeightForWidth(self.lineFrameRate.sizePolicy().hasHeightForWidth())
        self.lineFrameRate.setSizePolicy(sizePolicy3)
        self.lineFrameRate.setMinimumSize(QSize(100, 0))
        self.lineFrameRate.setMaximumSize(QSize(100, 16777215))
        self.lineFrameRate.setFont(font1)
        self.lineFrameRate.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineFrameRate, 2, 1, 1, 1)

        self.sliderFrameRate = QSlider(self.groupBox)
        self.sliderFrameRate.setObjectName(u"sliderFrameRate")
        sizePolicy3.setHeightForWidth(self.sliderFrameRate.sizePolicy().hasHeightForWidth())
        self.sliderFrameRate.setSizePolicy(sizePolicy3)
        self.sliderFrameRate.setMinimumSize(QSize(150, 0))
        self.sliderFrameRate.setMinimum(1)
        self.sliderFrameRate.setMaximum(20)
        self.sliderFrameRate.setValue(20)
        self.sliderFrameRate.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderFrameRate, 2, 2, 1, 1)

        self.labelFrameRange = QLabel(self.groupBox)
        self.labelFrameRange.setObjectName(u"labelFrameRange")
        self.labelFrameRange.setFont(font1)

        self.gridLayout_3.addWidget(self.labelFrameRange, 2, 3, 1, 1)

        self.lineGain = QLineEdit(self.groupBox)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setMinimumSize(QSize(100, 0))
        self.lineGain.setMaximumSize(QSize(100, 16777215))
        self.lineGain.setFont(font1)

        self.gridLayout_3.addWidget(self.lineGain, 0, 1, 1, 1)


        self.gridCentral.addWidget(self.groupBox, 3, 2, 1, 1)

        self.labelPosition = QLabel(self.centralwidget)
        self.labelPosition.setObjectName(u"labelPosition")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelPosition.sizePolicy().hasHeightForWidth())
        self.labelPosition.setSizePolicy(sizePolicy5)

        self.gridCentral.addWidget(self.labelPosition, 6, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.labelCameraPixmap = QLabel(self.groupBox_2)
        self.labelCameraPixmap.setObjectName(u"labelCameraPixmap")
        self.labelCameraPixmap.setMinimumSize(QSize(30, 30))
        self.labelCameraPixmap.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.labelCameraPixmap)

        self.labelStatusCamera = QLabel(self.groupBox_2)
        self.labelStatusCamera.setObjectName(u"labelStatusCamera")
        font4 = QFont()
        font4.setPointSize(12)
        self.labelStatusCamera.setFont(font4)

        self.horizontalLayout_2.addWidget(self.labelStatusCamera)

        self.labelControllerPixmap = QLabel(self.groupBox_2)
        self.labelControllerPixmap.setObjectName(u"labelControllerPixmap")
        self.labelControllerPixmap.setMinimumSize(QSize(30, 30))
        self.labelControllerPixmap.setMaximumSize(QSize(30, 30))
        self.labelControllerPixmap.setBaseSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.labelControllerPixmap)

        self.labelStatusController = QLabel(self.groupBox_2)
        self.labelStatusController.setObjectName(u"labelStatusController")
        self.labelStatusController.setFont(font4)

        self.horizontalLayout_2.addWidget(self.labelStatusController)

        self.labelCalibrationPixmap = QLabel(self.groupBox_2)
        self.labelCalibrationPixmap.setObjectName(u"labelCalibrationPixmap")
        self.labelCalibrationPixmap.setMinimumSize(QSize(30, 30))
        self.labelCalibrationPixmap.setMaximumSize(QSize(30, 30))
        self.labelCalibrationPixmap.setBaseSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.labelCalibrationPixmap)

        self.labelStatusCalibration = QLabel(self.groupBox_2)
        self.labelStatusCalibration.setObjectName(u"labelStatusCalibration")
        self.labelStatusCalibration.setFont(font4)

        self.horizontalLayout_2.addWidget(self.labelStatusCalibration)


        self.gridCentral.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.groupControl = QGroupBox(self.centralwidget)
        self.groupControl.setObjectName(u"groupControl")
        sizePolicy.setHeightForWidth(self.groupControl.sizePolicy().hasHeightForWidth())
        self.groupControl.setSizePolicy(sizePolicy)
        self.groupControl.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupControl)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.lineRepeat = QLineEdit(self.groupControl)
        self.lineRepeat.setObjectName(u"lineRepeat")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineRepeat.sizePolicy().hasHeightForWidth())
        self.lineRepeat.setSizePolicy(sizePolicy6)
        self.lineRepeat.setMinimumSize(QSize(0, 0))
        self.lineRepeat.setMaximumSize(QSize(40, 16777215))
        self.lineRepeat.setFont(font1)
        self.lineRepeat.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineRepeat, 1, 1, 1, 1)

        self.pushScreenDown = QPushButton(self.groupControl)
        self.pushScreenDown.setObjectName(u"pushScreenDown")
        sizePolicy3.setHeightForWidth(self.pushScreenDown.sizePolicy().hasHeightForWidth())
        self.pushScreenDown.setSizePolicy(sizePolicy3)
        self.pushScreenDown.setMinimumSize(QSize(0, 0))
        self.pushScreenDown.setMaximumSize(QSize(16777215, 16777215))
        self.pushScreenDown.setFont(font1)

        self.gridLayout_5.addWidget(self.pushScreenDown, 2, 1, 1, 2)

        self.labelRepeat = QLabel(self.groupControl)
        self.labelRepeat.setObjectName(u"labelRepeat")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.labelRepeat.sizePolicy().hasHeightForWidth())
        self.labelRepeat.setSizePolicy(sizePolicy7)
        self.labelRepeat.setMinimumSize(QSize(0, 0))
        self.labelRepeat.setMaximumSize(QSize(80, 80))
        self.labelRepeat.setFont(font1)
        self.labelRepeat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelRepeat, 1, 0, 1, 1)

        self.pushCapture = QPushButton(self.groupControl)
        self.pushCapture.setObjectName(u"pushCapture")
        sizePolicy3.setHeightForWidth(self.pushCapture.sizePolicy().hasHeightForWidth())
        self.pushCapture.setSizePolicy(sizePolicy3)
        self.pushCapture.setMinimumSize(QSize(140, 0))
        self.pushCapture.setMaximumSize(QSize(16777215, 16777215))
        self.pushCapture.setFont(font1)

        self.gridLayout_5.addWidget(self.pushCapture, 0, 3, 1, 2)

        self.labelRepeatRange = QLabel(self.groupControl)
        self.labelRepeatRange.setObjectName(u"labelRepeatRange")
        sizePolicy.setHeightForWidth(self.labelRepeatRange.sizePolicy().hasHeightForWidth())
        self.labelRepeatRange.setSizePolicy(sizePolicy)
        self.labelRepeatRange.setMaximumSize(QSize(16777215, 16777215))
        self.labelRepeatRange.setFont(font1)

        self.gridLayout_5.addWidget(self.labelRepeatRange, 1, 5, 1, 2)

        self.pushScreenUp = QPushButton(self.groupControl)
        self.pushScreenUp.setObjectName(u"pushScreenUp")
        sizePolicy3.setHeightForWidth(self.pushScreenUp.sizePolicy().hasHeightForWidth())
        self.pushScreenUp.setSizePolicy(sizePolicy3)
        self.pushScreenUp.setMinimumSize(QSize(0, 0))
        self.pushScreenUp.setMaximumSize(QSize(16777215, 16777215))
        self.pushScreenUp.setFont(font1)

        self.gridLayout_5.addWidget(self.pushScreenUp, 2, 3, 1, 2)

        self.pushStop = QPushButton(self.groupControl)
        self.pushStop.setObjectName(u"pushStop")
        sizePolicy3.setHeightForWidth(self.pushStop.sizePolicy().hasHeightForWidth())
        self.pushStop.setSizePolicy(sizePolicy3)
        self.pushStop.setMinimumSize(QSize(140, 0))
        self.pushStop.setMaximumSize(QSize(16777215, 16777215))
        self.pushStop.setFont(font1)

        self.gridLayout_5.addWidget(self.pushStop, 0, 5, 1, 2)

        self.labelScreenStatus = QLabel(self.groupControl)
        self.labelScreenStatus.setObjectName(u"labelScreenStatus")
        self.labelScreenStatus.setMinimumSize(QSize(0, 26))
        self.labelScreenStatus.setMaximumSize(QSize(16777215, 16777215))
        self.labelScreenStatus.setFont(font1)
        self.labelScreenStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.labelScreenStatus, 2, 5, 1, 2)

        self.labelScreen = QLabel(self.groupControl)
        self.labelScreen.setObjectName(u"labelScreen")
        sizePolicy7.setHeightForWidth(self.labelScreen.sizePolicy().hasHeightForWidth())
        self.labelScreen.setSizePolicy(sizePolicy7)
        self.labelScreen.setMinimumSize(QSize(0, 0))
        self.labelScreen.setMaximumSize(QSize(16777215, 16777215))
        self.labelScreen.setFont(font1)
        self.labelScreen.setLayoutDirection(Qt.LeftToRight)
        self.labelScreen.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelScreen, 2, 0, 1, 1)

        self.pushConnection = QPushButton(self.groupControl)
        self.pushConnection.setObjectName(u"pushConnection")
        sizePolicy3.setHeightForWidth(self.pushConnection.sizePolicy().hasHeightForWidth())
        self.pushConnection.setSizePolicy(sizePolicy3)
        self.pushConnection.setMinimumSize(QSize(140, 0))
        self.pushConnection.setMaximumSize(QSize(16777215, 16777215))
        self.pushConnection.setFont(font1)

        self.gridLayout_5.addWidget(self.pushConnection, 0, 1, 1, 2)

        self.sliderRepeat = QSlider(self.groupControl)
        self.sliderRepeat.setObjectName(u"sliderRepeat")
        sizePolicy3.setHeightForWidth(self.sliderRepeat.sizePolicy().hasHeightForWidth())
        self.sliderRepeat.setSizePolicy(sizePolicy3)
        self.sliderRepeat.setMaximumSize(QSize(16777215, 16777215))
        self.sliderRepeat.setMinimum(1)
        self.sliderRepeat.setMaximum(30)
        self.sliderRepeat.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.sliderRepeat, 1, 2, 1, 3)


        self.gridCentral.addWidget(self.groupControl, 2, 2, 1, 1)

        self.textLog = QTextBrowser(self.centralwidget)
        self.textLog.setObjectName(u"textLog")
        sizePolicy.setHeightForWidth(self.textLog.sizePolicy().hasHeightForWidth())
        self.textLog.setSizePolicy(sizePolicy)
        self.textLog.setMaximumSize(QSize(16777215, 16777215))
        self.textLog.setFrameShape(QFrame.Box)
        self.textLog.setFrameShadow(QFrame.Sunken)

        self.gridCentral.addWidget(self.textLog, 6, 2, 2, 1)

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
        self.labelCamera.setText("")
        self.groupImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.pushFilter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
#if QT_CONFIG(tooltip)
        self.pushRotateLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate 90\u00b0 counterclockwise", None))
#endif // QT_CONFIG(tooltip)
        self.pushRotateLeft.setText("")
#if QT_CONFIG(tooltip)
        self.pushRotateRight.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate 90\u00b0 clockwise", None))
#endif // QT_CONFIG(tooltip)
        self.pushRotateRight.setText("")
#if QT_CONFIG(tooltip)
        self.pushFilpRightLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Flip right and left", None))
#endif // QT_CONFIG(tooltip)
        self.pushFilpRightLeft.setText("")
#if QT_CONFIG(tooltip)
        self.pushFlipUpDown.setToolTip(QCoreApplication.translate("MainWindow", u"Flip up and down", None))
#endif // QT_CONFIG(tooltip)
        self.pushFlipUpDown.setText("")
        self.labelRotationAngle.setText(QCoreApplication.translate("MainWindow", u"Angle (deg)", None))
        self.lineRotationAngle.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.pushAngleUp.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate clockwise by user angle", None))
#endif // QT_CONFIG(tooltip)
        self.pushAngleUp.setText("")
#if QT_CONFIG(tooltip)
        self.pushAngleDown.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate counterclockwise by user angle", None))
#endif // QT_CONFIG(tooltip)
        self.pushAngleDown.setText("")
        self.pushCalibration.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.pushROI.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
        self.groupProfile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        ___qtablewidgetitem = self.tableProfiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"x size (mm)", None));
        ___qtablewidgetitem1 = self.tableProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"y size (mm)", None));
        ___qtablewidgetitem2 = self.tableProfiles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.pushOpenImage.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.lineExposureTime.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.labelGain.setText(QCoreApplication.translate("MainWindow", u"Gain (%)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"(25 - 1000000)", None))
        self.labelFrameRate.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"(0 - 100)", None))
        self.labelExposureTime.setText(QCoreApplication.translate("MainWindow", u"Exp. Time (\u03bcs)", None))
        self.lineFrameRate.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.labelFrameRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 20)", None))
        self.lineGain.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelPosition.setText(QCoreApplication.translate("MainWindow", u"Center: (0.00, 0.00) mm Size: (0.00, 0.00) mm", None))
        self.groupBox_2.setTitle("")
        self.labelCameraPixmap.setText("")
        self.labelStatusCamera.setText(QCoreApplication.translate("MainWindow", u"  Camera", None))
        self.labelControllerPixmap.setText("")
        self.labelStatusController.setText(QCoreApplication.translate("MainWindow", u"  Controller", None))
        self.labelCalibrationPixmap.setText("")
        self.labelStatusCalibration.setText(QCoreApplication.translate("MainWindow", u"  Calibration", None))
        self.groupControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.lineRepeat.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(tooltip)
        self.pushScreenDown.setToolTip(QCoreApplication.translate("MainWindow", u"Put the screen monitor into the vacuum chamber", None))
#endif // QT_CONFIG(tooltip)
        self.pushScreenDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
#if QT_CONFIG(tooltip)
        self.labelRepeat.setToolTip(QCoreApplication.translate("MainWindow", u"Set the number of repeated image captures", None))
#endif // QT_CONFIG(tooltip)
        self.labelRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.pushCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.labelRepeatRange.setText(QCoreApplication.translate("MainWindow", u"(1 - 30)", None))
#if QT_CONFIG(tooltip)
        self.pushScreenUp.setToolTip(QCoreApplication.translate("MainWindow", u"Remove the screen monitor from the vacuum chamber", None))
#endif // QT_CONFIG(tooltip)
        self.pushScreenUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.pushStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.labelScreenStatus.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
#if QT_CONFIG(tooltip)
        self.labelScreen.setToolTip(QCoreApplication.translate("MainWindow", u"Adjusting the physical position of the screen. Ensure the control device is connected.", None))
#endif // QT_CONFIG(tooltip)
        self.labelScreen.setText(QCoreApplication.translate("MainWindow", u"Screen", None))
#if QT_CONFIG(tooltip)
        self.pushConnection.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushConnection.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
    # retranslateUi

