import os
import pickle

from Cassiere.model.Cassiere import Cassiere


class ControlloreCassiere():
    def __init__(self, cassiere):
        self.model = cassiere

    def creaCassiere(self, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        cassiere = self.ricercaCassiereCodiceFiscale(codiceFiscale)
        if isinstance(cassiere, Cassiere):  # se il cassiere già esiste
            return False
        else:
            nuovoCassiere = Cassiere().creaCassiere(
                codiceFiscale=codiceFiscale,
                cognome=cognome,
                dataNascita=dataNascita,
                email=email,
                nome=nome,
                password=password,
                sesso=sesso,
                telefono=telefono
            )

        return nuovoCassiere

    def modificaCassiere(self,  nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        pass

    def rimuoviCassiere(self, idCassiere):
        cassiere = self.ricercaCassiereId(idCassiere)
        if isinstance(cassiere, Cassiere):
            cassiere.rimuoviCassiere()
            return True
        else:
            return False

    def ricercaCassiereCodiceFiscale(self, codiceFiscale):
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))

        if len(cassieri) > 0:
            for cassiere in cassieri.values():
                if cassiere.codiceFiscale == codiceFiscale:
                    return cassiere
        else:
            return None

    def ricercaCassiereId(self, id):
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))

        if len(cassieri) > 0:
            for cassiere in cassieri.values():
                if cassiere.id == id:
                    return cassiere
        else:
            return None

    def ricercaCassiereEmail(self, email):
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))

        if len(cassieri) > 0:
            for cassiere in cassieri.values():
                if cassiere.email == email:
                    return cassiere
        else:
            return None

    def ricercaCassiereNomeCognome(self, nome, cognome):
        if os.path.isfile('Cassiere/data/cassieri.pickle'):
            with open('Cassiere/data/cassieri.pickle', 'rb') as f:
                cassieri = dict(pickle.load(f))

        if len(cassieri) > 0:
            for cassiere in cassieri.values():
                if cassiere.nome == nome and cassiere.cognome == cognome:
                    return cassiere
        else:
            return None

    def getCassiere(self):
        return Cassiere.getCassiere()
