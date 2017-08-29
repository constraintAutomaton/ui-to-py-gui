from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from PyQt5.QtMultimedia import QSound
from test import Ui_MainWindow


class test(Ui_MainWindow):
    def __init__(self, w):
        self.setupUi(w)

class test(Ui_MainWindow):
    def __init__(self, w):
        self.setupUi(w)

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = test(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 