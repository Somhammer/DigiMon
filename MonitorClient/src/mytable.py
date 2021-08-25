import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MyCheckBox(QCheckBox):
    def __init__(self, parent, item):
        super().__init__()
        self.parent = parent
        self.item = item
        self.mycheckvalue = 2
        self.stateChanged.connect(self.__checkbox_change)

    def __checkbox_change(self, checkvalue):
        self.mycheckvalue = checkvalue
        self.check_signal.emit()

    def get_row(self):
        return self.item.row()

class MyQTableWidgetItemCheckBox(QTableWidgetItem):
    def __init__(self):
        super().__init__()
        self.setData(Qt.UserRole, 0)

    def __lt__(self, other):
        return self.data(Qt.UserRole) < other.data(Qt.UserRole)
    
    def my_setdata(self, value):
        self.setData(Qt.UserRole, value)

class MyTableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.gradient = [10,11,12,13,14]
        self.images = ['ABCD','EFGH','IJKL',"MNOP",'QRST']

        self.resize(200,200)
        self.setRowCount(5)
        self.setColumnCount(5)
        for idx, image in enumerate(self.images):
            #item = MyQTableWidgetItemCheckBox()
            item = QTableWidgetItem()
            self.setItem(idx, 0, item)
            #checkbox = MyCheckBox(self, item)
            checkbox = QCheckBox(self, item)
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(self.edit_data)
            self.setCellWidget(idx, 0, checkbox)

            twidget = QTableWidgetItem(str(self.gradient[idx]))
            twidget.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            #twidget.currentTextChanged.connect(self.edit_data)
            #twidget.setFlags(Qt.ItemIsSelectable & Qt.ItemIsEditable & Qt.ItemIsEnabled)

            self.setItem(idx, 1, twidget)
            self.setItem(idx, 2, QTableWidgetItem(image))

        self.resizeRowsToContents()
        self.resizeColumnsToContents()
        self.setColumnWidth(0, 10)

    def edit_data(self):
        print("MELONA to LEMONA")
        print(self.item(0,2).text())

    #def edit_data(self, section):
    #    cell = self.itemAt(row, column)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        #self.grid = QGridLayout(self)
        table = MyTableWidget(self)
        #self.grid.addWidget(table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    
    sys.exit(app.exec())