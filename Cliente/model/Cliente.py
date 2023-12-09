class Cliente():
    def __init__(self, abbonato, codiceFiscale, id, cognome, email, nome, sesso, tagliaScarpe):
        self.abbonato = abbonato
        self.codiceFiscale = codiceFiscale
        self.id = id
        self.cognome = cognome
        self.email = email
        self.nome = nome
        self.sesso = sesso
        self.tagliaScarpe = tagliaScarpe

    def isAbbbonato(self):
        return self.abbonato



