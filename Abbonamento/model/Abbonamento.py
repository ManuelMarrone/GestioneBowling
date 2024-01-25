import time
import os
import pickle
class Abbonamento():

    idIncrementale = 0
    id_disponibili = set()

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
        self.id = ""
        self.pagamentoRidotto = ""
        self.partiteGratuite = ""
        self.cfCliente = ""

    def creaId(self):
        # Riutilizzo degli id delle istanze cancellate
        if Abbonamento.id_disponibili:  # Se ci sono ID disponibili nell'insieme
            self.id = Abbonamento.id_disponibili.pop()  # Prendi un ID disponibile
        else:
            Abbonamento.idIncrementale += 1
            self.id = Abbonamento.idIncrementale

        return self.id
    def creaAbbonamento(self, dataFine, dataValidazione, partiteGratuite, pagamentoRidotto, cfCliente):
        self.id = self.creaId()
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
        Abbonamento.id_disponibili.add(self.id)  # Aggiungi l'ID dell'istanza eliminata agli ID disponibili
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
                daRimuovere = next((abbonamento for abbonamento in abbonamenti if abbonamento.id == self.id), None)
                abbonamenti.remove(daRimuovere)
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
        del self
    def getId(self):
        return self.id
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




