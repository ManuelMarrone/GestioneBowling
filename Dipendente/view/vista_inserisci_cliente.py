from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.uic.properties import QtCore
from PyQt6.QtCore import pyqtSignal


from Cliente.controller.controllore_cliente import ControlloreCliente

class VistaInserimento(QWidget):
    closed = pyqtSignal()
    def __init__(self, parent=None):
        super(VistaInserimento, self).__init__(parent)
        uic.loadUi('Dipendente/view/vistaInserimentoCliente.ui', self)

        self.inserisciButton.clicked.connect(self.creaNuovoCliente)
        self.annullaButton.clicked.connect(self.chiudiFinestra)


    def creaNuovoCliente(self):
        if self.controllaCampi():
            nome = self.textNome.text().capitalize().strip()
            cognome = self.textCognome.text().capitalize().strip()
            codiceFiscale = self.textCF.text().upper().strip()
            email = self.textEmail.text().strip()
            sesso = self.comboBoxSesso.currentText()
            abbonato = self.comboBoxAbbonato.currentText()
            tagliaScarpe = self.comboBoxTagliaScarpe.currentText()

            if abbonato == "Si":
                abbonato = True
            else:
                abbonato = False

            cliente = ControlloreCliente().creaCliente(
                abbonato=abbonato,
                codiceFiscale=codiceFiscale,
                cognome=cognome,
                email=email,
                nome=nome,
                sesso=sesso,
                tagliaScarpe=tagliaScarpe
            )
            if cliente is None:
                self.messaggio(tipo=0 , titolo="Inserimeno cliente", mex='<p style=color:white> Cliente già esistente')
            else:
                self.messaggio(tipo=1, titolo="Inserimento cliente", mex='<p style=color:white> Cliente inserito con successo')

            self.closed.emit()
            self.close()

    def controllaCampi(self):
        #nome e cognome devono avere almeno un carattere
        if len(self.textNome.text()) < 2:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Il nome deve avere almeno 2 caratteri")
        elif len(self.textCognome.text()) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il cognome deve avere almeno 2 caratteri")
        #cf di 16 caratteri e alfanumerico
        elif len(self.textCF.text()) != 16 or not self.textCF.text().isalnum():
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Il codice fiscale deve contenere 16 caratteri")
        #controllo sull'email
        elif len(self.textEmail.text()) <1:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Email almeno 1 carattere")
        else:
            return True

    def messaggio(self, tipo, titolo, mex):
        mexBox = QMessageBox()
        mexBox.setWindowTitle(titolo)
        if tipo == 0:
            mexBox.setIcon(QMessageBox.Icon.Warning)
        elif tipo == 1:
            mexBox.setIcon(QMessageBox.Icon.Information)
        mexBox.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mexBox.setText(mex)
        mexBox.exec()

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()
