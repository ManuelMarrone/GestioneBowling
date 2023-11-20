import sys
from PyQt6.QtWidgets import QApplication
from Home.VistaHome import VistaHome

if __name__ == "__main__":
    app = QApplication(sys.argv)
    VistaHome = VistaHome()
    VistaHome.show()
    sys.exit(app.exec())

