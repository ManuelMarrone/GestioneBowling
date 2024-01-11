import os
import pickle


class Scarpa():
    def __init__(self):
        self.disponibilita = True
        self.id = ""
        self.taglia = 0

    # def creaScarpa(self, disponibilita, id, taglia):
    #     self.disponibilita = disponibilita
    #     self.id = id
    #     self.taglia = taglia
    #     scarpe = []
    #     with open('Scarpa/data/scarpe.pickle', "rb") as f:
    #         scarpe = pickle.load(f)
    #     scarpe.append(self)
    #     with open('Scarpa/data/scarpe.pickle', "wb") as f:
    #         pickle.dump(scarpe, f, pickle.HIGHEST_PROTOCOL)
    #     return self

    def getScarpa(self):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
                return scarpe[self.id]

    def getScarpe(self):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
            return scarpe
        else:
            return None

    def setDisponibilitaScarpa(self, bool):
        self.disponibilita = bool
