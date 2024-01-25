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
        self.textPartiteGratuite.setText(str(self.controllerA.getPartiteGratuite()))
        self.textPartiteGratuite.setReadOnly(True)
        if self.controllerA.getPagamentoRidotto() == True:
            self.radioButtonSi.setChecked(True)
        else:
            self.radioButtonNo.setChecked(True)
        self.radioButtonNo.setEnabled(False)
        self.radioButtonSi.setEnabled(False)

        self.indietroButton.clicked.connect(self.chiudiFinestra)
        self.abbonamento = abbonamento
        self.eliminaButton.clicked.connect(self.rimuoviAbbonamento)

    def chiudiFinestra(self):
        self.close()
    def rimuoviAbbonamento(self):
        risultato = ControlloreAbbonamento().rimuoviAbbonamento(self.abbonamento)
        if risultato:
            #ControlloreCliente(self.cliente).setAbbonato(self.cliente.getCodiceFiscale())
            self.controllerC.setAbbonato(self.controllerA.getCfCliente(), val=False)
            self.messaggio(tipo=1, titolo="Rimozione cliente", mex="Abbonamento rimosso con successo")
            self.chiudiFinestra()
        else:
            self.messaggio(tipo=0, titolo="Rimozione cliente", mex="Errore nella rimozione dell'abbonamento!")

    def messaggio(self, tipo, titolo, mex):
        mexBox = QMessageBox()
        mexBox.setWindowTitle(titolo)
        if tipo == 0:
            mexBox.setIcon(QMessageBox.Icon.Warning)
        elif tipo == 1:
            mexBox.setIcon(QMessageBox.Icon.Information)
        mexBox.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mexBox.setText(mex)
        mexBox.exec()