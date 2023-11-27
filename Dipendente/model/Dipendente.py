import uuid


class Dipendente():
    def __init__(self):
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = None
        self.email = ""
        self.password = ""
        self.sesso = ""
        self.telefono = 0
        #creazione e immissione nel fil pickle nella classe cassiere e magazziniere

    def creaDipendente (self,  codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.id = str(uuid.uuid5())  # creazione di id random e univoco
        self.nome = nome
        self.password = password
        self.sesso = sesso
        self.telefono = telefono

    def modificaDipendente(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        self.codiceFiscale = nuovoCodiceFiscale
        self.cognome = nuovoCognome
        self.dataNascita = nuovaDataNascita
        self.email = nuovaEmail
        self.nome = nuovoNome
        self.password = nuovaPassword
        self.sesso = nuovoSesso
        self.telefono = nuovoTelefono
        #implementazione in cassiere e magazziniere

