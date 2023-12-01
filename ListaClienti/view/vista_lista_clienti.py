from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QListWidget, QListWidgetItem
from PyQt6.QtCore import QFile

from ListaClienti.controller.controllore_lista_clienti import ControllerListaClienti
class VistaListaClienti(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('ListaClienti/view/lista_clienti.ui', self) #Carica l'interfaccia utente dal file .ui
        self.controller = ControllerListaClienti()
        list_widget = self.findChild(QListWidget, "listWidget") #Trova la QListWidget all'interno del file .ui

        for cliente in self.controller.getListaClienti():
            list_item = QListWidgetItem(cliente)
            list_widget.addItem(list_item)

    def mimmo(self):
        pass



