from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Scarpa.controller.controllore_scarpa import ControlloreScarpa

class VistaScarpa(QWidget):

    def __init__(self, scarpa, parent = None):
        super(VistaScarpa, self).__init__(parent)
        uic.loadUi('Scarpa/view/scarpa.ui', self)
        self.controller = ControlloreScarpa(scarpa)

        self.labelId.setText(self.controller.getIdScarpa())
        self.labelTaglia.setText(f"Taglia: {self.controller.getTagliaScarpa()}")
        self.labelDisponibilita.setText(f"Disponibilita: {self.controller.getDisponibilitaScarpa()}")