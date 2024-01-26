from datetime import datetime, timedelta
import os
import pickle
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti

class Partita:
    def __init__(self):
        self.id = ""
        self.oraFine = None
        self.oraInizio = None

    def setOraInizio(self, ora):
        self.oraInizio = ora

    def setOraFine(self, ora):
        self.oraFine = ora

    def getOraInizio(self):
        return self.oraInizio

    def getOraFine(self):
        return self.oraFine

    # metodo chiamato appena vengono assegnate tutte le scarpe
    def creaPartita(self, gruppoDaAssegnare):
        numeroPartite = ControlloreGruppoClienti(gruppoDaAssegnare).getNumeroPartite()
        self.id = ControlloreGruppoClienti(gruppoDaAssegnare).getId() #id della partita identico all'id del gruppo, sono id univoci
        self.oraFine = datetime.now().time()

        secondiDaAggiungere = 10 * numeroPartite
        # Creare un oggetto timedelta con i secondi specificati
        delta = timedelta(seconds=secondiDaAggiungere)
        # Sommare il timedelta all'ora corrente
        self.oraInizio = self.oraFine + delta

        with open('Partita/data/partite.pickle', "rb") as f:
            partite = pickle.load(f)
        partite.append(self)
        with open('Partita/data/partite.pickle', "wb") as f:
            pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)
        return self



    def calcolaTempiAttesa(self, gruppoGiocante):
        pass
        #in realtà il tempo di attesa di fine partita è già stato calcolato e si trova in
        #self.oraFine, il metodo calcolaTempiAttesa potrebbe essere inutile

    def rimuoviPartita(self):
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                partite = pickle.load(f)
                daRimuovere = next((partita for partita in partite if partite.id == self.id), None)
                partite.remove(daRimuovere)
            with open('Partita/data/partite.pickle', 'wb') as f:
                pickle.dump(partite, f, pickle.HIGHEST_PROTOCOL)
        del self
