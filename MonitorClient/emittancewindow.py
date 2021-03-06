import os, sys
import time
import datetime
import logging

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pyqtgraph as pg

import math
import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

from logger import LogStringHandler
from ui_emittancewindow import Ui_EmittanceWindow

class EmittanceWindow(QDialog, Ui_EmittanceWindow):
    logger_signal = Signal(str, str)
    def __init__(self, parent):
        super(EmittanceWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = LogStringHandler(self.textLog)
        self.logger.addHandler(handler)

        self.outdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output', datetime.datetime.today().strftime('%y%m%d'))
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
        if not os.path.exists(os.path.join(self.outdir, 'image')):
            os.makedirs(os.path.join(self.outdir, 'image'))
        if not os.path.exists(os.path.join(self.outdir, 'profile')):
            os.makedirs(os.path.join(self.outdir, 'profile'))
        if not os.path.exists(os.path.join(self.outdir, 'emittance')):
            os.makedirs(os.path.join(self.outdir, 'emittance'))

        self.images = {}

        # Raw Data
        self.current = []
        self.xbeam_size = []
        self.ybeam_size = []

        # Mean Values
        self.xbeam_squared = {}
        self.ybeam_squared = {}

        self.user_setting_parameters = {
            "3DProfile":{},
            "QuadScan":{
                "converting":["Gradient/Current (T/m*A)", 1.0],
                "mass":["Mass (MeV/c^2)", 0.0],
                "charge":["Charge (C)", 0.0],
                "kenergy":["Kinetic Energy (MeV)", 0.0], 
                "elength":["Effective length (m)", 0.0],
                "drift":["Drift (m)",0.0]
            }
        }
        self.readonly_parameters = {
            "3DProfile":{},
            "QuadScan":{
                "momentum":["Momentum (MeV/c)",0.0], 
                "rigidity":["Rigidity (T*m)", 0.0]
            }
        }

        self.speed_of_light = 299792458 # m/s
        self.rest_mass = 0.0 # MeV/c^2
        self.kinetic_energy = 0.0 # MeV
        self.effective_length = 0.0 # m
        self.drift = 0.0 # m
        self.charge = 0.0 # C
        self.momentum = 0.0 # MeV/c
        self.ridgidity = 0.0 # T*m

        self.gview = pg.GraphicsView()
        self.glayout = pg.GraphicsLayout(border=(255,255,255))
        self.gview.setBackground('w')
        self.gview.setCentralItem(self.glayout)
        self.gridPlots.addWidget(self.gview)

        self.set_action()
        self.initialize_table()
        self.show()

    @Slot()
    def receive_signal(self):
        self.draw_plots_for_measurement()

    def set_action(self):
        self.logger_signal.connect(self.parent.receive_log)

        self.comboMethod.currentTextChanged.connect(self.initialize_measurement)
        self.pushRun.clicked.connect(self.measure_emittance)

        self.buttonBox.accepted.connect(self.click_ok)
        self.buttonBox.rejected.connect(self.click_cancel)

    def initialize_table(self):
        nrow = self.parent.tableProfiles.rowCount()
        ncol = self.parent.tableProfiles.columnCount()
        self.tableProfiles.setRowCount(nrow)
        for irow in range(nrow):
            item = QTableWidgetItem()
            checkbox = QCheckBox(self, item)
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(self.update_plots)
            self.tableProfiles.setItem(irow, 0, item)
            self.tableProfiles.setCellWidget(irow, 0, checkbox)

            for icol in range(ncol):
                value = self.parent.tableProfiles.item(irow, icol).text()
                item = QTableWidgetItem(value)
                if icol > 0:
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tableProfiles.setItem(irow, icol+1, item)

        self.tableProfiles.resizeRowsToContents()
        self.tableProfiles.resizeColumnsToContents()
        #self.tableProfiles.setColumnWidth(0, 15)

    def initialize_measurement(self):
        if self.comboMethod.currentText() == "3D Profile":
            idx = 0
            for key, value in self.user_setting_parameters['3DProfile'].items():
                label = QLabel(value[0])
                line = QLineEdit(str(value[1]))
                line.editingFinished.connect(self.calculate_parameters)
                self.gridParameters.addWidget(label, idx, 0)
                self.gridParameters.addWidget(line, idx, 1)
                idx += 1

            for key, value in self.readonly_parameters['3DProfile'].items():
                label = QLabel(value[0])
                line = QLineEdit(str(value[1]))
                line.setReadOnly(True)
                self.gridParameters.addWidget(label, idx, 0)
                self.gridParameters.addWidget(line, idx, 1)
                idx += 1
            
        elif self.comboMethod.currentText() == "Quadrupole Scan":
            idx = 0
            for key, value in self.user_setting_parameters['QuadScan'].items():
                label = QLabel(value[0])
                line = QLineEdit(str(value[1]))
                line.textChanged.connect(self.calculate_parameters)
                self.gridParameters.addWidget(label, idx, 0)
                self.gridParameters.addWidget(line, idx, 1)
                idx += 1
                
            for key, value in self.readonly_parameters['QuadScan'].items():
                label = QLabel(value[0])
                line = QLineEdit(str(value[1]))
                line.setReadOnly(True)
                self.gridParameters.addWidget(label, idx, 0)
                self.gridParameters.addWidget(line, idx, 1)
                idx += 1
        else:
            return

        self.glayout.clear()
        
        if self.comboMethod.currentText() == "3D Profile":
            self.profileX = self.glayout.addPlot(title="X axis beam profile", row=1, col=1)
            self.profileX.showGrid(x=True, y=True)
            self.profileX.setLabel('left', 'Range', '%')
            self.profileX.setLabel('bottom', 'Grids', 'mm')
            self.profileX.setXRange(-20, 20)
            self.profileX.setYRange(0, 100)

            self.profileY = self.glayout.addPlot(title="Y axis beam profile", row=1, col=2)
            self.profileY.showGrid(x=True, y=True)
            self.profileY.setLabel('left', 'Range', '%')
            self.profileY.setLabel('bottom', 'Grids', 'mm')
            self.profileY.setXRange(-20, 20)
            self.profileY.setYRange(0, 100)

            self.profileZ = self.glayout.addPlot(title="Z axis beam profile", row=2, col=1)
            self.profileZ.showGrid(x=True, y=True)
            self.profileZ.setLabel('left', 'Range', '%')
            self.profileZ.setLabel('bottom', 'Grids', 'mm')
            self.profileZ.setXRange(-20, 20)
            self.profileZ.setYRange(0, 100)

        elif self.comboMethod.currentText() == "Quadrupole Scan":
            self.plotSize = self.glayout.addPlot(title="Beam Size", row=1, col=1, rowspan=1, colspan=1)
            self.plotSize.showGrid(x=True, y=True)
            self.plotSize.setLabel('left', r'Beam Size <math>&radic;&sigma;<sup>`</sup><sub>11</sub></math>', 'mm')
            self.plotSize.setLabel('bottom', 'Coil Current', 'A')
            self.plotSize.setXRange(-10, 10)
            self.plotSize.setYRange(0, 20)
            #self.plotSize.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)
            #self.plotSize.plot(x1, y1, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=5, symbolPen=gara_pen)

            self.plotFitError = self.glayout.addPlot(title="Fit error", row=1, col=2, rowspan=1, colspan=1)
            self.plotFitError.showGrid(x=True, y=True)
            self.plotFitError.setLabel('left', 'Number of Events', '')
            self.plotFitError.setLabel('bottom', 'Fit Error', 'mm')
            self.plotFitError.setXRange(0, 20)
            self.plotFitError.setYRange(0, 20)

            self.plotXbeamSize = self.glayout.addPlot(title="", row=2, col=1, rowspan=1, colspan=1)
            self.plotXbeamSize.showGrid(x=True, y=True)
            self.plotXbeamSize.setLabel('left', r'Beam Size Squared <math>&sigma;<sup>`</sup><sub>x, 11</sub></math>', r'<math>mm<sup>2</sup></math>')
            self.plotXbeamSize.setLabel('bottom', r'Inverse Focal Length <math>f<sup>-1</sup></math>', r'<math>m<sup>-1</sup></math>')
            self.plotXbeamSize.setXRange(0, 20)
            self.plotXbeamSize.setYRange(0, 150)

            self.plotYbeamSize = self.glayout.addPlot(title="", row=2, col=2, rowspan=1, colspan=1)
            self.plotYbeamSize.showGrid(x=True, y=True)
            self.plotYbeamSize.setLabel('left', r'Beam Size Squared <math>&sigma;<sup>`</sup><sub>y, 11</sub></math>', r'<math>mm<sup>2</sup></math>')
            self.plotYbeamSize.setLabel('bottom', r'Inverse Focal Length <math>f<sup>-1</sup></math>', r'<math>m<sup>-1</sup></math>')
            self.plotYbeamSize.setXRange(0, 20)
            self.plotYbeamSize.setYRange(0, 150)
        else:
            return

        self.update_plots()

    def update_plots(self):
        gara_pen = pg.mkPen(color=(255,255,255), width=3)
        if self.comboMethod.currentText() == "3D Profile":
            pass
        elif self.comboMethod.currentText() == "Quadrupole Scan":
            self.plotSize.clearPlots()
            self.plotFitError.clearPlots()
            self.plotXbeamSize.clearPlots()
            self.plotYbeamSize.clearPlots()
            current = []
            xbeam_size = []
            xbeam_squared = []
            ybeam_size = []
            ybeam_squared = []
            for irow in range(self.tableProfiles.rowCount()):
                if not self.tableProfiles.cellWidget(irow, 0).isChecked(): continue
                current.append(float(self.tableProfiles.item(irow, 1).text()))
                xbeam_size.append(float(self.tableProfiles.item(irow, 2).text()))
                ybeam_size.append(float(self.tableProfiles.item(irow, 3).text()))
            self.current = current
            self.xbeam_size = xbeam_size
            self.ybeam_size = ybeam_size
            gradient = [i*self.user_setting_parameters['QuadScan']['converting'][1] for i in set(self.current)]
            focal_length = self.focal_length(gradient)
            self.xbeam_squared = {}
            temp = {i:[] for i in gradient}
            for idx, value in enumerate(self.xbeam_size):
                temp[self.current[idx]*self.user_setting_parameters['QuadScan']['converting'][1]].append(value)
            for key, value in temp.items():
                mean = np.mean(value)
                self.xbeam_squared[key] = (mean**2, 2*mean*np.std(value))
            self.ybeam_squared = {}
            temp = {i:[] for i in gradient}
            for idx, value in enumerate(self.ybeam_size):
                temp[self.current[idx]*self.user_setting_parameters['QuadScan']['converting'][1]].append(value)
            for key, value in temp.items():
                mean = np.mean(value)
                self.ybeam_squared[key] = (mean**2, 2*mean*np.std(value))
            xbeam_squared = [i[0] for i in self.xbeam_squared.values()]
            ybeam_squared = [i[0] for i in self.ybeam_squared.values()]

            if len(gradient + xbeam_size + ybeam_size) > 0:
                self.plotSize.setXRange(min(current), max(current))
                self.plotSize.setYRange(min(min(xbeam_size), min(ybeam_size)), max(max(xbeam_size), max(ybeam_size)))
                self.plotXbeamSize.setXRange(min(focal_length), max(focal_length))
                self.plotXbeamSize.setYRange(min(xbeam_squared), max(xbeam_squared))
                self.plotYbeamSize.setXRange(min(focal_length), max(focal_length))
                self.plotYbeamSize.setYRange(min(ybeam_squared), max(ybeam_squared))

            self.plotSize.plot(current, xbeam_size, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=10, symbolPen=gara_pen)
            self.plotSize.plot(current, ybeam_size, pen=gara_pen, symbol='o', symbolBrush=(252, 36, 3), symbolSize=10, symbolPen=gara_pen)
            self.plotXbeamSize.plot(focal_length, xbeam_squared, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=10, symbolPen=gara_pen)
            self.plotYbeamSize.plot(focal_length, ybeam_squared, pen=gara_pen, symbol='o', symbolBrush=(64,130,237), symbolSize=10, symbolPen=gara_pen)
        else:
            return

    def measure_emittance(self):
        # Sigma Matrix
        # (1,1) = emittance * beta
        # (1,2), (2,1) = -emittance * alpha
        # (2,2) = emittance * gamma

        if self.comboMethod.currentText() == "3D Profile":
            pass
        elif self.comboMethod.currentText() == "Quadrupole Scan":
            # After quadrupole * drift, sigma' = M*sigma*M**T, M = DQ, D: drift, Q: quadrupole
            # (1,1)' = d^2 * (1,1)*i**2 + 2*(d*(1,1) + d**2*(1,2))*i + ((1,1) + 2*d*(1,2) + d**2*(2,2))
            #        = a*i**2 + b*i + c
            # d: drift, i: inverse focal length
            # Finally,
            # (1,1) = a/d**2
            # (1,2), (2,1) = (b - 2*d*(1,1))/(2*d**2)
            # (2,2) = (c - (1,1) - 2*d*(1,2))/d**2
            # emittance**2 = det(sigma')

            drift = self.user_setting_parameters['QuadScan']['drift'][1]
            gradient = [i*self.user_setting_parameters['QuadScan']['converting'][1] for i in set(self.current)]
            focal_length = self.focal_length(gradient)
            beam_size_squared = {'x':[i[0] for i in self.xbeam_squared.values()], 'y':[i[0] for i in self.ybeam_squared.values()]}
            errors = {'x':[i[1] for i in self.xbeam_squared.values()], 'y':[i[1] for i in self.ybeam_squared.values()]}

            quad = lambda x, a, b, c: a*(x*x) + b*x + c
            for axis, size in beam_size_squared.items():
                if axis == 'x':
                    plot = self.plotXbeamSize
                    line_alpha = self.lineAlphaX
                    line_beta = self.lineBetaX
                    line_gamma = self.lineGammaX
                    line_emit = self.lineEmittanceX
                else:
                    plot = self.plotYbeamSize
                    line_alpha = self.lineAlphaY
                    line_beta = self.lineBetaY
                    line_gamma = self.lineGammaY
                    line_emit = self.lineEmittanceY
                try:
                    fitpara, fitconv = curve_fit(quad, focal_length, size)
                    fitline = quad(focal_length, *fitpara)
                    plot.plot(focal_length, fitline, pen=pg.mkPen(color=(227, 28, 14), width=2))

                    self.logger.info(f"{axis}-axis: Fit success")
                except:
                    fitpara = [0,0,0]
                    fitline = [0 for i in range(len(focal_length))]
                    self.logger.error(f"{axis}-axis: Fit failed")
            
                if drift != 0.0:
                    s11 = fitpara[0]/drift**2
                    s12 = (fitpara[1] - 2*drift*s11)/(2*drift**2)
                    s22 = (fitpara[2] - s11 - 2*drift*s12)/drift**2
                else:
                    s11 = 0
                    s12 = 0
                    s22 = 0
                determinant = s11*s22 - s12**2
                if determinant < 0:
                    self.logger.error(f"{axis}-axis: Determinant is lower than 0")
                    emittance = 0.0
                    alpha = 0.0
                    beta = 0.0
                    gamma = 0.0
                elif determinant == 0.0:
                    self.logger.warning(f"{axis}-axis: Emittance is 0")
                    emittance = 0.0
                    alpha = 0.0
                    beta = 0.0
                    gamma = 0.0
                else:
                    self.logger.info(f"{axis}-axis: Emittance measurement success")
                    emittance = math.sqrt(determinant) / math.pi
                    alpha = - s11 / emittance
                    beta = s12 / emittance
                    gamma = s22 / emittance
                
                line_alpha.setText(str(alpha))
                line_beta.setText(str(beta))
                line_gamma.setText(str(gamma))
                line_emit.setText(str(emittance))

                # plot2. beam size squared vs inverse focal length
                if len(size) > 0:
                    waist = focal_length[size.index(min(size))]
                else:
                    waist = 0.0

                plt.title(f"{emittance}"+r" $\pi$ mm.mrad")
                plt.xlabel(r"Inverse Focal length, $1/f$ $\mathsf{[m^{-1}]}$")
                plt.ylabel(r"Beam Size Squared, $\sigma^\prime_{"+f"{axis}"+r",11} \mathsf{[mm^2]}$")

                plt.errorbar(focal_length, size, errors[axis], elinewidth=1.05, fmt='o', color='#000000', zorder=3, capsize=2, label=r"$\sigma^\prime_{"+f"{axis}"+r"x,11}$")

                try:
                    plt.plot(focal_length, fitline, linestyle='dashed', linewidth=1.5, zorder=2, label='Fit curve')
                except:
                    pass
                plt.axvline(x=waist, color='#9c9897', linestyle='dashdot', linewidth=1, zorder=1, label='Waist')
                plt.legend()

                plt.savefig(os.path.join(self.outdir, 'emittance', f'{axis}-axis_emittance.png'))
                plt.close()
        
        # plot1. beam size vs current
        plt.title(f"Beam Size")
        plt.xlabel(r"Coil Current, I [A]")
        plt.ylabel(r"Beam Size $\sqrt{\sigma^\prime_{11}}$ [mm]")

        plt.scatter(self.current, self.xbeam_size, marker='o', color='#070ff0', label=r'Horizontal 1$\sigma$ Size')
        plt.scatter(self.current, self.ybeam_size, marker='x', color='#f0073a', label=r'Vertical 1$\sigma$ Size')

        plt.legend()

        plt.savefig(os.path.join(self.outdir, 'emittance', f'beamsize.png'))

    def focal_length(self, values):
        new = []
        drift = self.user_setting_parameters['QuadScan']['drift'][1]
        rigidity = self.readonly_parameters['QuadScan']['rigidity'][1]
        for i in values:
            if rigidity != 0.0:
                new.append(i * drift / rigidity)
            else:
                new.append(0.0)
        return new

    def calculate_parameters(self):
        if self.comboMethod.currentText() == "3D Profile":
            return
        elif self.comboMethod.currentText() == "Quadrupole Scan":
            for idx in range(self.gridParameters.rowCount()):
                name = self.gridParameters.itemAtPosition(idx, 0).widget().text()
                value = self.gridParameters.itemAtPosition(idx, 1).widget().text()

                if name == self.user_setting_parameters['QuadScan']['converting'][0]:
                    self.user_setting_parameters['QuadScan']['converting'][1] = float(value)
                elif name == self.user_setting_parameters['QuadScan']['mass'][0]:
                    self.user_setting_parameters['QuadScan']['mass'][1] = float(value)
                elif name == self.user_setting_parameters['QuadScan']['kenergy'][0]:
                    self.user_setting_parameters['QuadScan']['kenergy'][1] = float(value)                    
                elif name == self.user_setting_parameters['QuadScan']['charge'][0]:
                    self.user_setting_parameters['QuadScan']['charge'][1] = float(value)                    
                elif name == self.user_setting_parameters['QuadScan']['elength'][0]:
                    self.user_setting_parameters['QuadScan']['elength'][1] = float(value)                    
                elif name == self.user_setting_parameters['QuadScan']['drift'][0]: 
                    self.user_setting_parameters['QuadScan']['drift'][1] = float(value)                   

            mass = self.user_setting_parameters['QuadScan']['mass'][1]
            kenergy = self.user_setting_parameters['QuadScan']['kenergy'][1]
            charge = self.user_setting_parameters['QuadScan']['charge'][1]

            momentum = math.pow(mass + kenergy, 2) - math.pow(mass, 2)
            if momentum < 0:
                momentum = 0.0
            else:
                momentum = math.sqrt(momentum)
            if charge != 0:
                rigidity = momentum / charge
            else:
                rigidity = 0.0

            self.readonly_parameters['QuadScan']['momentum'][1] = momentum
            self.readonly_parameters['QuadScan']['rigidity'][1] = rigidity

            for idx in range(self.gridParameters.rowCount()):
                name = self.gridParameters.itemAtPosition(idx, 0).widget().text()
                line = self.gridParameters.itemAtPosition(idx, 1).widget()

                if name == self.readonly_parameters['QuadScan']['momentum'][0]:
                    line.setText(f'{momentum:.2f}')
                elif name == self.readonly_parameters['QuadScan']['rigidity'][0]:
                    line.setText(f'{rigidity:.2f}')
            
            # focal length = gradient * drift / rigidity
        else:
            return
        self.update_plots()

    def closeEvent(self, event):
        reply = self.click_cancel()
        if reply == True:
            event.accept()
        else:
            event.ignore()
    def click_ok(self):
        self.logger_signal.emit('INFO', str(f"Measured Emittance"))
        self.accept()

    def click_cancel(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to cancel it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()
            return True
        else:
            return False

    def return_para(self):
        return super().exec_()