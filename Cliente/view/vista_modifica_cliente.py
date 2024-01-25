from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIcon


from Cliente.controller.controllore_cliente import ControlloreCliente

class VistaModificaCliente(QWidget):
    closed = QtCore.pyqtSignal()
    def __init__(self, clienteSelezionato=None, parent=None):
        super(VistaModificaCliente, self).__init__(parent)
        uic.loadUi('Cliente/view/vistaModificaCliente.ui', self)

        icon = QIcon('Data/icon/user.svg')
        self.setWindowIcon(icon)
        self.setWindowTitle("Modifica")

        self.controller = ControlloreCliente(clienteSelezionato)
        self.loadDataClient()

        self.confermaButton.clicked.connect(self.goModificaAccount)
        self.annullaButton.clicked.connect(self.chiudiFinestra)

    def loadDataClient(self):
        self.textNome.setText(self.controller.getNome())
        self.textCognome.setText(self.controller.getCognome())
        self.textCF.setText(self.controller.getCodiceFiscale())
        self.textCF.setEnabled(False)
        self.textEmail.setText(self.controller.getEmail())
        self.comboBoxSesso.setCurrentText(self.controller.getSesso())
        self.comboBoxAbbonato.setCurrentText(self.controller.isAbbonato())
        self.comboBoxAbbonato.setEnabled(False)
        self.comboBoxTagliaScarpe.setCurrentText(self.controller.getTagliaScarpe())


    def goModificaAccount(self):
        if self.controllaCampi():
            nome = self.textNome.text().capitalize().strip()
            cognome = self.textCognome.text().capitalize().strip()
            email = self.textEmail.text().strip()
            sesso = self.comboBoxSesso.currentText()
            abbonato = self.comboBoxAbbonato.currentText()
            tagliaScarpe = self.comboBoxTagliaScarpe.currentText()

            if abbonato == "Si":
                abbonato = True
            else:
                abbonato = False

            risultato = self.controller.modificaCliente(
                nuovoNome=nome,
                nuovoCognome=cognome,
                codiceFiscale=self.controller.getCodiceFiscale(),
                nuovaEmail=email,
                nuovoSesso=sesso,
                nuovoAbbonato=abbonato,
                nuovaTagliaScarpe=tagliaScarpe
            )
            if not risultato:
                self.messaggio(tipo=0, titolo="Modifica cliente", mex="Errore durante la modifica del cliente")
            else:
                self.messaggio(tipo=1, titolo="Modifica cliente", mex="Cliente modificato con successo")
                self.closed.emit()
                self.close()

    def controllaCampi(self):
        # nome e cognome devono avere almeno un carattere
        if len(self.textNome.text()) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il nome deve avere almeno 2 caratteri")
        elif len(self.textCognome.text()) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Il cognome deve avere almeno 2 caratteri")
        # controllo sull'email
        elif len(self.textEmail.text()) < 1:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Email almeno 1 carattere")
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
