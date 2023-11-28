class Cliente():
    def __init__(self, abbonato, codiceFiscale, cognome, email, id, nome, sesso, tagliaScarpe):
        self.abbonato = abbonato
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.email = email
        self.id = id
        self.nome = nome
        self.sesso = sesso
        self.tagliaScarpe = tagliaScarpe

    def isAbbbonato(self):
        return self.abbonato



