from PyQt6 import uic
from PyQt6.QtWidgets import *

from Dipendente.controller.controllore_dipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, parent=None):
        super(VistaDipendente, self).__init__(parent)

        uic.loadUi('Dipendente/view/vistaDipendente.ui', self)
        ControlloreDipendente.ricercaDipendenteNomeCognome()  #cerca il dipendente dal nome e cognome preso dall'item
        #setta il text delle label




