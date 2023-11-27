import os
import pickle

from Dipendente.model.Dipendente import Dipendente


class Magazziniere(Dipendente):

    def __init__(self):
        super().__init__()

    def creaMagazziniere(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        super().creaDipendente(codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono)

        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'wb') as f:  # a serve per fare append in fondo al pickle
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def modificaMagazziniere(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword,
                         nuovoSesso, nuovoTelefono):
        super().modificaDipendente(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome,
                                   nuovaPassword, nuovoSesso, nuovoTelefono)

        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))
                magazzinieri[self.id].codiceFiscale = nuovoCodiceFiscale
                magazzinieri[self.id].cognome = nuovoCognome
                magazzinieri[self.id].dataNascita = nuovaDataNascita
                magazzinieri[self.id].email = nuovaEmail
                magazzinieri[self.id].nome = nuovoNome
                magazzinieri[self.id].password = nuovaPassword
                magazzinieri[self.id].sesso = nuovoSesso
                magazzinieri[self.id].telefono = nuovoTelefono
            with open('Magazziniere/data/magazzinieri.pickle', 'wb') as f:  # se ti sovrascriverà cambia wb con ab
                pickle.dump(magazzinieri, f, pickle.HIGHEST_PROTOCOL)

    def rimuovimagazzinieri(self):
        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))
                del magazzinieri[self.id]
            with open('Magazziniere/data/magazzinieri.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(magazzinieri, f, pickle.HIGHEST_PROTOCOL)
        del self

    def getMagazziniere(self):
        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))
                return magazzinieri[self.id]