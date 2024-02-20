import time
import os
import pickle
class Abbonamento():

    # def __init__(self, Abbonamenti):
    #     self.dataFine = Abbonamenti["dataFine"]
    #     self.dataValidazione = Abbonamenti["dataValidazione"]
    #     self.id = ""
    #     self.pagamentoRidotto = ""
    #     self.partiteGratuite = ""
    #     self.idCliente = ""

    def __init__(self):
        self.dataFine = None
        self.dataValidazione = None
        self.pagamentoRidotto = False
        self.partiteGratuite = ""
        self.cfCliente = ""

    def creaAbbonamento(self, dataFine, dataValidazione, partiteGratuite, pagamentoRidotto, cfCliente):
        self.dataFine = dataFine
        self.dataValidazione = dataValidazione
        self.partiteGratuite = partiteGratuite
        self.pagamentoRidotto = pagamentoRidotto
        self.cfCliente = cfCliente
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', "rb") as f:
                abbonamenti = pickle.load(f)
            abbonamenti.append(self)
            with open('Abbonamento/data/ListaAbbonamenti.pickle', "wb") as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
            return self
    def rimuoviAbbonamento(self):
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
                daRimuovere = next((abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente), None)
                abbonamenti.remove(daRimuovere)
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
        del self

    def getPartiteGratuite(self):
        return self.partiteGratuite
    # SE QUESTO METODO RITORNA FALSE ALLORA BISOGNA IMPOSTARE IL PAGAMENTO RIDOTTO A TRUE
    def getDataFine(self):
        return self.dataFine
    def getDataValidazione(self):
        return self.dataValidazione
    def getPagamentoRidotto(self):
        return self.pagamentoRidotto
    def getCfCliente(self):
        return self.cfCliente
    def isAbbonamentoScaduto(self):
        timestamp = int(time.time())
        return timestamp > self.getDataFine()

    def getAbbonamenti(self):
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
            return abbonamenti
        else:
            return None




