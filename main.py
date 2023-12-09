import sys
from PyQt6.QtWidgets import QApplication
from Login.view.VistaLogin import VistaLogin
#from ListaClienti.view.vista_lista_clienti import VistaListaClienti
#per favore aleandro quando hai finito di testare ricommenta come stava prima

if __name__ == "__main__":
    app = QApplication(sys.argv)
    VistaLogin = VistaLogin()
    VistaLogin.show()
    sys.exit(app.exec())

"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vistaclienti = VistaListaClienti()
    vistaclienti.show()
    sys.exit(app.exec())"""