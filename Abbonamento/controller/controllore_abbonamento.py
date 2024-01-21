import os
import pickle
from Abbonamento.model.Abbonamento import Abbonamento
class ControlloreAbbonamento():
    def __init__(self, abbonamento):
        self.model = abbonamento
    def getDataFine(self):
        return self.model.getDataFine
    def getDataValidazione(self):
        return self.model.getDataValidazione
    def getId(self):
        return self.model.getId
    def getPartiteGratuite(self):
        return self.model.getPartiteGratuite
    def getPagamentoRidotto(self):
        return self.model.getPagamentoRidotto
    def creaAbbonamento(self, dataFine, dataValidazione, partitaGratuita, pagmentoRidotto, idCliente):
        abbonamento = self.ricercaAbbonamentoIdCliente(idCliente)
        if isinstance(abbonamento, Abbonamento):  # se l'abbonamento già esiste
            return None
        else:
            nuovoAbbonamento = Abbonamento().creaAbbonamento(
              dataFine=dataFine,
              dataValidazione=dataValidazione,
              partitaGratuita=partitaGratuita,
              pagmentoRidotto=pagmentoRidotto,
              idCliente=idCliente
             )

        return nuovoAbbonamento
    def ricercaAbbonamentoIdCliente(self, id):
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
        if len(abbonamenti) > 0:
            for abbonamento in abbonamenti:
                if abbonamento.getIdCliente() == id:
                    return abbonamento
        else:
            return None