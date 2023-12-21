import os
import pickle


class Scarpa():
    def __init__(self, disponibilita, id, taglia):
        self.disponibilita = disponibilita
        self.id = id
        self.taglia = taglia

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
