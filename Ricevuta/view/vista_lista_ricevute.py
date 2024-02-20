from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Ricevuta.controller.controllore_ricevuta import ControlloreRicevuta
from Ricevuta.view.vista_ricevuta import VistaRicevuta


class VistaGestioneRicevute(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestioneRicevute, self).__init__(parent)

        uic.loadUi('Ricevuta/view/listaRicevute.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 50
        self.move(x, y)

        self.itemSelezionato = None

        self.riempiListaRicevute()

        self.ricevuteList.itemClicked.connect(self.ricevutaClicked)
        self.eliminaButton.clicked.connect(self.goEliminaRicevuta)
        self.visualizzaButton.clicked.connect(self.goVisualizzaRicevuta)
        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.goCerca)
    def riempiListaRicevute(self):
        listaRicevute = []
        self.ricevuteList.clear()
        listaRicevute = ControlloreRicevuta().visualizzaRicevute()
        if listaRicevute is not None:
            for ricevuta in listaRicevute:
                item = QListWidgetItem()
                item.setText(
                    "id: " + ControlloreRicevuta(ricevuta).getId() + ", data emissione: " + str(ControlloreRicevuta(ricevuta).getDataEmissione()) + ", ora emissione: " + (ControlloreRicevuta(ricevuta).getOraEmissione()).strftime("%H:%M:%S"))
                self.ricevuteList.addItem(item)

    def ricevutaClicked(self, item):
        self.itemSelezionato = item.text()

    def goEliminaRicevuta(self):
        if self.itemSelezionato is not None:
            idRicevuta = self.itemSelezionato.split("id:")[1].split(",")[0].strip()
            oraEmissione = self.itemSelezionato.split(", ora emissione: ")[1].strip()
            ricevutaSelezionata = ControlloreRicevuta().ricercaRicevutaIdOra(idRicevuta, oraEmissione)

            risultato = ControlloreRicevuta().rimuoviRicevuta(ricevutaSelezionata)
            if risultato:
                self.messaggio(tipo=1, titolo="Rimozione ricevuta", mex="Ricevuta rimossa con successo")
            else:
                self.messaggio(tipo=0, titolo="Rimozione ricevuta", mex="Errore nella rimozione della ricevuta!")
        self.riempiListaRicevute()

    def goVisualizzaRicevuta(self):
        if self.itemSelezionato is not None:
            idRicevuta = self.itemSelezionato.split("id:")[1].split(",")[0].strip()
            oraEmissione = self.itemSelezionato.split(", ora emissione: ")[1].strip()
            ricevutaSelezionata = ControlloreRicevuta().ricercaRicevutaIdOra(idRicevuta, oraEmissione)
            self.vista_ricevuta = VistaRicevuta(ricevutaSelezionata)
            self.vista_ricevuta.show()

    def goCerca(self):

        controllo = self.ricercaText.text().split()
        if len(controllo) == 0:
            self.riempiListaRicevute()
        elif len(controllo) >= 1:
            id = self.ricercaText.text().strip()
            ricevute = ControlloreRicevuta().ricercaRicevutaId(id)
            if ricevute is not None:
                self.ricevuteList.clear()
                for ricevuta in ricevute:
                    item = QListWidgetItem()
                    item.setText(
                        "id: " + ControlloreRicevuta(ricevuta).getId() + ", data emissione: " + str(
                            ControlloreRicevuta(ricevuta).getDataEmissione())+ ", ora emissione: " + (ControlloreRicevuta(ricevuta).getOraEmissione()).strftime("%H:%M:%S"))
                    self.ricevuteList.addItem(item)
            else:
                self.messaggio(tipo=1, titolo="Ricerca ricevuta", mex="La ricevuta non è presente")
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

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
