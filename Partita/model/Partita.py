from datetime import datetime, timedelta
import os
import pickle
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti

#va creata una partita con gruppo clienti e pista collegati, va aggiornato anche il cliente abbonato, sia la data di validazione dell'abbonamento se è la sua prima partita, sia le sue partite gratuite rimanenti
#L'idPartita è inutile se ogni gruppo può partecipare a una sola partita
class Partita:
    def __init__(self):
        self.idGruppo = ControlloreGruppoClienti
        self.idPista = ""
        self.oraInizio = datetime.now().strftime('%H:%M')
        timedeltaAggiuntivo = self.calcolaTempiAttesa()
        self.oraFine = self.oraInizio + timedeltaAggiuntivo


    def setOraInizio(self, ora):
        self.oraInizio = ora
    def setOraFine(self, ora):
        self.oraFine = ora
    def getOraInizio(self):
        return self.oraInizio
    def getOraFine(self):
        return self.oraFine
    def getIdGruppo(self):
        return self.idGruppo
    def getIdPista(self):
        return self.idPista

    # metodo chiamato appena vengono assegnate tutte le scarpe
    def creaPartita(self, oraInizio, oraFine, idGruppo, idPista):
        self.oraFine = oraFine

        secondiDaAggiungere = 10 * numeroPartite
        # Creare un oggetto timedelta con i secondi specificati
        delta = timedelta(seconds=secondiDaAggiungere)
        # Sommare il timedelta all'ora corrente
        self.oraInizio = self.oraFin + delta

        with open('Partita/data/partite.pickle', "rb") as f:
            partite = pickle.load(f)
        partite.append(self)
        with open('Partita/data/partite.pickle', "wb") as f:
            pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)
        return self



    def calcolaTempiAttesa(self):
        GruppoClienti = ControlloreGruppoClienti()

    def rimuoviPartita(self):
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
                daRimuovere = next((partita for partita in partite if partite.id == self.id), None)
                partite.remove(daRimuovere)
            with open('Partita/data/partite.pickle', 'wb') as f:
                pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)
        del self
