import os
import pickle

from Partita.model.Partita import Partita


class ControllorePartita():

    def __init__(self, partita = None):
        self.model = partita

    def setOraInizio(self, ora):
        self.model.setOraInizio(ora)

    def setOraFine(self, ora):
        self.model.setOraFine(ora)

    def getOraInizio(self):
        return self.model.getOraInizio()

    def getOraFine(self):
        return self.model.getOraFine()

    # metodo chiamato da vistaMagazziniere appena vengono assegnate tutte le scarpe
    #per ora si trova nella riga 221 di vista_magazziniere
    def creaPartita(self, gruppoDaAssegnare):
        return self.model.creaPartita(gruppoDaAssegnare)


    #metodo richiamato ciclicamente sul foreach di gruppi che hanno counterPartito == True
    def calcolaTempiAttesa(self):
        return self.model.calcolaTempiAttesa()

    def rimuoviPartita(self):
        self.model.rimuoviPartita()
