from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from datetime import datetime, timedelta

from Cliente.controller.controllore_cliente import ControlloreCliente
from GruppoClienti.view.vista_gruppo import VistaGruppo
from Cliente.view.vista_modifica_cliente import VistaModificaCliente
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
class VistaGestioneGruppi(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaGestioneGruppi, self).__init__(parent)

        uic.loadUi('GruppoClienti/view/lista_gruppo_clienti.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 50
        self.move(x, y)

        self.itemGruppoSelezionato = None
        self.riempiListaGruppi()
        self.gruppiList.itemClicked.connect(self.gruppoClicked)
        self.eliminaGruppo.clicked.connect(self.goEliminaGruppo)
        self.visualizzaGruppo.clicked.connect(self.goVisualizzaGruppo)
        self.indietroButton_2.clicked.connect(self.chiudiFinestra)

    def riempiListaGruppi(self):
        listaGruppi = []
        self.gruppiList.clear()
        listaGruppi = ControlloreGruppoClienti().visualizzaGruppi()
        if listaGruppi is not None:
            for gruppo in listaGruppi:
                item = QListWidgetItem()
                item.setText("nome gruppo: " + ControlloreGruppoClienti(gruppo).getId())
                self.gruppiList.addItem(item)

    def goVisualizzaGruppo(self):
        if self.itemGruppoSelezionato is not None:
            idGruppo = self.itemGruppoSelezionato.split("nome gruppo:")[1].split(",")[0].strip()
            gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
            self.vista_gruppo = VistaGruppo(gruppoSelezionato)
            self.vista_gruppo.show()                               # vista_gruppo DA CREARE PER VISUALIZZARE I MEMBRI DEL GRUPPO

    def gruppoClicked(self, item):
        self.itemGruppoSelezionato = item.text()

    def goEliminaGruppo(self):
        if self.itemGruppoSelezionato is not None:
            idGruppo = self.itemGruppoSelezionato.split("nome gruppo:")[1].split(",")[0].strip()
            gruppoSelezionato = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
            if gruppoSelezionato.isPartita() is False:                    # ATTENZIONE SE IL GRUPPO STA STA GIOCANDO NON PUO ESSERE ELIMINATO
                risultato = ControlloreGruppoClienti().rimuoviGruppo(gruppoSelezionato)
                if risultato:
                    self.messaggio(tipo=1, titolo="Rimozione gruppo", mex="Gruppo rimosso con successo")
                else:
                    self.messaggio(tipo=0, titolo="Rimozione gruppo", mex="Errore nella rimozione del gruppo!")
            else:
                self.messaggio(tipo=0, titolo="Rimozione gruppo",
                               mex="Non puoi rimuovere il gruppo mentre è in corso una partita")
        self.riempiListaGruppi()

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