# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hidden.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_HiddenWindow(object):
    def setupUi(self, CloseServer):
        if not CloseServer.objectName():
            CloseServer.setObjectName(u"CloseServer")
        CloseServer.resize(400, 70)
        icon = QIcon()
        icon.addFile(u"../icons/ncc.png", QSize(), QIcon.Normal, QIcon.Off)
        CloseServer.setWindowIcon(icon)
        self.gridLayout = QGridLayout(CloseServer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(CloseServer)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(CloseServer)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(CloseServer)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.retranslateUi(CloseServer)
        self.buttonBox.accepted.connect(CloseServer.accept)
        self.buttonBox.rejected.connect(CloseServer.reject)

        QMetaObject.connectSlotsByName(CloseServer)
    # setupUi

    def retranslateUi(self, CloseServer):
        CloseServer.setWindowTitle(QCoreApplication.translate("CloseServer", u"Close Server", None))
        self.label.setText(QCoreApplication.translate("CloseServer", u"Password: ", None))
    # retranslateUi

