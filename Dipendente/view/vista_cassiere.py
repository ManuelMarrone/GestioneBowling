from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from ListaClienti.view.vista_lista_clienti import VistaListaClienti

class VistaCassiere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        uic.loadUi('Dipendente/view/cassiereMain.ui', self)

        self.clientiButton.clicked.connect(self.goGestioneClienti)

    def goGestioneClienti(self):
        self.vista_gestione_clienti = VistaListaClienti()
        self.vista_gestione_clienti.show()