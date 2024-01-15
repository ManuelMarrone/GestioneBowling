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
        gruppi.append(self.id)
        gruppi.append(self.membri)
        gruppi.append(self.numeroPartite)
        gruppi.append(self.pistaOccupata)
        with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as file_pickle:
            pickle.dump(gruppi, file_pickle)
        with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as file_pickle:
            gruppi_caricati = pickle.load(file_pickle)

        print("LL: " + str(gruppi_caricati))
        return self

    def getGruppoClienti(self):
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
                print(gruppi)
        return

    def __str__(self):
        return "Id: " + self.id + "\n" + \
                "Membri : " + self.membri + "\n" + \
                "Numero Partite: " + self.numeroPartite + "\n" + \
                "Pista occupata: " + self.pistaOccupata
