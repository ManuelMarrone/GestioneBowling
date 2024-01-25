from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QWidget, QMessageBox

from Dipendente.controller.controllore_dipendente import ControlloreDipendente


class VistaModificaDipendente(QWidget):
    closed = QtCore.pyqtSignal()

    def __init__(self, dipendenteSelezionato=None, parent=None):
        super(VistaModificaDipendente, self).__init__(parent)
        uic.loadUi('Dipendente/view/vistaModificaDipendente.ui', self)
        self.controller = ControlloreDipendente(dipendenteSelezionato)

        self.confermaButton.clicked.connect(self.goModificaAccount)
        self.annullaButton.clicked.connect(self.chiudiFinestra)
        self.caricaDatiDipendente()

    def caricaDatiDipendente(self):
        self.textNome.setText(self.controller.getNome())
        self.textCognome.setText(self.controller.getCognome())
        self.comboBoxRuolo.setCurrentText(self.controller.getRuolo())
        self.CFLabel.setText(self.controller.getCF())
        data = QtCore.QDateTime.fromString(self.controller.getDataNascita(), "dd-MM-yyyy")
        self.textNascita.setDateTime(data)
        self.textEmail.setText(self.controller.getEmail())
        self.comboBoxSesso.setCurrentText(self.controller.getSesso())
        self.textTelefono.setText(self.controller.getTelefono())
        self.textVecchiaPassword.setText(self.controller.getPassword())


    def goModificaAccount(self):
        if self.controllaCampi():
            nome = self.textNome.text().capitalize().strip()
            cognome = self.textCognome.text().capitalize().strip()
            ruolo = self.comboBoxRuolo.currentText()
            self.CFLabel.setText(self.controller.getCF())
            dataNascita = self.textNascita.dateTime()  # formatta la data
            email = self.textEmail.text().strip()
            sesso = self.comboBoxSesso.currentText()
            telefono = self.textTelefono.text().strip()
            password = self.textNuovaPassword.text().strip()

            risultato = self.controller.modificaDipendente(
                nuovoRuolo=ruolo,
                codiceFiscale=self.controller.getCF(),
                nuovoCognome=cognome,
                nuovaDataNascita=dataNascita,
                nuovaEmail=email,
                nuovoNome=nome,
                nuovaPassword=password,
                nuovoSesso=sesso,
                nuovoTelefono=telefono
            )
            if not risultato:
                self.messaggio(tipo=0, titolo="Attenzione", mex="Errore durante la modifica del profilo")
            else:
                self.messaggio(tipo=1, titolo="Modifica Account", mex="Profilo modificato con successo")
                self.closed.emit()
                self.close()

    def controllaCampi(self):
        simboliSpeciali = ['$', '@', '#', '%']
        # nome e cognome devono avere almeno un carattere
        if len(self.textNome.text()) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il nome deve avere almeno 2 caratteri")
        elif len(self.textCognome.text()) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il cognome deve avere almeno 2 caratteri")
        # controllo sull'email
        elif len(self.textEmail.text()) < 1:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Email almeno 1 carattere")
        # numero di telefono solo 10 numeri
        elif len(self.textTelefono.text()) != 10 or not str(self.textTelefono.text()).isnumeric():
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il numero di telefono deve contenere 10 cifre")
        if self.textVecchiaPassword.text() != self.controller.getPassword():
            self.messaggio(tipo=1, titolo="Modifica Account",mex="La vecchia password non coincide con quella inserita")
        # password minimo 8 caratteri
        elif len(self.textNuovaPassword.text()) < 8 or not any(
                char.isdigit() for char in self.textNuovaPassword.text()) or not any(
            char.isdigit() for char in self.textNuovaPassword.text()) or not any(
            char.isupper() for char in self.textNuovaPassword.text()) or not any(
            char in simboliSpeciali for char in self.textNuovaPassword.text()):
            self.messaggio(tipo=0, titolo="Attenzione",mex="La password deve avere almeno 8 caratteri, un numero, una lettera maiuscola e uno dei simboli $@#%")
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
