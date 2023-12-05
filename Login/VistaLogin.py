from PyQt6 import uic
from PyQt6.QtWidgets import *

from Amministratore.view.vista_amministratore import VistaAmministratore


class VistaLogin(QWidget):
    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        uic.loadUi('Login/login.ui', self)

        self.loginButton.clicked.connect(self.goAccesso)  # definisce l'operazione al click del pulsante

    # controllo validità email e password e mostra il pannello relativo al tipo di utente

    def goAccesso(self):
        VistaLogin.close(self)

        email = self.textEmail.text()
        password = self.textPassword.text()

        if email == "admin@email" and password == "passwordadmin":
            self.vista_amministratore = VistaAmministratore()
            self.vista_amministratore.show()
        else:
            pass
            #verifica se il dipendente
            #se esiste riconosci il tipo di dipendente e valida i dati inseriti
            #manda al relativo pannello oppure segnala messaggio di errore

