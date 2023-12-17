from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Registra.VistaRegistra import VistaRegistra
from Dipendente.view.vista_dipendente import VistaDipendente
from Dipendente.view.vista_modifica_dipendente import VistaModificaDipendente


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
        self.cercaButton.clicked.connect(self.goCerca)

    def goCerca(self):
        controllo = self.ricercaText.text().split()
        if len(controllo) == 0:
            self.riempiListaDipendenti()
        elif len(controllo) == 2:
            nome, cognome = self.ricercaText.text().split()
            nome = nome.capitalize().strip()
            cognome = cognome.capitalize().strip()
            dipendenteRicercato = ControlloreDipendente.ricercaDipendenteNomeCognome(self, nome, cognome)
            if dipendenteRicercato is not None:
                self.dipendentiList.clear()
                self.controller = ControlloreDipendente(dipendenteRicercato)
                listaDipendenti = ControlloreDipendente.visualizzaDipendenti(self)
                if listaDipendenti is not None:
                    for dipendente in listaDipendenti:
                        if dipendente.nome == self.controller.getNome() and dipendente.cognome == self.controller.getCognome():
                            item = QListWidgetItem()
                            item.setText(
                                "nome: " + dipendente.nome + ", cognome: " + dipendente.cognome + ", ruolo: " + dipendente.ruolo)
                            self.dipendentiList.addItem(item)
            else:
                self.messaggio(tipo=1, titolo="Ricerca dipendente", mex="Il dipendente non è presente")
        else:
            self.messaggio(tipo=0, titolo="Attenzione",mex="Ricerca non valida")



    def riempiListaDipendenti(self):
        listaDipendenti = []
        self.dipendentiList.clear()
        listaDipendenti = ControlloreDipendente.visualizzaDipendenti(self)
        if listaDipendenti is not None:
            for dipendente in listaDipendenti:
                item = QListWidgetItem()
                item.setText(
                    "nome: " + dipendente.nome + ", cognome: " + dipendente.cognome + ", ruolo: " + dipendente.ruolo)
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
                self.messaggio(tipo=1, titolo="Rimozione cliente",mex="Cliente rimosso con successo")
            else:
                self.messaggio(tipo=0, titolo="Rimozione cliente",mex= "Errore nella rimozione del cliente!")
        self.riempiListaDipendenti()

    def goModifica(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome:")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()

            dipendenteSelezionato = ControlloreDipendente.ricercaDipendenteNomeCognome(self, nome, cognome)
            self.vista_modifica = VistaModificaDipendente(dipendenteSelezionato)
            self.vista_modifica.closed.connect(self.riempiListaDipendenti)
            self.vista_modifica.show()

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

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()
