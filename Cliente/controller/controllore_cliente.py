import os
import pickle

from Cliente.model.Cliente import Cliente
class ControlloreCliente():
    def __init__(self, cliente=None):
        self.model = cliente

    def getAbbonato(self):
        return self.model.abbonato

    def isAbbonato(self):
        if self.model.abbonato is True:
            return "Si"
        else:
            return "No"

    def getCodiceFiscale(self):
        return self.model.codiceFiscale

    def getCognome(self):
        return self.model.cognome

    def getEmail(self):
        return self.model.email

    def getId(self):
        return self.model.id

    def getNome(self):
        return self.model.nome

    def getSesso(self):
        return self.model.sesso

    def getTagliaScarpe(self):
        return self.model.tagliaScarpe

    def setAssegnato(self, x, id):
        self.model.setAssegnato(x, id)


    def modificaCliente(self,id, nuovoAbbonato, nuovoCodiceFiscale, nuovoCognome, nuovaEmail, nuovoNome,
                        nuovoSesso, nuovaTagliaScarpe):
        Cliente().modificaCliente(id = id,
            nuovoAbbonato=nuovoAbbonato,
            nuovoCodiceFiscale=nuovoCodiceFiscale,
            nuovoCognome=nuovoCognome,
            nuovaEmail=nuovaEmail,
            nuovoNome=nuovoNome,
            nuovoSesso=nuovoSesso,
            nuovaTagliaScarpe=nuovaTagliaScarpe
        )
        return True

    def rimuoviCliente(self, cliente):
        if isinstance(cliente, Cliente):
            cliente.rimuoviCliente()
            return True
        else:
            return False


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

    def ricercaClienteId(self, id):
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        if len(clienti) > 0:
            for cliente in clienti:
                if cliente.id == id:
                    return cliente
        else:
            return None

    def ricercaClienteEmail(self, email):
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)

        if len(clienti) > 0:
            for cliente in clienti:
                if cliente.email == email:
                    return cliente
        else:
            return None

    def ricercaClienteNomeCognome(self, nome, cognome):
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)

        if len(clienti) > 0:
            for cliente in clienti:
                if cliente.nome == nome and cliente.cognome == cognome:
                    return cliente
        else:
            return None

    def getCliente(self):
        return self.model.getCliente()

    def visualizzaClienti(self):
        return Cliente().getClienti()

    def creaCliente(self, abbonato, codiceFiscale, cognome, email, nome, sesso, tagliaScarpe, assegnato=False):
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
              tagliaScarpe=tagliaScarpe,
              assegnato=assegnato
             )

        return nuovoCliente