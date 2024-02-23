import os
import pickle


class GruppoClienti:
    def __init__(self):
        self.id = ""
        self.membri = ""
        self.numeroPartite = 0
        self.counterPartito = False

    def getMembri(self):
        return self.membri

    def getNumeroPartite(self):
        return self.numeroPartite

    def getCounterPartito(self):
        return self.counterPartito

    def setCounterPartito(self, id, bool):
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
                gruppo = next((gruppo for gruppo in gruppi if str(gruppo.id) == id), None)
                gruppo.counterPartito = bool
            with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
                pickle.dump(gruppi, f, pickle.HIGHEST_PROTOCOL)

    def getId(self):
        return self.id

    def creaGruppoClienti(self, id, membri, numeroPartite, counterPartito):
        self.id = id
        self.membri = membri
        self.numeroPartite = numeroPartite
        self.counterPartito = counterPartito
        gruppi = []
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', "rb") as f:
                gruppi = pickle.load(f)
            gruppi.append(self)
            with open('GruppoClienti/data/GruppoClienti.pickle', "wb") as f:
                pickle.dump(gruppi, f, pickle.HIGHEST_PROTOCOL)
        return self

    def getGruppoClienti(self):
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
            return gruppi
        else:
            return None

    def rimuoviGruppoClienti(self, id):
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
                daRimuovere = next((gruppo for gruppo in gruppi if str(gruppo.id) == str(id)), None)
                gruppi.remove(daRimuovere)
            with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
                pickle.dump(gruppi, f, pickle.HIGHEST_PROTOCOL)
        del self

    def decrementaNumPartite(self):
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
                gruppo = next((gruppo for gruppo in gruppi if gruppo.id == self.id), None)
                gruppo.numeroPartite -= 1
            with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
                pickle.dump(gruppi, f, pickle.HIGHEST_PROTOCOL)