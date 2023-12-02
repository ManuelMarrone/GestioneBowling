from PyQt6 import uic
from PyQt6.QtWidgets import *

from Dipendente.controller.controllore_dipendente import ControlloreDipendente


class VistaGestioneDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaGestioneDipendenti, self).__init__(parent)
        uic.loadUi('Amministratore/view/gestioneDipendenti.ui', self)
        self.riempiListaDipendenti()

    def riempiListaDipendenti(self):
        self.dipendentiList.clear()
        self.listaDipendenti = ControlloreDipendente.visualizzaDipendenti()
        if self.listaDipendenti is not None:
            self.dipendentiList.addItems(dipendente.__str__() for dipendente in self.listaDipendenti.values())