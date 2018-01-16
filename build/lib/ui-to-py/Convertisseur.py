# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Convertisseur.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LblInfo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblInfo.setFont(font)
        self.LblInfo.setFrameShape(QtWidgets.QFrame.Panel)
        self.LblInfo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LblInfo.setObjectName("LblInfo")
        self.horizontalLayout_4.addWidget(self.LblInfo)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)
        self.RbAjout = QtWidgets.QRadioButton(self.centralwidget)
        self.RbAjout.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.RbAjout.setObjectName("RbAjout")
        self.gridLayout.addWidget(self.RbAjout, 3, 1, 1, 1)
        self.RbCreer = QtWidgets.QRadioButton(self.centralwidget)
        self.RbCreer.setChecked(True)
        self.RbCreer.setObjectName("RbCreer")
        self.gridLayout.addWidget(self.RbCreer, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnGo = QtWidgets.QPushButton(self.centralwidget)
        self.BtnGo.setAutoDefault(False)
        self.BtnGo.setObjectName("BtnGo")
        self.horizontalLayout.addWidget(self.BtnGo)
        self.BtnCode = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCode.setEnabled(True)
        self.BtnCode.setAutoDefault(True)
        self.BtnCode.setObjectName("BtnCode")
        self.horizontalLayout.addWidget(self.BtnCode)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ChkSons = QtWidgets.QCheckBox(self.centralwidget)
        self.ChkSons.setObjectName("ChkSons")
        self.horizontalLayout_2.addWidget(self.ChkSons)
        self.ChkSame = QtWidgets.QCheckBox(self.centralwidget)
        self.ChkSame.setEnabled(True)
        self.ChkSame.setChecked(True)
        self.ChkSame.setObjectName("ChkSame")
        self.horizontalLayout_2.addWidget(self.ChkSame)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BtnQt = QtWidgets.QPushButton(self.centralwidget)
        self.BtnQt.setObjectName("BtnQt")
        self.horizontalLayout_3.addWidget(self.BtnQt)
        self.BtnPathQt = QtWidgets.QPushButton(self.centralwidget)
        self.BtnPathQt.setObjectName("BtnPathQt")
        self.horizontalLayout_3.addWidget(self.BtnPathQt)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ui to Py"))
        self.LblInfo.setText(_translate("MainWindow", "Les emplacements ne doivent pas contenir d\'espace exemple:\n"
"    C:/Users/HP/Google_Drive OUI\n"
"    C:/Users/HP/Google Drive NON\n"
"\n"
"*Les \'/ \' doivent être dans l\'autre sens.Le plus simple est de seulement\n"
" copier-coller l\'emplacement de la barre d\'état.\n"
"\n"
"Les scripts python sont crées dans le même emplacement que \n"
"les fichiers .py sortant"))
        self.RbAjout.setText(_translate("MainWindow", "Ajouter widget dans un script"))
        self.RbCreer.setText(_translate("MainWindow", "Créer un script"))
        self.BtnGo.setText(_translate("MainWindow", "Convertir .ui en .py"))
        self.BtnCode.setText(_translate("MainWindow", "Créer un script python"))
        self.ChkSons.setText(_translate("MainWindow", "Sons ON/OFF"))
        self.ChkSame.setText(_translate("MainWindow", "Ui et Py même nom"))
        self.BtnQt.setText(_translate("MainWindow", "Ouvrir Designer"))
        self.BtnPathQt.setText(_translate("MainWindow", "Configurer l\'emplacement de Qt Designer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

