from PyQt6 import uic
from PyQt6.QtWidgets import *

from Dipendente.controller.controllore_dipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, parent=None):
        super(VistaDipendente, self).__init__(parent)

        uic.loadUi('Dipendente/view/vistaDipendente.ui', self)
        self.controller = ControlloreDipendente(dipendente)
        self.impostaUI()

    def impostaUI(self):
        self.nomeLabel.setText(self.controller.getNome())
        self.cognomeLabel.setText(self.controller.getCognome())
        self.ruoloLabel.setText(self.controller.getRuolo())
        self.cfLabel.setText(self.controller.getCF())
        self.dataLabel.setText(self.controller.getDataNascita())
        self.emailLabel.setText(self.controller.getEmail())
        self.sessoLabel.setText(self.controller.getSesso())
        self.telefonoLabel.setText(self.controller.getTelefono())
        self.passwordLabel.setText(self.controller.getPassword())

        self.indietroButton.clicked.connect(self.chiudiFinestra)

    def chiudiFinestra(self):
        self.close()
