import os
import pickle

from Partita.model.Partita import Partita


class ControllorePartita():

    def __init__(self, partita=None):
        self.model = partita

    def setOraInizio(self, ora):
        self.model.setOraInizio(ora)

    def getOraInizio(self):
        return self.model.getOraInizio()

    def creaPartita(self, idGruppo, idPista, oraInizio):
        partita = self.ricercaPartitaIdGruppo(idGruppo)
        if isinstance(partita, Partita):
            return None
        else:
            nuovaPartita = Partita().creaPartita(
                idGruppo=idGruppo,
                idPista=idPista,
                oraInizio=oraInizio
            )
        return nuovaPartita
    def ricercaPartitaIdGruppo(self, idGruppo):
        partite = []
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
        if len(partite) > 0:
            for partita in partite:
                if partita.idGruppo == idGruppo:
                    return partita
        else:
            return None


    #metodo richiamato ciclicamente sul foreach di gruppi che hanno counterPartito == True
    def calcolaTempiAttesa(self):
        return self.model.calcolaTempiAttesa()

    def rimuoviPartita(self, partita):
        if isinstance(partita, Partita):
            partita.rimuoviPartita()
            return True
        else:
            return False
