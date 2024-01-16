import os
import pickle

from GruppoClienti.model.GruppoClienti import GruppoClienti
class ControlloreGruppoClienti:
    def __init__(self, gruppoClienti = None):
        self.model = gruppoClienti

    def visualizzaGruppi(self):
        return GruppoClienti().getGruppoClienti()