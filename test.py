# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HP\Google_Drive\Personnel\Python\Projet\Qt_convert\convertisseur.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(538, 433)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ChkSame = QtGui.QCheckBox(self.centralwidget)
        self.ChkSame.setEnabled(True)
        self.ChkSame.setChecked(True)
        self.ChkSame.setObjectName(_fromUtf8("ChkSame"))
        self.horizontalLayout_2.addWidget(self.ChkSame)
        self.ChkSons = QtGui.QCheckBox(self.centralwidget)
        self.ChkSons.setObjectName(_fromUtf8("ChkSons"))
        self.horizontalLayout_2.addWidget(self.ChkSons)
        self.ChkSameFolder = QtGui.QCheckBox(self.centralwidget)
        self.ChkSameFolder.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ChkSameFolder.setChecked(True)
        self.ChkSameFolder.setObjectName(_fromUtf8("ChkSameFolder"))
        self.horizontalLayout_2.addWidget(self.ChkSameFolder)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 3)
        self.LePy = QtGui.QLineEdit(self.centralwidget)
        self.LePy.setEnabled(False)
        self.LePy.setObjectName(_fromUtf8("LePy"))
        self.gridLayout.addWidget(self.LePy, 2, 1, 1, 1)
        self.LblUi = QtGui.QLabel(self.centralwidget)
        self.LblUi.setEnabled(True)
        self.LblUi.setObjectName(_fromUtf8("LblUi"))
        self.gridLayout.addWidget(self.LblUi, 0, 0, 1, 1)
        self.LeUi = QtGui.QLineEdit(self.centralwidget)
        self.LeUi.setObjectName(_fromUtf8("LeUi"))
        self.gridLayout.addWidget(self.LeUi, 0, 1, 1, 1)
        self.LePathPy = QtGui.QLineEdit(self.centralwidget)
        self.LePathPy.setEnabled(False)
        self.LePathPy.setObjectName(_fromUtf8("LePathPy"))
        self.gridLayout.addWidget(self.LePathPy, 4, 1, 1, 1)
        self.LblPathUi = QtGui.QLabel(self.centralwidget)
        self.LblPathUi.setObjectName(_fromUtf8("LblPathUi"))
        self.gridLayout.addWidget(self.LblPathUi, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.BtnQt = QtGui.QPushButton(self.centralwidget)
        self.BtnQt.setObjectName(_fromUtf8("BtnQt"))
        self.horizontalLayout_3.addWidget(self.BtnQt)
        self.BtnPathQt = QtGui.QPushButton(self.centralwidget)
        self.BtnPathQt.setObjectName(_fromUtf8("BtnPathQt"))
        self.horizontalLayout_3.addWidget(self.BtnPathQt)
        self.gridLayout.addLayout(self.horizontalLayout_3, 11, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.LblInfo = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LblInfo.setFont(font)
        self.LblInfo.setFrameShape(QtGui.QFrame.Panel)
        self.LblInfo.setFrameShadow(QtGui.QFrame.Plain)
        self.LblInfo.setObjectName(_fromUtf8("LblInfo"))
        self.horizontalLayout_4.addWidget(self.LblInfo)
        self.gridLayout.addLayout(self.horizontalLayout_4, 12, 0, 1, 2)
        self.LeScript = QtGui.QLineEdit(self.centralwidget)
        self.LeScript.setObjectName(_fromUtf8("LeScript"))
        self.gridLayout.addWidget(self.LeScript, 5, 1, 1, 1)
        self.LblPathPy = QtGui.QLabel(self.centralwidget)
        self.LblPathPy.setObjectName(_fromUtf8("LblPathPy"))
        self.gridLayout.addWidget(self.LblPathPy, 4, 0, 1, 1)
        self.LbPy = QtGui.QLabel(self.centralwidget)
        self.LbPy.setObjectName(_fromUtf8("LbPy"))
        self.gridLayout.addWidget(self.LbPy, 2, 0, 1, 1)
        self.LePathUi = QtGui.QLineEdit(self.centralwidget)
        self.LePathUi.setEnabled(True)
        self.LePathUi.setObjectName(_fromUtf8("LePathUi"))
        self.gridLayout.addWidget(self.LePathUi, 1, 1, 1, 1)
        self.LblFichierPython = QtGui.QLabel(self.centralwidget)
        self.LblFichierPython.setObjectName(_fromUtf8("LblFichierPython"))
        self.gridLayout.addWidget(self.LblFichierPython, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BtnCode = QtGui.QPushButton(self.centralwidget)
        self.BtnCode.setEnabled(True)
        self.BtnCode.setAutoDefault(True)
        self.BtnCode.setObjectName(_fromUtf8("BtnCode"))
        self.horizontalLayout.addWidget(self.BtnCode)
        self.BtnGo = QtGui.QPushButton(self.centralwidget)
        self.BtnGo.setAutoDefault(False)
        self.BtnGo.setObjectName(_fromUtf8("BtnGo"))
        self.horizontalLayout.addWidget(self.BtnGo)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 3)
        self.RbCreer = QtGui.QRadioButton(self.centralwidget)
        self.RbCreer.setObjectName(_fromUtf8("RbCreer"))
        self.gridLayout.addWidget(self.RbCreer, 10, 0, 1, 1)
        self.RbAjout = QtGui.QRadioButton(self.centralwidget)
        self.RbAjout.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.RbAjout.setObjectName(_fromUtf8("RbAjout"))
        self.gridLayout.addWidget(self.RbAjout, 10, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ui to Py", None))
        self.ChkSame.setText(_translate("MainWindow", "Ui et Py même nom", None))
        self.ChkSons.setText(_translate("MainWindow", "Sons ON/OFF", None))
        self.ChkSameFolder.setText(_translate("MainWindow", "Ui et Py même emplacement", None))
        self.LblUi.setText(_translate("MainWindow", "Fichier Ui", None))
        self.LblPathUi.setText(_translate("MainWindow", "Emplacement fichier Ui", None))
        self.BtnQt.setText(_translate("MainWindow", "Ouvrir Designer", None))
        self.BtnPathQt.setText(_translate("MainWindow", "Configurer l\'emplacement de Qt Designer", None))
        self.LblInfo.setText(_translate("MainWindow", "Les emplacements ne doivent pas contenir d\'espace exemple:\n"
"    C:/Users/HP/Google_Drive OUI\n"
"    C:/Users/HP/Google Drive NON\n"
"\n"
"*Les \'/ \' doivent être dans l\'autre sens.Le plus simple est de seulement\n"
" copier-coller l\'emplacement de la barre d\'état.\n"
"\n"
"Les scripts python sont crées dans le même emplacement que \n"
"les fichiers .py sortant", None))
        self.LblPathPy.setText(_translate("MainWindow", "Emplacement du fichier Py", None))
        self.LbPy.setText(_translate("MainWindow", "Fichier Py", None))
        self.LblFichierPython.setText(_translate("MainWindow", "Nom du script", None))
        self.BtnCode.setText(_translate("MainWindow", "Créer un script python", None))
        self.BtnGo.setText(_translate("MainWindow", "Convertir .ui en .py", None))
        self.RbCreer.setText(_translate("MainWindow", "Créer un script", None))
        self.RbAjout.setText(_translate("MainWindow", "Ajouter widget dans un script", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

