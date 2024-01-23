class CodaScarpe():
    def __init__(self):
        self.coda = []

    def aggiungiInCoda(self, cliente):
        #verifico che cliente non sia già in lista
        if cliente not in self.coda:
            self.coda.append(cliente)
            return True
        else:
            return False

    def rimuoviDaCoda(self, cliente):
        if cliente in self.coda:
            self.coda.remove(cliente)
            return True
        else:
            return False

    def visualizzaElementi(self):
        return self.coda