import os
import pickle


class Pista():

    def __init__(self, disponibilita, id):
        self.disponibilita = disponibilita
        self.id = id


    def getPista(self):
        piste = []
        if os.path.isfile('Pista/data/piste.pickle'):
            with open('Pista/data/piste.pickle', 'rb') as f:
                piste = pickle.load(f)
                return piste[self.id]

    def getPiste(self):
        piste = []
        if os.path.isfile('Pista/data/piste.pickle'):
            with open('Pista/data/piste.pickle', 'rb') as f:
                piste = pickle.load(f)
            return piste
        else:
            return None

    def setDisponibilita(self, bool):
        self.disponibilita = bool
