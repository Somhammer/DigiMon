# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emittance.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_EmittanceWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1017, 827)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboMethod = QComboBox(Dialog)
        self.comboMethod.addItem("")
        self.comboMethod.addItem("")
        self.comboMethod.addItem("")
        self.comboMethod.setObjectName(u"comboMethod")

        self.verticalLayout.addWidget(self.comboMethod)

        self.listProfiles = QListWidget(Dialog)
        self.listProfiles.setObjectName(u"listProfiles")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listProfiles.sizePolicy().hasHeightForWidth())
        self.listProfiles.setSizePolicy(sizePolicy)
        self.listProfiles.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.listProfiles)

        self.pushRun = QPushButton(Dialog)
        self.pushRun.setObjectName(u"pushRun")
        font = QFont()
        font.setPointSize(10)
        self.pushRun.setFont(font)

        self.verticalLayout.addWidget(self.pushRun)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.framePlot = QFrame(Dialog)
        self.framePlot.setObjectName(u"framePlot")
        self.framePlot.setMinimumSize(QSize(800, 600))
        self.framePlot.setFrameShape(QFrame.StyledPanel)
        self.framePlot.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.framePlot)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.gridResult = QGridLayout(self.groupBox)
        self.gridResult.setObjectName(u"gridResult")
        self.gridResult.setContentsMargins(0, 0, 0, 0)
        self.gridTwiss = QGridLayout()
        self.gridTwiss.setObjectName(u"gridTwiss")
        self.labelBeta = QLabel(self.groupBox)
        self.labelBeta.setObjectName(u"labelBeta")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.labelBeta.setFont(font2)
        self.labelBeta.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelBeta, 3, 0, 1, 1)

        self.lineEditGammaY = QLineEdit(self.groupBox)
        self.lineEditGammaY.setObjectName(u"lineEditGammaY")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditGammaY.sizePolicy().hasHeightForWidth())
        self.lineEditGammaY.setSizePolicy(sizePolicy1)
        self.lineEditGammaY.setFont(font2)

        self.gridTwiss.addWidget(self.lineEditGammaY, 4, 2, 1, 1)

        self.labelAlpha = QLabel(self.groupBox)
        self.labelAlpha.setObjectName(u"labelAlpha")
        self.labelAlpha.setMaximumSize(QSize(40, 16777215))
        self.labelAlpha.setFont(font2)
        self.labelAlpha.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelAlpha, 2, 0, 1, 1)

        self.labelTwissX = QLabel(self.groupBox)
        self.labelTwissX.setObjectName(u"labelTwissX")
        self.labelTwissX.setFont(font2)
        self.labelTwissX.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelTwissX, 1, 1, 1, 1)

        self.labelTwissY = QLabel(self.groupBox)
        self.labelTwissY.setObjectName(u"labelTwissY")
        self.labelTwissY.setFont(font2)
        self.labelTwissY.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelTwissY, 1, 2, 1, 1)

        self.labelGamma = QLabel(self.groupBox)
        self.labelGamma.setObjectName(u"labelGamma")
        self.labelGamma.setFont(font2)
        self.labelGamma.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelGamma, 4, 0, 1, 1)

        self.lineEditBetaY = QLineEdit(self.groupBox)
        self.lineEditBetaY.setObjectName(u"lineEditBetaY")
        sizePolicy1.setHeightForWidth(self.lineEditBetaY.sizePolicy().hasHeightForWidth())
        self.lineEditBetaY.setSizePolicy(sizePolicy1)
        self.lineEditBetaY.setFont(font2)

        self.gridTwiss.addWidget(self.lineEditBetaY, 3, 2, 1, 1)

        self.lineEditAlphaX = QLineEdit(self.groupBox)
        self.lineEditAlphaX.setObjectName(u"lineEditAlphaX")
        sizePolicy1.setHeightForWidth(self.lineEditAlphaX.sizePolicy().hasHeightForWidth())
        self.lineEditAlphaX.setSizePolicy(sizePolicy1)
        self.lineEditAlphaX.setFont(font2)

        self.gridTwiss.addWidget(self.lineEditAlphaX, 2, 1, 1, 1)

        self.lineEditGammaX = QLineEdit(self.groupBox)
        self.lineEditGammaX.setObjectName(u"lineEditGammaX")
        sizePolicy1.setHeightForWidth(self.lineEditGammaX.sizePolicy().hasHeightForWidth())
        self.lineEditGammaX.setSizePolicy(sizePolicy1)
        self.lineEditGammaX.setFont(font2)

        self.gridTwiss.addWidget(self.lineEditGammaX, 4, 1, 1, 1)

        self.labelTwiss = QLabel(self.groupBox)
        self.labelTwiss.setObjectName(u"labelTwiss")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.labelTwiss.setFont(font3)

        self.gridTwiss.addWidget(self.labelTwiss, 0, 0, 1, 3)

        self.lineEditBetaX = QLineEdit(self.groupBox)
        self.lineEditBetaX.setObjectName(u"lineEditBetaX")
        sizePolicy1.setHeightForWidth(self.lineEditBetaX.sizePolicy().hasHeightForWidth())
        self.lineEditBetaX.setSizePolicy(sizePolicy1)
        self.lineEditBetaX.setFont(font2)

        self.gridTwiss.addWidget(self.lineEditBetaX, 3, 1, 1, 1)

        self.lineEditAlphaY = QLineEdit(self.groupBox)
        self.lineEditAlphaY.setObjectName(u"lineEditAlphaY")
        sizePolicy1.setHeightForWidth(self.lineEditAlphaY.sizePolicy().hasHeightForWidth())
        self.lineEditAlphaY.setSizePolicy(sizePolicy1)
        self.lineEditAlphaY.setFont(font2)

        self.gridTwiss.addWidget(self.lineEditAlphaY, 2, 2, 1, 1)


        self.gridResult.addLayout(self.gridTwiss, 0, 1, 1, 1)

        self.gridEmittance = QGridLayout()
        self.gridEmittance.setSpacing(6)
        self.gridEmittance.setObjectName(u"gridEmittance")
        self.labelEmitX = QLabel(self.groupBox)
        self.labelEmitX.setObjectName(u"labelEmitX")
        self.labelEmitX.setMaximumSize(QSize(30, 16777215))
        self.labelEmitX.setFont(font2)
        self.labelEmitX.setAlignment(Qt.AlignCenter)

        self.gridEmittance.addWidget(self.labelEmitX, 1, 0, 1, 1)

        self.labelEmitY = QLabel(self.groupBox)
        self.labelEmitY.setObjectName(u"labelEmitY")
        self.labelEmitY.setMaximumSize(QSize(20, 16777215))
        self.labelEmitY.setFont(font2)
        self.labelEmitY.setAlignment(Qt.AlignCenter)

        self.gridEmittance.addWidget(self.labelEmitY, 2, 0, 1, 1)

        self.lineEmittanceY = QLineEdit(self.groupBox)
        self.lineEmittanceY.setObjectName(u"lineEmittanceY")
        sizePolicy1.setHeightForWidth(self.lineEmittanceY.sizePolicy().hasHeightForWidth())
        self.lineEmittanceY.setSizePolicy(sizePolicy1)
        self.lineEmittanceY.setFont(font2)

        self.gridEmittance.addWidget(self.lineEmittanceY, 2, 1, 1, 1)

        self.labelblank2 = QLabel(self.groupBox)
        self.labelblank2.setObjectName(u"labelblank2")

        self.gridEmittance.addWidget(self.labelblank2, 4, 0, 1, 2)

        self.labelEmittance = QLabel(self.groupBox)
        self.labelEmittance.setObjectName(u"labelEmittance")
        sizePolicy.setHeightForWidth(self.labelEmittance.sizePolicy().hasHeightForWidth())
        self.labelEmittance.setSizePolicy(sizePolicy)
        self.labelEmittance.setMaximumSize(QSize(16777215, 166))
        self.labelEmittance.setFont(font3)
        self.labelEmittance.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridEmittance.addWidget(self.labelEmittance, 0, 0, 1, 2)

        self.labelblank1 = QLabel(self.groupBox)
        self.labelblank1.setObjectName(u"labelblank1")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.labelblank1.setFont(font4)

        self.gridEmittance.addWidget(self.labelblank1, 3, 0, 1, 2)

        self.lineEmittanceX = QLineEdit(self.groupBox)
        self.lineEmittanceX.setObjectName(u"lineEmittanceX")
        sizePolicy1.setHeightForWidth(self.lineEmittanceX.sizePolicy().hasHeightForWidth())
        self.lineEmittanceX.setSizePolicy(sizePolicy1)
        self.lineEmittanceX.setFont(font2)

        self.gridEmittance.addWidget(self.lineEmittanceX, 1, 1, 1, 1)

        self.labelunit1 = QLabel(self.groupBox)
        self.labelunit1.setObjectName(u"labelunit1")
        self.labelunit1.setMaximumSize(QSize(80, 16777215))
        self.labelunit1.setFont(font3)

        self.gridEmittance.addWidget(self.labelunit1, 1, 2, 1, 1)

        self.labelunit2 = QLabel(self.groupBox)
        self.labelunit2.setObjectName(u"labelunit2")
        self.labelunit2.setMaximumSize(QSize(80, 16777215))
        self.labelunit2.setFont(font3)

        self.gridEmittance.addWidget(self.labelunit2, 2, 2, 1, 1)


        self.gridResult.addLayout(self.gridEmittance, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboMethod.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboMethod.setItemText(1, QCoreApplication.translate("Dialog", u"3D Profile", None))
        self.comboMethod.setItemText(2, QCoreApplication.translate("Dialog", u"Quadrupole Scan", None))

        self.pushRun.setText(QCoreApplication.translate("Dialog", u"Run", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Result", None))
        self.labelBeta.setText(QCoreApplication.translate("Dialog", u"beta", None))
        self.labelAlpha.setText(QCoreApplication.translate("Dialog", u"alpha", None))
        self.labelTwissX.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.labelTwissY.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.labelGamma.setText(QCoreApplication.translate("Dialog", u"gamma", None))
        self.labelTwiss.setText(QCoreApplication.translate("Dialog", u"Twiss Parameters", None))
        self.labelEmitX.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.labelEmitY.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.labelblank2.setText("")
        self.labelEmittance.setText(QCoreApplication.translate("Dialog", u"Emittance", None))
        self.labelblank1.setText("")
        self.labelunit1.setText(QCoreApplication.translate("Dialog", u"mm mrad", None))
        self.labelunit2.setText(QCoreApplication.translate("Dialog", u"mm mrad", None))
    # retranslateUi

