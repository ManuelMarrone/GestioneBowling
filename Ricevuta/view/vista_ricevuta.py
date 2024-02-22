from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

from Ricevuta.controller.controllore_ricevuta import ControlloreRicevuta


class VistaRicevuta(QWidget):
    closed = pyqtSignal()

    def __init__(self, ricevuta, parent=None):
        super(VistaRicevuta, self).__init__(parent)

        uic.loadUi('Ricevuta/view/vistaRicevuta.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 50
        self.move(x, y)

        self.controller = ControlloreRicevuta(ricevuta)

        self.impostaUI()

        self.indietroButton.clicked.connect(self.chiudiFinestra)

    def impostaUI(self):
        item = QListWidgetItem()
        item.setText(
            "id:  " + self.controller.getId() + ", data: " + str(self.controller.getDataEmissione()) + ", ora: " + (
                self.controller.getOraEmissione()).strftime("%H:%M:%S") + "\n")
        self.visualizzaList.addItem(item)
        for membro in self.controller.getMembri():
            item = QListWidgetItem()
            item.setText(membro)
            self.visualizzaList.addItem(item)

        item = QListWidgetItem()
        item.setText("\n" + "importo totale:  " + str(self.controller.getImporto()) + "€")
        self.visualizzaList.addItem(item)

    def chiudiFinestra(self):
        self.closed.emit()
        self.close()
