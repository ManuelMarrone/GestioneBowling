import os
import pickle

from Dipendente.model.Dipendente import Dipendente


class Cassiere(Dipendente):

    def __init__(self):
        super().__init__()

    def creaCassiere(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        super().creaDipendente(codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono)

        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'wb') as f:          #a serve per fare append in fondo al pickle
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def modificaCassiere(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        super().modificaDipendente(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono)

        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))
                cassieri[self.id].codiceFiscale = nuovoCodiceFiscale
                cassieri[self.id].cognome = nuovoCognome
                cassieri[self.id].dataNascita = nuovaDataNascita
                cassieri[self.id].email = nuovaEmail
                cassieri[self.id].nome = nuovoNome
                cassieri[self.id].password = nuovaPassword
                cassieri[self.id].sesso = nuovoSesso
                cassieri[self.id].telefono = nuovoTelefono
            with open('Cassiere/data/cassieri.pickle', 'wb') as f:                      #se ti sovrascriverà cambia wb con ab
                pickle.dump(cassieri, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviCassiere(self):
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))
                del cassieri[self.id]
            with open('Cassiere/data/cassieri.pickle', 'wb') as f:      #riscrive i cassieri sena l'eliminato
                    pickle.dump(cassieri, f, pickle.HIGHEST_PROTOCOL)
        del self

    def getCassiere(self):
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))
                return cassieri[self.id]

