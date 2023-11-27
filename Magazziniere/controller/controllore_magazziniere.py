import os
import pickle

from Magazziniere.model.Magazziniere import Magazziniere

class ControlloreMagazziniere():
    def __init__(self, magazziniere):
        self.model = magazziniere

    def creaMagazziniere(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        magazziniere = self.ricercaMagazziniereCodiceFiscale(codiceFiscale)
        if isinstance(magazziniere, Magazziniere):  # se il magazziniere già esiste
            return False
        else:
            nuovoMagazziniere = Magazziniere.creaMagazziniere(
                codiceFiscale=codiceFiscale,
                cognome=cognome,
                dataNascita=dataNascita,
                email=email,
                nome=nome,
                password=password,
                sesso=sesso,
                telefono=telefono
            )

        return nuovoMagazziniere

    def modificaMagazziniere(self, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        pass

    def rimuoviMagazziniere(self, idMagazziniere):
        magazziniere = self.ricercaMagazziniereId(idMagazziniere)
        if isinstance(magazziniere, Magazziniere):
            magazziniere.rimuovimagazziniere()
            return True
        else:
            return False

    def ricercaMagazziniereCodiceFiscale(self, codiceFiscale):
        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))

        if len(magazzinieri) > 0:
            for magazziniere in magazzinieri.values():
                if magazziniere.codiceFiscale == codiceFiscale:
                    return magazziniere
        else:
            return None

    def ricercaMagazziniereId(self, id):
        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))

        if len(magazzinieri) > 0:
            for magazziniere in magazzinieri.values():
                if magazziniere.id == id:
                    return magazziniere
        else:
            return None

    def ricercaMagazziniereEmail(self, email):
        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))

        if len(magazzinieri) > 0:
            for magazziniere in magazzinieri.values():
                if magazziniere.email == email:
                    return magazzinieri
        else:
            return None

    def ricercaMagazziniereNomeCognome(self, nome, cognome):
        if os.path.isfile('Magazziniere/data/magazzinieri.pickle'):
            with open('Magazziniere/data/magazzinieri.pickle', 'rb') as f:
                magazzinieri = dict(pickle.load(f))

        if len(magazzinieri) > 0:
            for magazziniere in magazzinieri.values():
                if magazziniere.nome == nome and magazziniere.cognome == cognome:
                    return magazziniere
        else:
            return None

    def getMagazziniere(self):
        return Magazziniere.getMagazziniere()
