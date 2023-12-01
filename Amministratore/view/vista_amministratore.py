from PyQt6 import uic
from PyQt6.QtWidgets import *


class VistaAmministratore(QWidget):
    def __init__(self, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        uic.loadUi('Amministratore/view/amministratoreMain.ui', self)
