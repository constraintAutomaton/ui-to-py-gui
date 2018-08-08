# coding: utf-8
import sys
import os
from Convertisseur import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Convertisseur(Ui_MainWindow):
    def __init__(self, w):
        super().__init__()
        self.setupUi(w)

        self.ui = ''
        self.py = ''
        self.pathUi = ''
        self.pathPy = ''
        self.scriptName = ''

        self.workingDir = os.getcwd()

        self.BtnGo.clicked.connect(self.convertirPy)
        self.BtnCode.clicked.connect(self.convertirScript)
        self.BtnQt.clicked.connect(self.ouvrirQt)
        self.BtnPathQt.clicked.connect(self.modifierEmplacementQt)

    def convertirPy(self):
        # Fait la convertion de ui a py dÃ©pendement des input fornie
        # pyuic5 -o MonAppli.py -x MonAppli.ui
        # ajouter un label de statue
        # fichier qui permet d'ouvrir au dernier path utilise
        os.chdir(self.workingDir)
        with open(r'pathFileBrowser.txt', 'r') as f:
            path = f.read()
        boul = True
        while boul == True:

            try:
                uiFile = QtWidgets.QFileDialog.getOpenFileName(
                    directory=path, filter="ui Files (*.ui);;All Files (*);;")
                self.ui = uiFile[0][uiFile[0].rfind(
                    '/') + 1:].replace('.ui', '')

                self.pathUi = uiFile[0][:uiFile[0].rfind('/') + 1]

                # fichier qui permet d'ouvrir au dernier path utilise
                with open('pathFileBrowser.txt', 'w') as f:
                    f.write(self.pathUi)

                if self.ChkSame.isChecked() == False:

                    self.py, ok = QtWidgets.QInputDialog.getText(
                        QtWidgets.QMainWindow(), "Nom du fichier py", "Entrez le nom")
                else:
                    self.py = self.ui

                if self.ui == '' or self.py == '' or self.pathUi == '':
                    raise ValueError("Vous devez remplir tous les champs")
                
                os.chdir(self.pathUi)
                os.system('pyuic5 -x {}.ui -o {}.py '.format(self.ui, self.py))

            except:
                break
            else:
                boul = False



    def appelConvertion(self):
        # CrÃ©e une base pour la crÃ©ation de Gui Ã  partir du fichier ui initial
        self.convertirPy()

        # permet d'obtenir le type de widget (mainWindow, Ui form )
        extension = ''

        with open(os.path.join(self.pathUi,self.py+'.py'),'r') as f:
            for line in f:
                if 'class' in line:
                    start = ' '
                    end = '('
                    nameClass = line[line.find(
                        start) + len(start):line.rfind(end)]
                if 'MainWindow = QtWidgets.' in line:
                    extension = line[line.index('.') + 1:]
                    break
                elif 'Dialog = QtWidgets.' in line:
                    extension = line[line.index('.') + 1:]
                    break
                elif 'Form = QtWidgets.' in line:
                    extension = line[line.index('.') + 1:]
                    break

        # Partie de la structure
        self.importation = "from PyQt5 import QtGui, QtCore, QtWidgets\nimport sys\nimport os\nfrom PyQt5.QtMultimedia import QSound\nfrom {} import {}\n\n".format(
            self.py, nameClass)
        self.presentation = "def main():\n    app = QtWidgets.QApplication(sys.argv)\n    w = QtWidgets.{}    prog = {}(w)\n    w.show()\n    sys.exit(app.exec_())\n\nif __name__ == '__main__':\n    main() ".format(
            extension, self.py)
        self.coeur = "class {}({}):\n    def __init__(self, w):\n        self.setupUi(w)\n\n".format(
            self.py, nameClass)

    def convertirScript(self):

        self.appelConvertion()
        
        if self.RbAjout.isChecked():
            self.ajoutScript()
        else:

            self.scriptName, ok = QtWidgets.QInputDialog.getText(
                QtWidgets.QMainWindow(), "Nom du script", "Entrez le nom")

            with open(os.path.join(self.pathUi,self.scriptName+'.py'), 'w') as script:
                script.write(self.importation)
                script.write(self.coeur)
                script.write(self.presentation)

               

    def ajoutScript(self):
        # fichier qui permet d'ouvrir au dernier path utilise
        with open('pathFileBrowser.txt', 'r') as f:
            path = f.read()

        scriptName = QtWidgets.QFileDialog.getOpenFileName(
            directory=path, filter="ui Files (*.py);;All Files (*);;")
        self.scriptName = scriptName[0][scriptName[0].rfind(
            '/') + 1:].replace('.py', '')

        # fichier qui permet d'ouvrir au dernier path utilise
        with open('pathFileBrowser.txt', 'w') as f:
            f.write(self.pathUi)

        # Permet de transformer self.coeur en list tout en gardant les \n

        coeur = self.coeur.split('\n')
        for i, line in enumerate(coeur):
            coeur[i] += '\n'
         # dans self.coeur il y a deux saut de line pour le formatage qui rentre en interfÃ©rence
        del coeur[-1]
        del coeur[-1]

        with open(os.path.join(self.pathUi,self.scriptName), 'r+') as script:

            contenus = script.readlines()

            for i, line in enumerate(contenus):

                if line.startswith('\n'):
                    contenus.insert(i, '\n\n')
                    i += 1
                    for line in coeur:
                        contenus.insert(i, line)
                        i += 1
                    break

            contenus = ''.join(contenus)
            script.seek(0)
            script.write(contenus)
            script.truncate()
        self.LblInfo.setText(
            '{}.ui ajouté Ã  {}.py'.format(self.py, self.scriptName))

    def ouvrirQt(self):
        os.chdir(self.workingDir)
        with open('pathQt.txt', 'r') as f:
            path = f.read()
        os.system('{}'.format(path))
        self.LblInfo.setText('Ouverture de Qt Designer ')

    def modifierEmplacementQt(self):
        path, ok = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(
        ), "Modifier l\'emplacement de Qt Designer", "Entrer le nouvel emplacement")

        with open('pathQt.txt', 'w') as f:
            f.write(path)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = Convertisseur(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()