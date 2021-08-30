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
        Dialog.resize(1006, 596)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushLoad = QPushButton(Dialog)
        self.pushLoad.setObjectName(u"pushLoad")
        self.pushLoad.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.pushLoad, 0, 2, 1, 1)

        self.groupCamera = QGroupBox(Dialog)
        self.groupCamera.setObjectName(u"groupCamera")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupCamera.sizePolicy().hasHeightForWidth())
        self.groupCamera.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupCamera.setFont(font)
        self.gridCamera = QGridLayout(self.groupCamera)
        self.gridCamera.setObjectName(u"gridCamera")
        self.sliderExposureTime = QSlider(self.groupCamera)
        self.sliderExposureTime.setObjectName(u"sliderExposureTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sliderExposureTime.sizePolicy().hasHeightForWidth())
        self.sliderExposureTime.setSizePolicy(sizePolicy1)
        self.sliderExposureTime.setFocusPolicy(Qt.TabFocus)
        self.sliderExposureTime.setMinimum(1)
        self.sliderExposureTime.setMaximum(1000)
        self.sliderExposureTime.setValue(500)
        self.sliderExposureTime.setOrientation(Qt.Horizontal)

        self.gridCamera.addWidget(self.sliderExposureTime, 1, 2, 1, 2)

        self.lineGain = QLineEdit(self.groupCamera)
        self.lineGain.setObjectName(u"lineGain")
        self.lineGain.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineGain.sizePolicy().hasHeightForWidth())
        self.lineGain.setSizePolicy(sizePolicy2)
        self.lineGain.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.lineGain.setFont(font1)
        self.lineGain.setFocusPolicy(Qt.NoFocus)
        self.lineGain.setReadOnly(True)

        self.gridCamera.addWidget(self.lineGain, 0, 1, 1, 1)

        self.labelExposureTime = QLabel(self.groupCamera)
        self.labelExposureTime.setObjectName(u"labelExposureTime")
        self.labelExposureTime.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTime, 1, 0, 1, 1)

        self.lineExposureTime = QLineEdit(self.groupCamera)
        self.lineExposureTime.setObjectName(u"lineExposureTime")
        sizePolicy2.setHeightForWidth(self.lineExposureTime.sizePolicy().hasHeightForWidth())
        self.lineExposureTime.setSizePolicy(sizePolicy2)
        self.lineExposureTime.setMaximumSize(QSize(50, 16777215))
        self.lineExposureTime.setFont(font1)
        self.lineExposureTime.setFocusPolicy(Qt.NoFocus)
        self.lineExposureTime.setReadOnly(True)

        self.gridCamera.addWidget(self.lineExposureTime, 1, 1, 1, 1)

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

        self.labelExposureTimeRange = QLabel(self.groupCamera)
        self.labelExposureTimeRange.setObjectName(u"labelExposureTimeRange")
        self.labelExposureTimeRange.setFont(font1)

        self.gridCamera.addWidget(self.labelExposureTimeRange, 1, 4, 1, 1)

        self.labelGainRange = QLabel(self.groupCamera)
        self.labelGainRange.setObjectName(u"labelGainRange")
        sizePolicy.setHeightForWidth(self.labelGainRange.sizePolicy().hasHeightForWidth())
        self.labelGainRange.setSizePolicy(sizePolicy)
        self.labelGainRange.setMaximumSize(QSize(100, 16777215))
        self.labelGainRange.setFont(font1)

        self.gridCamera.addWidget(self.labelGainRange, 0, 4, 1, 1)


        self.gridLayout_3.addWidget(self.groupCamera, 1, 1, 1, 4)

        self.pushOk = QPushButton(Dialog)
        self.pushOk.setObjectName(u"pushOk")
        self.pushOk.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.pushOk, 4, 3, 1, 1)

        self.comboSetup = QComboBox(Dialog)
        self.comboSetup.setObjectName(u"comboSetup")
        self.comboSetup.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.comboSetup, 0, 0, 1, 1)

        self.pushSave = QPushButton(Dialog)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.pushSave, 0, 1, 1, 1)

        self.groupROI = QGroupBox(Dialog)
        self.groupROI.setObjectName(u"groupROI")
        self.groupROI.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupROI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelWidth = QLabel(self.groupROI)
        self.labelWidth.setObjectName(u"labelWidth")
        self.labelWidth.setMaximumSize(QSize(1000, 16777215))
        self.labelWidth.setFont(font1)

        self.gridLayout_2.addWidget(self.labelWidth, 4, 0, 1, 1)

        self.sliderX0 = QSlider(self.groupROI)
        self.sliderX0.setObjectName(u"sliderX0")
        sizePolicy1.setHeightForWidth(self.sliderX0.sizePolicy().hasHeightForWidth())
        self.sliderX0.setSizePolicy(sizePolicy1)
        self.sliderX0.setFocusPolicy(Qt.StrongFocus)
        self.sliderX0.setMaximum(1000)
        self.sliderX0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderX0, 1, 2, 1, 1)

        self.labelX0 = QLabel(self.groupROI)
        self.labelX0.setObjectName(u"labelX0")
        self.labelX0.setMaximumSize(QSize(50, 16777215))
        self.labelX0.setFont(font1)

        self.gridLayout_2.addWidget(self.labelX0, 1, 0, 1, 1)

        self.lineX0 = QLineEdit(self.groupROI)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy2.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy2)
        self.lineX0.setMaximumSize(QSize(50, 16777215))
        self.lineX0.setFont(font1)
        self.lineX0.setFocusPolicy(Qt.NoFocus)
        self.lineX0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineX0, 1, 1, 1, 1)

        self.lineHeight = QLineEdit(self.groupROI)
        self.lineHeight.setObjectName(u"lineHeight")
        sizePolicy2.setHeightForWidth(self.lineHeight.sizePolicy().hasHeightForWidth())
        self.lineHeight.setSizePolicy(sizePolicy2)
        self.lineHeight.setMaximumSize(QSize(50, 16777215))
        self.lineHeight.setFont(font1)
        self.lineHeight.setFocusPolicy(Qt.NoFocus)
        self.lineHeight.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineHeight, 5, 1, 1, 1)

        self.sliderHeight = QSlider(self.groupROI)
        self.sliderHeight.setObjectName(u"sliderHeight")
        sizePolicy1.setHeightForWidth(self.sliderHeight.sizePolicy().hasHeightForWidth())
        self.sliderHeight.setSizePolicy(sizePolicy1)
        self.sliderHeight.setMaximum(1000)
        self.sliderHeight.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderHeight, 5, 2, 1, 1)

        self.sliderWidth = QSlider(self.groupROI)
        self.sliderWidth.setObjectName(u"sliderWidth")
        sizePolicy1.setHeightForWidth(self.sliderWidth.sizePolicy().hasHeightForWidth())
        self.sliderWidth.setSizePolicy(sizePolicy1)
        self.sliderWidth.setMaximum(1000)
        self.sliderWidth.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderWidth, 4, 2, 1, 1)

        self.labelSizePixel = QLabel(self.groupROI)
        self.labelSizePixel.setObjectName(u"labelSizePixel")
        self.labelSizePixel.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSizePixel, 3, 2, 1, 1)

        self.lineWidth = QLineEdit(self.groupROI)
        self.lineWidth.setObjectName(u"lineWidth")
        sizePolicy2.setHeightForWidth(self.lineWidth.sizePolicy().hasHeightForWidth())
        self.lineWidth.setSizePolicy(sizePolicy2)
        self.lineWidth.setMaximumSize(QSize(50, 16777215))
        self.lineWidth.setFont(font1)
        self.lineWidth.setFocusPolicy(Qt.NoFocus)
        self.lineWidth.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineWidth, 4, 1, 1, 1)

        self.lineY0 = QLineEdit(self.groupROI)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy2.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy2)
        self.lineY0.setMaximumSize(QSize(50, 16777215))
        self.lineY0.setFont(font1)
        self.lineY0.setFocusPolicy(Qt.NoFocus)
        self.lineY0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineY0, 2, 1, 1, 1)

        self.labelY0 = QLabel(self.groupROI)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setMaximumSize(QSize(50, 16777215))
        self.labelY0.setFont(font1)

        self.gridLayout_2.addWidget(self.labelY0, 2, 0, 1, 1)

        self.labelHeight = QLabel(self.groupROI)
        self.labelHeight.setObjectName(u"labelHeight")
        self.labelHeight.setMaximumSize(QSize(100, 16777215))
        self.labelHeight.setFont(font1)

        self.gridLayout_2.addWidget(self.labelHeight, 5, 0, 1, 1)

        self.labelSize = QLabel(self.groupROI)
        self.labelSize.setObjectName(u"labelSize")
        self.labelSize.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSize, 3, 0, 1, 2)

        self.labelSP = QLabel(self.groupROI)
        self.labelSP.setObjectName(u"labelSP")
        self.labelSP.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSP, 0, 0, 1, 2)

        self.sliderY0 = QSlider(self.groupROI)
        self.sliderY0.setObjectName(u"sliderY0")
        sizePolicy1.setHeightForWidth(self.sliderY0.sizePolicy().hasHeightForWidth())
        self.sliderY0.setSizePolicy(sizePolicy1)
        self.sliderY0.setMaximum(1000)
        self.sliderY0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderY0, 2, 2, 1, 1)

        self.labelSPPixel = QLabel(self.groupROI)
        self.labelSPPixel.setObjectName(u"labelSPPixel")
        self.labelSPPixel.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSPPixel, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupROI, 2, 1, 1, 4)

        self.pushCalibration = QPushButton(Dialog)
        self.pushCalibration.setObjectName(u"pushCalibration")
        self.pushCalibration.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.pushCalibration, 4, 1, 1, 1)

        self.pushCancel = QPushButton(Dialog)
        self.pushCancel.setObjectName(u"pushCancel")
        self.pushCancel.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_3.addWidget(self.pushCancel, 4, 4, 1, 1)

        self.frameImage = QFrame(Dialog)
        self.frameImage.setObjectName(u"frameImage")
        sizePolicy.setHeightForWidth(self.frameImage.sizePolicy().hasHeightForWidth())
        self.frameImage.setSizePolicy(sizePolicy)
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

        self.gridLayout.addWidget(self.labelImage, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameImage, 1, 0, 5, 1)

        self.groupFilter = QGroupBox(Dialog)
        self.groupFilter.setObjectName(u"groupFilter")
        self.groupFilter.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupFilter)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboFilter = QComboBox(self.groupFilter)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        sizePolicy.setHeightForWidth(self.comboFilter.sizePolicy().hasHeightForWidth())
        self.comboFilter.setSizePolicy(sizePolicy)
        self.comboFilter.setFont(font1)

        self.gridLayout_4.addWidget(self.comboFilter, 0, 0, 1, 1)

        self.listParameters = QListWidget(self.groupFilter)
        self.listParameters.setObjectName(u"listParameters")
        sizePolicy.setHeightForWidth(self.listParameters.sizePolicy().hasHeightForWidth())
        self.listParameters.setSizePolicy(sizePolicy)
        self.listParameters.setFont(font1)

        self.gridLayout_4.addWidget(self.listParameters, 1, 0, 1, 2)

        self.pushFilterApply = QPushButton(self.groupFilter)
        self.pushFilterApply.setObjectName(u"pushFilterApply")
        sizePolicy1.setHeightForWidth(self.pushFilterApply.sizePolicy().hasHeightForWidth())
        self.pushFilterApply.setSizePolicy(sizePolicy1)
        self.pushFilterApply.setFont(font1)

        self.gridLayout_4.addWidget(self.pushFilterApply, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupFilter, 3, 1, 1, 4)

        QWidget.setTabOrder(self.sliderGain, self.sliderExposureTime)
        QWidget.setTabOrder(self.sliderExposureTime, self.sliderX0)
        QWidget.setTabOrder(self.sliderX0, self.sliderWidth)
        QWidget.setTabOrder(self.sliderWidth, self.sliderHeight)
        QWidget.setTabOrder(self.sliderHeight, self.sliderY0)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Setup", None))
        self.pushLoad.setText(QCoreApplication.translate("Dialog", u"Load", None))
        self.groupCamera.setTitle(QCoreApplication.translate("Dialog", u"Camera", None))
        self.lineGain.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.labelExposureTime.setText(QCoreApplication.translate("Dialog", u"Exposure Time (ms)", None))
        self.lineExposureTime.setText(QCoreApplication.translate("Dialog", u"500", None))
        self.labelGain.setText(QCoreApplication.translate("Dialog", u"Gain (%)", None))
        self.labelExposureTimeRange.setText(QCoreApplication.translate("Dialog", u"(1- 1000)", None))
        self.labelGainRange.setText(QCoreApplication.translate("Dialog", u"(0 - 200)", None))
        self.pushOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pushSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.groupROI.setTitle(QCoreApplication.translate("Dialog", u"Region of Interest", None))
        self.labelWidth.setText(QCoreApplication.translate("Dialog", u"  width (%)", None))
        self.labelX0.setText(QCoreApplication.translate("Dialog", u"  x (%)", None))
        self.lineX0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lineHeight.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.labelSizePixel.setText(QCoreApplication.translate("Dialog", u"(0,0) pixel", None))
        self.lineWidth.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.lineY0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.labelY0.setText(QCoreApplication.translate("Dialog", u"  y (%)", None))
        self.labelHeight.setText(QCoreApplication.translate("Dialog", u"  height (%)", None))
        self.labelSize.setText(QCoreApplication.translate("Dialog", u"ROI Size", None))
        self.labelSP.setText(QCoreApplication.translate("Dialog", u"Start Point", None))
        self.labelSPPixel.setText(QCoreApplication.translate("Dialog", u"(0,0) pixel", None))
        self.pushCalibration.setText(QCoreApplication.translate("Dialog", u"Calibration", None))
        self.pushCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.labelImage.setText("")
        self.groupFilter.setTitle(QCoreApplication.translate("Dialog", u"Filter", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Dialog", u"No Filter", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Dialog", u"Background Substraction", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("Dialog", u"Gaussian", None))
        self.comboFilter.setItemText(4, QCoreApplication.translate("Dialog", u"Median", None))
        self.comboFilter.setItemText(5, QCoreApplication.translate("Dialog", u"Bilateral", None))

        self.pushFilterApply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

