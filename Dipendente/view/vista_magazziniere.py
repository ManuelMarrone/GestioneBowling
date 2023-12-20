from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class VistaMagazziniere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaMagazziniere, self).__init__(parent)
        uic.loadUi('Dipendente/view/magazziniereMain.ui', self)