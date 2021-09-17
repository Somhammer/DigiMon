from PySide6.QtWidgets import *
from PySide6.QtCore import *

class DigiLabel(QLabel):
    clicked = Signal()
    move = Signal()
    ldclicked = Signal()
    rdclicked = Signal()
    def __init__(self, parent):
        super(DigiLabel, self).__init__(parent)
        #self.setMouseTracking(True)
        self.x = None
        self.y = None
        self.left = None

        self.x_end = None
        self.y_end = None

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        self.x_end = event.x()
        self.y_end = event.y()

        if event.button() == Qt.RightButton:
            self.left = False
        elif event.button() == Qt.LeftButton:
            self.left = True

    def mouseMoveEvent(self, event):
        self.x_end = event.x()
        self.y_end = event.y()
        self.move.emit()
        
    def mouseReleaseEvent(self, event):
        self.clicked.emit()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ldclicked.emit()
        elif event.button() == Qt.RightButton:
            self.rdclicked.emit()