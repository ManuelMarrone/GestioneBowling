import os
import pickle

from Dipendente.model.Dipendente import Dipendente


class Cassiere(Dipendente):
    def __init__(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        super().__init__(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono)

        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'ab') as f:          #a serve per fare append in fondo al pickle
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def modificaCassiere(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        super().modificaDipendente(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono)
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))                              #sicuro che non preleva un elemento alla volta?
                clienti[self.id].codiceFiscale = nuovoCodiceFiscale
                clienti[self.id].cognome = nuovoCognome
                clienti[self.id].dataNascita = nuovaDataNascita
                clienti[self.id].email = nuovaEmail
                clienti[self.id].nome = nuovoNome
                clienti[self.id].password = nuovaPassword
                clienti[self.id].sesso = nuovoSesso
                clienti[self.id].telefono = nuovoTelefono
            with open('Cassiere/data/cassieri.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviCassiere(self):
        super().rimuoviDipendente()
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                del clienti[self.id]

    def getCassiere(self):
        super().getDipendente()

