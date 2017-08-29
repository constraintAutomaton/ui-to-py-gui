import sys
import os
from Convertisseur import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtMultimedia import QSound


class Convertisseur(Ui_MainWindow):
    def __init__(self, w):
        self.setupUi(w)
        
        self.ui = ''
        self.py = ''
        self.pathUi = ''
        self.scriptName = ''


        self.audioLose = QSound(r"audio\GameOver.wav")
        self.audioWin = QSound(r"Victory_ff7-_AudioTrimmer_com_.wav")

        self.BtnGo.clicked.connect(self.convertirPy)
        self.BtnCode.clicked.connect(self.convertirScript)
        self.BtnQt.clicked.connect(self.ouvrirQt)
        self.BtnPathQt.clicked.connect(self.modifierEmplacementQt)

        self.ChkSame.stateChanged.connect(lambda :self.changementInfoConvertion(self.ChkSame.text()))
        

        #self.setTabOrder(self.LeUi,self.LePathUi)
        #self.setTabOrder(self.LePathUi,self.LeScript)
        #self.setTabOrder(self.LeScript,self.BtnGo)
        #self.setTabOrder(self.BtnGo,self.BtnCode)
        #self.setTabOrder(self.BtnCode,self.BtnQt)

    def convertirPy(self):
        #Fait la convertion de ui a py dépendement des input fornie
        #pyuic5 -o MonAppli.py -x MonAppli.ui
        # ajouter un label de statue
        boul = True
        while boul == True:
            try:

                self.ui = self.LeUi.text()
                self.pathUi = self.LePathUi.text()

               
                if  self.ChkSame.isChecked():

                    self.py = self.ui
                else:
                    self.py = self.LePy.text()
                    
                    

                if self.ui == '' or self.py == '' or self.pathUi == '':
                    raise ValueError("Vous devez remplir tous les champs")
                    
                    self.LblInfo.setText("Vous devez remplir tous les champs")
                    
                    if self.ChkSons.isChecked() :
                        self.audioLose.play()
                os.chdir(self.pathUi)
                os.system('pyuic5 -x {}.ui -o {}.py '.format(self.ui, self.py))
                    

            except:
                print("Le fichier ou l'emplacement est introuvable")
                self.LblInfo.setText("Le fichier ou l'emplacement est introuvable")
                if self.ChkSons.isChecked():
                    self.audioLose.play()
                break
            else:
                boul = False


        if boul == False and self.ChkSons.isChecked() :
            self.audioWin.play()
        elif boul == False:
            self.LblInfo.setText('Convertion de {}.ui en {}.py réussit '.format(self.ui, self.py))

    def changementInfoConvertion(self, nom):
        #Permet de controler les input de l'utilisateur par rapport au info relatif au convertissement
        

        if nom == 'Ui et Py même nom' and self.ChkSame.isChecked():

            self.LePy.setEnabled(False)

        else :

            self.LePy.setEnabled(True)

    def appelConvertion(self):
        # Crée une base pour la création de Gui à partir du fichier ui initial
        self.scriptName = self.LeScript.text()
        self.convertirPy()

        # permet d'obtenir le type de widget (mainWindow, Ui form )
        extension = ''

        with open('{}\{}.py'.format(self.pathUi,self.py), 'r') as f:
            for line in f:
                if 'class' in line:
                    start = ' '
                    end = '('
                    nameClass = line[line.find(start)+len(start):line.rfind(end)]
                if 'MainWindow = QtWidgets.' in line:
                    extension = line[line.index('.')+1:]
                    break
                


        # Partie de la structure
        self.importation = "from PyQt5 import QtGui, QtCore, QtWidgets\nimport sys\nimport os\nfrom PyQt5.QtMultimedia import QSound\nfrom {} import {}\n\n".format(
            self.py,nameClass)
        self.presentation = "def main():\n    app = QtWidgets.QApplication(sys.argv)\n    w = QtWidgets.{}    prog = {}(w)\n    w.show()\n    sys.exit(app.exec_())\n\nif __name__ == '__main__':\n    main() ".format(
            extension,self.py)
        self.coeur = "class {}({}):\n    def __init__(self, w):\n        self.setupUi(w)\n\n".format(
            self.py, nameClass)
        print(self.importation,self.coeur, self.presentation)

    def convertirScript(self):
        self.appelConvertion()
        if self.RbAjout.isChecked():
            self.ajoutScript()
        else:

            with open('{}\{}.py'.format(self.pathUi,self.scriptName),'w') as script:
                script.write(self.importation)
                script.write(self.coeur)
                script.write(self.presentation)

                if  self.ChkSons.isChecked():
                    self.audioWin.play()
            self.LblInfo.setText('Script {}.py créer'.format(self.scriptName))

    def ajoutScript(self):
        self.appelConvertion()
        # Permet de transformer self.coeur en list tout en gardant les \n

        coeur = self.coeur.split('\n')
        for i,line in enumerate(coeur):
            coeur[i] += '\n'
         # dans self.coeur il y a deux saut de line pour le formatage qui rentre en interférence
        del coeur[-1]
        del coeur[-1]

        with open(r'{}\{}.py'.format(self.pathUi, self.scriptName), 'r+') as script:

            contenus = script.readlines()

            for i,line in enumerate(contenus):

                if line.startswith('\n'):
                    contenus.insert(i,'\n\n' )
                    i += 1
                    for line in coeur:
                        contenus.insert(i,line)
                        i += 1
                    break

            contenus = ''.join(contenus)
            script.seek(0)
            script.write(contenus)
            script.truncate()
        self.LblInfo.setText( '{}.ui ajouter à {}.py'.format(self.py,self.scriptName))

    def ouvrirQt(self):
        with open('pathQt.txt','r') as f:
            path = f.read()
        os.system('start {}'.format(path))
        self.LblInfo.setText('Ouverture de Qt Designer ')

    def modifierEmplacementQt(self):
        path, ok = QtGui.QInputDialog.getText(self, 'Modifier l\'emplacement de Qt Designer',
                                              'Entrer le nouvel emplacement')
        print('to')
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
