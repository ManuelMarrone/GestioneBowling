from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Cliente.controller.controllore_cliente import ControlloreCliente
from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Cliente.view.vista_inserisci_cliente import VistaInserimento
from Cliente.view.vista_cliente import VistaCliente
from Cliente.view.vista_modifica_cliente import VistaModificaCliente
from Abbonamento.view.vista_abbonamento import VistaAbbonamento

class VistaGestioneClienti(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestioneClienti, self).__init__(parent)

        uic.loadUi('Cliente/view/lista_clienti.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 50
        self.move(x, y)

        self.idCliente = None
        self.itemSelezionato = None
        self.abbona.clicked.connect(self.goCreaAbbonamento)
        self.abbonamentoButton.clicked.connect(self.goGestisciAbbonamento)
        self.aggiungiButton.clicked.connect(self.goCreaCliente)
        self.riempiListaClienti()
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.eliminaButton.clicked.connect(self.goEliminaCliente)
        self.visualizzaButton.clicked.connect(self.goVisualizza)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.modificaButton.clicked.connect(self.goModifica)
        #self.cercaButton.clicked.connect(self.goCerca)

    # def goCerca(self):
    #     controllo = self.ricercaText.text().split()
    #     if len(controllo) == 0:
    #         self.riempiListaDipendenti()
    #     elif len(controllo) == 2:
    #         nome, cognome = self.ricercaText.text().split()
    #         nome = nome.capitalize().strip()
    #         cognome = cognome.capitalize().strip()
    #         dipendenteRicercato = ControlloreDipendente.ricercaDipendenteNomeCognome(self, nome, cognome)
    #         if dipendenteRicercato is not None:
    #             self.dipendentiList.clear()
    #             self.controller = ControlloreDipendente(dipendenteRicercato)
    #             listaDipendenti = ControlloreDipendente.visualizzaDipendenti(self)
    #             if listaDipendenti is not None:
    #                 for dipendente in listaDipendenti:
    #                     if dipendente.nome == self.controller.getNome() and dipendente.cognome == self.controller.getCognome():
    #                         item = QListWidgetItem()
    #                         item.setText(
    #                             "nome: " + dipendente.nome + ", cognome: " + dipendente.cognome + ", ruolo: " + dipendente.ruolo)
    #                         self.dipendentiList.addItem(item)
    #         else:
    #             self.messaggio(tipo=1, titolo="Ricerca dipendente", mex="Il dipendente non è presente")
    #     else:
    #         self.messaggio(tipo=0, titolo="Attenzione",mex="Ricerca non valida")
    def goCreaAbbonamento(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome: ")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            idCliente = ControlloreCliente.getId(clienteSelezionato) # Viene preso l'id del cliente selezionato

            ControlloreAbbonamento.creaAbbonamento(idCliente=idCliente, )

    def goGestisciAbbonamento(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome: ")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()

            clienteSelezionato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            # Preleva l'abbonamento collegato al cliente selezionato tramite l'id
            abbonamento = ControlloreAbbonamento.ricercaAbbonamentoIdCliente(ControlloreCliente.getId(clienteSelezionato))
            self.vista_abbonamento = VistaAbbonamento(abbonamento, clienteSelezionato)
            self.vista_abbonamento.show()

    def riempiListaClienti(self):
        listaClienti = []
        self.clientiList.clear()
        listaClienti = ControlloreCliente().visualizzaClienti()
        if listaClienti is not None:
            for cliente in listaClienti:
                item = QListWidgetItem()
                item.setText("nome: " + cliente.nome + ", cognome: " + cliente.cognome)
                self.clientiList.addItem(item)

    def goCreaCliente(self):
        self.vista_inserisci = VistaInserimento()
        self.vista_inserisci.closed.connect(self.riempiListaClienti)
        self.vista_inserisci.show()

    def goVisualizza(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome: ")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()

            clienteSelezionato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            self.vista_cliente = VistaCliente(clienteSelezionato)
            self.vista_cliente.show()

    def clienteClicked(self, item):
        print("Clicked")
        self.itemSelezionato = item.text()

    def goEliminaCliente(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome:")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente().ricercaClienteNomeCognome(nome, cognome)
            if clienteSelezionato.isAssegnato() is False:
                risultato = ControlloreCliente().rimuoviCliente(clienteSelezionato)
                if risultato:
                    self.messaggio(tipo=1, titolo="Rimozione cliente",mex="Cliente rimosso con successo")
                else:
                    self.messaggio(tipo=0, titolo="Rimozione cliente",mex= "Errore nella rimozione del cliente!")
            else:
                self.messaggio(tipo=0, titolo="Rimozione cliente", mex="Non puoi rimuovere il cliente mentre è assegnato ad un gruppo")
        self.riempiListaClienti()

    def goModifica(self):
        if self.itemSelezionato is not None:
            nome = self.itemSelezionato.split("nome:")[1].split(",")[0].strip()
            cognome = self.itemSelezionato.split("cognome:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente.ricercaClienteNomeCognome(self, nome, cognome)
            if clienteSelezionato.isAssegnato() is False:
                self.vista_modifica = VistaModificaCliente(clienteSelezionato)
                self.vista_modifica.closed.connect(self.riempiListaClienti)
                self.vista_modifica.show()
            else:
                self.messaggio(tipo=0, titolo="Modifica cliente",
                               mex="Non puoi modificare il cliente mentre è assegnato ad un gruppo")

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
