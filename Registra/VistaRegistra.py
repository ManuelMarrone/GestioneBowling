from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.uic.properties import QtCore

from Dipendente.controller.controllore_dipendente import ControlloreDipendente

class VistaRegistra(QWidget):
    def __init__(self, parent=None):
        super(VistaRegistra, self).__init__(parent)
        print("Ciao")
        uic.loadUi('Registra/registra.ui', self)
        print("hola")

        self.controlloreDipendenti = ControlloreDipendente()
        self.registraButton.clicked.connect(self.creaAccount)
        self.annullaButton.clicked.connect(VistaRegistra.close())


    def creaAccount(self):

        if self.controllaCampi():
            nome = self.textNome.text().capitalize().strip()
            cognome = self.textCognome.text().capitalize().strip()
            ruolo = self.comboBoxRuolo.currentText()
            codiceFiscale = self.textCF.text().upper().strip()
            dataNascita = self.textNascita.dateTime() #formatta la data
            email = self.textEmail.text().strip()
            sesso = self.comboBoxSesso.currentText()
            telefono = self.textTelefono.text().strip()
            password = self.textPassword.text().strip()

            dipendente = self.controlloreDipendenti.creaDipendente(
                ruolo=ruolo,
                codiceFiscale=codiceFiscale,
                cognome=cognome,
                dataNascita=dataNascita,
                email=email,
                nome=nome,
                password=password,
                sesso=sesso,
                telefono=telefono
            )
            if dipendente is None:
                self.messaggio(tipo=0 , titolo="Creazione Account", mex='<p style=color:white> Errore! Account già esistente!')
            else:
                self.messaggio(tipo=1, titolo="Creazione Account", mex='<p style=color:white> Registrato con successo,<br> con id: "{}" e password: "{}"</p>'.format(
                        dipendente.id,
                        dipendente.password))

            self.close()

    def controllaCampi(self):
        #nome e cognome devono avere almeno un carattere
        if len(self.textNome.text()) < 1:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Il nome deve avere almeno un carattere")
        elif len(self.textCognome.text()) < 1:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il cognome deve avere almeno un carattere")
        #cf di 16 caratteri e alfanumerico
        elif len(self.textCF.text()) != 16 or not self.textCF.text().isalnum():
            self.messaggio(self.messaggio(tipo = 0, titolo="Attenzione", mex="Il codice fiscale deve contenere 16 caratteri"))
        #controllo sull'email
        elif len(self.textEmal.text()) <1:
            self.messaggio(self.messaggio(tipo = 0, titolo="Attenzione", mex="Email almeno 1 carattere"))
        #numero di telefono solo 10 numeri
        elif len(self.textTelefono.text()) != 10 or not str(self.textTelefono.text()).isnumeric():
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il numero di telefono deve contenere 10 cifre")
        #password minimo 8 caratteri
        elif len(self.textPassword.text()) < 8:
            self.messaggio(tipo=0, titolo="Attenzione", mex="La password deve avere almeno 8 caratteri")

    def messaggio(self, tipo, titolo, mex):
        mexBox = QMessageBox()
        mexBox.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mexBox.setWindowTitle(titolo)
        if tipo == 0:
            mexBox.setIcon(QMessageBox.Icon.Warning)
        elif tipo == 1:
            mexBox.setIcon(QMessageBox.Icon.Information)
        mexBox.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mexBox.setText(mex)
        mexBox.exec()

