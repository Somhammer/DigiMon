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
        Dialog.resize(710, 318)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboFilter = QComboBox(Dialog)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")

        self.gridLayout.addWidget(self.comboFilter, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridParameters = QGridLayout(self.groupBox)
        self.gridParameters.setObjectName(u"gridParameters")

        self.gridLayout.addWidget(self.groupBox, 1, 0, 2, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 2, 3, 1)

        self.frameImage = QFrame(Dialog)
        self.frameImage.setObjectName(u"frameImage")
        self.frameImage.setFrameShape(QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frameImage, 0, 1, 3, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Dialog", u"Gaussian", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("Dialog", u"Median", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("Dialog", u"Bilateral", None))

        self.groupBox.setTitle("")
    # retranslateUi

