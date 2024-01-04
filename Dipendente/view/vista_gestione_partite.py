from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

# ci sono degli import da fare
from Cliente.controller.controllore_cliente import ControlloreCliente
from Dipendente.view.vista_lista_clienti import VistaGestioneClienti
from Pista.controller.controllore_pista import ControllorePista

class VistaGestionePartite(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestionePartite, self).__init__(parent)
        uic.loadUi('Dipendente/view/gestionePartite.ui', self)

        self.idCliente = None
        self.itemSelezionato = None

        self.riempiListaPiste()
        self.riempiListaClienti()
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)



    def goCerca(self):
        controllo = self.ricercaText.text().split()
        if len(controllo) == 0:
            self.riempiListaClienti()
        elif len(controllo) == 2:
            nome, cognome = self.ricercaText.text().split()
            nome = nome.capitalize().strip()
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
                            item.setText("nome: " + cliente.nome + ", cognome: " + cliente.cognome)
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
                item.setText("nome: " + cliente.nome + ", cognome: " + cliente.cognome)
                self.clientiList.addItem(item)

    def riempiListaPiste(self):
        listaPiste = []
        self.pisteList.clear()
        listaPiste = ControllorePista.visualizzaPiste(self)
        if listaPiste is not None:
            for pista in listaPiste:
                item = QListWidgetItem()
                item.setText("id: " + pista.id + ", stato: " + pista.disponibilita)
                self.pisteList.addItem(item)

    def goVisualizza(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome:")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()

            clienteSelezionato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            self.vista_cliente = VistaGestioneClienti(clienteSelezionato)
            self.vista_cliente.show()

    def clienteClicked(self, item):
        self.itemSelezionato = item.text()


    def chiudiFinestra(self):
        self.closed.emit()
        self.close()



