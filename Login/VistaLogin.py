from PyQt6 import uic
from PyQt6.QtWidgets import *

from ListaScarpe.view.vista_lista_scarpe import VistaListaScarpe


class VistaLogin(QWidget):
    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        self.setGeometry(350, 80, 800, 600) #(x,y,larghezza,altezza) x,y left corner
        self.setWindowTitle("Accesso")
        self.layoutFinestra = QGridLayout()
        self.setStyleSheet("background-color: #FCD19C")

        self.gruppoWidget = QGroupBox("Accedi")
        self.gruppoWidget.setStyleSheet("background-color: #B0ABAB")
        self.gruppoWidget.setStyleSheet("QGroupBox { border: 5px solid red;}")
        self.layoutFinestra.addWidget(self.gruppoWidget)

        self.layoutGruppo = QVBoxLayout()

        self.emailLabel = QLabel("Email", self)
        self.button1 = QPushButton('Test', self)
        self.layoutGruppo.addWidget(self.emailLabel)
        self.layoutGruppo.addWidget(self.button1)

        self.gruppoWidget.setLayout(self.layoutGruppo)
        self.button2 = QPushButton('Test', self)
        self.layoutFinestra.addWidget(self.button2)


        # self.servizi_button.clicked.connect(self.go_lista_scarpe) #definisce l'operazione al click del pulsante

    def go_lista_scarpe(self):
        self.vista_lista_scarpe = VistaListaScarpe()
        self.vista_lista_scarpe.show()
