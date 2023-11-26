from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget
from PyQt6.QtGui import QGuiApplication, QStandardItemModel, QStandardItem

from ListaAbbonamenti.controller.controllore_lista_abbonamenti import ControllerListaAbbonamenti
# from Abbonamento.view.vista_abbonamento import VistaServizio

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("lista abbonamenti")
        self.resize_to_screen()
        self.setup_ui()

    def resize_to_screen(self):
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry() #Preleva la grandezza del desktop
        self.setGeometry(screen_geometry) #Imposta la finestra principale alla grandezza del desktop

    def setup_ui(self):
        central_widget = QWidget() #Serve come contenitore per il layout e il QListWidget che sarà aggiunto dopo
        self.setCentralWidget(central_widget) #Imposta il contenitore al centro della finestra principale

        layout = QVBoxLayout(central_widget) #stiamo creando un layout verticale che verrà utilizzato per organizzare gli elementi all'interno del central_widget

        list_widget = QListWidget() #Crea la lista

        self.controller = ControllerListaAbbonamenti()

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

        list_widget.addItems(items) #aggiunge gli elementi della lista
        layout.addWidget(list_widget) #aggiunge la lista al layout

def main():
    app = QApplication([]) #Crea un oggetto QApplication, che rappresenta l'applicazione
    window = MyWindow() #Crea un'istanza della classe MyWindow, che è una finestra principale ( QMainWindow)
    window.show() #Mostra la finestra principale. Questo metodo rende visibile la finestra sullo schermo
    app.exec() #Avvia l'esecuzione dell'applicazione e attende che vengano gestiti gli eventi

if __name__ == "__main__":  #Questo blocco assicura che il codice all'interno di main()venga eseguito solo se il file Python
    main()                  #viene eseguito direttamente dall'interprete Python. Se il file viene importato da un altro script,
                            #il codice all'interno del blocco ifnon verrà eseguito automaticamente