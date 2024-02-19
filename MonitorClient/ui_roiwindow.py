# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roi.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from digilabel import DigiLabel

class Ui_ROIWindow(object):
    def setupUi(self, ROIWindow):
        if not ROIWindow.objectName():
            ROIWindow.setObjectName(u"ROIWindow")
        ROIWindow.resize(644, 397)
        self.gridLayout_3 = QGridLayout(ROIWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 77, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(ROIWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        font = QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 4, 1, 3, 1)

        self.label_3 = QLabel(ROIWindow)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(ROIWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.groupROI = QGroupBox(ROIWindow)
        self.groupROI.setObjectName(u"groupROI")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.groupROI.setFont(font2)
        self.gridLayout_2 = QGridLayout(self.groupROI)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sliderWidth = QSlider(self.groupROI)
        self.sliderWidth.setObjectName(u"sliderWidth")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderWidth.sizePolicy().hasHeightForWidth())
        self.sliderWidth.setSizePolicy(sizePolicy)
        self.sliderWidth.setMaximum(1000)
        self.sliderWidth.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderWidth, 4, 2, 1, 1)

        self.sliderY0 = QSlider(self.groupROI)
        self.sliderY0.setObjectName(u"sliderY0")
        sizePolicy.setHeightForWidth(self.sliderY0.sizePolicy().hasHeightForWidth())
        self.sliderY0.setSizePolicy(sizePolicy)
        self.sliderY0.setMaximum(1000)
        self.sliderY0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderY0, 2, 2, 1, 1)

        self.sliderX0 = QSlider(self.groupROI)
        self.sliderX0.setObjectName(u"sliderX0")
        sizePolicy.setHeightForWidth(self.sliderX0.sizePolicy().hasHeightForWidth())
        self.sliderX0.setSizePolicy(sizePolicy)
        self.sliderX0.setFocusPolicy(Qt.StrongFocus)
        self.sliderX0.setMaximum(1000)
        self.sliderX0.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderX0, 1, 2, 1, 1)

        self.labelX0 = QLabel(self.groupROI)
        self.labelX0.setObjectName(u"labelX0")
        self.labelX0.setMaximumSize(QSize(50, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.labelX0.setFont(font3)

        self.gridLayout_2.addWidget(self.labelX0, 1, 0, 1, 1)

        self.labelHeight = QLabel(self.groupROI)
        self.labelHeight.setObjectName(u"labelHeight")
        self.labelHeight.setMaximumSize(QSize(100, 16777215))
        self.labelHeight.setFont(font3)

        self.gridLayout_2.addWidget(self.labelHeight, 5, 0, 1, 1)

        self.labelSPPixel = QLabel(self.groupROI)
        self.labelSPPixel.setObjectName(u"labelSPPixel")
        self.labelSPPixel.setFont(font3)

        self.gridLayout_2.addWidget(self.labelSPPixel, 0, 2, 1, 1)

        self.lineWidth = QLineEdit(self.groupROI)
        self.lineWidth.setObjectName(u"lineWidth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineWidth.sizePolicy().hasHeightForWidth())
        self.lineWidth.setSizePolicy(sizePolicy1)
        self.lineWidth.setMaximumSize(QSize(50, 16777215))
        self.lineWidth.setFont(font3)
        self.lineWidth.setFocusPolicy(Qt.NoFocus)
        self.lineWidth.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineWidth, 4, 1, 1, 1)

        self.lineHeight = QLineEdit(self.groupROI)
        self.lineHeight.setObjectName(u"lineHeight")
        sizePolicy1.setHeightForWidth(self.lineHeight.sizePolicy().hasHeightForWidth())
        self.lineHeight.setSizePolicy(sizePolicy1)
        self.lineHeight.setMaximumSize(QSize(50, 16777215))
        self.lineHeight.setFont(font3)
        self.lineHeight.setFocusPolicy(Qt.NoFocus)
        self.lineHeight.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineHeight, 5, 1, 1, 1)

        self.labelSP = QLabel(self.groupROI)
        self.labelSP.setObjectName(u"labelSP")
        self.labelSP.setFont(font3)

        self.gridLayout_2.addWidget(self.labelSP, 0, 0, 1, 2)

        self.lineY0 = QLineEdit(self.groupROI)
        self.lineY0.setObjectName(u"lineY0")
        sizePolicy1.setHeightForWidth(self.lineY0.sizePolicy().hasHeightForWidth())
        self.lineY0.setSizePolicy(sizePolicy1)
        self.lineY0.setMaximumSize(QSize(50, 16777215))
        self.lineY0.setFont(font3)
        self.lineY0.setFocusPolicy(Qt.NoFocus)
        self.lineY0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineY0, 2, 1, 1, 1)

        self.labelY0 = QLabel(self.groupROI)
        self.labelY0.setObjectName(u"labelY0")
        self.labelY0.setMaximumSize(QSize(50, 16777215))
        self.labelY0.setFont(font3)

        self.gridLayout_2.addWidget(self.labelY0, 2, 0, 1, 1)

        self.labelSize = QLabel(self.groupROI)
        self.labelSize.setObjectName(u"labelSize")
        self.labelSize.setFont(font3)

        self.gridLayout_2.addWidget(self.labelSize, 3, 0, 1, 2)

        self.lineX0 = QLineEdit(self.groupROI)
        self.lineX0.setObjectName(u"lineX0")
        sizePolicy1.setHeightForWidth(self.lineX0.sizePolicy().hasHeightForWidth())
        self.lineX0.setSizePolicy(sizePolicy1)
        self.lineX0.setMaximumSize(QSize(50, 16777215))
        self.lineX0.setFont(font3)
        self.lineX0.setFocusPolicy(Qt.NoFocus)
        self.lineX0.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineX0, 1, 1, 1, 1)

        self.labelSizePixel = QLabel(self.groupROI)
        self.labelSizePixel.setObjectName(u"labelSizePixel")
        self.labelSizePixel.setFont(font3)

        self.gridLayout_2.addWidget(self.labelSizePixel, 3, 2, 1, 1)

        self.sliderHeight = QSlider(self.groupROI)
        self.sliderHeight.setObjectName(u"sliderHeight")
        sizePolicy.setHeightForWidth(self.sliderHeight.sizePolicy().hasHeightForWidth())
        self.sliderHeight.setSizePolicy(sizePolicy)
        self.sliderHeight.setMaximum(1000)
        self.sliderHeight.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sliderHeight, 5, 2, 1, 1)

        self.labelWidth = QLabel(self.groupROI)
        self.labelWidth.setObjectName(u"labelWidth")
        self.labelWidth.setMaximumSize(QSize(1000, 16777215))
        self.labelWidth.setFont(font3)

        self.gridLayout_2.addWidget(self.labelWidth, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupROI, 0, 1, 1, 1)

        self.frameImage = QFrame(ROIWindow)
        self.frameImage.setObjectName(u"frameImage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameImage.sizePolicy().hasHeightForWidth())
        self.frameImage.setSizePolicy(sizePolicy2)
        self.frameImage.setMinimumSize(QSize(310, 310))
        self.frameImage.setMaximumSize(QSize(310, 310))
        self.frameImage.setBaseSize(QSize(0, 0))
        self.frameImage.setLayoutDirection(Qt.LeftToRight)
        self.frameImage.setFrameShape(QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frameImage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImage = DigiLabel(self.frameImage)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setMinimumSize(QSize(300, 300))
        self.labelImage.setMaximumSize(QSize(16777215, 16777215))
        self.labelImage.setBaseSize(QSize(0, 0))
        self.labelImage.setFocusPolicy(Qt.ClickFocus)
        self.labelImage.setFrameShape(QFrame.NoFrame)
        self.labelImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelImage, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameImage, 0, 0, 3, 1)

        self.label_4 = QLabel(ROIWindow)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.label_4.setFont(font4)

        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)


        self.retranslateUi(ROIWindow)
        self.buttonBox.accepted.connect(ROIWindow.accept)
        self.buttonBox.rejected.connect(ROIWindow.reject)

        QMetaObject.connectSlotsByName(ROIWindow)
    # setupUi

    def retranslateUi(self, ROIWindow):
        ROIWindow.setWindowTitle(QCoreApplication.translate("ROIWindow", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("ROIWindow", u"Double click: Apply ROI", None))
        self.label_2.setText(QCoreApplication.translate("ROIWindow", u"Left click + drag: Select ROI", None))
        self.groupROI.setTitle(QCoreApplication.translate("ROIWindow", u"Region of Interest", None))
        self.labelX0.setText(QCoreApplication.translate("ROIWindow", u"  x (%)", None))
        self.labelHeight.setText(QCoreApplication.translate("ROIWindow", u"  height (%)", None))
        self.labelSPPixel.setText(QCoreApplication.translate("ROIWindow", u"(0,0) pixel", None))
        self.lineWidth.setText(QCoreApplication.translate("ROIWindow", u"0", None))
        self.lineHeight.setText(QCoreApplication.translate("ROIWindow", u"0", None))
        self.labelSP.setText(QCoreApplication.translate("ROIWindow", u"Start Point", None))
        self.lineY0.setText(QCoreApplication.translate("ROIWindow", u"0", None))
        self.labelY0.setText(QCoreApplication.translate("ROIWindow", u"  y (%)", None))
        self.labelSize.setText(QCoreApplication.translate("ROIWindow", u"ROI Size", None))
        self.lineX0.setText(QCoreApplication.translate("ROIWindow", u"0", None))
        self.labelSizePixel.setText(QCoreApplication.translate("ROIWindow", u"(0,0) pixel", None))
        self.labelWidth.setText(QCoreApplication.translate("ROIWindow", u"  width (%)", None))
        self.labelImage.setText("")
        self.label_4.setText(QCoreApplication.translate("ROIWindow", u"Right double click: Cancel", None))
    # retranslateUi

