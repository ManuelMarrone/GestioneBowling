import os
import pickle

from Pista.model.Pista import Pista


class ControllorePista():
    def __init__(self, pista):
        self.model = pista

    def getId(self):
        return self.model.id

    def getDisponibilita(self):
        return self.model.disponibilita

    def ricercaPistaId(self, id):
        piste = []
        if os.path.isfile('Pista/data/piste.pickle'):
            with open('Pista/data/piste.pickle', 'rb') as f:
                piste = pickle.load(f)
        if len(piste) > 0:
            for pista in piste:
                if pista.id == id:
                    return pista
        else:
            return None

    def getPista(self):
        return self.model.getPista()

    def visualizzaPiste(self):
        return Pista().getPiste()

    def setDisponibilita(self, bool):
        self.model.setDisponibilita(bool)