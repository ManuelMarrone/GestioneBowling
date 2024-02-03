import os
import pickle

from Cliente.model.Cliente import Cliente


class ControlloreCliente():
    def __init__(self, cliente=None):
        self.model = cliente

    def getAbbonato(self):
        return self.model.getAbbonato()

    def setAbbonato(self, val):
        self.model.setAbbonato(val)

    def isAbbonato(self):
        return self.model.isAbbonato()

    def getCodiceFiscale(self):
        return self.model.getCodiceFiscale()

    def getCognome(self):
        return self.model.getCognome()

    def getEmail(self):
        return self.model.getEmail()

    def getNome(self):
        return self.model.getNome()

    def getSesso(self):
        return self.model.getSesso()

    def getTagliaScarpe(self):
        return self.model.getTagliaScarpe()

    def getAssegnato(self):
        return self.model.isAssegnato()

    def setAssegnato(self, x, cf):
        self.model.setAssegnato(x, cf)

    def modificaCliente(self, nuovoAbbonato, codiceFiscale, nuovoCognome, nuovaEmail, nuovoNome,
                        nuovoSesso, nuovaTagliaScarpe):
        Cliente().modificaCliente(
            nuovoAbbonato=nuovoAbbonato,
            codiceFiscale=codiceFiscale,
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

    def getIdScarpa(self):
        return self.model.getIdScarpa()

    def setIdScarpa(self, idS, cf):
        self.model.setIdScarpa(idS, cf)

    def visualizzaClienti(self):
        return self.model.getClienti()

    def creaCliente(self, abbonato, codiceFiscale, cognome, email, nome, sesso, tagliaScarpe, assegnato, idScarpa):
        cliente = self.ricercaClienteCodiceFiscale(codiceFiscale)
        if isinstance(cliente, Cliente):  # se il cliente già esiste
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
                assegnato=assegnato,
                idScarpa=idScarpa
            )

        return nuovoCliente
