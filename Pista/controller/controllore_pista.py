import os
import pickle

from Pista.model.Pista import Pista


class ControllorePista():
    def __init__(self, pista=None):
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

    def creaPista(self, disponibilita, id):
        pistetemp = []
        pista = None
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                pistetemp = pickle.load(f)
        if len(pistetemp) > 0:
             for pistatemp in pistetemp:
                 if pistatemp.id == id:
                    pista = pistatemp
        else:
            pista = None

        if isinstance(pista, Pista):  # se la pista già esiste
            return None
        else:
            nuovaPista = Pista().creaPista(
               disponibilita=disponibilita,
               id=id
            )

        return nuovaPista