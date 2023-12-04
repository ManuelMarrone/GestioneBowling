from PyQt6 import uic
from PyQt6.QtWidgets import *

from Amministratore.view.vista_gestione_dipendenti import VistaGestioneDipendenti


class VistaAmministratore(QWidget):
    def __init__(self, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        uic.loadUi('Amministratore/view/amministratoreMain.ui', self)

        self.gestioneDipendentiButton.clicked.connect(self.go_dipendenti)

    def go_dipendenti(self):
        VistaAmministratore.close(self)
        VistaGestioneDipendenti().show()
