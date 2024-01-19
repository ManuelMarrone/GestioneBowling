import os
import pickle


class GruppoClienti:
    def __init__(self):
        self.id = ""
        self.membri = ""
        self.numeroPartite = 0
        self.pistaOccupata = ""
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

    def getPistaOccupata(self):
        return self.pistaOccupata

    def modificaGruppoClienti(self, id, nuovoMembri, nuovoNumeroPartite, nuovoPistaOccupata ):
        self.nuovoMembri = nuovoMembri
        self.nuovoNumeroPartite = nuovoNumeroPartite
        self.nuovoPistaOccupata = nuovoPistaOccupata

        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
                gruppo = next((gruppo for gruppo in gruppi if gruppi.id == id), None)
                gruppo.membri = nuovoMembri
                gruppo.numeroPartite = nuovoNumeroPartite
                gruppo.pistaOccupata = nuovoPistaOccupata

            with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
                pickle.dump(gruppi, f, pickle.HIGHEST_PROTOCOL)

    def creaGruppoClienti(self, id, membri, numeroPartite, pistaOccupata, counterPartito = False):
        self.id = id
        self.membri = membri
        self.numeroPartite = numeroPartite
        self.pistaOccupata = pistaOccupata
        self.counterPartito = counterPartito
        gruppi = []
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', "rb") as f:
                gruppi = pickle.load(f)
            gruppi.append(self)
            with open('GruppoClienti/data/GruppoClienti.pickle', "wb") as f:
                pickle.dump(gruppi, f, pickle.HIGHEST_PROTOCOL)
        print("LL: " + str(gruppi))
        return self

    def getGruppoClienti(self):
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
                print(gruppi)
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

    # def __str__(self):
    #     return "Id: " + str(self.id) + "\n" + \
    #             "Membri : " + str(self.membri) + "\n" + \
    #             "Numero Partite: " + str(self.numeroPartite) + "\n" + \
    #             "Pista occupata: " + str(self.pistaOccupata)
