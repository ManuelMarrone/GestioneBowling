from PyQt6 import uic
from PyQt6.QtWidgets import *

from Cliente.controller.controllore_cliente import ControlloreCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__(parent)

        uic.loadUi('Dipendente/view/vistaCliente.ui', self)
        self.controller = ControlloreCliente(cliente)

        self.nomeLabel.setText(self.controller.getNome())
        self.cognomeLabel.setText(self.controller.getCognome())
        self.cfLabel.setText(self.controller.getCodiceFiscale())
        self.emailLabel.setText(self.controller.getEmail())
        self.sessoLabel.setText(self.controller.getSesso())
        self.abbonatoLabel.setText(self.controller.isAbbonato())
        self.tagliaScarpeLabel.setText(str(self.controller.getTagliaScarpe()))

        self.indietroButton.clicked.connect(self.chiudiFinestra)

    def chiudiFinestra(self):
        self.close()
