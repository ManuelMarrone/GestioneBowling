import os
import pickle
idIncrementale = 0
class Cliente():
    def __init__(self):
        self.abbonato = ""
        self.codiceFiscale = ""
        self.id = ""
        self.cognome = ""
        self.email = ""
        self.nome = ""
        self.sesso = ""
        self.tagliaScarpe = ""

    def creaId(self, nome, cognome):
        global idIncrementale
        idIncrementale += 1
        idGenerato = nome[0:2] + cognome[0:2] + str(idIncrementale)
        return idGenerato

    def creaCliente(self, abbonato, codiceFiscale, cognome, email, nome, sesso, tagliaScarpe):
        self.abbonato = abbonato
        self.codiceFiscale = codiceFiscale
        self.id = self.creaId(nome, cognome)
        self.cognome = cognome
        self.email = email
        self.nome = nome
        self.sesso = sesso
        self.tagliaScarpe = tagliaScarpe
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', "rb") as f:
                clienti = pickle.load(f)
            clienti.append(self)
            with open('Cliente/data/ListaClienti.pickle', "wb") as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        return self

    def modificaCliente(self,id, nuovoAbbonato, nuovoCodiceFiscale, nuovoCognome, nuovaEmail, nuovoNome,
                        nuovoSesso, nuovaTagliaScarpe):
        self.abbonato = nuovoAbbonato
        self.codiceFiscale = nuovoCodiceFiscale
        self.cognome = nuovoCognome
        self.email = nuovaEmail
        self.nome = nuovoNome
        self.sesso = nuovoSesso
        self.tagliaScarpe = nuovaTagliaScarpe

        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if cliente.id == id), None)
                cliente.abbonato = nuovoAbbonato
                cliente.codiceFiscale = nuovoCodiceFiscale
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
                daRimuovere = next((cliente for cliente in clienti if cliente.id == self.id), None)
                clienti.remove(daRimuovere)
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        del self

    def isAbbbonato(self):
        return self.abbonato

    def getCliente(self):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                return clienti[self.id]

    def getClienti(self):
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                    clienti = pickle.load(f)
            return clienti
        else:
            return None
    def __str__(self):
        return  "abbonato: " + self.abbonato + "\n" + \
                "Codice Fiscale: " + self.codiceFiscale + "\n" + \
                "Id: " + self.id + "\n" + \
                "Cognome: " + self.cognome + "\n" + \
                "Email: " + self.email + "\n" + \
                "Nome: " + self.nome + "\n" + \
                "Sesso: " + self.sesso + "\n" + \
                "Taglia Scarpe: " + self.tagliaScarpe
