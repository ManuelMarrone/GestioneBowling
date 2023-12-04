from PyQt6 import uic
from PyQt6.QtGui import QGuiApplication, QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QTableWidgetItem

from ListaClienti.controller.controllore_lista_clienti import ControllerListaClienti
class VistaListaClienti(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('ListaClienti/view/lista_clienti.ui', self) #Carica l'interfaccia utente dal file .ui
        self.controller = ControllerListaClienti()
        self.setWindowTitle("Lista clienti")
        self.resize_to_screen()

        self.list = QStandardItemModel(self.tableView)
        col = 4
        self.list.setColumnCount(col)
        Header = ["ID", "NOME E COGNOME", None, None]
        path1 = "Data/icon/edit.svg"
        path2 = "Data/icon/user.svg"

        self.list.setHorizontalHeaderLabels(Header)
        for cliente, row in self.controller.getListaClienti():
            item = QTableWidgetItem()
            self.list.setItem(row, 0, cliente.id)
            self.list.setItem(row, 1, cliente.nome)
            self.list.setItem(row, 2, self.AddIcon(item.column(), path1))
            self.list.setItem(row, 3, self.AddIcon(item.column(), path2))


    def AddIcon(self, item, path):
        # Creazione di più icone e combinazione in un'unica icona
        icon = QIcon(QPixmap(path))

        # Dimensioni delle icone
        icon_size = 24
        icon.pixmap(icon_size)

        # Creazione di un oggetto QListWidgetItem e impostazione dell'icona
        item.setIcon(icon)


    def resize_to_screen(self):
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry() #Preleva la grandezza del desktop
        self.setGeometry(screen_geometry) #Imposta la finestra principale alla grandezza del desktop



