# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        if not CalibrationWindow.objectName():
            CalibrationWindow.setObjectName(u"CalibrationWindow")
        CalibrationWindow.resize(832, 690)
        self.gridLayout_2 = QGridLayout(CalibrationWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frameOrigin = QFrame(CalibrationWindow)
        self.frameOrigin.setObjectName(u"frameOrigin")
        self.frameOrigin.setMinimumSize(QSize(400, 400))
        self.frameOrigin.setMaximumSize(QSize(400, 400))
        self.frameOrigin.setBaseSize(QSize(0, 0))
        self.frameOrigin.setFrameShape(QFrame.StyledPanel)
        self.frameOrigin.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frameOrigin)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.labelOrigin = QLabel(self.frameOrigin)
        self.labelOrigin.setObjectName(u"labelOrigin")
        self.labelOrigin.setMinimumSize(QSize(0, 0))
        self.labelOrigin.setMaximumSize(QSize(16777215, 16777215))
        self.labelOrigin.setBaseSize(QSize(0, 0))
        self.labelOrigin.setFocusPolicy(Qt.ClickFocus)
        self.labelOrigin.setFrameShape(QFrame.NoFrame)
        self.labelOrigin.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.labelOrigin, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameOrigin, 1, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelExplanation2 = QLabel(CalibrationWindow)
        self.labelExplanation2.setObjectName(u"labelExplanation2")
        font = QFont()
        font.setPointSize(11)
        self.labelExplanation2.setFont(font)

        self.verticalLayout.addWidget(self.labelExplanation2)

        self.label_4 = QLabel(CalibrationWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(CalibrationWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.labelExplanation = QLabel(CalibrationWindow)
        self.labelExplanation.setObjectName(u"labelExplanation")
        self.labelExplanation.setFont(font)

        self.verticalLayout.addWidget(self.labelExplanation)

        self.labelPosition = QLabel(CalibrationWindow)
        self.labelPosition.setObjectName(u"labelPosition")
        self.labelPosition.setFont(font)

        self.verticalLayout.addWidget(self.labelPosition)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 2)

        self.pushCalCapture = QPushButton(CalibrationWindow)
        self.pushCalCapture.setObjectName(u"pushCalCapture")
        self.pushCalCapture.setFont(font)

        self.gridLayout_2.addWidget(self.pushCalCapture, 0, 1, 1, 1)

        self.pushConvert = QPushButton(CalibrationWindow)
        self.pushConvert.setObjectName(u"pushConvert")
        self.pushConvert.setFont(font)
        self.pushConvert.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_2.addWidget(self.pushConvert, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(CalibrationWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 3, 3, 1, 3)

        self.frameTrans = QFrame(CalibrationWindow)
        self.frameTrans.setObjectName(u"frameTrans")
        self.frameTrans.setMinimumSize(QSize(400, 400))
        self.frameTrans.setMaximumSize(QSize(400, 400))
        self.frameTrans.setBaseSize(QSize(0, 0))
        self.frameTrans.setFrameShape(QFrame.StyledPanel)
        self.frameTrans.setFrameShadow(QFrame.Plain)
        self.gridLayout_12 = QGridLayout(self.frameTrans)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.labelTrans = QLabel(self.frameTrans)
        self.labelTrans.setObjectName(u"labelTrans")
        self.labelTrans.setMinimumSize(QSize(0, 0))
        self.labelTrans.setMaximumSize(QSize(16777215, 16777215))
        self.labelTrans.setBaseSize(QSize(0, 0))
        self.labelTrans.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.labelTrans, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addWidget(self.frameTrans, 1, 3, 1, 3)

        self.pushOpenImage = QPushButton(CalibrationWindow)
        self.pushOpenImage.setObjectName(u"pushOpenImage")
        self.pushOpenImage.setFont(font)
        self.pushOpenImage.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_2.addWidget(self.pushOpenImage, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.linePixel2y = QLineEdit(CalibrationWindow)
        self.linePixel2y.setObjectName(u"linePixel2y")
        self.linePixel2y.setMaximumSize(QSize(80, 16777215))
        self.linePixel2y.setFont(font)

        self.gridLayout.addWidget(self.linePixel2y, 4, 4, 1, 1)

        self.label_9 = QLabel(CalibrationWindow)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)

        self.linePixel4x = QLineEdit(CalibrationWindow)
        self.linePixel4x.setObjectName(u"linePixel4x")
        self.linePixel4x.setMaximumSize(QSize(80, 16777215))
        self.linePixel4x.setFont(font)

        self.gridLayout.addWidget(self.linePixel4x, 6, 3, 1, 1)

        self.linePixel4y = QLineEdit(CalibrationWindow)
        self.linePixel4y.setObjectName(u"linePixel4y")
        self.linePixel4y.setMaximumSize(QSize(80, 16777215))
        self.linePixel4y.setFont(font)

        self.gridLayout.addWidget(self.linePixel4y, 6, 4, 1, 1)

        self.lineReal2x = QLineEdit(CalibrationWindow)
        self.lineReal2x.setObjectName(u"lineReal2x")
        self.lineReal2x.setMaximumSize(QSize(80, 16777215))
        self.lineReal2x.setFont(font)

        self.gridLayout.addWidget(self.lineReal2x, 4, 1, 1, 1)

        self.lineReal3y = QLineEdit(CalibrationWindow)
        self.lineReal3y.setObjectName(u"lineReal3y")
        self.lineReal3y.setMaximumSize(QSize(80, 16777215))
        self.lineReal3y.setFont(font)

        self.gridLayout.addWidget(self.lineReal3y, 5, 2, 1, 1)

        self.label = QLabel(CalibrationWindow)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 3, 1, 2)

        self.lineReal3x = QLineEdit(CalibrationWindow)
        self.lineReal3x.setObjectName(u"lineReal3x")
        self.lineReal3x.setMaximumSize(QSize(80, 16777215))
        self.lineReal3x.setFont(font)

        self.gridLayout.addWidget(self.lineReal3x, 5, 1, 1, 1)

        self.lineReal4x = QLineEdit(CalibrationWindow)
        self.lineReal4x.setObjectName(u"lineReal4x")
        self.lineReal4x.setMaximumSize(QSize(80, 16777215))
        self.lineReal4x.setFont(font)

        self.gridLayout.addWidget(self.lineReal4x, 6, 1, 1, 1)

        self.label_14 = QLabel(CalibrationWindow)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.label_8 = QLabel(CalibrationWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_3 = QLabel(CalibrationWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)

        self.label_7 = QLabel(CalibrationWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 2)

        self.lineReal4y = QLineEdit(CalibrationWindow)
        self.lineReal4y.setObjectName(u"lineReal4y")
        self.lineReal4y.setMaximumSize(QSize(80, 16777215))
        self.lineReal4y.setFont(font)

        self.gridLayout.addWidget(self.lineReal4y, 6, 2, 1, 1)

        self.lineReal1y = QLineEdit(CalibrationWindow)
        self.lineReal1y.setObjectName(u"lineReal1y")
        self.lineReal1y.setMaximumSize(QSize(80, 16777215))
        self.lineReal1y.setFont(font)

        self.gridLayout.addWidget(self.lineReal1y, 3, 2, 1, 1)

        self.linePixel2x = QLineEdit(CalibrationWindow)
        self.linePixel2x.setObjectName(u"linePixel2x")
        self.linePixel2x.setMaximumSize(QSize(80, 16777215))
        self.linePixel2x.setFont(font)

        self.gridLayout.addWidget(self.linePixel2x, 4, 3, 1, 1)

        self.lineReal1x = QLineEdit(CalibrationWindow)
        self.lineReal1x.setObjectName(u"lineReal1x")
        self.lineReal1x.setMaximumSize(QSize(80, 16777215))
        self.lineReal1x.setFont(font)

        self.gridLayout.addWidget(self.lineReal1x, 3, 1, 1, 1)

        self.label_12 = QLabel(CalibrationWindow)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_11 = QLabel(CalibrationWindow)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.linePixel3y = QLineEdit(CalibrationWindow)
        self.linePixel3y.setObjectName(u"linePixel3y")
        self.linePixel3y.setMaximumSize(QSize(80, 16777215))
        self.linePixel3y.setFont(font)

        self.gridLayout.addWidget(self.linePixel3y, 5, 4, 1, 1)

        self.label_2 = QLabel(CalibrationWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.linePixel1x = QLineEdit(CalibrationWindow)
        self.linePixel1x.setObjectName(u"linePixel1x")
        self.linePixel1x.setMaximumSize(QSize(80, 16777215))
        self.linePixel1x.setFont(font)

        self.gridLayout.addWidget(self.linePixel1x, 3, 3, 1, 1)

        self.label_13 = QLabel(CalibrationWindow)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.labelPerspective = QLabel(CalibrationWindow)
        self.labelPerspective.setObjectName(u"labelPerspective")
        self.labelPerspective.setFont(font)

        self.gridLayout.addWidget(self.labelPerspective, 0, 0, 1, 5)

        self.linePixel1y = QLineEdit(CalibrationWindow)
        self.linePixel1y.setObjectName(u"linePixel1y")
        self.linePixel1y.setMaximumSize(QSize(80, 16777215))
        self.linePixel1y.setFont(font)

        self.gridLayout.addWidget(self.linePixel1y, 3, 4, 1, 1)

        self.label_10 = QLabel(CalibrationWindow)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)

        self.lineReal2y = QLineEdit(CalibrationWindow)
        self.lineReal2y.setObjectName(u"lineReal2y")
        self.lineReal2y.setMaximumSize(QSize(80, 16777215))
        self.lineReal2y.setFont(font)

        self.gridLayout.addWidget(self.lineReal2y, 4, 2, 1, 1)

        self.linePixel3x = QLineEdit(CalibrationWindow)
        self.linePixel3x.setObjectName(u"linePixel3x")
        self.linePixel3x.setMaximumSize(QSize(80, 16777215))
        self.linePixel3x.setFont(font)

        self.gridLayout.addWidget(self.linePixel3x, 5, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 3, 1, 3)

        self.pushReset = QPushButton(CalibrationWindow)
        self.pushReset.setObjectName(u"pushReset")
        self.pushReset.setMinimumSize(QSize(132, 28))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.pushReset.setFont(font1)

        self.gridLayout_2.addWidget(self.pushReset, 0, 3, 1, 1)

        QWidget.setTabOrder(self.pushCalCapture, self.lineReal1x)
        QWidget.setTabOrder(self.lineReal1x, self.lineReal1y)
        QWidget.setTabOrder(self.lineReal1y, self.lineReal2x)
        QWidget.setTabOrder(self.lineReal2x, self.lineReal2y)
        QWidget.setTabOrder(self.lineReal2y, self.lineReal3x)
        QWidget.setTabOrder(self.lineReal3x, self.lineReal3y)
        QWidget.setTabOrder(self.lineReal3y, self.lineReal4x)
        QWidget.setTabOrder(self.lineReal4x, self.lineReal4y)
        QWidget.setTabOrder(self.lineReal4y, self.linePixel1x)
        QWidget.setTabOrder(self.linePixel1x, self.linePixel1y)
        QWidget.setTabOrder(self.linePixel1y, self.linePixel2x)
        QWidget.setTabOrder(self.linePixel2x, self.linePixel2y)
        QWidget.setTabOrder(self.linePixel2y, self.linePixel3x)
        QWidget.setTabOrder(self.linePixel3x, self.linePixel3y)
        QWidget.setTabOrder(self.linePixel3y, self.linePixel4x)
        QWidget.setTabOrder(self.linePixel4x, self.linePixel4y)

        self.retranslateUi(CalibrationWindow)
        self.buttonBox.accepted.connect(CalibrationWindow.accept)
        self.buttonBox.rejected.connect(CalibrationWindow.reject)

        QMetaObject.connectSlotsByName(CalibrationWindow)
    # setupUi

    def retranslateUi(self, CalibrationWindow):
        CalibrationWindow.setWindowTitle(QCoreApplication.translate("CalibrationWindow", u"Dialog", None))
        self.labelOrigin.setText("")
        self.labelExplanation2.setText(QCoreApplication.translate("CalibrationWindow", u"Left click: Add transformation point", None))
        self.label_4.setText(QCoreApplication.translate("CalibrationWindow", u"Right click: Erase transformation point", None))
        self.label_5.setText(QCoreApplication.translate("CalibrationWindow", u"Ctrl + right double click: Enlarge calibration image", None))
        self.labelExplanation.setText(QCoreApplication.translate("CalibrationWindow", u"Ctrl + arrow keys: Move last point", None))
        self.labelPosition.setText(QCoreApplication.translate("CalibrationWindow", u"Current Position:", None))
        self.pushCalCapture.setText(QCoreApplication.translate("CalibrationWindow", u"Capture", None))
        self.pushConvert.setText(QCoreApplication.translate("CalibrationWindow", u"Convert", None))
        self.labelTrans.setText("")
        self.pushOpenImage.setText(QCoreApplication.translate("CalibrationWindow", u"Open", None))
        self.linePixel2y.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("CalibrationWindow", u"x (mm)", None))
        self.linePixel4x.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.linePixel4y.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.lineReal2x.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.lineReal3y.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.label.setText(QCoreApplication.translate("CalibrationWindow", u"Pixel space", None))
        self.lineReal3x.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.lineReal4x.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.label_14.setText(QCoreApplication.translate("CalibrationWindow", u"4", None))
        self.label_8.setText(QCoreApplication.translate("CalibrationWindow", u"Point", None))
        self.label_3.setText(QCoreApplication.translate("CalibrationWindow", u"y", None))
        self.label_7.setText(QCoreApplication.translate("CalibrationWindow", u"Real space ", None))
        self.lineReal4y.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.lineReal1y.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.linePixel2x.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.lineReal1x.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.label_12.setText(QCoreApplication.translate("CalibrationWindow", u"2", None))
        self.label_11.setText(QCoreApplication.translate("CalibrationWindow", u"1", None))
        self.linePixel3y.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("CalibrationWindow", u"x", None))
        self.linePixel1x.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("CalibrationWindow", u"3", None))
        self.labelPerspective.setText(QCoreApplication.translate("CalibrationWindow", u"Perspective Matrix", None))
        self.linePixel1y.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("CalibrationWindow", u"y (mm)", None))
        self.lineReal2y.setText(QCoreApplication.translate("CalibrationWindow", u"0.0", None))
        self.linePixel3x.setText(QCoreApplication.translate("CalibrationWindow", u"0", None))
        self.pushReset.setText(QCoreApplication.translate("CalibrationWindow", u"Reset", None))
    # retranslateUi

