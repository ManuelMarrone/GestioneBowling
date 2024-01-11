from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Cliente.controller.controllore_cliente import ControlloreCliente
from Scarpa.controller.controllore_scarpa import ControlloreScarpa


class VistaMagazziniere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaMagazziniere, self).__init__(parent)
        uic.loadUi('Dipendente/view/magazziniereMain.ui', self)

        self.idDipendente = None
        self.itemSelezionato = None
        self.itemClienteSelezionato = None

        self.riempiListaScarpe()
        self.scarpeList.itemClicked.connect(self.scarpaClicked)
        self.esciButton.clicked.connect(self.chiudiFinestra)
        self.assegnaButton.clicked.connect(self.assegnaScarpa)
        self.clientiList.itemClicked.connect(self.clienteClicked)


    def scarpaClicked(self, item):
        self.itemSelezionato = item.text()

    def clienteClicked(self, item):
        self.itemClienteSelezionato = item.text()

    def riempiListaScarpe(self):
        listaScarpe = []
        self.scarpeList.clear()
        listaScarpe = ControlloreScarpa.visualizzaScarpe(self)
        if listaScarpe is not None:
            for scarpa in listaScarpe:
                if scarpa.disponibilita is True:
                    item = QListWidgetItem()
                    item.setText(
                        "Scarpa " + str(scarpa.taglia) + ", id: " + str(scarpa.id))
                    self.scarpeList.addItem(item)

    def assegnaScarpa(self):
        if self.itemSelezionato is not None and self.itemClienteSelezionato is not None:
            taglia = self.itemSelezionato.split("Scarpa")[1].split(",")[0].strip()
            id = self.itemSelezionato.split("id:")[1]

            nome = self.itemClienteSelezionato.split("Nome")[1].split(",")[0].strip()
            cognome = self.itemClienteSelezionato.split("Cognome")[1].split(",")[0].strip()


            #da finire, mancano i gruppi di clienti
            # scarpaSelezionata = ControlloreScarpa.ricercaScarpaId(self, taglia)
            # clienteSelezionato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            # ControlloreScarpa(scarpaSelezionata).assegnaScarpa(self, clienteSelezionato)

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()