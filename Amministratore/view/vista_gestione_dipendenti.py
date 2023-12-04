from PyQt6 import uic
from PyQt6.QtWidgets import *

from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Registra.VistaRegistra import VistaRegistra


class VistaGestioneDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaGestioneDipendenti, self).__init__(parent)

        uic.loadUi('Amministratore/view/gestioneDipendenti.ui', self)

        self.aggiungiButton.clicked.connect(self.goCreaDipendente)
        # self.riempiListaDipendenti()

    def riempiListaDipendenti(self):
        self.dipendentiList.clear()
        print("1")
        self.listaDipendenti = ControlloreDipendente.visualizzaDipendenti()
        print("2")
        if self.listaDipendenti is not None:
            print("3")
            self.dipendentiList.addItems(dipendente.__str__() for dipendente in self.listaDipendenti.values())

    def goCreaDipendente(self):
        VistaRegistra.show()
