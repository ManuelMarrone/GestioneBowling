import os
import pickle
class Cliente():
    def __init__(self):
        self.abbonato = ""
        self.codiceFiscale = ""
        self.cognome = ""
        self.email = ""
        self.nome = ""
        self.sesso = ""
        self.tagliaScarpe = ""
        self.assegnato = False
        self.idScarpa = ""

    def creaCliente(self, abbonato, codiceFiscale, cognome, email, nome, sesso, tagliaScarpe, assegnato, idScarpa):
        self.abbonato = abbonato
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.email = email
        self.nome = nome
        self.sesso = sesso
        self.tagliaScarpe = tagliaScarpe
        self.assegnato = assegnato
        self.idScarpa = idScarpa
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', "rb") as f:
                clienti = pickle.load(f)
            clienti.append(self)
            with open('Cliente/data/ListaClienti.pickle', "wb") as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        return self

    def modificaCliente(self, nuovoAbbonato, codiceFiscale, nuovoCognome, nuovaEmail, nuovoNome,
                        nuovoSesso, nuovaTagliaScarpe):
        self.abbonato = nuovoAbbonato
        self.codiceFiscale = codiceFiscale
        self.cognome = nuovoCognome
        self.email = nuovaEmail
        self.nome = nuovoNome
        self.sesso = nuovoSesso
        self.tagliaScarpe = nuovaTagliaScarpe

        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if cliente.codiceFiscale == codiceFiscale), None)
                cliente.abbonato = nuovoAbbonato
                cliente.cognome = nuovoCognome
                cliente.email = nuovaEmail
                cliente.nome = nuovoNome
                cliente.sesso = nuovoSesso
                cliente.tagliaScarpe = nuovaTagliaScarpe
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:  # se ti sovrascriverà cambia wb con ab
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviCliente(self):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                daRimuovere = next((cliente for cliente in clienti if cliente.codiceFiscale == self.codiceFiscale), None)
                clienti.remove(daRimuovere)
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        del self


    def getAbbonato(self):
        return self.abbonato

    def isAbbonato(self):
        if self.abbonato is True:
            return "Si"
        else:
            return "No"

    def isAssegnato(self):
        return self.assegnato

    def getCognome(self):
        return self.cognome
    def getNome(self):
        return self.nome
    def getCodiceFiscale(self):
        return self.codiceFiscale
    def getEmail(self):
        return self.email
    def getSesso(self):
        return self.sesso
    def getIdScarpa(self):
        return self.idScarpa
    def getTagliaScarpe(self):
        return self.tagliaScarpe

    def setIdScarpa(self, idScarpa, cfCliente):  #da cambiare con il codice fiscale
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if str(cliente.codiceFiscale) == cfCliente), None)
                cliente.idScarpa = idScarpa
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def getCliente(self):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                return clienti[self.codiceFiscale]

    def getClienti(self):
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                    clienti = pickle.load(f)
            return clienti
        else:
            return None

    def setAbbonato(self, val):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if cliente.codiceFiscale == self.codiceFiscale), None)
                cliente.abbonato = val
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def setAssegnato(self, val):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if cliente.codiceFiscale == self.codiceFiscale), None)
                cliente.assegnato = val
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
