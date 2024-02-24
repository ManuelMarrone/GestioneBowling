import os
import pickle

from datetime import datetime, timedelta
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from Partita.model.Partita import Partita
from Pista.controller.controllore_pista import ControllorePista


class ControllorePartita():

    def __init__(self, partita=None):
        self.model = partita

    def getIdGruppo(self):
        return self.model.getIdGruppo()
    def getIdPista(self):
        return self.model.getIdPista()
    def setOraInizio(self, ora):
        self.model.setOraInizio(ora)
    def getOraInizio(self):
        if self.model is not None:
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

    def rimuoviPartita(self, partita):
        if isinstance(partita, Partita):
            partita.rimuoviPartita()
            return True
        else:
            return False

    def visualizzaPartite(self):
        return Partita().getPartite()

    def ricercaIdGruppoPerPista(self, idPista):
        partite = []
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
        if len(partite) > 0:
            for partita in partite:
                if partita.idPista == idPista:
                    return partita.idGruppo
        else:
            return None
    def calcolaTempoDiAttesa(self, pista):
        durata_media = 20  # durata media di una partita
        ritardo_membro = 3  # ritardo per ogni membro del gruppo

        idGruppo = ControllorePartita().ricercaIdGruppoPerPista(ControllorePista(pista).getId())
        gruppo = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
        partita = ControllorePartita().ricercaPartitaIdGruppo(idGruppo)
        if ControllorePartita(partita).getOraInizio() is not None:
            dataInizioPartita = ControllorePartita(partita).getOraInizio()

            numPartite = ControlloreGruppoClienti(gruppo).getNumeroPartite()
            numMembri = len(ControlloreGruppoClienti(gruppo).getMembri())
            tempoDiAttesa = numPartite * durata_media + numMembri * ritardo_membro

            data_e_ora_corrente = datetime.now()
            nuova_data_e_ora = dataInizioPartita + timedelta(minutes=tempoDiAttesa)
            if nuova_data_e_ora > data_e_ora_corrente:
                differenza_in_secondi = (nuova_data_e_ora - data_e_ora_corrente).total_seconds()
                differenza_in_minuti = int(differenza_in_secondi / 60)
                return str(differenza_in_minuti) + " minuti"
            else:
                return str(0) + " minuti"
        else:
            return "Partita non ancora iniziata"