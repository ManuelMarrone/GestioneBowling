from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Dipendente.view.vista_gestione_partite import VistaGestionePartite
from Dipendente.view.vista_lista_clienti import VistaGestioneClienti

class VistaCassiere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        uic.loadUi('Dipendente/view/cassiereMain.ui', self)

        self.clientiButton.clicked.connect(self.goGestioneClienti)
        self.partiteButton.clicked.connect(self.goGestionePartite)

    def goGestioneClienti(self):
        VistaCassiere.close(self)
        self.vista_gestione_clienti = VistaGestioneClienti()
        self.vista_gestione_clienti.closed.connect(self.show)
        self.vista_gestione_clienti.show()

    def goGestionePartite(self):
        VistaCassiere.close(self)
        self.VistaGestionePartite = VistaGestionePartite()
        self.VistaGestionePartite.closed.connect(self.show)
        self.VistaGestionePartite.show()