from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QGuiApplication, QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

from ListaClienti.controller.controllore_lista_clienti import ControllerListaClienti
class VistaListaClienti(QMainWindow):
    def __init__(self):
        super().__init__()

        #uic.loadUi('ListaClienti/view/lista_clienti.ui', self) #Carica l'interfaccia utente dal file .ui
        self.controller = ControllerListaClienti()
        self.setWindowTitle("Lista clienti")
        self.resize_to_screen()

        #print(len(self.controller.getListaClienti()[0][1]))
        self.ListaClienti = self.controller.getListaClienti()

        self.list = QTableWidget()
        self.list.setRowCount(len(self.ListaClienti))
        self.list.setColumnCount(4)

        Header = ["ID", "NOME E COGNOME", None, None] #Lista che contiene l'header della mia tabella
        path1 = "Data/icon/edit.svg"
        path2 = "Data/icon/user.svg"
        self.list.setHorizontalHeaderLabels(Header)

        for rowIndex, cliente in enumerate(self.controller.getListaClienti()):
            self.list.setItem(rowIndex, 0, QTableWidgetItem(cliente.cognome))
            self.list.setItem(rowIndex, 1, QTableWidgetItem(cliente.nome))

            #Caricamento delle icone
            icon1 = self.AddIcon(path1)
            self.list.setItem(rowIndex, 2, icon1)
            icon2 = self.AddIcon(path2)
            self.list.setItem(rowIndex, 3, icon2)


        # Imposta la grandezza delle celle al contenuto
        self.list.resizeColumnsToContents()
        self.list.resizeRowsToContents()

        # Layout principale
        layout = QVBoxLayout()
        layout.addWidget(self.list)

        # Widget principale
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        #RIDURRE LA GRANNDEZZA DELLA TABELLA E COLLEGARE LE ICONE
        h=1


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
    """
    print("id ", cliente.id)
    print("cognome ", cliente.cognome)
    print("sesso ", cliente.sesso)
    print("nome ", cliente.nome)
    print("email ", cliente.email)
    print("tagliascarpe ", cliente.tagliaScarpe)
    """



