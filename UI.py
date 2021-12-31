import os.path

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
import sys
from collections import deque
from PIL import Image
import actions


# Image object to be place in table cells
class ImageWidget(QtWidgets.QWidget):

    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QtGui.QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class UI(QtWidgets.QMainWindow):
    # populate base Array
    baseAr = list()
    d = "skintemplates/Base/"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            baseAr.append(full_path)

    # populate head Array
    headAr = list()
    d = "skintemplates/head/"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            headAr.append(full_path)

    # populate legs array
    pantsAr = list()
    d = "skintemplates/pants/"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            pantsAr.append(full_path)

    # populate arms array
    shirtAr = list()
    d = "skintemplates/shirt/"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            shirtAr.append(full_path)

    # test code to populate q, DELETE LATER
    q = deque()

    q.append(Image.open(baseAr[1]))
    q.append(Image.open(headAr[0]))
    q.append(Image.open(pantsAr[0]))
    q.append(Image.open(shirtAr[1]))

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('SkinUI.ui', self)

        # link UI with methods
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        self.compileButton = self.findChild(QtWidgets.QPushButton, 'compileButton')
        self.baseTable = self.findChild(QtWidgets.QTableWidget, 'baseTable')

        self.fillBaseTable()

        self.compileButton.clicked.connect(self.compile)
        self.show()

    # calls recompile method, and resets imageLabel
    def compile(self):
        actions.recompileImage(self.q)
        img = QPixmap('skin.png')
        self.imageLabel.setPixmap(img)

    def fillBaseTable(self):
        # counter to hold array place
        self.baseTable.setRowCount(2)

        counter = 0
        row = 0
        column = 0

        # iterate through columns
        for i in self.baseAr:
            # edge case
            if i == 0:
                self.baseTable.setColumnCount(column + 1)
                self.baseTable.setCellWidget(row, column, ImageWidget(i, self.baseTable))
                row += 1
                continue

            if row == 2:
                row = 0
                column += 1
                self.baseTable.setColumnCount(column + 1)

            self.baseTable.setCellWidget(row, column, ImageWidget(i, self.baseTable))
            row += 1


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
