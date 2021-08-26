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
        Dialog.resize(1128, 890)
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

        self.tableProfiles = QTableWidget(Dialog)
        if (self.tableProfiles.columnCount() < 5):
            self.tableProfiles.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProfiles.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableProfiles.setObjectName(u"tableProfiles")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableProfiles.sizePolicy().hasHeightForWidth())
        self.tableProfiles.setSizePolicy(sizePolicy)
        self.tableProfiles.setMaximumSize(QSize(300, 16777215))
        self.tableProfiles.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableProfiles)

        self.groupParameters = QGroupBox(Dialog)
        self.groupParameters.setObjectName(u"groupParameters")
        self.gridParameters = QGridLayout(self.groupParameters)
        self.gridParameters.setObjectName(u"gridParameters")

        self.verticalLayout.addWidget(self.groupParameters)

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
        self.gridPlots = QGridLayout(self.framePlot)
        self.gridPlots.setObjectName(u"gridPlots")
        self.gridPlots.setContentsMargins(0, 0, 0, 0)

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
        self.gridEmittance = QGridLayout()
        self.gridEmittance.setSpacing(6)
        self.gridEmittance.setObjectName(u"gridEmittance")
        self.lineEmittanceY = QLineEdit(self.groupBox)
        self.lineEmittanceY.setObjectName(u"lineEmittanceY")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEmittanceY.sizePolicy().hasHeightForWidth())
        self.lineEmittanceY.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.lineEmittanceY.setFont(font2)
        self.lineEmittanceY.setReadOnly(True)

        self.gridEmittance.addWidget(self.lineEmittanceY, 2, 1, 1, 1)

        self.labelEmitY = QLabel(self.groupBox)
        self.labelEmitY.setObjectName(u"labelEmitY")
        self.labelEmitY.setMaximumSize(QSize(20, 16777215))
        self.labelEmitY.setFont(font2)
        self.labelEmitY.setAlignment(Qt.AlignCenter)

        self.gridEmittance.addWidget(self.labelEmitY, 2, 0, 1, 1)

        self.labelEmittance = QLabel(self.groupBox)
        self.labelEmittance.setObjectName(u"labelEmittance")
        sizePolicy.setHeightForWidth(self.labelEmittance.sizePolicy().hasHeightForWidth())
        self.labelEmittance.setSizePolicy(sizePolicy)
        self.labelEmittance.setMaximumSize(QSize(16777215, 10))
        self.labelEmittance.setFont(font2)
        self.labelEmittance.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridEmittance.addWidget(self.labelEmittance, 0, 0, 1, 2)

        self.labelunit1 = QLabel(self.groupBox)
        self.labelunit1.setObjectName(u"labelunit1")
        self.labelunit1.setMaximumSize(QSize(80, 16777215))
        self.labelunit1.setFont(font2)

        self.gridEmittance.addWidget(self.labelunit1, 1, 2, 1, 1)

        self.labelEmitX = QLabel(self.groupBox)
        self.labelEmitX.setObjectName(u"labelEmitX")
        self.labelEmitX.setMaximumSize(QSize(30, 16777215))
        self.labelEmitX.setFont(font2)
        self.labelEmitX.setAlignment(Qt.AlignCenter)

        self.gridEmittance.addWidget(self.labelEmitX, 1, 0, 1, 1)

        self.labelunit2 = QLabel(self.groupBox)
        self.labelunit2.setObjectName(u"labelunit2")
        self.labelunit2.setMaximumSize(QSize(80, 16777215))
        self.labelunit2.setFont(font2)

        self.gridEmittance.addWidget(self.labelunit2, 2, 2, 1, 1)

        self.lineEmittanceX = QLineEdit(self.groupBox)
        self.lineEmittanceX.setObjectName(u"lineEmittanceX")
        sizePolicy1.setHeightForWidth(self.lineEmittanceX.sizePolicy().hasHeightForWidth())
        self.lineEmittanceX.setSizePolicy(sizePolicy1)
        self.lineEmittanceX.setFont(font2)
        self.lineEmittanceX.setReadOnly(True)

        self.gridEmittance.addWidget(self.lineEmittanceX, 1, 1, 1, 1)


        self.gridResult.addLayout(self.gridEmittance, 0, 0, 1, 1)

        self.gridTwiss = QGridLayout()
        self.gridTwiss.setObjectName(u"gridTwiss")
        self.labelBeta = QLabel(self.groupBox)
        self.labelBeta.setObjectName(u"labelBeta")
        self.labelBeta.setMaximumSize(QSize(60, 16777215))
        self.labelBeta.setFont(font2)
        self.labelBeta.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelBeta, 3, 0, 1, 1)

        self.lineGammaY = QLineEdit(self.groupBox)
        self.lineGammaY.setObjectName(u"lineGammaY")
        sizePolicy1.setHeightForWidth(self.lineGammaY.sizePolicy().hasHeightForWidth())
        self.lineGammaY.setSizePolicy(sizePolicy1)
        self.lineGammaY.setFont(font2)
        self.lineGammaY.setReadOnly(True)

        self.gridTwiss.addWidget(self.lineGammaY, 4, 2, 1, 1)

        self.labelAlpha = QLabel(self.groupBox)
        self.labelAlpha.setObjectName(u"labelAlpha")
        self.labelAlpha.setMaximumSize(QSize(60, 16777215))
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
        self.labelGamma.setMaximumSize(QSize(60, 16777215))
        self.labelGamma.setFont(font2)
        self.labelGamma.setAlignment(Qt.AlignCenter)

        self.gridTwiss.addWidget(self.labelGamma, 4, 0, 1, 1)

        self.lineBetaY = QLineEdit(self.groupBox)
        self.lineBetaY.setObjectName(u"lineBetaY")
        sizePolicy1.setHeightForWidth(self.lineBetaY.sizePolicy().hasHeightForWidth())
        self.lineBetaY.setSizePolicy(sizePolicy1)
        self.lineBetaY.setFont(font2)
        self.lineBetaY.setReadOnly(True)

        self.gridTwiss.addWidget(self.lineBetaY, 3, 2, 1, 1)

        self.lineAlphaX = QLineEdit(self.groupBox)
        self.lineAlphaX.setObjectName(u"lineAlphaX")
        sizePolicy1.setHeightForWidth(self.lineAlphaX.sizePolicy().hasHeightForWidth())
        self.lineAlphaX.setSizePolicy(sizePolicy1)
        self.lineAlphaX.setFont(font2)
        self.lineAlphaX.setReadOnly(True)

        self.gridTwiss.addWidget(self.lineAlphaX, 2, 1, 1, 1)

        self.lineGammaX = QLineEdit(self.groupBox)
        self.lineGammaX.setObjectName(u"lineGammaX")
        sizePolicy1.setHeightForWidth(self.lineGammaX.sizePolicy().hasHeightForWidth())
        self.lineGammaX.setSizePolicy(sizePolicy1)
        self.lineGammaX.setFont(font2)
        self.lineGammaX.setReadOnly(True)

        self.gridTwiss.addWidget(self.lineGammaX, 4, 1, 1, 1)

        self.labelTwiss = QLabel(self.groupBox)
        self.labelTwiss.setObjectName(u"labelTwiss")
        self.labelTwiss.setFont(font2)

        self.gridTwiss.addWidget(self.labelTwiss, 0, 0, 1, 3)

        self.lineBetaX = QLineEdit(self.groupBox)
        self.lineBetaX.setObjectName(u"lineBetaX")
        sizePolicy1.setHeightForWidth(self.lineBetaX.sizePolicy().hasHeightForWidth())
        self.lineBetaX.setSizePolicy(sizePolicy1)
        self.lineBetaX.setFont(font2)
        self.lineBetaX.setReadOnly(True)

        self.gridTwiss.addWidget(self.lineBetaX, 3, 1, 1, 1)

        self.lineAlphaY = QLineEdit(self.groupBox)
        self.lineAlphaY.setObjectName(u"lineAlphaY")
        sizePolicy1.setHeightForWidth(self.lineAlphaY.sizePolicy().hasHeightForWidth())
        self.lineAlphaY.setSizePolicy(sizePolicy1)
        self.lineAlphaY.setFont(font2)
        self.lineAlphaY.setReadOnly(True)

        self.gridTwiss.addWidget(self.lineAlphaY, 2, 2, 1, 1)


        self.gridResult.addLayout(self.gridTwiss, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.textLog = QTextBrowser(Dialog)
        self.textLog.setObjectName(u"textLog")

        self.verticalLayout_2.addWidget(self.textLog)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboMethod.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboMethod.setItemText(1, QCoreApplication.translate("Dialog", u"3D Profile", None))
        self.comboMethod.setItemText(2, QCoreApplication.translate("Dialog", u"Quadrupole Scan", None))

        ___qtablewidgetitem = self.tableProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Current", None));
        ___qtablewidgetitem1 = self.tableProfiles.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Beam Size(x)", None));
        ___qtablewidgetitem2 = self.tableProfiles.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Beam Size(y)", None));
        ___qtablewidgetitem3 = self.tableProfiles.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Image", None));
        self.groupParameters.setTitle(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.pushRun.setText(QCoreApplication.translate("Dialog", u"Run", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Result", None))
        self.lineEmittanceY.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.labelEmitY.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.labelEmittance.setText(QCoreApplication.translate("Dialog", u"Emittance", None))
        self.labelunit1.setText(QCoreApplication.translate("Dialog", u"mm mrad", None))
        self.labelEmitX.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.labelunit2.setText(QCoreApplication.translate("Dialog", u"mm mrad", None))
        self.lineEmittanceX.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.labelBeta.setText(QCoreApplication.translate("Dialog", u"beta", None))
        self.lineGammaY.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.labelAlpha.setText(QCoreApplication.translate("Dialog", u"alpha", None))
        self.labelTwissX.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.labelTwissY.setText(QCoreApplication.translate("Dialog", u"y", None))
        self.labelGamma.setText(QCoreApplication.translate("Dialog", u"gamma", None))
        self.lineBetaY.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.lineAlphaX.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.lineGammaX.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.labelTwiss.setText(QCoreApplication.translate("Dialog", u"Twiss Parameters", None))
        self.lineBetaX.setText(QCoreApplication.translate("Dialog", u"0.0", None))
        self.lineAlphaY.setText(QCoreApplication.translate("Dialog", u"0.0", None))
    # retranslateUi

