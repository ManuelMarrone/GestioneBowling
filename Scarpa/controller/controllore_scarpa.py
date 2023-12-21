import os
import pickle

from Scarpa.model.Scarpa import Scarpa


class ControlloreScarpa():
    def __init__(self, scarpa):
        self.model = scarpa

    def getIdScarpa(self):
        return self.model.id

    def getDisponibilitaScarpa(self):
        return self.model.disponibilita

    def getTagliaScarpa(self):
        return self.model.taglia

    def ricercaScarpaTaglia(self, taglia):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
        if len(scarpe) > 0:
            for scarpa in scarpe:
                if scarpa.taglia == taglia:
                    return scarpa
        else:
            return None

    def getScarpa(self):
        return self.model.getScarpa()

    def visualizzaScarpe(self):
        return Scarpa().getScarpe()

    def setDisponibilitaScarpa(self, bool):
        self.model.setDisponibilitaScarpa(bool)