import os
import Convertisseur
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSound


class Convertisseur(QtGui.QMainWindow, Convertisseur.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.ui = ''
        self.py = ''
        self.pathUi = ''
        self.pathPy = ''
        self.scriptName = ''


        self.audioLose = QSound(r"C:\Users\HP\Google_Drive\Personnel\Python\Projet\Qt_convert\audio\GameOver.wav")
        self.audioWin = QSound(r"C:\Users\HP\Google_Drive\Personnel\Python\Projet\Qt_convert\audio\Victory_ff7-_AudioTrimmer_com_.wav")

        self.BtnGo.clicked.connect(self.convertirPy)
        self.BtnCode.clicked.connect(self.convertirScript)
        self.BtnQt.clicked.connect(self.ouvrirQt)
        self.BtnPathQt.clicked.connect(self.modifierEmplacementQt)

        self.ChkSame.stateChanged.connect(lambda :self.changementInfoConvertion(self.ChkSame.text()))
        self.ChkSameFolder.stateChanged.connect(lambda :self.changementInfoConvertion(self.ChkSameFolder.text()))

        self.setTabOrder(self.LeUi,self.LePathUi)
        self.setTabOrder(self.LePathUi,self.LeScript)
        self.setTabOrder(self.LeScript,self.BtnGo)
        self.setTabOrder(self.BtnGo,self.BtnCode)
        self.setTabOrder(self.BtnCode,self.BtnQt)

    def convertirPy(self):
        #Fait la convertion de ui a py dépendement des input fornie
        #pyuic4 -o MonAppli.py -x MonAppli.ui
        # ajouter un label de statue
        boul = True
        while boul == True:
            try:

                self.ui = self.LeUi.text()
                self.pathUi = self.LePathUi.text()

                if self.ChkSameFolder.isChecked() and self.ChkSame.isChecked():

                    self.py = self.ui
                    self.pathPy = self.pathUi


                elif self.ChkSameFolder.isChecked() == False and self.ChkSame.isChecked():

                    self.py = self.ui
                    self.pathPy = self.LePathPy.text()
                elif self.ChkSameFolder.isChecked() and self.ChkSame.isChecked() == False:
                    self.py = self.LePy.text()
                    self.pathPy = self.pathUi
                else:

                    self.py = self.LePy.text()
                    self.pathPy = self.LePathPy.text()

                if self.ui == '' or self.py == '' or self.pathPy =='' or self.pathUi == '':
                    raise ValueError("Vous devez remplir tous les champs")
                    self.LblInfo.setText("Vous devez remplir tous les champs")
                    if self.ChkSons.isChecked() :
                        self.audioLose.play()

                os.system('pyuic4 -o {}\{}.py -x {}\{}.ui'.format(self.pathPy, self.py, self.pathUi, self.ui))

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
        if nom == 'Ui et Py même emplacement' and self.ChkSameFolder.isChecked() == False:

            self.LePathPy.setEnabled(True)

        elif nom == 'Ui et Py même emplacement' and self.ChkSameFolder.isChecked():

            self.LePathPy.setEnabled(False)

        elif nom == 'Ui et Py même nom' and self.ChkSame.isChecked():

            self.LePy.setEnabled(False)

        else :

            self.LePy.setEnabled(True)

    def appelConvertion(self):
        # Crée une base pour la création de Gui à partir du fichier ui initial
        self.scriptName = self.LeScript.text()
        self.convertirPy()

        # permet d'obtenir le type de widget (mainWindow, Ui form )
        extension = ''

        with open('{}\{}.py'.format(self.pathPy, self.py), 'r') as f:
            for line in f:
                if line.startswith('class'):
                    extension = line

                    extension = extension.replace('(object):', '')
                    extension = extension.replace('class ', '')
                    extension = extension.replace('\n', '')


        # Partie de la structure
        self.importation = "from PyQt4 import QtGui\nimport sys\nimport os\nfrom PyQt4.QtGui import QSound\nimport {}\n\n".format(
            self.py)
        self.presentation = "def main():\n    app = QtGui.QApplication(sys.argv)\n    form = {}()\n    form.show()\n    sys.exit(app.exec_())\n\nif __name__ == '__main__':\n    main() ".format(
            self.py)
        self.coeur = "class {}(QtGui.QMainWindow, {}.{}):\n    def __init__(self):\n        super(self.__class__, self).__init__()\n        self.setupUi(self)\n\n".format(
            self.py, self.py, extension)

    def convertirScript(self):
        self.appelConvertion()
        if self.RbAjout.isChecked():
            self.ajoutScript()
        else:

            with open('{}\{}.py'.format(self.pathPy,self.scriptName),'w') as script:
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

        with open(r'{}\{}.py'.format(self.pathPy, self.scriptName), 'r+') as script:

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
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = Convertisseur()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
