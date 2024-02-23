import os
import pickle

class Dipendente:
    def __init__(self):
        self.ruolo = ""
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = None
        self.email = ""
        self.nome = ""
        self.password = ""
        self.sesso = ""
        self.telefono = 0

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getRuolo(self):
        return self.ruolo

    def getCF(self):
        return self.codiceFiscale

    def getDataNascita(self):
        return (self.dataNascita).toString("dd-MM-yyyy")

    def getEmail(self):
        return self.email

    def getSesso(self):
        return self.sesso

    def getTelefono(self):
        return str(self.telefono)

    def getPassword(self):
        return self.password


    def creaDipendente(self, ruolo, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        self.ruolo = ruolo
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.nome = nome
        self.password = password
        self.sesso = sesso
        self.telefono = telefono
        dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', "rb") as f:
                dipendenti = pickle.load(f)
            dipendenti.append(self)
            with open('Dipendente/data/dipendenti.pickle', "wb") as f:
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)
        return self

    def modificaDipendente(self, nuovoRuolo, codiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome,
                           nuovaPassword, nuovoSesso, nuovoTelefono):
        self.ruolo = nuovoRuolo
        self.cognome = nuovoCognome
        self.dataNascita = nuovaDataNascita
        self.email = nuovaEmail
        self.nome = nuovoNome
        self.password = nuovaPassword
        self.sesso = nuovoSesso
        self.telefono = nuovoTelefono

        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
                dipendente = next((dipendente for dipendente in dipendenti if dipendente.codiceFiscale == codiceFiscale), None)
                dipendente.ruolo = nuovoRuolo
                dipendente.cognome = nuovoCognome
                dipendente.dataNascita = nuovaDataNascita
                dipendente.email = nuovaEmail
                dipendente.nome = nuovoNome
                dipendente.password = nuovaPassword
                dipendente.sesso = nuovoSesso
                dipendente.telefono = nuovoTelefono
            with open('Dipendente/data/dipendenti.pickle', 'wb') as f:  # se ti sovrascriverà cambia wb con ab
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviDipendente(self):
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
                daRimuovere = next((dipendente for dipendente in dipendenti if dipendente.codiceFiscale == self.codiceFiscale), None)
                dipendenti.remove(daRimuovere)
            with open('Dipendente/data/dipendenti.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)
        del self

    def getDipendente(self):
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
                return dipendenti[self.codiceFiscale]

    def getDipendenti(self):
        dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
            return dipendenti
        else:
            return None
