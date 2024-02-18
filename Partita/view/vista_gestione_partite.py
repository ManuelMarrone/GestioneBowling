import os
import pickle
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from datetime import datetime

# ci sono degli import da fare
from Cliente.controller.controllore_cliente import ControlloreCliente
from Pista.controller.controllore_pista import ControllorePista
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from GruppoClienti.view.vista_gestione_gruppi import VistaGestioneGruppi
from Partita.controller.controllore_partita import ControllorePartita
from Partita.view.vista_lista_partite import VistaListaPartite

class VistaGestionePartite(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestionePartite, self).__init__(parent)
        uic.loadUi('Partita/view/gestionePartite.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 50
        self.move(x, y)

        self.clientiList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.riempiListaClienti()

        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)
        self.selezionaButton.clicked.connect(self.creaGruppoClienti)
        self.gestioneGruppi.clicked.connect(self.goGestioneGruppi)
        self.listaPartite.clicked.connect(self.goListaPartite)


        # contatore_piste_libere = 0
        # tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
        # for i in tutte_le_piste:
        #     if "True" in i:
        #         contatore_piste_libere = contatore_piste_libere + 1
        #
        # self.messaggioPiste(contatore_piste_libere)

    def selectedItems(self):
        selected_items = self.clientiList.selectedItems()
        selected_texts = [item.text() for item in selected_items]
        print("Elementi selezionati:", selected_texts)
        if not selected_texts:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Nessun cliente selezionato.")
        elif len(selected_texts) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Devi selezionare almeno 2 clienti per gruppo")
        elif len(selected_texts) > 8:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Puoi selezionare massimo 8 clienti per gruppo")
        else:
            return selected_texts

    def goCerca(self):
        controllo = self.ricercaText.text().split()
        if len(controllo) == 0:
            self.riempiListaClienti()
        elif len(controllo) == 2:
            nome, cognome = self.ricercaText.text().split()
            nome = nome.capitalize().strip()
            cognome = cognome.capitalize().strip()
            clienteRicercato = ControlloreCliente().ricercaClienteNomeCognome(nome, cognome)
            if clienteRicercato is not None:                    #se il cliente è presente aggiorna la lista
                self.clientiList.clear()
                self.controller = ControlloreCliente(clienteRicercato)
                listaClienti = ControlloreCliente().visualizzaClienti()
                if listaClienti is not None:
                    for cliente in listaClienti:
                        if cliente.nome == self.controller.getNome() and cliente.cognome == self.controller.getCognome():
                            item = QListWidgetItem()
                            item.setText("nome: " + cliente.getNome() + ", cognome: " + cliente.getCognome())
                            self.clientiList.addItem(item)
            else:
                self.messaggio(tipo=1, titolo="Ricerca cliente", mex="Il cliente non è presente")
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

    def riempiListaClienti(self):
        listaClienti = []
        self.clientiList.clear()
        listaClienti = ControlloreCliente().visualizzaClienti()
        print(listaClienti)
        if listaClienti is not None:
            for cliente in listaClienti:
                if cliente.assegnato is False:
                    item = QListWidgetItem()
                    item.setText("nome: " + cliente.getNome() + ", cognome: " + cliente.getCognome() + ", codice fiscale: "+ cliente.getCodiceFiscale())
                    self.clientiList.addItem(item)

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

    def creaId(self):
        while True:
            id_gruppo, ok = QInputDialog.getText(self, 'Nome gruppo', 'Che nome si intende associare al gruppo?')
            if not ok:
                return None  # Se l'utente annulla, restituisci None
            if len(id_gruppo) < 4:
                self.messaggio(tipo=0, titolo="Attenzione",
                               mex="Il nome associato al gruppo dev'essere almeno di 4 caratteri")
            elif len(id_gruppo) > 15:
                self.messaggio(tipo=0, titolo="Attenzione",
                               mex="Il nome associato al gruppo dev'essere minore di 15 caratteri")
            elif next((gruppo for gruppo in ControlloreGruppoClienti().visualizzaGruppi() if gruppo.id == id_gruppo), None) is not None:
                self.messaggio(tipo=0, titolo="Attenzione", mex="Nome già esistente, sceglierne uno nuovo")
            else:
                return id_gruppo

    def numeroPartite(self):
        while True:
            numero_partite, ok = QInputDialog.getInt(self, 'Numero Partite','Quante partite intende effettuare il gruppo?')
            if not ok:
                return None
            if numero_partite <= 0:
                self.messaggio(tipo=0, titolo="Attenzione", mex="Il gruppo deve effettuare almeno una partita")
            else:
                return numero_partite

    def creaGruppoClienti(self):
        # SVUOTA I GRUPPI, LE PARTITE E RISETTA I CLIENTI A NON ASSEGNATI (FALSE)
        # with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
        #     pickle.dump([], f, pickle.HIGHEST_PROTOCOL)
        # with open('Partita/data/partite.pickle', 'wb') as f:
        #     pickle.dump([], f, pickle.HIGHEST_PROTOCOL)
        # for cliente in ControlloreCliente().visualizzaClienti():
        #     print(ControlloreCliente(cliente).getCodiceFiscale(), "Settato")
        #     ControlloreCliente(cliente).setAssegnato(val=False)
        # for pista in ControllorePista().visualizzaPiste():
        #     print(ControllorePista(pista).getId(), "Libera")
        #     ControllorePista(pista).setDisponibilita(occupata=False)

        clienti_selezionati = self.selectedItems()
        if clienti_selezionati is not None:
            gruppo_clienti = []
            for cliente in clienti_selezionati:
                codiceFiscale = cliente.split("codice fiscale:")[1].split(",")[0].strip()
                clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)
                gruppo_clienti.append(clienteSelezionato)
                ControlloreCliente(clienteSelezionato).setAssegnato(val=True) #DA METTERE SOLO QUANDO SI è SICURI CHE è STATA ASSEGNATA ANCHE LA PISTA

            id_gruppo = self.creaId()
            if id_gruppo is not None:
                numero_partite = self.numeroPartite()
                if numero_partite is not None:
                    ControlloreGruppoClienti().creaGruppoClienti(id_gruppo, gruppo_clienti, numero_partite, counterPartito=False)
                    self.riempiListaClienti()
                    self.messaggio(tipo=1, titolo="Gruppo clienti", mex="Gruppo clienti creato con successo")
                    self.assegnaPista(id_gruppo)
                else:
                    self.messaggio(tipo=1, titolo="Gruppo clienti", mex="Gruppo clienti annullato")
            else:
                self.messaggio(tipo=1, titolo="Gruppo clienti", mex="Gruppo clienti annullato")


    def messaggioPiste(self, contatore_piste_libere):
        if contatore_piste_libere > 0:
            self.messaggioTempo.setText("Ci sono " + str(contatore_piste_libere) + " piste libere")
        else:
            self.messaggioTempo.setText("Tutte le piste sono occupate")

    def assegnaPista(self, idGruppo):
        listaPiste = ControllorePista().visualizzaPiste()
        if listaPiste is not None:
            pista_disponibile = None
            for pista in listaPiste:
                print("La pista è ", pista.id, pista.disponibilita)
                if ControllorePista(pista).getDisponibilita() == False:
                    pista_disponibile = pista
                    break
            print("La prima pista disponibile è ", pista_disponibile)
            if pista_disponibile is not None:
                ControllorePista(pista_disponibile).setDisponibilita(occupata=True) # DA METTERE SOLO QUANDO
                idPista = ControllorePista(pista_disponibile).getId()
                print("idPista ", idPista)
                oraInizio = None
                ControllorePartita().creaPartita(idGruppo, idPista, oraInizio)
                self.messaggio(tipo=1, titolo="Partita", mex="Al gruppo clienti "+str(idGruppo)+" è stata asssegnata la pista "+str(idPista))
            else:
                print("Non c'è nessuna pista disponibile")
                #Il gruppo va messo in coda

    def goGestioneGruppi(self):
        VistaGestionePartite.close(self)
        self.vista_gestione_gruppi = VistaGestioneGruppi()
        self.vista_gestione_gruppi.closed.connect(self.show)
        self.vista_gestione_gruppi.show()

    def goListaPartite(self):
        VistaGestionePartite.close(self)
        self.vista_lista_partite = VistaListaPartite()
        self.vista_lista_partite.closed.connect(self.show)
        self.vista_lista_partite.show()



