import json
import pickle
import os.path

from Cliente.model.Cliente import Cliente
class ListaClienti():
    def __init__(self):
        self.lista_clienti = []
        if os.path.isfile('ListaClienti/data/lista_clienti_salvata.pickle'):
            with open('ListaClienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
        else:
            with open('ListaClienti/data/lista_clienti_iniziali.json', 'r') as f:
                lista_clienti_iniziali = json.load(f)
                for cliente_iniziale in lista_clienti_iniziali:
                    self.aggiungiCliente(
                        Cliente(cliente_iniziale["abbonato"],
                                cliente_iniziale["codiceFiscale"],
                                cliente_iniziale["id"],
                                cliente_iniziale["cognome"],
                                cliente_iniziale["email"],
                                cliente_iniziale["nome"],
                                cliente_iniziale["sesso"],
                                cliente_iniziale["tagliaScarpe"])
                    )
    def aggiungiCliente(self, cliente):
        self.lista_clienti.append(cliente)
    def getClienteByIndex(self, index):
        return self.lista_clienti[index]
    def getListaClienti(self):
        return self.lista_clienti
    def saveData(self):
        with open('ListaClienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)
