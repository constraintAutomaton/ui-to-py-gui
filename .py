from PyQt4 import QtGui
import sys
import os
from PyQt4.QtGui import QSound
import test


class test(QtGui.QMainWindow, test.Ui_Dialog):
 def __init__(self):
       super(self.__class__, self).__init__()
        self.setupUi(self)

class test(QtGui.QMainWindow, test.Ui_Dialog):
 def __init__(self):
       super(self.__class__, self).__init__()
        self.setupUi(self)

def main():
  app = QtGui.QApplication(sys.argv)
    form = test()
   form.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main() 