from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

# ci sono degli import da fare
from Cliente.controller.controllore_cliente import ControlloreCliente


class VistaGestionePartite(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestionePartite, self).__init__(parent)
        uic.loadUi('Dipendente/view/gestionePartite.ui', self)

        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCercaCliente)

    def goCercaCliente(self):
        controllo = self.ricercaText.text().split()
        if len(controllo) == 0:                                 #se il controllo è vero riempie la lista dei clienti
            self.riempiListaClienti()
        elif len(controllo) == 2:
            nome, cognome = self.ricercaText.text().split()
            nome = nome.capitalize().strip()                    #Trasforma il primo carattere in maiuscolo e separa le parole
            cognome = cognome.capitalize().strip()
            clienteRicercato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            if clienteRicercato is not None:                    #se il cliente è presente aggiorna la lista
                self.clientiList.clear()
                self.controller = ControlloreCliente(clienteRicercato)
                listaClienti = ControlloreCliente.visualizzaClienti(self)
                if listaClienti is not None:
                    for cliente in listaClienti:
                        if cliente.nome == self.controller.getNome() and cliente.cognome == self.controller.getCognome():
                            item = QListWidgetItem()
                            item.setText(
                                "nome: " + cliente.nome + ", cognome: " + cliente.cognome + ", ruolo: " + cliente.ruolo)
                            self.clientiList.addItem(item)
            else:
                self.messaggio(tipo=1, titolo="Ricerca cliente", mex="Il cliente non è presente")
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

    def riempiListaClienti(self):
        listaClienti = []
        self.clientiList.clear()
        listaClienti = ControlloreCliente.visualizzaClienti(self)
        if listaClienti is not None:
            for cliente in listaClienti:
                item = QListWidgetItem()
                item.setText(
                    "nome: " + cliente.nome + ", cognome: " + cliente.cognome + ", ruolo: " + cliente.ruolo)
                self.clientiList.addItem(item)

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()



