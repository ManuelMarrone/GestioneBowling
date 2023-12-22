import os
import pickle
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

    def creaCliente(self, abbonato, codiceFiscale, id, cognome, email, nome, sesso, tagliaScarpe):
        self.abbonato = abbonato
        self.codiceFiscale = codiceFiscale
        self.id = id
        self.cognome = cognome
        self.email = email
        self.nome = nome
        self.sesso = sesso
        self.tagliaScarpe = tagliaScarpe
        clienti = []
        if os.path.isfile('ListaClienti/data/ListaClienti.pickle'):
            with open('ListaClienti/data/ListaClienti.pickle', "rb") as f:
                clienti = pickle.load(f)
            clienti.append(self)
            with open('ListaClienti/data/ListaClienti.pickle', "wb") as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        return self

    def isAbbbonato(self):
        return self.abbonato

    def getCliente(self):
        if os.path.isfile('ListaClienti/data/ListaClienti.pickle'):
            with open('ListaClienti/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                return clienti[self.id]

    def getClienti(self):
        clienti = []
        if os.path.isfile('ListaClienti/data/ListaClienti.pickle'):
            with open('ListaClienti/data/ListaClienti.pickle', 'rb') as f:
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
