import os
import pickle
idIncrementale = 0

class Dipendente:


    def __init__(self):
        self.ruolo = ""
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = None
        self.email = ""
        self.nome = ""
        self.id = ""
        self.password = ""
        self.sesso = ""
        self.telefono = 0

    # creazione id univoco
    def creaId(self, nome, cognome):
        global idIncrementale
        print("entrato nel crea id")
        idIncrementale += 1
        print("1")
        idGenerato = nome[0:2] + cognome[0:2] + str(idIncrementale)
        print("2")
        print("3")
        return idGenerato

    def creaDipendente(self, ruolo, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        print("ingresso nel model")
        self.ruolo = ruolo
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.nome = nome
        self.id = self.creaId(nome, cognome)
        self.password = password
        self.sesso = sesso
        self.telefono = telefono
        print("model")
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'wb') as f:  # a serve per fare append in fondo al pickle
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

        return self

    def modificaDipendente(self, nuovoRuolo, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome,
                           nuovaPassword, nuovoSesso, nuovoTelefono):
        self.ruolo = nuovoRuolo
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
                dipendenti[self.id].ruolo = nuovoRuolo
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

