from Dipendente.model.Dipendente import Dipendente

class Magazziniere(Dipendente):
    def __init__(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        super().__init__(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono)


