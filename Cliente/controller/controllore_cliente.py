import os
import pickle

from ListaClienti.controller.Cliente import Cliente
class ControlloreCliente():
    def __init__(self, cliente=None):
        self.model = cliente

    def getAbbonato(self):
        return self.model.Abbonato

    def getCodiceFiscale(self):
        return self.model.CodiceFiscale

    def getCognome(self):
        return self.model.Cognome

    def getEmail(self):
        return self.model.Email

    def getId(self):
        return self.model.Id

    def getNome(self):
        return self.model.Nome

    def getSesso(self):
        return self.model.Sesso

    def getTagliaScarpe(self):
        return self.model.TagliaScarpe

    def getCliente(self):
        return self.model.getCliente()

    def visualizzaClienti(self):
        return Cliente().getClienti()