import time
import os
import pickle


class Abbonamento():

    def __init__(self):
        self.dataFine = None
        self.dataValidazione = None
        self.pagamentoRidotto = False
        self.partiteGratuite = ""
        self.cfCliente = ""
        self.partiteDaPagareAbbonamento = 0

    def getDataFine(self):
        return self.dataFine

    def getDataValidazione(self):
        return self.dataValidazione

    def getCfCliente(self):
        return self.cfCliente

    def getPartiteGratuite(self):
        return self.partiteGratuite

    def getPagamentoRidotto(self):
        return self.pagamentoRidotto

    def rimuoviAbbonamento(self):
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
                daRimuovere = next(
                    (abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente), None)
                abbonamenti.remove(daRimuovere)
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
        del self

    # def isAbbonamentoScaduto(self):
    #     timestamp = int(time.time())
    #     return timestamp > self.getDataFine()

    def setPagamentoRidotto(self, bool):
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
                abbonamento = next(
                    (abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente), None)
                abbonamento.pagamentoRidotto = bool
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)

    def verificaPartiteMax(self, numPartite):
        if int(self.partiteGratuite) - numPartite < 0:
            self.setPagamentoRidotto(True)
            if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
                with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                    abbonamenti = pickle.load(f)
                    abbonamento = next(
                        (abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente), None)
                    abbonamento.partiteGratuite = 0
                with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                    pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
            return False
        elif int(self.partiteGratuite) - numPartite == 0:
            if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
                with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                    abbonamenti = pickle.load(f)
                    abbonamento = next(
                        (abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente), None)
                    abbonamento.partiteGratuite = 0
                with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                    pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
            return False
        else:
            if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
                with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                    abbonamenti = pickle.load(f)
                    abbonamento = next(
                        (abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente), None)
                    partiteRimanenti = int(self.partiteGratuite) - numPartite
                    abbonamento.partiteGratuite = partiteRimanenti
                with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                    pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
                return True

    def setPartiteDaPagareAbbonamento(self, valore):
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
                abbonamento = next(
                    (abbonamento for abbonamento in abbonamenti if abbonamento.cfCliente == self.cfCliente),
                    None)
                abbonamento.partiteDaPagareAbbonamento = valore
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)

    def getPartiteDaPagareAbbonamento(self):
        return self.partiteDaPagareAbbonamento

    def creaAbbonamento(self, dataFine, dataValidazione, partiteGratuite, pagamentoRidotto, cfCliente,
                        partiteDaPagareAbbonamento):
        self.dataFine = dataFine
        self.dataValidazione = dataValidazione
        self.partiteGratuite = partiteGratuite
        self.pagamentoRidotto = pagamentoRidotto
        self.cfCliente = cfCliente
        self.partiteDaPagareAbbonamento = partiteDaPagareAbbonamento
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', "rb") as f:
                abbonamenti = pickle.load(f)
            abbonamenti.append(self)
            with open('Abbonamento/data/ListaAbbonamenti.pickle', "wb") as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
            return self

    def getAbbonamenti(self):
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
            return abbonamenti
        else:
            return None

