from PyQt6 import uic
from PyQt6.QtGui import QGuiApplication, QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QTableView

from ListaClienti.controller.controllore_lista_clienti import ControllerListaClienti
class VistaListaClienti(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('ListaClienti/view/lista_clienti.ui', self) #Carica l'interfaccia utente dal file .ui
        self.controller = ControllerListaClienti()
        self.setWindowTitle("Lista clienti")
        self.resize_to_screen()

        self.list = QTableWidget(self.table) # Prelevo la tabella dal file.ui

        col = 4 #Numero di colonne
        self.list.setColumnCount(col)
        Header = ["ID", "NOME E COGNOME", None, None] #Lista che contiene l'headre della mia tabella
        path1 = "Data/icon/edit.svg"
        path2 = "Data/icon/user.svg"
        self.list.setHorizontalHeaderLabels(Header)

        for rowIndex, cliente in enumerate(self.controller.getListaClienti()):
            print(cliente.nome)
            print(rowIndex)
            self.list.setItem(rowIndex, 0, QTableWidgetItem(str(cliente.id)))
            print(QTableWidgetItem(cliente.id))
            self.list.setItem(rowIndex, 1, QTableWidgetItem(str(cliente.nome)))
            #Caricamento delle icone
            icon1 = self.AddIcon(path1)
            self.list.setItem(rowIndex, 2, icon1)
            icon2 = self.AddIcon(path2)
            self.list.setItem(rowIndex, 3, icon2)


        # Imposta la grandezza delle celle al contenuto
        self.list.resizeColumnsToContents()
        self.list.resizeRowsToContents()



    def AddIcon(self, path):
        # Creazione di più icone e combinazione in un'unica icona
        icon = QIcon(QPixmap(path))
        item = QTableWidgetItem()

        # Dimensioni delle icone
        icon_size = 24
        icon.pixmap(icon_size)

        # Creazione di un oggetto QListWidgetItem e impostazione dell'icona
        item.setIcon(icon)
        return item


    def resize_to_screen(self):
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry() #Preleva la grandezza del desktop
        self.setGeometry(screen_geometry) #Imposta la finestra principale alla grandezza del desktop



