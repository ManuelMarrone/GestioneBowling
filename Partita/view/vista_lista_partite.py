from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from datetime import datetime, timedelta

from Cliente.controller.controllore_cliente import ControlloreCliente
from CodaScarpe.controller.controllore_coda_scarpe import ControlloreCodaScarpe
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from Partita.controller.controllore_partita import ControllorePartita
from Pista.controller.controllore_pista import ControllorePista
from Scarpa.controller.controllore_scarpa import ControlloreScarpa


class VistaListaPartite(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaListaPartite, self).__init__(parent)

        uic.loadUi('Partita/view/listaPartite.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 50
        self.move(x, y)

        self.itemPartitaSelezionata = None
        self.riempiListaPartite()
        self.partiteList.itemClicked.connect(self.partitaClicked)
        self.terminaButton.clicked.connect(self.finePartita)
        self.indietroButton_2.clicked.connect(self.chiudiFinestra)

    def riempiListaPartite(self):
        listaPartite = []
        self.partiteList.clear()
        listaPartite = ControllorePartita().visualizzaPartite()
        if listaPartite is not None:
            for partita in listaPartite:
                idGruppo = ControllorePartita(partita).getIdGruppo()
                gruppo = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
                item = QListWidgetItem()
                item.setText("Gruppo : " + str(ControllorePartita(partita).getIdGruppo()) + ", Ora inizio : " + str(
                    ControllorePartita(partita).getOraInizio()) + ", Numero partite : " + str(
                    ControlloreGruppoClienti(gruppo).getNumeroPartite()))
                self.partiteList.addItem(item)

    def partitaClicked(self, item):
        self.itemPartitaSelezionata = item.text()

    def finePartita(self):
        if self.itemPartitaSelezionata is not None:
            idGruppo = self.itemPartitaSelezionata.split("Gruppo :")[1].split(",")[0].strip()
            gruppo = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
            partitaSelezionata = ControllorePartita().ricercaPartitaIdGruppo(idGruppo)

            if ControlloreGruppoClienti(gruppo).getNumeroPartite() > 0:
                ControlloreGruppoClienti(gruppo).decrementaNumPartite()
            else:
                # preleva l'oggetto della pista occupata
                idPista = ControllorePartita(partitaSelezionata).getIdPista()
                pista = ControllorePista().ricercaPistaId(idPista)
                ControllorePista(pista).setDisponibilita(occupata=False)

                membri = ControlloreGruppoClienti(gruppo).getMembri()
                for membro in membri:
                    # preleva idScarpa della scarpa assegnata al cliente
                    idScarpa = ControlloreCliente(membro).getIdScarpa()
                    # preleva l'oggetto della relativa scarpa
                    scarpa = ControlloreScarpa().ricercaScarpaId(idScarpa)

                    ControlloreCodaScarpe().liberaCoda(scarpa)

                    if scarpa is not None:
                        # scarpa nuovamente disponibile per altri clienti
                        ControlloreScarpa(scarpa).setDisponibilitaScarpa(True, idScarpa)

                    # ripristino della disponibilita per giocare in altri gruppi
                    ControlloreCliente(membro).setAssegnato(val=False)

                    # ripristino idScarpa del cliente a nessuna scarpa aseegnata
                    cfCliente = ControlloreCliente(membro).getCodiceFiscale()
                    ControlloreCliente(membro).setIdScarpa("", cfCliente)

                ControllorePartita().rimuoviPartita(partitaSelezionata)
                # preleva id del gruppo da eliminare
                ControlloreGruppoClienti(gruppo).rimuoviGruppo(idGruppo)
        self.riempiListaPartite()

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
