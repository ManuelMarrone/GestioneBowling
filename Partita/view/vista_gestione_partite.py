from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

import time

# ci sono degli import da fare
from Cliente.controller.controllore_cliente import ControlloreCliente
from Dipendente.view.vista_lista_clienti import VistaGestioneClienti
from Pista.controller.controllore_pista import ControllorePista
from GruppoClienti.model.GruppoClienti import GruppoClienti


class VistaGestionePartite(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestionePartite, self).__init__(parent)
        uic.loadUi('Partita/view/gestionePartite.ui', self)


        self.clientiList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.pisteList.setEditable(True)


        self.idCliente = None
        self.itemSelezionato = None

        self.riempiListaPiste()
        self.riempiListaClienti()
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)

        self.selezionaButton.clicked.connect(self.creaGruppoClienti)
        self.assegnaButton.clicked.connect(self.assegnaPista)

        tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
        if "True" not in tutte_le_piste:
            self.messaggioTempo.setText("Tutte le piste sono occupate")

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
                item.setText("nome: " + cliente.nome + ", cognome: " + cliente.cognome + ", id: " + cliente.id)
                self.clientiList.addItem(item)

    def riempiListaPiste(self):
        listaPiste = []
        self.pisteList.clear()
        listaPiste = ControllorePista.visualizzaPiste(self)
        if listaPiste is not None:
            for pista in listaPiste:
                item = QComboBox()
                item.addItem("id: " + str(pista.id) + " disponibilità: " + str(pista.disponibilita))
                self.pisteList.addItem(item.currentText())

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

        if len(clienti_selezionati) < 2:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="Devi selezionare almeno 2 clienti per gruppo")
            return

        gruppo_clienti = []
        for i in range(0, len(clienti_selezionati), 8):
            gruppo_clienti = clienti_selezionati[i:i+8]


        print("Clienti nel gruppo:")
        for c in gruppo_clienti:
            print(c)


        numero_partite, ok = QInputDialog.getInt(self, 'Numero Partte', 'quante partite intende effettuare il gruppo?')
        while numero_partite <= 0 :
            self.messaggio(tipo = 0, titolo = "Attenzione", mex = "un gruppo deve effettuare almeno una partita")
            numero_partite, ok = QInputDialog.getInt(self, 'Numero Partte', 'quante partite intende effettuare il gruppo?')


        GruppoClienti.creaGruppoClienti(self,1 , gruppo_clienti, numero_partite)

    def assegnaPista(self):
        tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
        pista_scelta = self.pisteList.currentText()

        if "True" not in tutte_le_piste:
            self.messaggioTempo.setText("La prossima pista sarà libera tra 20 minuti")


        if "False" in pista_scelta:
            self.messaggio(tipo = 0, titolo="Attenzione", mex="La pista selezionata non è disponibile")
        else:
            print(tutte_le_piste)