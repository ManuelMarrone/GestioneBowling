from Cliente.controller.controllore_cliente import ControlloreCliente
from CodaScarpe.model.CodaScarpe import CodaScarpe
from Scarpa.controller.controllore_scarpa import ControlloreScarpa


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
        coda = self.visualizzaElementi()
        if len(coda) != 0:
            for clienteCoda in coda:
                cliente = ControlloreCliente().ricercaClienteCodiceFiscale(clienteCoda)

                if ControlloreScarpa(scarpa).getTagliaScarpa() is not None:
                    if int(ControlloreCliente(cliente).getTagliaScarpe()) == int(ControlloreScarpa(scarpa).getTagliaScarpa()):
                        # se la scarpa liberata corrisponde con quella del cliente in coda allora procedi
                        # libera il cliente in coda
                        self.rimuoviDaCoda(clienteCoda)
                        self.setNotifica(val=True)

    def setNotifica(self, val):
        self.model.setNotifica(val)

    def getNotifica(self):
        return self.model.getNotifica()
