from PyQt6 import uic
from PyQt6.QtWidgets import *

from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Cliente.controller.controllore_cliente import ControlloreCliente

class VistaAbbonamento(QWidget):
    def __init__(self, abbonamento, cliente, parent=None):
        super(VistaAbbonamento, self).__init__(parent)

        uic.loadUi('Abbonamento/view/vistaAbbonamento.ui', self)

        self.controllerA = ControlloreAbbonamento(abbonamento)
        self.controllerC = ControlloreCliente(cliente)


        self.textNome.setText(self.controllerC.getNome())
        self.textCognome.setText(self.controllerC.getCognome())
        self.dateScadenza.setDate(self.controllerA.getDataFine())
        self.dateValidazione.setDate(self.controllerA.getDataValidazione())
        self.textPartiteGratuite.setText(self.controllerC.getNome())
        if self.controllerA.getPagamentoRidotto() == True:
            self.radioButtonSi.setChecked(True)
        else:
            self.radioButtonNo.setChecked(True)

        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.eliminaButton.clicked.connect(self.eliminaAbbonamento)

    def chiudiFinestra(self):
        self.close()
    def eliminaAbbonamento(self):
        pass