import json
import pickle
import os.path

from Abbonamento.model.Abbonamento import Abbonamento
class ListaAbbonamenti():
    def __init__(self):
        self.lista_abbonamenti = []
        if os.path.isfile('ListaAbbonamenti/data/lista_abbonamenti_salvata.pickle'):
            with open('ListaAbbonamenti/data/lista_abbonamenti_salvata.pickle', 'rb') as f:
                self.lista_abbonamenti = pickle.load(f)
        else:
            with open('ListaAbbonamenti/data/lista_abbonamenti_iniziali.json', 'r') as f:
                lista_abbonamenti_iniziali = json.load(f)
                for abbonamento_iniziale in lista_abbonamenti_iniziali:
                    self.aggiungi_abbonamento(
                        Abbonamento(abbonamento_iniziale["dataFine"],
                                    abbonamento_iniziale["dataValidazione"],
                                    abbonamento_iniziale["id"],
                                    abbonamento_iniziale["pagamentoRidotto"],
                                    abbonamento_iniziale["partiteGratuite"])
                    )

    def aggiungiAbbonamento(self, abbonamento):
        self.lista_abbonamenti.append(abbonamento)

    def getAbbonamentoByIndex(self, index):
        return self.lista_abbonamenti[index]

    def getListaAbbonamenti(self):
        return self.lista_abbonamenti

    def saveData(self):
        with open('ListaAbbonamenti/data/lista_abbonamenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_abbonamenti, handle, pickle.HIGHEST_PROTOCOL)