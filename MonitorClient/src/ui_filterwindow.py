# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_FilterWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(678, 318)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboFilter = QComboBox(Dialog)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")

        self.gridLayout.addWidget(self.comboFilter, 0, 0, 1, 1)

        self.pushOk = QPushButton(Dialog)
        self.pushOk.setObjectName(u"pushOk")

        self.gridLayout.addWidget(self.pushOk, 0, 3, 1, 1)

        self.frameImage = QFrame(Dialog)
        self.frameImage.setObjectName(u"frameImage")
        self.frameImage.setMinimumSize(QSize(300, 300))
        self.frameImage.setFrameShape(QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QFrame.Raised)
        self.gridImage = QGridLayout(self.frameImage)
        self.gridImage.setObjectName(u"gridImage")
        self.gridImage.setContentsMargins(0, 0, 0, 0)
        self.labelImage = QLabel(self.frameImage)
        self.labelImage.setObjectName(u"labelImage")

        self.gridImage.addWidget(self.labelImage, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameImage, 0, 2, 4, 1)

        self.pushApply = QPushButton(Dialog)
        self.pushApply.setObjectName(u"pushApply")

        self.gridLayout.addWidget(self.pushApply, 0, 1, 1, 1)

        self.pushCancel = QPushButton(Dialog)
        self.pushCancel.setObjectName(u"pushCancel")

        self.gridLayout.addWidget(self.pushCancel, 1, 3, 1, 1)

        self.listParameters = QListWidget(Dialog)
        self.listParameters.setObjectName(u"listParameters")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listParameters.sizePolicy().hasHeightForWidth())
        self.listParameters.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.listParameters, 1, 0, 3, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Dialog", u"Background Substraction", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Dialog", u"Gaussian", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("Dialog", u"Median", None))
        self.comboFilter.setItemText(4, QCoreApplication.translate("Dialog", u"Bilateral", None))

        self.pushOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.labelImage.setText("")
        self.pushApply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.pushCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

