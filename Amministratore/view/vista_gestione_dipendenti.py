from PyQt6 import uic
from PyQt6.QtWidgets import *

from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Registra.VistaRegistra import VistaRegistra
from Dipendente.view.vista_dipendente import VistaDipendente


class VistaGestioneDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaGestioneDipendenti, self).__init__(parent)

        uic.loadUi('Amministratore/view/gestioneDipendenti.ui', self)

        self.aggiungiButton.clicked.connect(self.goCreaDipendente)
        self.riempiListaDipendenti()
        self.dipendentiList.itemClicked.connect()

    def riempiListaDipendenti(self):
        listaDipendenti = []
        self.dipendentiList.clear()
        listaDipendenti = ControlloreDipendente.visualizzaDipendenti(self)
        if listaDipendenti is not None:
            print(listaDipendenti)
            for dipendente in listaDipendenti:
                item = QListWidgetItem()
                item.setText("nome: " + dipendente.nome + ", cognome: " +  dipendente.cognome + ", ruolo: " + dipendente.ruolo)
                self.dipendentiList.addItem(item)



    def goCreaDipendente(self):
        self.vista_registra = VistaRegistra()
        self.vista_registra.show()
