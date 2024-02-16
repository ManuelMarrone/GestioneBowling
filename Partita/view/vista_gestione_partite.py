import os
import pickle
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

# ci sono degli import da fare
from Cliente.controller.controllore_cliente import ControlloreCliente
from Cliente.view.vista_lista_clienti import VistaGestioneClienti
from Pista.controller.controllore_pista import ControllorePista
from GruppoClienti.model.GruppoClienti import GruppoClienti
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti

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
        self.clientiList.setEnabled(False)
        self.pisteList.setCurrentText("Seleziona una pista")
        self.pisteListself.currentIndexChanged.connect(self.assegnaPista)
        self.clientiList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)


        self.idCliente = None

        self.riempiListaPiste()
        self.riempiListaClienti()

        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)
        self.selezionaButton.clicked.connect(self.creaGruppoClienti)
        self.inviaButton.clicked.connect(self.goInvia)


        contatore_piste_libere = 0
        tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
        for i in tutte_le_piste:
            if "True" in i:
                contatore_piste_libere = contatore_piste_libere + 1

        self.messaggioPiste(contatore_piste_libere)

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

    def riempiListaPiste(self):
        listaPiste = []
        self.pisteList.clear()
        listaPiste = ControllorePista().visualizzaPiste()
        if listaPiste is not None:
            for pista in listaPiste:
                if pista.getDisponibilita() == True:
                    item = QComboBox()
                    item.addItem(str(pista.getId()))
                    self.pisteList.addItem(item.currentText())

    def goVisualizza(self):
        if self.itemSelezionato is not None:
            cf = self.itemSelezionato.split(", codice fiscale: ")[1].strip()

            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(cf)
            self.vista_cliente = VistaGestioneClienti(clienteSelezionato)
            self.vista_cliente.show()

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
            print("L' id del gruppo è : ", ControlloreGruppoClienti().ricercaGruppoId(id_gruppo))
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
        # SVUOTA E RISETTA I CLIENTI A NON ASSEGNATI (FALSE)
        # with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
        #     pickle.dump([], f, pickle.HIGHEST_PROTOCOL)
        # for cliente in ControlloreCliente().visualizzaClienti():
        #     print(ControlloreCliente(cliente).getCodiceFiscale(), "Settato")
        #     ControlloreCliente(cliente).setAssegnato(val=False)

        clienti_selezionati = self.selectedItems()
        if clienti_selezionati is not None:
            gruppo_clienti = []
            for cliente in clienti_selezionati:
                codiceFiscale = cliente.split("codice fiscale:")[1].split(",")[0].strip()
                print(codiceFiscale)
                clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(codiceFiscale)
                gruppo_clienti.append(clienteSelezionato)
                #ControlloreCliente(clienteSelezionato).setAssegnato(val=True) DA METTERE SOLO QUANDO SI è SICURI CHE è STATA ASSEGNATA ANCHE LA PISTA

            #self.clientiList.setEnabled(False)
            id_gruppo = self.creaId()
            if id_gruppo is not None:
                numero_partite = self.numeroPartite()
                if numero_partite is not None:
                    GruppoClienti().creaGruppoClienti(id_gruppo, gruppo_clienti, numero_partite, counterPartito=False)
                    self.messaggio(tipo=1, titolo="Gruppo clienti", mex="Gruppo clienti creato con successo, ora devi assegnargli una pista")
                    self.pisteList.setEnabled(True)
                else:
                    self.messaggio(tipo=1, titolo="Gruppo clienti", mex="Gruppo clienti annullato")
            else:
                self.messaggio(tipo=1, titolo="Gruppo clienti", mex="Gruppo clienti annullato")



            # GruppoClienti().creaGruppoClienti(id_gruppo, gruppo_clienti, numero_partite, id_pista_occupata)
            # for cliente in clientiSelezionati:
            #     print(ControlloreCliente(cliente).getAssegnato())


            #     cfCliente = clienteSelezionato.codiceFiscale  # Viene preso il codice fiscale del cliente selezionato

        #
        #         if len(clienti_selezionati) > 8:
        #             self.messaggio(tipo=0, titolo="Attenzione", mex="Puoi selezionare massimo 8 clienti per gruppo")
        #             return
        #
        #         if len(clienti_selezionati) < 2:
        #             self.messaggio(tipo=0, titolo="Attenzione", mex="Devi selezionare almeno 2 clienti per gruppo")
        #             return
        #
        #         "elimina i clienti nel gruppo da quelli assegnabili"
        #         for i in range(self.clientiList.count()):
        #             ele = self.clientiList.item(i)
        #             elemento = ele.text()
        #             for j in gruppo_clienti:
        #                 if j == elemento:
        #                     self.clientiList.item(i).setHidden(True)
        #                     for cliente in ControlloreCliente().visualizzaClienti():
        #                         codiceFiscale = j.split("codice fiscale:")[1].strip()
        #                         if cliente.getCodiceFiscale() == codiceFiscale:
        #                             self.controller = ControlloreCliente(cliente)
        #                             self.controller.setAssegnato(True, cliente.getCodiceFiscale())
        #
        #         "chiede il n° partite e verifica che un gruppo giochi almeno una partita"
        #         numero_partite, ok = QInputDialog.getInt(self, 'Numero Partite',
        #                                                  'quante partite intende effettuare il gruppo?')
        #         while numero_partite <= 0:
        #             self.messaggio(tipo=0, titolo="Attenzione", mex="un gruppo deve effettuare almeno una partita")
        #             numero_partite, ok = QInputDialog.getInt(self, 'Numero Partite',
        #                                                      'quante partite intende effettuare il gruppo?')
        #

        #
        #         GruppoClienti().creaGruppoClienti(id_gruppo, gruppo_clienti, numero_partite, id_pista_occupata)
        #
        #         "controlla che ci siano piste libere"
        #         if str(self.messaggioTempo.text()) == "Tutte le piste sono occupate":
        #             self.messaggio(tipo=0, titolo="Attenzione", mex="Devi aspettare che una pista si liberi")
        #             return
        #         else:
        #             if "True" not in self.pisteList.currentText():
        #                 self.messaggio(tipo=0, titolo="Attenzione pista già occupata", mex="Devi selezionare una pista libera")
        #                 return
        #             pista_occupata = self.pisteList.currentText()
        #             id_pista_occupata = pista_occupata[4]
        #             print("pre: " + self.pisteList.currentText())
        #
        #             indice = self.pisteList.currentIndex()
        #             testo = self.pisteList.currentText()
        #
        #             nuovo_testo = testo.replace("True", "False")
        #
        #             self.pisteList.setItemText(indice, nuovo_testo)
        #
        #             print("post: " + self.pisteList.currentText())
        #
        #             contatore_piste_libere = 0
        #             tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
        #             for i in tutte_le_piste:
        #                 if "True" in i:
        #                     contatore_piste_libere = contatore_piste_libere + 1
        #             self.messaggioPiste(contatore_piste_libere)
        #
        #             print(id_pista_occupata + "   " + str(self.messaggioTempo.text()))
        #
        #
        #         "cambia lo stato della pista nel pickle"
        #         lista_piste = ControllorePista().visualizzaPiste()
        #         for pista in lista_piste:
        #             if str(pista.getId()) == str(id_pista_occupata):
        #                 ControllorePista(pista).setDisponibilita(False, id_pista_occupata)
        #
        #
        #         self.clientiList.clearSelection()

    def messaggioPiste(self, contatore_piste_libere):
        if contatore_piste_libere > 0:
            self.messaggioTempo.setText("Ci sono " + str(contatore_piste_libere) + " piste libere")
        else:
            self.messaggioTempo.setText("Tutte le piste sono occupate")

    def assegnaPista(self):
        pista_selezionata = self.pisteList.currentText()
        if pista_selezionata is not None or pista_selezionata != "Seleziona una pista":
            self.pisteList.setEnabled(False)
            self.clientiList.setEnabled(True)
            return pista_selezionata
        else:
            self.messaggio(tipo=0, titolo="Selezione pista", mex="La pista selezionata non è valida")


