import sys
from PyQt6.QtWidgets import QApplication
from Login.VistaLogin import VistaLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    VistaLogin = VistaLogin()
    VistaLogin.show()
    sys.exit(app.exec())


