class Dipendente():
    def __init__(self, codiceFiscale, cognome, dataNascita, email, id, nome, password, sesso, telefono):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.id = id
        self.nome = nome
        self.password = password
        self.sesso = sesso
        self.telefono = telefono

    def ricercaDipendenteCodiceFiscale(self, codiceFiscale):
        pass