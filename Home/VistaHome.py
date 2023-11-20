from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        uic.loadUi('Home/VistaHome.ui', self)

        self.servizi_button.clicked.connect(self.go_lista_servizi)
        self.clienti_button.clicked.connect(self.go_lista_clienti)

    def go_lista_scarpe(self):
        self.vista_lista_scarpe = VistaListaScarpe()
        self.vista_lista_scarpe.show()
