from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic
from PyQt6.QtWidgets import *

from Amministratore.view.vista_gestione_dipendenti import VistaGestioneDipendenti


class VistaAmministratore(QWidget):
    closed = pyqtSignal()
    def __init__(self, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        uic.loadUi('Amministratore/view/amministratoreMain.ui', self)

        self.gestioneDipendentiButton.clicked.connect(self.goDipendenti)
        self.esciButton.clicked.connect(self.chiudiFinestra)

    def goDipendenti(self):
        VistaAmministratore.close(self)
        self.vista_gestione_dipendenti = VistaGestioneDipendenti()
        self.vista_gestione_dipendenti.closed.connect(self.show)
        self.vista_gestione_dipendenti.show()

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()
