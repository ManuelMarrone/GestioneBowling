from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class VistaCassiere(QWidget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super(VistaCassiere, self).__init__(parent)
        uic.loadUi('Dipendente/view/cassiereMain.ui', self)