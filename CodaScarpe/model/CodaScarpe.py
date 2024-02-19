import os
import pickle
from Cliente.controller.controllore_cliente import ControlloreCliente
from Scarpa.controller.controllore_scarpa import ControlloreScarpa


class CodaScarpe():
    def __init__(self):
        self.coda = []
        self.notifica = False

    def aggiungiInCoda(self, cliente):
        if os.path.isfile('CodaScarpe/data/codaScarpe.pickle'):
            with open('CodaScarpe/data/codaScarpe.pickle', "rb") as f:
                self.coda = pickle.load(f)
            if cliente not in self.coda:
                self.coda.append(cliente)
                with open('CodaScarpe/data/codaScarpe.pickle', "wb") as f:
                    pickle.dump(self.coda, f, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.notifica, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False


    def rimuoviDaCoda(self, cliente):
        if os.path.isfile('CodaScarpe/data/codaScarpe.pickle'):
            with open('CodaScarpe/data/codaScarpe.pickle', "rb") as f:
                self.coda = pickle.load(f)
            if cliente in self.coda:
                self.coda.remove(cliente)
                with open('CodaScarpe/data/codaScarpe.pickle', "wb") as f:
                    pickle.dump(self.coda, f, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(self.notifica, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False

    def visualizzaElementi(self):
        if os.path.isfile('CodaScarpe/data/codaScarpe.pickle'):
            with open('CodaScarpe/data/codaScarpe.pickle', "rb") as f:
                self.coda = pickle.load(f)
            return self.coda

    def setNotifica(self, val):
        if os.path.isfile('CodaScarpe/data/codaScarpe.pickle'):
            with open('CodaScarpe/data/codaScarpe.pickle', "rb") as f:
                self.coda = pickle.load(f)
                self.notifica = pickle.load(f)

                self.notifica = val
            with open('CodaScarpe/data/codaScarpe.pickle', "wb") as f:
                pickle.dump(self.coda, f, pickle.HIGHEST_PROTOCOL)
                pickle.dump(self.notifica, f, pickle.HIGHEST_PROTOCOL)


    def getNotifica(self):
        if os.path.isfile('CodaScarpe/data/codaScarpe.pickle'):
            with open('CodaScarpe/data/codaScarpe.pickle', "rb") as f:
                self.coda = pickle.load(f)
                self.notifica = pickle.load(f)
                return self.notifica

    def liberaCoda(self, scarpa):
        self.coda = self.visualizzaElementi()
        if len(self.coda) != 0:
            for clienteCoda in self.coda:
                cliente = ControlloreCliente().ricercaClienteCodiceFiscale(clienteCoda)

                if ControlloreScarpa(scarpa).getTagliaScarpa() is not None:
                    if int(ControlloreCliente(cliente).getTagliaScarpe()) == int(
                            ControlloreScarpa(scarpa).getTagliaScarpa()):
                        # se la scarpa liberata corrisponde con quella del cliente in coda allora procedi
                        # libera il cliente in coda
                        self.rimuoviDaCoda(clienteCoda)
                        self.setNotifica(True)