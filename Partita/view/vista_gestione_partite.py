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

        self.clientiList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.pisteList.setEditable(False)

        self.idCliente = None
        self.itemSelezionato = None

        self.riempiListaPiste()
        self.riempiListaClienti()

        self.clientiList.itemClicked.connect(self.clienteClicked)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)
        self.selezionaButton.clicked.connect(self.creaGruppoClienti)
        #self.assegnaButton.clicked.connect(self.assegnaPista)
        self.inviaButton.clicked.connect(self.goInvia)


        contatore_piste_libere = 0
        tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
        for i in tutte_le_piste:
            if "True" in i:
                contatore_piste_libere = contatore_piste_libere + 1

        self.messaggioPiste(contatore_piste_libere)

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
                item = QComboBox()
                item.addItem("id: " + str(pista.getId()) + " disponibilità: " + str(pista.getDisponibilita()))
                self.pisteList.addItem(item.currentText())

    def goVisualizza(self):
        if self.itemSelezionato is not None:
            cf = self.itemSelezionato.split(", codice fiscale: ")[1].strip()

            clienteSelezionato = ControlloreCliente().ricercaClienteCodiceFiscale(cf)
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
            self.messaggio(tipo=0, titolo="Attenzione", mex="Nessun cliente selezionato.")
            return

        clienti_selezionati = []

        for i in clienti_scelti:
            cliente = i.text()
            clienti_selezionati.append(cliente)

        if len(clienti_selezionati) > 8:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Puoi selezionare massimo 8 clienti per gruppo")
            return

        if len(clienti_selezionati) < 2:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Devi selezionare almeno 2 clienti per gruppo")
            return

        gruppo_clienti = []
        for i in range(0, len(clienti_selezionati), 8):
            gruppo_clienti = clienti_selezionati[i:i+8]
        print("Clienti nel gruppo:")
        for c in gruppo_clienti:
            print(c)

        "controlla che ci siano piste libere"
        if str(self.messaggioTempo.text()) == "Tutte le piste sono occupate":
            self.messaggio(tipo=0, titolo="Attenzione", mex="Devi aspettare che una pista si liberi")
            return
        else:
            if "True" not in self.pisteList.currentText():
                self.messaggio(tipo=0, titolo="Attenzione pista già occupata", mex="Devi selezionare una pista libera")
                return
            pista_occupata = self.pisteList.currentText()
            id_pista_occupata = pista_occupata[4]
            print("pre: " + self.pisteList.currentText())

            indice = self.pisteList.currentIndex()
            testo = self.pisteList.currentText()

            nuovo_testo = testo.replace("True", "False")

            self.pisteList.setItemText(indice, nuovo_testo)

            print("post: " + self.pisteList.currentText())

            contatore_piste_libere = 0
            tutte_le_piste = [self.pisteList.itemText(i) for i in range(self.pisteList.count())]
            for i in tutte_le_piste:
                if "True" in i:
                    contatore_piste_libere = contatore_piste_libere + 1
            self.messaggioPiste(contatore_piste_libere)

            print(id_pista_occupata + "   " + str(self.messaggioTempo.text()))

        "elimina i clienti nel gruppo da queli assegnabili"
        for i in range(self.clientiList.count()):
            ele = self.clientiList.item(i)
            elemento = ele.text()
            for j in gruppo_clienti:
                if j == elemento:
                    self.clientiList.item(i).setHidden(True)
                    for cliente in ControlloreCliente().visualizzaClienti():
                        codiceFiscale = j.split("codice fiscale:")[1].strip()
                        if cliente.getCodiceFiscale() == codiceFiscale:
                            self.controller = ControlloreCliente(cliente)
                            self.controller.setAssegnato(True, cliente.getCodiceFiscale())

        "chiede il n° partite e verifica che un gruppo giochi almeno una partita"
        numero_partite, ok = QInputDialog.getInt(self, 'Numero Partite', 'quante partite intende effettuare il gruppo?')
        while numero_partite <= 0:
            self.messaggio(tipo=0, titolo="Attenzione", mex="un gruppo deve effettuare almeno una partita")
            numero_partite, ok = QInputDialog.getInt(self, 'Numero Partite', 'quante partite intende effettuare il gruppo?')

        "chiede e assegna l'id al gruppo"
        gruppi = ControlloreGruppoClienti().visualizzaGruppi()
        id_gruppo, ok = QInputDialog.getText(self, 'Id gruppo', 'che id si intende associare al gruppo?')
        while len(id_gruppo) != 4:
            self.messaggio(tipo=0, titolo="Attenzione", mex="L'id associato al gruppo dev'essere di 4 elementi")
            id_gruppo, ok = QInputDialog.getText(self, 'Id gruppo', 'che id si intende associare al gruppo?')

        for i in gruppi:
            if str(i.getId()) == str(id_gruppo):
                while str(i.getId()) == str(id_gruppo):
                    self.messaggio(tipo=0, titolo="Attenzione", mex="Id già esistente, sceglierne uno nuovo")
                    id_gruppo, ok = QInputDialog.getText(self, 'Id gruppo', 'che id si intende associare al gruppo?')

        GruppoClienti().creaGruppoClienti(id_gruppo, gruppo_clienti, numero_partite, id_pista_occupata)

        "cambia lo stato della pista nel pickle"
        lista_piste = ControllorePista().visualizzaPiste()
        for pista in lista_piste:
            if str(pista.getId()) == str(id_pista_occupata):
                ControllorePista(pista).setDisponibilita(False, id_pista_occupata)


        self.clientiList.clearSelection()

    def messaggioPiste(self, contatore_piste_libere):
        if contatore_piste_libere > 0:
            self.messaggioTempo.setText("Ci sono " + str(contatore_piste_libere) + " piste libere")
        else:
            self.messaggioTempo.setText("Tutte le piste sono occupate")

    def goInvia(self):
        "time.sleep(x)"
        x = ControlloreGruppoClienti().visualizzaGruppi()
        for i in range(len(x)):
            print("numero partite " + str(x[i].numeroPartite) + " del gruppo: " + str(x[i].id))