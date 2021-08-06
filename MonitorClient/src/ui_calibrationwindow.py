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
        Dialog.resize(780, 348)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frameOrigin = QFrame(Dialog)
        self.frameOrigin.setObjectName(u"frameOrigin")
        self.frameOrigin.setFrameShape(QFrame.StyledPanel)
        self.frameOrigin.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frameOrigin, 0, 1, 1, 1)

        self.frameTrans = QFrame(Dialog)
        self.frameTrans.setObjectName(u"frameTrans")
        self.frameTrans.setFrameShape(QFrame.StyledPanel)
        self.frameTrans.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frameTrans, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 2)

        self.listPictures = QListWidget(Dialog)
        self.listPictures.setObjectName(u"listPictures")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listPictures.sizePolicy().hasHeightForWidth())
        self.listPictures.setSizePolicy(sizePolicy)
        self.listPictures.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.listPictures, 0, 0, 2, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

