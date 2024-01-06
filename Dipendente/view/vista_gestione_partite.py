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


        self.clientiList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.idCliente = None
        self.itemSelezionato = None

        self.riempiListaPiste()
        self.riempiListaClienti()
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)

        self.selezionaButton.clicked.connect(self.creaGruppoClienti)


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
                item = QComboBox()
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

    def creaGruppoClienti(self):
        clienti_scelti = self.clientiList.selectedItems()

        if not clienti_scelti:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Nessun cliente selezionato.")
            return

        clienti_selezionati = []

        for i in clienti_scelti:
            cliente = i.text()
            clienti_selezionati.append(cliente)

        if len(clienti_selezionati) > 8:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Puoi selezionare massimo 8 clienti per gruppo")
            return

        gruppo_clienti = []
        for i in range(0, len(clienti_selezionati), 8):
            gruppo_clienti = clienti_selezionati[i:i+8]

        print("Liste accorpolate:")
        for c in gruppo_clienti:
            print(c)