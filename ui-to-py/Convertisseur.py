# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Convertisseur.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnGo = QtWidgets.QPushButton(self.groupBox)
        self.BtnGo.setAutoDefault(False)
        self.BtnGo.setObjectName("BtnGo")
        self.horizontalLayout.addWidget(self.BtnGo)
        self.BtnCode = QtWidgets.QPushButton(self.groupBox)
        self.BtnCode.setEnabled(True)
        self.BtnCode.setAutoDefault(True)
        self.BtnCode.setObjectName("BtnCode")
        self.horizontalLayout.addWidget(self.BtnCode)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BtnQt = QtWidgets.QPushButton(self.groupBox)
        self.BtnQt.setObjectName("BtnQt")
        self.horizontalLayout_3.addWidget(self.BtnQt)
        self.BtnPathQt = QtWidgets.QPushButton(self.groupBox)
        self.BtnPathQt.setObjectName("BtnPathQt")
        self.horizontalLayout_3.addWidget(self.BtnPathQt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.RbCreer = QtWidgets.QRadioButton(self.groupBox_2)
        self.RbCreer.setChecked(True)
        self.RbCreer.setObjectName("RbCreer")
        self.horizontalLayout_4.addWidget(self.RbCreer)
        self.RbAjout = QtWidgets.QRadioButton(self.groupBox_2)
        self.RbAjout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RbAjout.setObjectName("RbAjout")
        self.horizontalLayout_4.addWidget(self.RbAjout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ChkSame = QtWidgets.QCheckBox(self.groupBox_2)
        self.ChkSame.setEnabled(True)
        self.ChkSame.setChecked(True)
        self.ChkSame.setObjectName("ChkSame")
        self.horizontalLayout_2.addWidget(self.ChkSame)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ui to Py"))
        self.groupBox.setTitle(_translate("MainWindow", "Action"))
        self.BtnGo.setText(_translate("MainWindow", "Convert .ui to .py"))
        self.BtnCode.setText(_translate("MainWindow", "Create a python script"))
        self.BtnQt.setText(_translate("MainWindow", "Open Qt designer"))
        self.BtnPathQt.setText(_translate("MainWindow", "Configure Qt designer location"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Option"))
        self.RbCreer.setText(_translate("MainWindow", "Create a script"))
        self.RbAjout.setText(_translate("MainWindow", "Add a widget in a script"))
        self.ChkSame.setText(_translate("MainWindow", "Output file same name as input file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

