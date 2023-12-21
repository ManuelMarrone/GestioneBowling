import os
import pickle

class ControlloreCliente():
    def __init__(self, cliente):
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


    def ricercaClienteNomeCognome(self, nome, cognome):
        dipendenti = []
        if os.path.isfile('Dipendente/data/dati_cliente.json'):
            with open('Dipendente/data/dati_cliente.json', 'rb') as f:
                dipendenti = pickle.load(f)

        if len(dipendenti) > 0:
            for dipendente in dipendenti:
                if dipendente.nome == nome and dipendente.cognome == cognome:
                    return dipendente
        else:
            return None