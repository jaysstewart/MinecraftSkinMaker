from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
from collections import deque
import glob
from PIL import Image
import actions


class UI(QtWidgets.QMainWindow):
    # populate base Array
    baseAr = list()
    for filename in glob.glob("skintemplates/Base/*.png"):
        im = Image.open(filename)
        baseAr.append(im)

    # populate head Array
    headAr = list()
    for filename in glob.glob("skintemplates/head/*.png"):
        im = Image.open(filename)
        headAr.append(im)

    # populate legs array
    legsAr = list()
    for filename in glob.glob("skintemplates/pants/*.png"):
        im = Image.open(filename)
        legsAr.append(im)

    # populate arms array
    armsAr = list()
    for filename in glob.glob("skintemplates/shirt/*.png"):
        im = Image.open(filename)
        armsAr.append(im)

    # test code to populate q, DELETE LATER
    q = deque()
    q.append(baseAr[0])
    q.append(headAr[0])
    q.append(legsAr[0])
    q.append(armsAr[1])

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('SkinUI.ui', self)

        # link UI with methods
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        self.compileButton = self.findChild(QtWidgets.QPushButton, 'compileButton')
        self.baseTable = self.findChild(QtWidgets.QTableWidget, 'baseTable')

        self.baseTable.setRowCount(4)
        self.baseTable.setColumnCount(1)
        # self.newItem = self.QTableWidgetItem("test")

        # self.baseTable.setItem(0,0, self.newItem)

        self.compileButton.clicked.connect(self.compile)
        self.show()

    # calls recompile method, and resets imageLabel
    def compile(self):
        actions.recompileImage(self.q)
        img = QPixmap('skin.png')
        self.imageLabel.setPixmap(img)


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
