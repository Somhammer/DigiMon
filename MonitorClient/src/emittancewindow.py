import os, sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

import numpy as np
from scipy.optimize import curve_fit

from src.ui_emittancewindow import Ui_EmittanceWindow

class EmittanceWindow(QDialog, Ui_EmittanceWindow):
    logger_signal = Signal(str, str)
    def __init__(self, parent, images, xbeam_size, ybeam_size):
        super(EmittanceWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)

        self.images = images
        self.xbeam_size = xbeam_size
        self.ybeam_size = ybeam_size

        self.emittance = [0.0, 0.0]
        self.alpha = [0.0, 0.0]
        self.beta = [0.0, 0.0]
        self.gamma = [0.0, 0.0]

        for image in self.images:
            item = QListWidgetItem(image)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked)
            self.listProfiles.addItem(item)

        self.set_action()
        self.show()

    def set_action(self):
        self.logger_signal.connect(self.parent.receive_log)

        self.comboMethod.currentTextChanged.connect(self.draw_plots_for_measurement)
        self.pushRun.clicked.connect(self.measure_emittance)

    def draw_plots_for_measurement(self):
        if self.comboMethod.currentText() == "3D Profile":
            try:
                self.plots_for_3d_profile()
            except:
                self.logger_signal.emit("ERROR","Measurement is failed.")
        elif self.comboMethod.currentText() == "Quadrupole Scan":
            self.plots_for_quad_scan()
        else:
            return
    
    def plots_for_3d_profile(self):
        pass

    def plots_for_quad_scan(self):
            self.gview = pg.GraphicsView()
            self.glayout = pg.GraphicsLayout(border=(255,255,255))
            self.gview.setCentralItem(glayout)

            self.plotSize = glayout.addPlot(title="Beam Size", row=1, col=1)
            self.plotSize.showGrid(x=True, y=True)
            self.plotSize.setLabel('left', 'Beam Size', 'mm')
            self.plotSize.setLabel('bottom', 'Coil Current', 'A')
            self.plotSize.setXRange(-10, 10)
            self.plotSize.setYRange(0, 20)
            self.plotSize.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            self.plotSize.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)

            self.plotFitError = glayout.addPlot(title="Beam Size", row=1, col=2)
            self.plotFitError.showGrid(x=True, y=True)
            self.plotFitError.setLabel('left', 'Beam Size', 'mm')
            self.plotFitError.setLabel('bottom', 'Coil Current', 'A')
            self.plotFitError.setXRange(-10, 10)
            self.plotFitError.setYRange(0, 20)

            self.plotXbeamSize = glayout.addPlot(title="Beam Size", row=1, col=2)
            self.plotXbeamSize.showGrid(x=True, y=True)
            self.plotXbeamSize.setLabel('left', 'Beam Size', 'mm')
            self.plotXbeamSize.setLabel('bottom', 'Coil Current', 'A')
            self.plotXbeamSize.setXRange(-10, 10)
            self.plotXbeamSize.setYRange(0, 20)

            self.plotYbeamSize = glayout.addPlot(title="Beam Size", row=1, col=2)
            self.plotYbeamSize.showGrid(x=True, y=True)
            self.plotYbeamSize.setLabel('left', 'Beam Size', 'mm')
            self.plotYbeamSize.setLabel('bottom', 'Coil Current', 'A')
            self.plotYbeamSize.setXRange(-10, 10)
            self.plotYbeamSize.setYRange(0, 20)

            self.gridPlot.addWidget(gview)
    def measure_emittance(self):
        if self.comboMethod.currentText() == "3D Profile":
            self.execute_3d_profile()
        elif self.comboMethod.currentText() == "Quadrupole Scan":
            self.execute_quad_scan()
        else:
            return

    def execute_3d_profile(self):
        pass

    def execute_quad_scan(self):
        pass
    