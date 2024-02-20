from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from datetime import datetime, timedelta

from Cliente.controller.controllore_cliente import ControlloreCliente
from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Cliente.view.vista_inserisci_cliente import VistaInserimento
from Cliente.view.vista_cliente import VistaCliente
from Cliente.view.vista_modifica_cliente import VistaModificaCliente
from Abbonamento.view.vista_abbonamento import VistaAbbonamento
from Ricevuta.controller.controllore_ricevuta import ControlloreRicevuta


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

        self.itemSelezionato = None
        self.abbonaButton.clicked.connect(self.goCreaAbbonamento)
        self.abbonamentoButton.clicked.connect(self.goGestisciAbbonamento)
        self.aggiungiButton.clicked.connect(self.goCreaCliente)
        self.riempiListaClienti()
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.eliminaButton.clicked.connect(self.goEliminaCliente)
        self.visualizzaButton.clicked.connect(self.goVisualizza)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.modificaButton.clicked.connect(self.goModifica)
        self.cercaButton.clicked.connect(self.goCerca)

    def goCerca(self):
        ricerca = self.ricercaText.text().split()
        selezione = self.selettoreComboBox.currentIndex()
        if selezione == 0:
            if self.controlloNomeCognome(ricerca):
                sottostringhe = self.ricercaText.text().split()

                nome = sottostringhe[0].capitalize().strip()
                cognome = ' '.join(sottostringhe[1:]).capitalize().strip()

                clientiRicercati = ControlloreCliente().ricercaClienteNomeCognome(nome, cognome)
                if clientiRicercati is not None:
                    self.clientiList.clear()

                    for cliente in clientiRicercati:
                        item = QListWidgetItem()
                        item.setText(
                            "nome: " + ControlloreCliente(
                                cliente).getNome() + ", cognome: " + ControlloreCliente(
                                cliente).getCognome() + ", codice fiscale: " + ControlloreCliente(
                                cliente).getCodiceFiscale())
                        self.clientiList.addItem(item)
                else:
                    self.messaggio(tipo=1, titolo="Ricerca cliente", mex="Il cliente non è presente")

        elif selezione == 1:
            if self.controlloCodiceFiscale(ricerca):
                codiceFiscale = self.ricercaText.text().upper()
                clienteRicercato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)
                if clienteRicercato is not None:
                    self.clientiList.clear()

                    item = QListWidgetItem()
                    item.setText(
                        "nome: " + ControlloreCliente(
                            clienteRicercato).getNome() + ", cognome: " + ControlloreCliente(
                            clienteRicercato).getCognome() + ", codice fiscale: " + ControlloreCliente(
                            clienteRicercato).getCodiceFiscale())
                    self.clientiList.addItem(item)
                else:
                    self.messaggio(tipo=1, titolo="Ricerca cliente", mex="Il cliente non è presente")

        elif selezione == 2:
            if self.controlloEmail(ricerca):
                email = self.ricercaText.text()
                clientiRicercati = ControlloreCliente().ricercaClienteEmail(email)
                if clientiRicercati is not None:
                    self.clientiList.clear()
                    for cliente in clientiRicercati:
                                item = QListWidgetItem()
                                item.setText(
                                    "nome: " + ControlloreCliente(
                                        cliente).getNome() + ", cognome: " + ControlloreCliente(
                                        cliente).getCognome() + ", codice fiscale: " + ControlloreCliente(
                                        ControlloreCliente(cliente)).getCodiceFiscale() + ", email: " +ControlloreCliente(
                                        cliente).getEmail())
                                self.clientiList.addItem(item)
                else:
                    self.messaggio(tipo=1, titolo="Ricerca cliente", mex="Il cliente non è presente")

    def controlloEmail(self, ricerca):
        if len(ricerca) == 0:
            self.riempiListaClienti()
        elif len(ricerca) == 1:
            return True
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

    def controlloCodiceFiscale(self, ricerca):
        if len(ricerca) == 0:
            self.riempiListaClienti()
        elif len(ricerca) == 1 and len(ricerca[0]) == 16:
            return True
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

    def controlloNomeCognome(self, ricerca):
        if len(ricerca) == 0:
            self.riempiListaClienti()
        elif len(ricerca) >= 2:
            return True

    def goCreaAbbonamento(self):
        if self.itemSelezionato is not None:
            codiceFiscale = self.itemSelezionato.split("codice fiscale:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)

            if clienteSelezionato.abbonato is False:
                if self.optTessera(codiceFiscale, clienteSelezionato):
                    cfCliente = ControlloreCliente(clienteSelezionato).getCodiceFiscale()  # Viene preso il codice fiscale del cliente selezionato

                    data_validazione = datetime.now() #DATA CHE GLI DOVRA' ESSERE PASSATA ma per il momento prendiamo quella corrente
                    data_fine = data_validazione + timedelta(days=30)
                    ControlloreAbbonamento().creaAbbonamento(dataFine=data_fine.strftime("%Y-%m-%d"),
                                                             dataValidazione=data_validazione.strftime("%Y-%m-%d %H:%M"),
                                                             partiteGratuite=15,
                                                             pagamentoRidotto=False,
                                                             cfCliente=cfCliente)
                    ControlloreCliente(clienteSelezionato).setAbbonato(val=True)
                    self.messaggio(tipo=1, titolo="Abbonamento cliente",
                                   mex='<p style=color:white> Cliente abbonato con successo')
                else:
                    self.messaggio(tipo=1, titolo="Abbonamento", mex="Abbonamento annullato")

            else:
                self.messaggio(tipo=0, titolo="Abbonamento cliente",mex='<p style=color:white> Il cliente risulta gia abbonato')


    def optTessera(self, codiceFiscale, cliente):
        # opzione tessera
        opzioni = ['Si', 'No']
        surpluss = 0
        while True:
            scelta, ok = QInputDialog.getItem(None, 'Tessera', 'Il cliente necessita della tessera?', opzioni,
                                              editable=False)
            if ok:
                if scelta == 'Si':
                    surpluss = 5
                else:
                    surpluss = 0
            else:
                return False
            importo = 30
            clienti=[]
            nome = ControlloreCliente(cliente).getNome()
            cognome = ControlloreCliente(cliente).getCognome()
            importoTot = importo+surpluss
            clienti.append(nome+" "+cognome+" "+str(importoTot)+"€")
            ControlloreRicevuta().creaRicevuta(dataEmissione=datetime.now().date(), id=codiceFiscale, importo=importoTot,
                                               oraEmissione=datetime.now().time(), membri=clienti, tipo="Abbonamento")
            return True

    def goGestisciAbbonamento(self):
        if self.itemSelezionato is not None:
            codiceFiscale = self.itemSelezionato.split("codice fiscale:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)

            if clienteSelezionato.abbonato is True:
                abbonamento = ControlloreAbbonamento().ricercaAbbonamentoCfCliente(clienteSelezionato.getCodiceFiscale())  # Preleva l'abbonamento collegato al cliente selezionato tramite l'id
                self.vista_abbonamento = VistaAbbonamento(abbonamento, clienteSelezionato)
                self.vista_abbonamento.show()
            else:
                self.messaggio(tipo=0, titolo="Abbonamento cliente",
                               mex='<p style=color:white> Il cliente selezionato non risulta abbonato')

    def riempiListaClienti(self):
        listaClienti = []
        self.clientiList.clear()
        listaClienti = ControlloreCliente().visualizzaClienti()
        if listaClienti is not None:
            for cliente in listaClienti:
                item = QListWidgetItem()
                item.setText(
                    "nome: " + ControlloreCliente(cliente).getNome() + ", cognome: " + ControlloreCliente(cliente).getCognome() + ", codice fiscale: " + ControlloreCliente(cliente).getCodiceFiscale())
                self.clientiList.addItem(item)

    def goCreaCliente(self):
        self.vista_inserisci = VistaInserimento()
        self.vista_inserisci.closed.connect(self.riempiListaClienti)
        self.vista_inserisci.show()

    def goVisualizza(self):
        if self.itemSelezionato is not None:
            codiceFiscale = self.itemSelezionato.split("codice fiscale:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)
            self.vista_cliente = VistaCliente(clienteSelezionato)
            self.vista_cliente.show()

    def clienteClicked(self, item):
        self.itemSelezionato = item.text()

    def goEliminaCliente(self):
        if self.itemSelezionato is not None:
            codiceFiscale = self.itemSelezionato.split("codice fiscale:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)
            if clienteSelezionato.isAssegnato() is False:
                if clienteSelezionato.getAbbonato() is False:
                    risultato = ControlloreCliente().rimuoviCliente(clienteSelezionato)
                    if risultato:
                        self.messaggio(tipo=1, titolo="Rimozione cliente", mex="Cliente rimosso con successo")
                    else:
                        self.messaggio(tipo=0, titolo="Rimozione cliente", mex="Errore nella rimozione del cliente!")
                else:
                    self.messaggio(tipo=0, titolo="Rimozione cliente",
                                   mex="Non puoi rimuovere il cliente se ha un abbonamento attivo")
            else:
                self.messaggio(tipo=0, titolo="Rimozione cliente",
                               mex="Non puoi rimuovere il cliente mentre è assegnato ad un gruppo")
        self.riempiListaClienti()

    def goModifica(self):
        if self.itemSelezionato is not None:
            codiceFiscale = self.itemSelezionato.split("codice fiscale:")[1].split(",")[0].strip()
            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)
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
