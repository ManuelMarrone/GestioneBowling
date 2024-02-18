from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from datetime import datetime, timedelta

from GruppoClienti.view.vista_gruppo import VistaGruppo
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
        self.visualizzaGruppo.clicked.connect(self.goVisualizzaGruppo)
        self.indietroButton_2.clicked.connect(self.chiudiFinestra)
        self.cercaButton.clicked.connect(self.cercaGruppo)
    def cercaGruppo(self):
        idList = self.ricercaText.text().split()
        if len(idList) == 0:
            self.riempiListaGruppi()
        elif len(idList) == 1:
            id = idList[0]
            gruppoRicercato = ControlloreGruppoClienti().ricercaGruppoId(id)
            if gruppoRicercato is not None:
                self.gruppiList.clear()
                self.controller = ControlloreGruppoClienti(gruppoRicercato)
                listaGruppi = ControlloreGruppoClienti().visualizzaGruppi()
                if listaGruppi is not None:
                    for gruppo in listaGruppi:
                        idGruppo = ControlloreGruppoClienti(gruppo).getId()
                        if idGruppo == self.controller.getId():
                            item = QListWidgetItem()
                            item.setText("nome gruppo: " + ControlloreGruppoClienti(gruppo).getId())
                            self.gruppiList.addItem(item)
            else:
                self.messaggio(tipo=1, titolo="Ricerca gruppo", mex="Il gruppo non è presente")
        else:
            self.messaggio(tipo=0, titolo="Attenzione", mex="Ricerca non valida")

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