from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Registra.VistaRegistra import VistaRegistra
from Dipendente.view.vista_dipendente import VistaDipendente

class VistaGestioneDipendenti(QWidget):
    closed = pyqtSignal()
    def __init__(self, parent=None):
        super(VistaGestioneDipendenti, self).__init__(parent)

        uic.loadUi('Amministratore/view/gestioneDipendenti.ui', self)

        self.idDipendente = None
        self.itemSelezionato = None

        self.aggiungiButton.clicked.connect(self.goCreaDipendente)
        self.riempiListaDipendenti()
        self.dipendentiList.itemClicked.connect(self.dipendenteClicked)
        self.eliminaButton.clicked.connect(self.goEliminaDipendente)
        self.visualizzaButton.clicked.connect(self.goVisualizza)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.modificaButton.clicked.connect(self.goModifica)

    def riempiListaDipendenti(self):
        listaDipendenti = []
        self.dipendentiList.clear()
        listaDipendenti = ControlloreDipendente.visualizzaDipendenti(self)
        if listaDipendenti is not None:
            for dipendente in listaDipendenti:
                item = QListWidgetItem()
                item.setText("nome: " + dipendente.nome + ", cognome: " + dipendente.cognome + ", ruolo: " + dipendente.ruolo)
                self.dipendentiList.addItem(item)

    def goCreaDipendente(self):
        self.vista_registra = VistaRegistra()
        self.vista_registra.closed.connect(self.riempiListaDipendenti)
        self.vista_registra.show()

    def goVisualizza(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome:")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()

            dipendenteSelezionato = ControlloreDipendente.ricercaDipendenteNomeCognome(self, nome, cognome)
            self.vista_dipendente = VistaDipendente(dipendenteSelezionato)
            self.vista_dipendente.show()

    def dipendenteClicked(self, item):
        self.itemSelezionato = item.text()

    def goEliminaDipendente(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome:")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()
            dipendenteSelezionato = ControlloreDipendente.ricercaDipendenteNomeCognome(self, nome, cognome)
            risultato = ControlloreDipendente.rimuoviDipendente(self, dipendenteSelezionato)
            if risultato:
                self.messageBox("Cliente rimosso con successo")
            else:
                self.messageBox("Errore nella rimozione del cliente!")
        self.riempiListaDipendenti()

    def goModifica(self):
        if self.itemSelezionato is not None:
            #fai VistaModifica

    def messageBox(self, mex):
        mb = QMessageBox()
        mb.setWindowTitle("Rimozione cliente")
        mb.setIcon(QMessageBox.Icon.Information)
        mb.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mb.setText(mex)
        mb.exec()


    def chiudiFinestra(self):
        self.closed.emit()
        self.close()