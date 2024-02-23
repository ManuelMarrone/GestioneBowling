import os
import pickle


class Partita:
    def __init__(self):
        self.idGruppo = ""
        self.idPista = ""
        self.oraInizio = None

    def setOraInizio(self, ora):
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
                partita = next((partita for partita in partite if partita.idGruppo == self.idGruppo), None)
                partita.oraInizio = ora
            with open('Partita/data/partite.pickle', 'wb') as f:
                pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)

    def getOraInizio(self):
        return self.oraInizio

    def getIdGruppo(self):
        return self.idGruppo

    def getIdPista(self):
        return self.idPista

    # metodo chiamato appena vengono assegnate tutte le scarpe
    def creaPartita(self, idGruppo, idPista, oraInizio):
        self.idGruppo = idGruppo
        self.idPista = idPista
        self.oraInizio = oraInizio
        partite = []
        with open('Partita/data/partite.pickle', "rb") as f:
            partite = pickle.load(f)
        partite.append(self)
        with open('Partita/data/partite.pickle', "wb") as f:
            pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)
        return self


    def rimuoviPartita(self):
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
                daRimuovere = next((partita for partita in partite if partita.idGruppo == self.idGruppo), None)
                partite.remove(daRimuovere)
            with open('Partita/data/partite.pickle', 'wb') as f:
                pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)
        del self

    def getPartite(self):
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
            return partite
        else:
            return None

    def __eq__(self, other):
        if isinstance(other, Partita):
            return (self.idGruppo == other.idGruppo)
        return False
