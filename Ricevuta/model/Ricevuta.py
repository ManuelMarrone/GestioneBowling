import pickle
import os

class Ricevuta():
    def __init__(self):
        dataEmissione = None
        id = 0
        importo = 0.0
        oraEmissione = None
        membri = []
        tipo = ""

    def getMembri(self):
        return self.membri
    def getTipo(self):
        return self.tipo

    def getId(self):
        return self.id

    def getDataEmissione(self):
        return self.dataEmissione

    def getImporto(self):
        return self.importo

    def getOraEmissione(self):
        return self.oraEmissione

    def creaRicevuta(self, dataEmissione, id, importo, oraEmissione, membri, tipo):
        self.dataEmissione = dataEmissione
        self.id = id #preferibilimente lo stesso della classe partita
        self.importo = importo
        self.oraEmissione = oraEmissione
        self.membri = membri
        self.tipo =tipo
        ricevute = []
        with open('Ricevuta/data/ricevute.pickle', "rb") as f:
          ricevute = pickle.load(f)
        ricevute.append(self)
        with open('Ricevuta/data/ricevute.pickle', "wb") as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)
        return self

    def getRicevute(self):
        ricevute = []
        if os.path.isfile('Ricevuta/data/ricevute.pickle'):
            with open('Ricevuta/data/ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
            return ricevute
        else:
            return None

    def eliminaRicevuta(self):
        if os.path.isfile('Ricevuta/data/ricevute.pickle'):
            with open('Ricevuta/data/ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
                daRimuovere = next((ricevuta for ricevuta in ricevute if str(ricevuta.id) == str(self.id) and ricevuta.oraEmissione == self.oraEmissione), None)
                ricevute.remove(daRimuovere)
            with open('Ricevuta/data/ricevute.pickle', 'wb') as f:
                pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)
        del self
