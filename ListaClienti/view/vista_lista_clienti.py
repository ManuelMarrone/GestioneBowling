from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from ListaClienti.controller.controllore_lista_clienti import ControllerListaClienti
#from servizio.view.vista_servizio import VistaServizio

class VistaListaClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)
        uic.loadUi('ListaClienti/view/lista_clienti.ui', self)

        self.controller = ControllerListaClienti()
        #FINIRE DI CONTROLLARE LA LISTA

        self.listview_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_servizi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

        self.open_button.clicked.connect(self.show_selected)

    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaServizi, self).closeEvent(event)

    def show_selected(self):
        selected = self.list_view.selectedIndexes()[0].row()
        servizio_selezionato = self.controller.get_servizio_by_index(selected)
        self.vista_servizio = VistaServizio(servizio_selezionato)
        self.vista_servizio.show()