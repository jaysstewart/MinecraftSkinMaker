from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
from collections import deque
import glob
from PIL import Image
import actions


class UI(QtWidgets.QMainWindow):

    def setImage(self):
        img = QPixmap('skin.png')
        self.imageLabel.setPixmap(img)

    def __init__(self):
        #q = deque()
        #for filename in glob.glob("skintemplatetests/*.png"):
        #    im = Image.open(filename)
        #    q.append(im)
        super(UI, self).__init__()
        uic.loadUi('SkinUI.ui', self)
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        self.compileButton = self.findChild(QtWidgets.QPushButton, 'compileButton')
        self.compileButton.clicked.connect(self.setImage)
        self.show()





app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
