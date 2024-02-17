from PyQt6 import uic
from PyQt6.QtWidgets import *

from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti


class VistaGruppo(QWidget):
    def __init__(self, gruppo, parent=None):
        super(VistaGruppo, self).__init__(parent)

        uic.loadUi('GruppoClienti/view/vistaGruppo.ui', self)

        listaClienti = ControlloreGruppoClienti(gruppo).getMembri()
        if listaClienti is not None:
            for cliente in listaClienti:
                item = QListWidgetItem()
                item.setText(
                    "nome: " + cliente.getNome() + ", cognome: " + cliente.getCognome() + ", codice fiscale: " + cliente.getCodiceFiscale())
                self.membriList.addItem(item)

        self.indietroButton.clicked.connect(self.chiudiFinestra)

    def chiudiFinestra(self):
        self.close()
