import os
import pickle
from unittest import TestCase

from Partita.controller.controllore_partita import ControllorePartita


class TestAssegnamentoPista(TestCase):
    def testCreaPartita(self):
        self.controllorePartita = ControllorePartita()
        self.partita = self.controllorePartita.creaPartita("test", "pista1",
                                                           "13:02:50")

        partite = None
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Partita/data/partite.pickle', "rb") as f:
                partite = pickle.load(f)

        # verifica se il file esiste
        self.assertIsNotNone(partite)
        # verifica se la partita è nel file
        self.assertIn(self.partita, partite)

    def testRimuoviPartita(self):
        self.controllorePartita = ControllorePartita()
        self.partita = self.controllorePartita.creaPartita("test2", "pista1",
                                                           "13:02:50")
        partite = None
        partite = self.controllorePartita.visualizzaPartite()
        self.assertIsNotNone(partite)
        self.assertIn(self.partita, partite)
        self.controllorePartita.rimuoviPartita(self.partita)
        partite = self.controllorePartita.visualizzaPartite()
        self.assertNotIn(self.partita, partite)
