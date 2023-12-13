import os
import pickle

from Dipendente.model.Dipendente import Dipendente

class ControlloreDipendente():
    def __init__(self):
        pass

    def modificaDipendente(self,nuovoRuolo, nuovoCodiceFiscale, nuovoCognome, nuovaDataNascita, nuovaEmail, nuovoNome, nuovaPassword, nuovoSesso, nuovoTelefono):
        pass

    def rimuoviDipendente(self, idDipendente):
        dipendente = self.ricercaDipendenteId(idDipendente)
        if isinstance(dipendente, Dipendente):
            Dipendente().rimuoviDipendente()
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
        else:
            return None

    def ricercaDipendenteId(self, id):
        dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
        if len(dipendenti) > 0:
            for dipendente in dipendenti:
                if dipendente.id == id:
                    return dipendente
                else:
                    return None
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
        else:
            return None

    def getDipendente(self):
        return Dipendente().getDipendente()

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

