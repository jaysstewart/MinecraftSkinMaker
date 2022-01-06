import os.path
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys
from collections import deque
from PIL import Image
import actions


# Image object to be place in table cells
class ImageWidget(QtWidgets.QWidget):

    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.path = imagePath
        self.picture = QtGui.QPixmap(self.path)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.picture)

    def getPath(self):
        return self.path




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

    #q.append(Image.open(headAr[0]))
    #q.append(Image.open(pantsAr[0]))
    #q.append(Image.open(shirtAr[1]))

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('SkinUI.ui', self)

        # link UI with python object
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        self.compileButton = self.findChild(QtWidgets.QPushButton, 'compileButton')
        self.baseTable = self.findChild(QtWidgets.QTableWidget, 'baseTable')
        self.headTable = self.findChild(QtWidgets.QTableWidget, 'headTable')
        self.shirtTable = self.findChild(QtWidgets.QTableWidget, 'shirtTable')
        self.pantsTable = self.findChild(QtWidgets.QTableWidget, 'pantsTable')

        # fill tables with array of images
        self.fillTable(self.baseAr, self.baseTable)
        self.fillTable(self.headAr, self.headTable)
        self.fillTable(self.shirtAr, self.shirtTable)
        self.fillTable(self.pantsAr, self.pantsTable)

        # calls table listeners to make selections.
        self.baseTable.selectionModel().selectionChanged.connect(self.baseSelect)
        self.headTable.selectionModel().selectionChanged.connect(self.headSelect)
        self.shirtTable.selectionModel().selectionChanged.connect(self.shirtSelect)
        self.pantsTable.selectionModel().selectionChanged.connect(self.pantsSelect)

        self.compileButton.clicked.connect(self.compile)
        self.show()

    # base table click listener
    def baseSelect(self, selected, deselected):
        for ix in selected.indexes():
            self.q.append((self.baseTable.cellWidget(ix.row(), ix.column()).getPath()))
            print(len(self.q))
        for ix in deselected.indexes():
            self.q.remove((self.baseTable.cellWidget(ix.row(), ix.column()).getPath()))


    # head table click listener
    def headSelect(self, selected, deselected):
        for ix in selected.indexes():
            self.q.append((self.headTable.cellWidget(ix.row(), ix.column()).getPath()))
        for ix in deselected.indexes():
            self.q.remove((self.headTable.cellWidget(ix.row(), ix.column()).getPath()))

    # shirt table click listener
    def shirtSelect(self, selected, deselected):
        for ix in selected.indexes():
            self.q.append((self.shirtTable.cellWidget(ix.row(), ix.column()).getPath()))
        for ix in deselected.indexes():
            self.q.remove((self.shirtTable.cellWidget(ix.row(), ix.column()).getPath()))

    # pants table click listener
    def pantsSelect(self, selected, deselected):
        for ix in selected.indexes():
            self.q.append((self.pantsTable.cellWidget(ix.row(), ix.column()).getPath()))
        for ix in deselected.indexes():
            self.q.remove((self.pantsTable.cellWidget(ix.row(), ix.column()).getPath()))


    # calls recompile method, and resets imageLabel
    def compile(self):
        actions.recompileImage(self.q)
        img = QPixmap('skin.png')
        self.imageLabel.setPixmap(img)

    # dynamically fill tables with images from array

    def fillTable(self, ar, table):

        table.setColumnCount(2)
        table.setRowCount(2)
        row = 0
        column = 0

        # iterate through columns
        for i in ar:
            # edge case
            if i == 0:
                table.setRowCount(row + 1)
                table.setCellWidget(row, column, ImageWidget(i, table))
                column += 1
                continue
            elif column == 2:
                row += 1
                column = 0
                table.setRowCount(row + 1)

            table.setCellWidget(row, column, ImageWidget(i, table))
            column += 1


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
