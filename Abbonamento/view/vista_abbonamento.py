from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDateTime

from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Cliente.controller.controllore_cliente import ControlloreCliente

class VistaAbbonamento(QWidget):
    def __init__(self, abbonamento, cliente, parent=None):
        super(VistaAbbonamento, self).__init__(parent)

        uic.loadUi('Abbonamento/view/vistaAbbonamento.ui', self)

        self.controllerA = ControlloreAbbonamento(abbonamento)
        self.controllerC = ControlloreCliente(cliente)


        self.textNome.setText(self.controllerC.getNome())
        self.textNome.setReadOnly(True)
        self.textCognome.setText(self.controllerC.getCognome())
        self.textCognome.setReadOnly(True)
        data_fine = QDateTime.fromString(self.controllerA.getDataFine(), "yyyy-MM-dd HH:mm")
        self.dateScadenza.setDateTime(data_fine)
        self.dateScadenza.setReadOnly(True)
        data_scadenza = QDateTime.fromString(self.controllerA.getDataValidazione(), "yyyy-MM-dd HH:mm")
        self.dateValidazione.setDateTime(data_scadenza)
        self.dateValidazione.setReadOnly(True)
        self.textPartiteGratuite.setText(self.controllerC.getNome())
        self.textPartiteGratuite.setReadOnly(True)
        if self.controllerA.getPagamentoRidotto() == True:
            self.radioButtonSi.setChecked(True)
        else:
            self.radioButtonNo.setChecked(True)
        self.radioButtonNo.setEnabled(False)
        self.radioButtonSi.setEnabled(False)

        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.eliminaButton.clicked.connect(self.eliminaAbbonamento)

    def chiudiFinestra(self):
        self.close()
    def eliminaAbbonamento(self):
        pass
        # finire