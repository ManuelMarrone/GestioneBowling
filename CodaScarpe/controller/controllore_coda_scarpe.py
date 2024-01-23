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