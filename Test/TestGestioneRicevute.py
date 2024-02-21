
import os
import pickle
from unittest import TestCase

from Ricevuta.controller.controllore_ricevuta import ControlloreRicevuta
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from Cliente.controller.controllore_cliente import ControlloreCliente

class TestGestioneRicevute(TestCase):
    def testCreaRicevuta(self):
        self.controlloreRicevuta = ControlloreRicevuta()
        self.ricevuta = self.controlloreRicevuta.creaRicevuta("02/07/24", "test",
                                15.0, "15:07:14", [], "Abbonamento")

        ricevute = None
        if os.path.isfile('Ricevuta/data/ricevute.pickle'):
            with open('Ricevuta/data/ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        #verifica se il file esiste
        self.assertIsNotNone(ricevute)
        #verifica se la ricevuta è nel file
        self.assertIn(self.ricevuta, ricevute)

    def testRimuoviRicevuta(self):
        self.controlloreRicevuta = ControlloreRicevuta()
        self.ricevuta = self.controlloreRicevuta.creaRicevuta( "02/07/24",
                "test2", 15, "15:07:14", [], "Abbonamento")

        ricevute = None
        ricevute = self.controlloreRicevuta.visualizzaRicevute()
        self.assertIsNotNone(ricevute)
        self.assertIn(self.ricevuta, ricevute)
        self.controlloreRicevuta.rimuoviRicevuta(self.ricevuta)
        ricevute = self.controlloreRicevuta.visualizzaRicevute()
        self.assertNotIn(self.ricevuta, ricevute)

    def testCalcolaImporto(self):
        self.controlloreGruppo = ControlloreGruppoClienti()
        self.controlloreRicevuta = ControlloreRicevuta()
        self.controlloreCliente = ControlloreCliente()

        #creazione di clienti
        self.cliente1 = self.controlloreCliente.creaCliente(False,
        "GGFFFFFFFFFFFFFF", "Rossi", "ros@email", "Marco",
                                "Uomo", "38", False, "")

        self.cliente2 = self.controlloreCliente.creaCliente(False,
        "FFFFFFFFFFFFFFFF", "Rossi", "ros@email", "Marco",
                                "Uomo", "38", False, "")

        #creazione gruppo
        self.controlloreGruppo.creaGruppoClienti( "test3", [self.cliente1,self.cliente2],
                                                  13, False)

        importo = self.controlloreRicevuta.calcolaImportoPartita("test3")
        self.assertEqual(130.0 , importo)

