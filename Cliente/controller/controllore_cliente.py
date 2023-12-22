import os
import pickle

from Cliente.model.Cliente import Cliente
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

    def ricercaClienteCodiceFiscale(self, codiceFiscale):
         clienti = []
         if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
         if len(clienti) > 0:
             for cliente in clienti:
                 if cliente.codiceFiscale == codiceFiscale:
                     return cliente
         else:
            return None
    def creaCliente(self, abbonato, codiceFiscale, cognome, email, nome, sesso, tagliaScarpe):
        cliente = self.ricercaClienteCodiceFiscale(codiceFiscale)
        if isinstance(cliente, Cliente):  # se il magazziniere già esiste
            return None
        else:
            nuovoCliente = Cliente().creaCliente(
              abbonato=abbonato,
              codiceFiscale=codiceFiscale,
              cognome=cognome,
              email=email,
              nome=nome,
              sesso=sesso,
              tagliaScarpe=tagliaScarpe
             )

        return nuovoCliente