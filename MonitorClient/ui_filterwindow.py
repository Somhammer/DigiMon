# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import os
from variables import BASE_PATH

class Ui_FilterWindow(object):
    def setupUi(self, FilterWindow):
        if not FilterWindow.objectName():
            FilterWindow.setObjectName(u"FilterWindow")
        FilterWindow.resize(727, 329)
        icon = QIcon()
        icon.addFile(os.path.join(BASE_PATH, "icons/ncc.png"), QSize(), QIcon.Normal, QIcon.Off)
        FilterWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(FilterWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(FilterWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 3)

        self.frameImage = QFrame(FilterWindow)
        self.frameImage.setObjectName(u"frameImage")
        self.frameImage.setMinimumSize(QSize(310, 310))
        self.frameImage.setMaximumSize(QSize(310, 310))
        self.frameImage.setFrameShape(QFrame.Box)
        self.frameImage.setFrameShadow(QFrame.Plain)
        self.gridImage = QGridLayout(self.frameImage)
        self.gridImage.setObjectName(u"gridImage")
        self.gridImage.setContentsMargins(0, 0, 0, 0)
        self.labelImage = QLabel(self.frameImage)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setMinimumSize(QSize(300, 300))
        self.labelImage.setMaximumSize(QSize(300, 300))

        self.gridImage.addWidget(self.labelImage, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameImage, 0, 0, 4, 1)

        self.pushApplyFilter = QPushButton(FilterWindow)
        self.pushApplyFilter.setObjectName(u"pushApplyFilter")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushApplyFilter.sizePolicy().hasHeightForWidth())
        self.pushApplyFilter.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.pushApplyFilter.setFont(font1)

        self.gridLayout.addWidget(self.pushApplyFilter, 0, 3, 1, 1)

        self.comboFilter = QComboBox(FilterWindow)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboFilter.sizePolicy().hasHeightForWidth())
        self.comboFilter.setSizePolicy(sizePolicy1)
        self.comboFilter.setFont(font1)

        self.gridLayout.addWidget(self.comboFilter, 0, 1, 1, 2)

        self.listParameters = QListWidget(FilterWindow)
        self.listParameters.setObjectName(u"listParameters")
        sizePolicy1.setHeightForWidth(self.listParameters.sizePolicy().hasHeightForWidth())
        self.listParameters.setSizePolicy(sizePolicy1)
        self.listParameters.setFont(font1)

        self.gridLayout.addWidget(self.listParameters, 1, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 3)


        self.retranslateUi(FilterWindow)
        self.buttonBox.accepted.connect(FilterWindow.accept)
        self.buttonBox.rejected.connect(FilterWindow.reject)

        QMetaObject.connectSlotsByName(FilterWindow)
    # setupUi

    def retranslateUi(self, FilterWindow):
        FilterWindow.setWindowTitle(QCoreApplication.translate("FilterWindow", u"Dialog", None))
        self.labelImage.setText("")
        self.pushApplyFilter.setText(QCoreApplication.translate("FilterWindow", u"Apply", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("FilterWindow", u"Select", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("FilterWindow", u"No Filter", None))
        self.comboFilter.setItemText(2, QCoreApplication.translate("FilterWindow", u"Gaussian", None))
        self.comboFilter.setItemText(3, QCoreApplication.translate("FilterWindow", u"Median", None))
        self.comboFilter.setItemText(4, QCoreApplication.translate("FilterWindow", u"Bilateral", None))

    # retranslateUi

