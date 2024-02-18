import threading
import time

import schedule
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal, QTimer
from datetime import datetime

from Cliente.controller.controllore_cliente import ControlloreCliente
from Pista.controller.controllore_pista import ControllorePista
from Scarpa.controller.controllore_scarpa import ControlloreScarpa
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from CodaScarpe.controller.controllore_coda_scarpe import ControlloreCodaScarpe
from Partita.controller.controllore_partita import ControllorePartita

class VistaMagazziniere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaMagazziniere, self).__init__(parent)
        uic.loadUi('Dipendente/view/magazziniereMain.ui', self)

        self.controllerCoda = ControlloreCodaScarpe()
        self.itemSelezionato = None
        self.itemClienteSelezionato = None

        self.impostaUI()


    def impostaUI(self):
        #liste e combobox
        self.riempiListaScarpe()
        self.riempiBoxGruppi()
        self.riempiListaClienti()
        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.gruppiComboBox.activated.connect(self.riempiListaClienti)
        self.gruppiComboBox.activated.connect(self.iniziaPartita)

        self.scarpeList.itemClicked.connect(self.scarpaClicked)

        #pulsanti
        self.esciButton.clicked.connect(self.chiudiFinestra)
        self.assegnaButton.clicked.connect(self.assegnaScarpa)

        self.buttonCercaGruppo.clicked.connect(self.cercaGruppo)
        self.buttonCercaScarpa.clicked.connect(self.cercaScarpa)
        self.aggiornaButton.clicked.connect(self.notifica)

    def cercaGruppo(self):
        idList = self.ricercaGruppo.text().split()
        if len(idList) == 0:
            self.riempiBoxGruppi()
        elif len(idList) == 1:
            id = idList[0]
            gruppoRicercato = ControlloreGruppoClienti().ricercaGruppoId(id)
            if gruppoRicercato is not None:
                self.gruppiComboBox.clear()
                self.controller = ControlloreGruppoClienti(gruppoRicercato)
                listaGruppi = ControlloreGruppoClienti().visualizzaGruppi()
                if listaGruppi is not None:
                    for gruppo in listaGruppi:
                        idGruppo = ControlloreGruppoClienti(gruppo).getId()
                        if idGruppo == self.controller.getId():
                            if gruppo.getCounterPartito() is False:
                                self.gruppiComboBox.addItem(str(idGruppo))
                                self.riempiListaClienti()

                    if len(self.gruppiComboBox) == 0:
                        self.messaggio(tipo=1, titolo="Ricerca gruppo", mex="Il gruppo non è presente")
            else:
                self.messaggio(tipo=1, titolo="Ricerca gruppo", mex="Il gruppo non è presente")
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

    def cercaScarpa(self):
        tagliaLista = self.ricercaScarpa.text().split()
        if len(tagliaLista) == 0:
            self.riempiListaScarpe()
        elif len(tagliaLista) == 1:
            self.scarpeList.clear()
            taglia = tagliaLista[0]
            listaScarpe = ControlloreScarpa().visualizzaScarpe()
            if listaScarpe is not None and taglia.isdigit():
                for scarpa in listaScarpe:
                    tagliaScarpa = scarpa.getTagliaScarpa()
                    if int(taglia) == tagliaScarpa:
                        if scarpa.getDisponibilitaScarpa() is True:
                            item = QListWidgetItem()
                            item.setText("Scarpa " + str(scarpa.getTagliaScarpa()) + ", id: " + str(scarpa.getIdScarpa()))
                            self.scarpeList.addItem(item)
                if len(self.scarpeList) == 0:
                    self.messaggio(tipo=1, titolo="Ricerca scarpa", mex="Nessuna scarpa di quella taglia è disponibile")
            else:
                self.messaggio(tipo=1, titolo="Ricerca scarpa", mex="Nessuna scarpa disponibile")
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

    def scarpaClicked(self, item):
        self.itemSelezionato = item.text()

    def clienteClicked(self, item):
        self.itemClienteSelezionato = item.text()

    def riempiListaScarpe(self):
        self.scarpeList.clear()
        listaScarpe = ControlloreScarpa().visualizzaScarpe()
        if listaScarpe is not None:
            for scarpa in listaScarpe:
                if scarpa.getDisponibilitaScarpa() is True:
                    item = QListWidgetItem()
                    item.setText(
                        "Scarpa " + str(scarpa.getTagliaScarpa()) + ", id: " + str(scarpa.getIdScarpa()))
                    self.scarpeList.addItem(item)

    def riempiListaClienti(self):
        self.clientiList.clear()
        idSelezionato = self.gruppiComboBox.currentText()
        gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idSelezionato)
        if gruppoSelezionato is not None:
            for cliente in ControlloreGruppoClienti(gruppoSelezionato).getMembri():
                cf = ControlloreCliente(cliente).getCodiceFiscale()
                clienteGruppo = ControlloreCliente().ricercaClienteCodiceFiscale(cf)
                nome = ControlloreCliente(clienteGruppo).getNome()
                cognome = ControlloreCliente(clienteGruppo).getCognome()


                taglia = ControlloreCliente(clienteGruppo).getTagliaScarpe()
                idScarpa = ControlloreCliente(clienteGruppo).getIdScarpa()
                if taglia != "0" and idScarpa == "":
                    item = QListWidgetItem()
                    item.setText(
                        nome + " " + cognome + " taglia:" + taglia + " codice fiscale: " + cf)
                    self.clientiList.addItem(item)

    def riempiBoxGruppi(self):
        gruppi = []
        self.gruppiComboBox.clear()
        gruppi = ControlloreGruppoClienti().visualizzaGruppi()
        if gruppi is not None:
            for gruppo in gruppi:
                if gruppo.getCounterPartito() is False:
                    self.gruppiComboBox.addItem(str(gruppo.getId()))

    def assegnaScarpa(self):
        self.avvisiLabel.clear()
        # se sono stati selezionati una scarpa e un cliente allora procede
        if self.itemSelezionato is not None and self.itemClienteSelezionato is not None:
            # preleva taglia e id della scarpa selezionata
            taglia = self.itemSelezionato.split("Scarpa")[1].split(",")[0].strip()
            idScarpa = self.itemSelezionato.split("id:")[1].strip()

            # preleva nome e cognome del cliente selezionato
            cf = self.itemClienteSelezionato.split("codice fiscale:")[1].strip()


            # preleva l'oggetto della scarpa selezionata
            scarpaSelezionata = ControlloreScarpa().ricercaScarpaId(idScarpa)
            # preleva l'oggetto del cliente selezionato
            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(cf)

            # preleva l'id del gruppo a cui si sta facendo riferimento
            idSelezionato = self.gruppiComboBox.currentText()
            # preleva l'oggetto relativo a quel gruppo
            gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idSelezionato)

            scarpa = ControlloreScarpa(scarpaSelezionata)

            self.itemSelezionato = None
            self.itemClienteSelezionato = None

            if scarpa.controllaTaglia(taglia, clienteSelezionato):
                if scarpa.assegnaScarpa(gruppoSelezionato, clienteSelezionato, idScarpa) is True:
                    self.riempiListaScarpe()
                    self.riempiListaClienti()
                    self.iniziaPartita()
            else:
                self.messaggio(tipo=0, titolo="Assegnamento scarpa",
                               mex="La taglia della scarpa selezionata non corrisponde con quella richiesta dal cliente")
        elif self.itemClienteSelezionato is not None:
            self.codaScarpe()
        else:
            self.messaggio(tipo=0, titolo="Assegnamento scarpa", mex="Selezionare un cliente e una scarpa")

    def codaScarpe(self):
        tagliaRichiesta = self.itemClienteSelezionato.split("taglia:")[1].strip().split()[0]
        if self.verificaDiponibilitaTaglia(tagliaRichiesta) is False:
            cfCliente = self.itemClienteSelezionato.split("codice fiscale:")[1].strip()

            if self.controllerCoda.aggiungiInCoda(cfCliente) is False:
                self.messaggio(tipo=0, titolo="Coda per scarpe",
                               mex="Cliente già in coda")
            else:
                self.messaggio(tipo=1, titolo="Assegnamento scarpa",
                               mex="Taglia non disponibile per il cliente, inserimento in coda")

            print(self.controllerCoda.visualizzaElementi())

    def verificaDiponibilitaTaglia(self, tagliaRichiesta):
        scarpePresenti = [self.scarpeList.item(index).text() for index in range(self.scarpeList.count())]
        for scarpa in scarpePresenti:
            if tagliaRichiesta == scarpa.split("Scarpa")[1].split(",")[0].strip():
                return True
        return False

    def iniziaPartita(self):
        # se la lista dei clienti partecipanti al gruppo è vuota
        # vuol dire o che nessun cliente richiede scarpe o che ogni cliente richiedente è stato soddisfatto
        if self.clientiList.count() == 0:
            # se ci sono gruppi esistenti
            if self.gruppiComboBox.count() > 0:

                # estraggo l'indice all'interno della comboBox del gruppo soddisfatto
                currentIndex = self.gruppiComboBox.currentIndex()

                # estraggo l'id del gruppo soddisfatto
                idSelezionato = self.gruppiComboBox.currentText()
                # prelevo l'oggetto del gruppo
                gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idSelezionato)

                partita = ControllorePartita().ricercaPartitaIdGruppo(idSelezionato)
                currentData = datetime.now()
                ControllorePartita(partita).setOraInizio(currentData)

                # rimuove l'elemento corrente dalla QComboBox
                self.gruppiComboBox.removeItem(currentIndex)
                # d'ora in poi non comparirà più il gruppo nella vista del magazziniere
                ControlloreGruppoClienti(gruppoSelezionato).setCounterPartito(idSelezionato, True)
                # aggiorna i gruppi da soddisfare
                self.riempiBoxGruppi()

    def notifica(self):
        if self.controllerCoda.getNotifica():
            self.avvisiLabel.setText("Attenzione\nLe taglie richieste sono tornate disponibili")

        self.riempiListaScarpe()
        self.riempiListaClienti()


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
