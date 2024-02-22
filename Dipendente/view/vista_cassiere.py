from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Partita.view.vista_gestione_partite import VistaGestionePartite
from Cliente.view.vista_lista_clienti import VistaGestioneClienti
from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Ricevuta.view.vista_lista_ricevute import VistaGestioneRicevute


class VistaCassiere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        uic.loadUi('Dipendente/view/cassiereMain.ui', self)
        self.impostaUI()

    def impostaUI(self):
        self.clientiButton.clicked.connect(self.goGestioneClienti)
        self.partiteButton.clicked.connect(self.goGestionePartite)
        self.ricevuteButton.clicked.connect(self.goGestioneRicevute)
        self.esciButton.clicked.connect(self.chiudiFinestra)

    def goGestioneRicevute(self):
        VistaCassiere.close(self)
        self.vista_gestione_ricevute= VistaGestioneRicevute()
        self.vista_gestione_ricevute.closed.connect(self.show)
        self.vista_gestione_ricevute.show()

    def goGestioneClienti(self):
        VistaCassiere.close(self)
        ControlloreAbbonamento().controllo_scadenze()
        self.vista_gestione_clienti = VistaGestioneClienti()
        self.vista_gestione_clienti.closed.connect(self.show)
        self.vista_gestione_clienti.show()

    def goGestionePartite(self):
        VistaCassiere.close(self)
        self.VistaGestionePartite = VistaGestionePartite()
        self.VistaGestionePartite.closed.connect(self.show)
        self.VistaGestionePartite.show()

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()
