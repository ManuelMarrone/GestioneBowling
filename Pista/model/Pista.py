import os
import pickle


class Pista():

    def __init__(self, disponibilita=None, id=0):
        self.disponibilita = disponibilita
        self.id = id

    def getPista(self):
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

    def getId(self):
        return self.id

    def getDisponibilita(self):
        return self.disponibilita

    def setDisponibilita(self, occupata):
        if os.path.isfile('Pista/data/piste.pickle'):
            with open('Pista/data/piste.pickle', 'rb') as f:
                piste = pickle.load(f)
                pista = next((pista for pista in piste if pista.id == self.id), None)
                pista.disponibilita = occupata
            with open('Pista/data/piste.pickle', 'wb') as f:
                pickle.dump(piste, f, pickle.HIGHEST_PROTOCOL)
