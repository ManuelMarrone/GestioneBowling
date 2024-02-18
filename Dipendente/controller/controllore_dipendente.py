import os
import pickle

from Dipendente.model.Dipendente import Dipendente

class ControlloreDipendente():

    def __init__(self, dipendente=None):
        self.model = dipendente

    def getNome(self):
        return self.model.getNome()

    def getCognome(self):
        return self.model.getCognome()

    def getRuolo(self):
        return self.model.getRuolo()

    def getCF(self):
        return self.model.getCF()

    def getDataNascita(self):
        return self.model.getDataNascita()

    def getEmail(self):
        return self.model.getEmail()

    def getSesso(self):
        return self.model.getSesso()

    def getTelefono(self):
        return self.model.getTelefono()

    def getPassword(self):
        return self.model.getPassword()

    def modificaDipendente(self, nuovoRuolo, codiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        Dipendente().modificaDipendente(
            nuovoRuolo=nuovoRuolo,
            codiceFiscale=codiceFiscale,
            nuovoCognome=nuovoCognome,
            nuovaDataNascita=nuovaDataNascita,
            nuovaEmail=nuovaEmail,
            nuovoNome=nuovoNome,
            nuovaPassword=nuovaPassword,
            nuovoSesso=nuovoSesso,
            nuovoTelefono=nuovoTelefono
        )
        return True

    def rimuoviDipendente(self, dipendente):
        if isinstance(dipendente, Dipendente):
            dipendente.rimuoviDipendente()
            return True
        else:
            return False

    def ricercaDipendenteCodiceFiscale(self, codiceFiscale):
        dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
        if len(dipendenti) > 0:
            for dipendente in dipendenti:
                if dipendente.codiceFiscale == codiceFiscale:
                    return dipendente
        else:
            return None

    def ricercaDipendenteEmail(self, email):
        dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)

        if len(dipendenti) > 0:
            for dipendente in dipendenti:
                if dipendente.email == email:
                    return dipendente
        else:
            return None

    def ricercaDipendenteNomeCognome(self, nome, cognome):
        dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)

        if len(dipendenti) > 0:
            for dipendente in dipendenti:
                if dipendente.nome == nome and dipendente.cognome == cognome:
                    return dipendente
        else:
            return None

    def getDipendente(self):
        return self.model.getDipendente()

    def visualizzaDipendenti(self):
        return Dipendente().getDipendenti()

    def creaDipendente(self, ruolo, codiceFiscale, cognome, dataNascita, email, nome, password, sesso, telefono):
        dipendente = self.ricercaDipendenteCodiceFiscale(codiceFiscale)
        if isinstance(dipendente, Dipendente):  # se il magazziniere già esiste
            return None
        else:
            nuovoDipendente = Dipendente().creaDipendente(
              ruolo=ruolo,
              codiceFiscale=codiceFiscale,
              cognome=cognome,
              dataNascita=dataNascita,
              email=email,
              nome=nome,
              password=password,
              sesso=sesso,
              telefono=telefono
             )

        return nuovoDipendente




