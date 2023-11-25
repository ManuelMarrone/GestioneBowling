from PyQt6 import uic
from PyQt6.QtWidgets import *


class VistaAmministratore(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('amministratoreMain.ui', self)
