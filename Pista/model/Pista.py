import os
import pickle


class Pista():

    def __init__(self, disponibilita=None, id=0):
        self.disponibilita = disponibilita
        self.id = id

    def creaPista(self, disponibilita, id):
        self.disponibilita = disponibilita
        self.id = id
        piste = []
        if os.path.isfile('Pista/data/piste.pickle'):
            with open('Pista/data/piste.pickle', "rb") as f:
                piste = pickle.load(f)
            piste.append(self)
            print(piste)
            with open('Pista/data/piste.pickle', "wb") as f:
                pickle.dump(piste, f, pickle.HIGHEST_PROTOCOL)
        return self

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

    def setDisponibilita(self, bool, id):
        if os.path.isfile('Pista/data/piste.pickle'):
            with open('Pista/data/piste.pickle', 'rb') as f:
                piste = pickle.load(f)
                pista = next((pista for pista in piste if str(pista.id) == str(id)), None)
                pista.disponibilita = bool
            with open('Pista/data/piste.pickle', 'wb') as f:
                pickle.dump(piste, f, pickle.HIGHEST_PROTOCOL)
