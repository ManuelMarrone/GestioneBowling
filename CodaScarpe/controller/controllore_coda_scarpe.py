from CodaScarpe.model.CodaScarpe import CodaScarpe

class ControlloreCodaScarpe():
    def __init__(self, codaScarpe = None):
        self.model = codaScarpe

    def aggiungiInCoda(self, cliente):
        return CodaScarpe().aggiungiInCoda(cliente)

    def rimuoviDaCoda(self, cliente):
        return CodaScarpe().rimuoviDaCoda(cliente)