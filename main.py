import os
import pickle
import sys
from PyQt6.QtWidgets import QApplication
from Login.view.VistaLogin import VistaLogin
from Dipendente.view.vista_lista_clienti import VistaGestioneClienti
from Pista.controller.controllore_pista import ControllorePista

if __name__ == "__main__":
    # pista1 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=1
    # )
    # pista2 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=2
    # )
    # pista3 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=3
    # )
    # pista4 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=4
    # )
    # pista5 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=5
    # )
    app = QApplication(sys.argv)
    VistaLogin = VistaLogin()
    VistaLogin.show()
    sys.exit(app.exec())


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     vistaclienti = VistaGestioneClienti()
#     vistaclienti.show()
#     sys.exit(app.exec())

