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
        Dialog.resize(824, 496)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelPosition = QLabel(Dialog)
        self.labelPosition.setObjectName(u"labelPosition")

        self.gridLayout.addWidget(self.labelPosition, 3, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 1)

        self.pushOpen = QPushButton(Dialog)
        self.pushOpen.setObjectName(u"pushOpen")

        self.gridLayout.addWidget(self.pushOpen, 0, 0, 1, 1)

        self.frameTrans = QFrame(Dialog)
        self.frameTrans.setObjectName(u"frameTrans")
        self.frameTrans.setMinimumSize(QSize(400, 400))
        self.frameTrans.setFrameShape(QFrame.StyledPanel)
        self.frameTrans.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameTrans)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelTrans = QLabel(self.frameTrans)
        self.labelTrans.setObjectName(u"labelTrans")

        self.gridLayout_3.addWidget(self.labelTrans, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameTrans, 1, 2, 1, 1)

        self.frameOrigin = QFrame(Dialog)
        self.frameOrigin.setObjectName(u"frameOrigin")
        self.frameOrigin.setMinimumSize(QSize(400, 400))
        self.frameOrigin.setFrameShape(QFrame.StyledPanel)
        self.frameOrigin.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameOrigin)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelOrigin = QLabel(self.frameOrigin)
        self.labelOrigin.setObjectName(u"labelOrigin")

        self.gridLayout_2.addWidget(self.labelOrigin, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameOrigin, 1, 0, 1, 2)

        self.pushConvert = QPushButton(Dialog)
        self.pushConvert.setObjectName(u"pushConvert")

        self.gridLayout.addWidget(self.pushConvert, 3, 1, 1, 1)

        self.labelExplain = QLabel(Dialog)
        self.labelExplain.setObjectName(u"labelExplain")

        self.gridLayout.addWidget(self.labelExplain, 2, 0, 1, 2)

        self.labelFile = QLabel(Dialog)
        self.labelFile.setObjectName(u"labelFile")

        self.gridLayout.addWidget(self.labelFile, 0, 1, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Calibration", None))
        self.labelPosition.setText(QCoreApplication.translate("Dialog", u"Position:", None))
        self.pushOpen.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.labelTrans.setText("")
        self.labelOrigin.setText("")
        self.pushConvert.setText(QCoreApplication.translate("Dialog", u"Convert", None))
        self.labelExplain.setText(QCoreApplication.translate("Dialog", u"Left click: Add point,  Right click: Erase point", None))
        self.labelFile.setText(QCoreApplication.translate("Dialog", u"Image:", None))
    # retranslateUi

