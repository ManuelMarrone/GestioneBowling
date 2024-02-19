
from CodaScarpe.model.CodaScarpe import CodaScarpe



class ControlloreCodaScarpe():
    def __init__(self):
        self.model = CodaScarpe()

    def aggiungiInCoda(self, cliente):
        return self.model.aggiungiInCoda(cliente)

    def rimuoviDaCoda(self, cliente):
        return self.model.rimuoviDaCoda(cliente)

    def visualizzaElementi(self):
        return self.model.visualizzaElementi()

    def liberaCoda(self, scarpa):
        self.model.liberaCoda(scarpa)

    def setNotifica(self, val):
        self.model.setNotifica(val)

    def getNotifica(self):
        return self.model.getNotifica()
