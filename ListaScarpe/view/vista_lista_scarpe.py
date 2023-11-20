from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from ListaScarpe.controller.controllore_lista_scarpe import ControllerListaScarpe
from Scarpa.view.vista_scarpa import VistaScarpa

class VistaListaScarpe(QWidget):
    def __init__(self, parent=None):
        super(VistaListaScarpe, self).__init__(parent)
        uic.loadUi('ListaScarpe/view/lista_scarpe.ui',self)

        self.controller = ControllerListaScarpe()

        self.listview_model = QStandardItemModel(self.list_view)
        for scarpa in self.controller.get_lista_scarpe():
            item = QStandardItem()
            item.setText(scarpa.id)
            item.setEditable(False)
            font = item.font()
            font.setSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

        self.open_button.clicked.connect(self.show_selected)

    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaScarpe, self).closeEvent(event)

    def show_selected(self):
        selected = self.list_view.selectedIndexes()[0].row()
        scarpa_selezionata = self.controller.get_scarpa_by_index(selected)
        self.vista_scarpa = VistaScarpa(scarpa_selezionata)
        self.vista_scarpa.show()
