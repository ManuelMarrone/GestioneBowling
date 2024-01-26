import threading
import time

from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal, QTimer

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
        self.gruppiComboBox.activated.connect(self.iniziaCounter)

        self.scarpeList.itemClicked.connect(self.scarpaClicked)

        #pulsanti
        self.esciButton.clicked.connect(self.chiudiFinestra)
        self.assegnaButton.clicked.connect(self.assegnaScarpa)

        self.buttonCercaGruppo.clicked.connect(self.cercaGruppo)
        self.buttonCercaScarpa.clicked.connect(self.cercaScarpa)

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
                nome = cliente.split("nome:")[1].split(",")[0].strip()
                cognome = cliente.split("cognome:")[1].split(",")[0].strip()
                cf = cliente.split("codice fiscale: ")[1].strip()

                istanza = ControlloreCliente().ricercaClienteCodiceFiscale(cf)

                taglia = istanza.getTagliaScarpe()
                idScarpa = istanza.getIdScarpa()
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
                    self.iniziaCounter()
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

    def iniziaCounter(self):
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



                #si era pensato di creare un numero di partite pari al numero di partite
                #dichiarate dal gruppo, ma a questo punto conviene creare un solo oggetto
                #partita per ogni gruppo giocante
                ControllorePartita().creaPartita(gruppoSelezionato)




                # rimuove l'elemento corrente dalla QComboBox
                self.gruppiComboBox.removeItem(currentIndex)
                # d'ora in poi non comparirà più il gruppo nella vista del magazziniere
                gruppoSelezionato.setCounterPartito(idSelezionato, True)
                # aggiorna i gruppi da soddisfare
                self.riempiBoxGruppi()

                # preleva l'id della pista occupata dal gruppo
                idPistaOccupata = gruppoSelezionato.getPistaOccupata()
                # avvia un thread per liberare la pista dopo un certo tempo
                threading.Thread(target=self.finePartita, args=(idPistaOccupata, gruppoSelezionato)).start()

    def finePartita(self, idPistaOccupata, gruppoSelezionato):
        # preleva numero partite del gruppo
        numPartite = gruppoSelezionato.getNumeroPartite()
        tempo_di_attesa = 10 * numPartite  # Tempo di attesa in secondi
        print("inizia attesa" + str(tempo_di_attesa))
        time.sleep(tempo_di_attesa)
        print("fine attesa")

        # preleva l'oggetto della pista occupta
        pista = ControllorePista().ricercaPistaId(idPistaOccupata)
        # rende nuovamente disponibile la pista
        pista.setDisponibilita(True, idPistaOccupata)

        membri = gruppoSelezionato.getMembri()
        if membri is not None:
            for membro in membri:
                # preleva dati cliente
                cfCliente = membro.split("codice fiscale:")[1].strip()

                # preleva oggetto cliente
                clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(cfCliente)

                # preleva idScarpa della scarpa assegnata al cliente
                idScarpa = clienteSelezionato.getIdScarpa()
                # preleva l'oggetto della relativa scarpa
                scarpa = ControlloreScarpa().ricercaScarpaId(idScarpa)
                if scarpa is not None:
                    # scarpa nuovamente disponibile per altri clienti
                    scarpa.setDisponibilitaScarpa(True, idScarpa)

                if self.liberaCoda(scarpa):
                    self.avvisiLabel.setText("Attenzione\nLe taglie richieste sono tornate disponibili")

                # ripristino della disponibilita per giocare in altri gruppi
                clienteSelezionato.setAssegnato(False, cfCliente)

                # ripristino idScarpa del cliente a nessuna scarpa aseegnata
                clienteSelezionato.setIdScarpa("", cfCliente)


        else:
            print("errore nel ripristino disponibilità")

        # preleva id del gruppo da eliminare
        idGruppo = gruppoSelezionato.getId()
        # rimozione gruppo
        ControlloreGruppoClienti(gruppoSelezionato).rimuoviGruppo(idGruppo)
        self.riempiListaScarpe()
        self.riempiListaClienti()

    def liberaCoda(self, scarpa):
        print(self.controllerCoda.visualizzaElementi())
        # vedo se posso liberare il cliente dalla coda
        coda = self.controllerCoda.visualizzaElementi()
        if len(coda) != 0:
            for clienteCoda in coda:
                cliente = ControlloreCliente().ricercaClienteCodiceFiscale(clienteCoda)

                if scarpa.getTagliaScarpa() is not None:
                    if int(cliente.getTagliaScarpe()) == int(scarpa.getTagliaScarpa()):
                        # se la scarpa liberata corrisponde con quella del cliente in coda allora procedi
                        # libera il cliente in coda
                        return self.controllerCoda.rimuoviDaCoda(clienteCoda)



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
