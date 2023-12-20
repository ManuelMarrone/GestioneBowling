from PyQt6 import uic
from PyQt6.QtWidgets import *

from Amministratore.view.vista_amministratore import VistaAmministratore
from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Dipendente.view.vista_cassiere import VistaCassiere
from Dipendente.view.vista_magazziniere import VistaMagazziniere


class VistaLogin(QWidget):
    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        uic.loadUi('Login/view/login.ui', self)

        self.loginButton.clicked.connect(self.goAccesso)  # definisce l'operazione al click del pulsante

    # controllo validità email e password e mostra il pannello relativo al tipo di utente

    def goAccesso(self):
        VistaLogin.close(self)

        email = self.textEmail.text()
        password = self.textPassword.text()

        if email == "a" and password == "b":
            self.vista_amministratore = VistaAmministratore()
            self.vista_amministratore.closed.connect(self.show)
            self.vista_amministratore.show()
        else:
            # verifica se il dipendente esiste
            # se esiste riconosci il tipo di dipendente e valida i dati inseriti
            # manda al relativo pannello oppure segnala messaggio di errore
            dipendente = ControlloreDipendente.ricercaDipendenteEmail(self,email)

            if dipendente is not None:
                self.controller = ControlloreDipendente(dipendente)
                if password == self.controller.getPassword():         #verifica password del dipendente
                    if self.controller.getRuolo() == "Cassiere":
                        self.vista_cassiere = VistaCassiere()
                        self.vista_cassiere.closed.connect(self.show)
                        self.vista_cassiere.show()
                    else:
                        pass
                        self.vista_magazziniere = VistaMagazziniere()
                        self.vista_magazziniere.closed.connect(self.show)
                        self.vista_magazziniere.show()
                else:
                    pass
                    self.messaggio(tipo=0, titolo="Login dipendente",mex= "Password errata")
            else:
                pass
                self.messaggio(tipo=0, titolo="Login dipendente", mex="Dipendente non trovato")

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