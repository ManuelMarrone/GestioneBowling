
import os
import pickle
from unittest import TestCase

from Cliente.controller.controllore_cliente import ControlloreCliente

class TestGestioneClienti(TestCase):
    def testCreaCliente(self):
        self.controlloreCliente = ControlloreCliente()
        self.cliente = self.controlloreCliente.creaCliente(False,
        "FFFFFFFFFFFFFFFF", "Rossi", "ros@email", "Marco",
                                "Uomo", "38", False, "")
        clienti = None
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        #verifica se il file esiste
        self.assertIsNotNone(clienti)
        #verifica se il cliente è nel file
        self.assertIn(self.cliente, clienti)

    def testRimuoviCliente(self):
        self.controlloreCliente = ControlloreCliente()
        self.cliente = self.controlloreCliente.creaCliente(False,
        "GFFFFFFFFFFFFFFF", "Rossi", "ros@email", "Marco",
                                "Uomo", "38", False, "")
        clienti = None
        clienti = self.controlloreCliente.visualizzaClienti()
        self.assertIsNotNone(clienti)
        self.assertIn(self.cliente, clienti)
        self.controlloreCliente.rimuoviCliente(self.cliente)
        clienti = self.controlloreCliente.visualizzaClienti()
        self.assertNotIn(self.cliente, clienti)
