import os
import pickle


class GruppoClienti:
    def __init__(self):
        self.id = ""
        self.membri = ""
        self.numeroPartite = 0
        self.pistaOccupata = ""



    def creaGruppoClienti(self, id, membri, numeroPartite, pistaOccupata):
        self.id = id
        self.membri = membri
        self.numeroPartite = numeroPartite
        self.pistaOccupata = pistaOccupata
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


    def __str__(self):
        return "Id: " + self.id + "\n" + \
                "Membri : " + self.membri + "\n" + \
                "Numero Partite: " + self.numeroPartite + "\n" + \
                "Pista occupata: " + self.pistaOccupata
