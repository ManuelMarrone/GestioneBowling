from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Cliente.controller.controllore_cliente import ControlloreCliente
from Scarpa.controller.controllore_scarpa import ControlloreScarpa
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti

class VistaMagazziniere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaMagazziniere, self).__init__(parent)
        uic.loadUi('Dipendente/view/magazziniereMain.ui', self)

        self.idDipendente = None
        self.itemSelezionato = None
        self.itemClienteSelezionato = None

        self.riempiListaScarpe()
        self.riempiBoxGruppi()
        self.riempiListaClienti()
        self.scarpeList.itemClicked.connect(self.scarpaClicked)
        self.esciButton.clicked.connect(self.chiudiFinestra)
        self.assegnaButton.clicked.connect(self.assegnaScarpa)
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.gruppiComboBox.activated.connect(self.riempiListaClienti)


    def scarpaClicked(self, item):
        self.itemSelezionato = item.text()

    def clienteClicked(self, item):
        self.itemClienteSelezionato = item.text()

    def riempiListaScarpe(self):
        listaScarpe = []
        self.scarpeList.clear()
        listaScarpe = ControlloreScarpa().visualizzaScarpe()
        if listaScarpe is not None:
            for scarpa in listaScarpe:
                if scarpa.getDisponibilitaScarpa() is True:
                    item = QListWidgetItem()
                    item.setText(
                        "Scarpa " + str(scarpa.getTagliaScarpa()) + ", id: " + str(scarpa.getIdScarpa()))
                    self.scarpeList.addItem(item)

    def riempiListaClienti(self):
        self.clientiList.clear()
        idSelezionato = self.gruppiComboBox.currentText()
        gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idSelezionato)
        if gruppoSelezionato is not None:
            for cliente in ControlloreGruppoClienti(gruppoSelezionato).getMembri():
                nome = cliente.split("nome: ")[1].split(",")[0].strip()
                cognome = cliente.split("cognome:")[1].split(",")[0].strip()
                istanza = ControlloreCliente().ricercaClienteNomeCognome(nome, cognome)
                taglia = ControlloreCliente(istanza).getTagliaScarpe()
                IdScarpa = ControlloreCliente(istanza).getIdScarpa()
                if taglia != "0" and IdScarpa == "":
                    item = QListWidgetItem()
                    item.setText(
                        nome + " " + cognome+ " taglia:" + taglia)
                    self.clientiList.addItem(item)

    def riempiBoxGruppi(self):
        gruppi = []
        self.gruppiComboBox.clear()
        gruppi = ControlloreGruppoClienti().visualizzaGruppi()
        if gruppi is not None:
            for gruppo in gruppi:
                self.gruppiComboBox.addItem(str(gruppo.getId()))

    def assegnaScarpa(self):
        if self.itemSelezionato is not None and self.itemClienteSelezionato is not None:
            taglia = self.itemSelezionato.split("Scarpa")[1].split(",")[0].strip()
            idScarpa = self.itemSelezionato.split("id:")[1].strip()

            nome, cognome = self.itemClienteSelezionato.split()[:2]

            scarpaSelezionata = ControlloreScarpa().ricercaScarpaId(idScarpa)
            clienteSelezionato = ControlloreCliente().ricercaClienteNomeCognome(nome, cognome)

            idSelezionato = self.gruppiComboBox.currentText()
            gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idSelezionato)

            scarpa = ControlloreScarpa(scarpaSelezionata)
            scarpa.assegnaScarpa(gruppoSelezionato, clienteSelezionato, idScarpa)
            self.riempiListaScarpe()
            self.riempiListaClienti()
        else:
            self.messaggio(tipo=0, titolo="Assegnamento scarpa", mex="Selezionare un cliente e una scarpa")

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()

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
