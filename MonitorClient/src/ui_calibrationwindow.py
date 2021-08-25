# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_CalibrationWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(924, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frameOrigin = QFrame(Dialog)
        self.frameOrigin.setObjectName(u"frameOrigin")
        self.frameOrigin.setMinimumSize(QSize(450, 450))
        self.frameOrigin.setMaximumSize(QSize(450, 450))
        self.frameOrigin.setFrameShape(QFrame.StyledPanel)
        self.frameOrigin.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameOrigin)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelOrigin = QLabel(self.frameOrigin)
        self.labelOrigin.setObjectName(u"labelOrigin")
        self.labelOrigin.setMinimumSize(QSize(450, 450))
        self.labelOrigin.setMaximumSize(QSize(450, 450))
        self.labelOrigin.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_2.addWidget(self.labelOrigin, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frameOrigin, 1, 0, 1, 1)

        self.frameTrans = QFrame(Dialog)
        self.frameTrans.setObjectName(u"frameTrans")
        self.frameTrans.setMinimumSize(QSize(450, 450))
        self.frameTrans.setMaximumSize(QSize(450, 450))
        self.frameTrans.setFrameShape(QFrame.StyledPanel)
        self.frameTrans.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameTrans)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelTrans = QLabel(self.frameTrans)
        self.labelTrans.setObjectName(u"labelTrans")
        self.labelTrans.setMinimumSize(QSize(450, 450))
        self.labelTrans.setMaximumSize(QSize(450, 450))

        self.gridLayout_3.addWidget(self.labelTrans, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameTrans, 1, 1, 1, 4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 2, 1, 1, 1)

        self.linePixelHeight = QLineEdit(Dialog)
        self.linePixelHeight.setObjectName(u"linePixelHeight")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.linePixelHeight.sizePolicy().hasHeightForWidth())
        self.linePixelHeight.setSizePolicy(sizePolicy1)
        self.linePixelHeight.setMaximumSize(QSize(80, 16777215))
        self.linePixelHeight.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_4.addWidget(self.linePixelHeight, 3, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(10, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 3, 1, 1)

        self.lineHeight = QLineEdit(Dialog)
        self.lineHeight.setObjectName(u"lineHeight")
        sizePolicy1.setHeightForWidth(self.lineHeight.sizePolicy().hasHeightForWidth())
        self.lineHeight.setSizePolicy(sizePolicy1)
        self.lineHeight.setMaximumSize(QSize(80, 16777215))
        self.lineHeight.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_4.addWidget(self.lineHeight, 0, 4, 1, 1)

        self.lineWidth = QLineEdit(Dialog)
        self.lineWidth.setObjectName(u"lineWidth")
        sizePolicy1.setHeightForWidth(self.lineWidth.sizePolicy().hasHeightForWidth())
        self.lineWidth.setSizePolicy(sizePolicy1)
        self.lineWidth.setMaximumSize(QSize(80, 16777215))
        self.lineWidth.setFocusPolicy(Qt.ClickFocus)
        self.lineWidth.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.lineWidth, 0, 2, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 3, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)

        self.linePixelWidth = QLineEdit(Dialog)
        self.linePixelWidth.setObjectName(u"linePixelWidth")
        sizePolicy1.setHeightForWidth(self.linePixelWidth.sizePolicy().hasHeightForWidth())
        self.linePixelWidth.setSizePolicy(sizePolicy1)
        self.linePixelWidth.setMaximumSize(QSize(80, 16777215))
        self.linePixelWidth.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_4.addWidget(self.linePixelWidth, 2, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 5)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 4, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 2, 1, 1, 4)

        self.pushOpen = QPushButton(Dialog)
        self.pushOpen.setObjectName(u"pushOpen")
        self.pushOpen.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.pushOpen, 0, 2, 1, 1)

        self.pushConvert = QPushButton(Dialog)
        self.pushConvert.setObjectName(u"pushConvert")
        self.pushConvert.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.pushConvert, 3, 2, 1, 1)

        self.pushOk = QPushButton(Dialog)
        self.pushOk.setObjectName(u"pushOk")
        self.pushOk.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.pushOk, 3, 3, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 2)

        self.labelExplain = QLabel(Dialog)
        self.labelExplain.setObjectName(u"labelExplain")

        self.gridLayout_5.addWidget(self.labelExplain, 1, 0, 1, 2)

        self.labelPosition = QLabel(Dialog)
        self.labelPosition.setObjectName(u"labelPosition")

        self.gridLayout_5.addWidget(self.labelPosition, 2, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.pushCancel = QPushButton(Dialog)
        self.pushCancel.setObjectName(u"pushCancel")
        self.pushCancel.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.pushCancel, 3, 4, 1, 1)

        self.pushSave = QPushButton(Dialog)
        self.pushSave.setObjectName(u"pushSave")
        sizePolicy1.setHeightForWidth(self.pushSave.sizePolicy().hasHeightForWidth())
        self.pushSave.setSizePolicy(sizePolicy1)
        self.pushSave.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.pushSave, 0, 1, 1, 1)

        self.comboCalibration = QComboBox(Dialog)
        self.comboCalibration.addItem("")
        self.comboCalibration.setObjectName(u"comboCalibration")
        sizePolicy1.setHeightForWidth(self.comboCalibration.sizePolicy().hasHeightForWidth())
        self.comboCalibration.setSizePolicy(sizePolicy1)
        self.comboCalibration.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.comboCalibration, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Calibration", None))
        self.labelOrigin.setText("")
        self.labelTrans.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Horizontal:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Vertical:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Transformed image size:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Pixel to actual length of original image", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"mm/pixel", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"mm/pixel", None))
        self.pushOpen.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.pushConvert.setText(QCoreApplication.translate("Dialog", u"Convert", None))
        self.pushOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ctrl + arrow keys: Move last point", None))
        self.labelExplain.setText(QCoreApplication.translate("Dialog", u"Left click: Add point,  Right click: Erase point", None))
        self.labelPosition.setText(QCoreApplication.translate("Dialog", u"Position:", None))
        self.pushCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.comboCalibration.setItemText(0, "")

    # retranslateUi

