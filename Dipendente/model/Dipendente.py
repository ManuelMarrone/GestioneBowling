import os
import pickle
import uuid


class Dipendente():
    idIncrementale = 1

    def __init__(self):
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = None
        self.email = ""
        self.id = ""
        self.password = ""
        self.sesso = ""
        self.telefono = 0

    def creaDipendente(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.nome = nome
        self.id = self.creaId(self.nome, self.cognome)
        self.password = password
        self.sesso = sesso
        self.telefono = telefono

        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'wb') as f:  # a serve per fare append in fondo al pickle
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def modificaDipendente(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome,
                           nuovaPassword, nuovoSesso, nuovoTelefono):
        self.codiceFiscale = nuovoCodiceFiscale
        self.cognome = nuovoCognome
        self.dataNascita = nuovaDataNascita
        self.email = nuovaEmail
        self.nome = nuovoNome
        self.password = nuovaPassword
        self.sesso = nuovoSesso
        self.telefono = nuovoTelefono

        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = dict(pickle.load(f))
                dipendenti[self.id].codiceFiscale = nuovoCodiceFiscale
                dipendenti[self.id].cognome = nuovoCognome
                dipendenti[self.id].dataNascita = nuovaDataNascita
                dipendenti[self.id].email = nuovaEmail
                dipendenti[self.id].nome = nuovoNome
                dipendenti[self.id].password = nuovaPassword
                dipendenti[self.id].sesso = nuovoSesso
                dipendenti[self.id].telefono = nuovoTelefono
            with open('Dipendente/data/dipendenti.pickle', 'wb') as f:  # se ti sovrascriverà cambia wb con ab
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviDipendente(self):
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = dict(pickle.load(f))
                del dipendenti[self.id]
            with open('Dipendente/data/dipendenti.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)
        del self

    def getDipendente(self):
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = dict(pickle.load(f))
                return dipendenti[self.id]

    def getDipendenti(self):
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = dict(pickle.load(f))
                return dipendenti or None


    # creazione id univoco
    def creaId(nome, cognome):
        global idIncrementale
        id = nome[0:2] + cognome[0:2] + idIncrementale
        idIncrementale += 1
        return id
