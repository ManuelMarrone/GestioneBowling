import os
import pickle
from datetime import datetime
from collections import Counter

from PyQt6.QtWidgets import QMessageBox


class ControlloreStatistiche():
    def __init__(self):
        self.dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                self.dipendenti = pickle.load(f)
        if len(self.dipendenti) == 0:
            self.messaggio(tipo=0, titolo="Statistiche dipendenti", mex="Errore nel calcolo delle statistiche!")

        self.clienti = []
        if os.path.isfile('Cliente/data/ListaCLienti.pickle'):
            with open('Cliente/data/ListaCLienti.pickle', 'rb') as f:
                self.clienti = pickle.load(f)
        if len(self.clienti) == 0:
            self.messaggio(tipo=0, titolo="Statistiche clienti", mex="Errore nel calcolo delle statistiche!")

        self.abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                self.abbonamenti = pickle.load(f)
        if len(self.abbonamenti) == 0:
            self.messaggio(tipo=0, titolo="Statistiche abbonamenti", mex="Errore nel calcolo delle statistiche!")


    #statistiche sui dipendenti
    def etaMediaDipendenti(self):
        self.oggi = datetime.now()
        etaTot = 0
        if len(self.dipendenti) > 0:
            for dipendente in self.dipendenti:
                eta = self.oggi.year - dipendente.dataNascita.date().year() - (
                            (self.oggi.month, self.oggi.day) < (
                dipendente.dataNascita.date().month(), dipendente.dataNascita.date().day()))
                etaTot += eta
        etaMedia = etaTot / len(self.dipendenti)
        return int(etaMedia),len(self.dipendenti)

    def percRuoliDipendenti(self):
        #%di cassieri e % di magazzinieri
        contCas = 0
        contMag = 0
        if len(self.dipendenti) > 0:
           for dipendente in self.dipendenti:
               if(dipendente.ruolo=="Cassiere"):
                  contCas += 1
               else:
                  contMag += 1
        percCassieri = (contCas/len(self.dipendenti))*100
        percMagazzinieri = (contMag/len(self.dipendenti))*100
        percMagazzinieri = round(percMagazzinieri, 2)
        percCassieri = round(percCassieri, 2)
        return percCassieri,percMagazzinieri

    def percSessoDipendenti(self):
        #%maschi e femmine
        contM = 0
        contF = 0
        contAltro = 0
        if len(self.dipendenti) > 0:
            for dipendente in self.dipendenti:
                if (dipendente.sesso == "Uomo"):
                    contM += 1
                elif(dipendente.sesso == "Donna"):
                    contF += 1
                else:
                    contAltro += 1
        percUomo = (contM / len(self.dipendenti)) * 100
        percDonna = (contF / len(self.dipendenti)) * 100
        percAltro = (contAltro / len(self.dipendenti)) * 100
        percUomo = round(percUomo, 2)
        percDonna = round(percDonna, 2)
        percAltro = round(percAltro, 2)
        return percUomo,percDonna,percAltro

    #statistiche sui clienti
    def percClientiAbbonati(self):
        #% di abbonati
        contAbbonati = 0
        for cliente in self.clienti:
            if (cliente.abbonato == True):
                contAbbonati += 1
        percAbbonati = (contAbbonati / len(self.clienti)) * 100
        percAbbonati = round(percAbbonati, 2)
        return percAbbonati,len(self.clienti)

    def statisticaTaglieScarpe(self):
        #taglie di scarpe più richieste
        taglie = []
        for cliente in self.clienti:
            taglie.append(cliente.tagliaScarpe)
        conteggioTaglie = Counter(taglie)
        tagliaPiuFrequente, numeroOccorrenze = conteggioTaglie.most_common(1)[0]
        return tagliaPiuFrequente,numeroOccorrenze

    def percSessoClienti(self):
        # %maschi e femmine
        contM = 0
        contF = 0
        contAltro = 0
        if len(self.clienti) > 0:
            for cliente in self.clienti:
                if (cliente.sesso == "Uomo"):
                    contM += 1
                elif (cliente.sesso == "Donna"):
                    contF += 1
                else:
                    contAltro += 1
        percUomo = (contM / len(self.clienti)) * 100
        percDonna = (contF / len(self.clienti)) * 100
        percAltro = (contAltro / len(self.clienti)) * 100
        percUomo = round(percUomo, 2)
        percDonna = round(percDonna, 2)
        percAltro = round(percAltro, 2)
        return percUomo, percDonna, percAltro

    #statistiche sugli abbonamenti
    #attributi a disposizione: dataFine, dataValidazione tipo datetime
    #pagamentoRidotto:bool, partiteGratuite: int, cfCliente
    def numeroAbbonamentiAttivi(self):
        return len(self.abbonamenti)

    def clientiSenzaPartiteGratutite(self):
        contatore = 0
        for abbonamento in self.abbonamenti:
            if abbonamento.getPartiteGratuite() == 0:
                contatore += 1
        return contatore

    def mediaPartiteGratuite(self):
        somma = 0
        for abbonamento in self.abbonamenti:
            somma += abbonamento.getPartiteGratuite()
        media = somma/len(self.abbonamenti)
        return media

    def dataPrimoAbbonamento(self):
        date = []
        for abbonamento in self.abbonamenti:
            date.append((abbonamento.getDataValidazione()))
        return min(date)

    def statisticheRicevute(self):
        pass

    def statistichePartite(self):
        pass
        #numero di partite medio fatte da gruppi di clienti
        #partite totali fatte
        #tempo medio di una partita

    def messaggio(self, tipo, titolo, mex):
        mexBox = QMessageBox()
        mexBox.setWindowTitle(titolo)
        if tipo == 0:
            mexBox.setIcon(QMessageBox.Icon.Warning)
        elif tipo == 1:
            mexBox.setIcon(QMessageBox.Icon.Information)
        mexBox.setStyleSheet("background-color: rgb(54, 54, 54); color: white;")
        mexBox.setText(mex)
        mexBox.exec()