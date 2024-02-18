import os
import pickle


class Amministratore():
    def __init__(self):
        self.cognome = ""
        self.email = ""
        self.id = 0
        self.nome = ""
        self.password = ""

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getAmministratore(self):
        if os.path.isfile('Amministratore/data/amministratore.pickle'):
            with open('Amministratore/data/amministratore.pickle', 'rb') as f:
                amministratore = pickle.load(f)
                return amministratore[self.id]
