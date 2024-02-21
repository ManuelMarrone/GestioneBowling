import os
import pickle
from datetime import datetime
from collections import Counter

from PyQt6.QtWidgets import QMessageBox

from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Cliente.controller.controllore_cliente import ControlloreCliente
from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Partita.controller.controllore_partita import ControllorePartita
from Ricevuta.controller.controllore_ricevuta import ControlloreRicevuta


class ControlloreStatistiche():
    def __init__(self):
        self.dipendenti = []
        if os.path.isfile('Dipendente/data/dipendenti.pickle'):
            with open('Dipendente/data/dipendenti.pickle', 'rb') as f:
                self.dipendenti = pickle.load(f)

        self.clienti = []
        if os.path.isfile('Cliente/data/ListaCLienti.pickle'):
            with open('Cliente/data/ListaCLienti.pickle', 'rb') as f:
                self.clienti = pickle.load(f)

        self.abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                self.abbonamenti = pickle.load(f)

        self.ricevute = []
        if os.path.isfile('Ricevuta/data/ricevute.pickle'):
            with open('Ricevuta/data/ricevute.pickle', 'rb') as f:
                self.ricevute = pickle.load(f)

        self.partite = []
        if os.path.isfile('Partita/data/partite.pickle'):
            with open('Partita/data/partite.pickle', 'rb') as f:
                self.partite = pickle.load(f)




    #statistiche sui dipendenti
    def etaMediaDipendenti(self):
        if len(self.dipendenti) > 0:
            self.oggi = datetime.now()
            etaTot = 0
            for dipendente in self.dipendenti:
                data = datetime.strptime(ControlloreDipendente(dipendente).getDataNascita(), '%d-%m-%Y')

                eta = self.oggi.year - data.date().year - (
                            (self.oggi.month, self.oggi.day) < (
                data.date().month, data.date().day))
                etaTot += eta
            etaMedia = etaTot / len(self.dipendenti)
            return int(etaMedia),len(self.dipendenti)
        else:
            return 0,0

    def percRuoliDipendenti(self):
        #%di cassieri e % di magazzinieri
        if len(self.dipendenti) > 0:
            contCas = 0
            contMag = 0
            for dipendente in self.dipendenti:
               if( ControlloreDipendente(dipendente).getRuolo()=="Cassiere"):
                  contCas += 1
               else:
                  contMag += 1
            percCassieri = (contCas/len(self.dipendenti))*100
            percMagazzinieri = (contMag/len(self.dipendenti))*100
            percMagazzinieri = round(percMagazzinieri, 2)
            percCassieri = round(percCassieri, 2)
            return percCassieri,percMagazzinieri
        else:
            return 0,0

    def percSessoDipendenti(self):
        #%maschi e femmine
        if len(self.dipendenti) > 0:
            contM = 0
            contF = 0
            contAltro = 0

            for dipendente in self.dipendenti:
                if ( ControlloreDipendente(dipendente).getSesso() == "Uomo"):
                    contM += 1
                elif(ControlloreDipendente(dipendente).getSesso() == "Donna"):
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
        else:
            return 0,0,0

    #statistiche sui clienti
    def percClientiAbbonati(self):
        #% di abbonati
        if len(self.clienti) > 0:
            contAbbonati = 0
            for cliente in self.clienti:
                if (ControlloreCliente(cliente).getAbbonato() == True):
                    contAbbonati += 1
            percAbbonati = (contAbbonati / len(self.clienti)) * 100
            percAbbonati = round(percAbbonati, 2)
            return percAbbonati,len(self.clienti)
        else:
            return 0,0

    def statisticaTaglieScarpe(self):
        #taglie di scarpe più richieste
        if len(self.clienti) > 0:
            taglie = []
            for cliente in self.clienti:
                taglie.append(ControlloreCliente(cliente).getTagliaScarpe())
            conteggioTaglie = Counter(taglie)
            tagliaPiuFrequente, numeroOccorrenze = conteggioTaglie.most_common(1)[0]
            return tagliaPiuFrequente,numeroOccorrenze
        else:
            return 0,0

    def percSessoClienti(self):
        # %maschi e femmine
        if len(self.clienti) > 0:
            contM = 0
            contF = 0
            contAltro = 0

            for cliente in self.clienti:
                if (ControlloreCliente(cliente).getSesso() == "Uomo"):
                    contM += 1
                elif (ControlloreCliente(cliente).getSesso() == "Donna"):
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
        else:
            return 0,0,0

    #statistiche sugli abbonamenti
    #attributi a disposizione: dataFine, dataValidazione tipo datetime
    #pagamentoRidotto:bool, partiteGratuite: int, cfCliente
    def numeroAbbonamentiAttivi(self):
        return len(self.abbonamenti)

    def clientiSenzaPartiteGratutite(self):
        if len(self.abbonamenti) > 0:
            contatore = 0
            for abbonamento in self.abbonamenti:
                if ControlloreAbbonamento(abbonamento).getPartiteGratuite() == 0:
                    contatore += 1
            return contatore
        else:
            return 0

    def mediaPartiteGratuite(self):
        if len(self.abbonamenti) > 0:
            somma = 0
            for abbonamento in self.abbonamenti:
                somma += ControlloreAbbonamento(abbonamento).getPartiteGratuite()
            media = somma/len(self.abbonamenti)
            return media
        else:
            return 0

    def dataPrimoAbbonamento(self):
        if len(self.abbonamenti) > 0:
            date = []
            for abbonamento in self.abbonamenti:
                date.append((ControlloreAbbonamento(abbonamento).getDataValidazione()))
            return min(date)
        else:
            return 0

    #numero ricevute
    def numeroRicevute(self):
        return len(self.ricevute)
    #percentuale di abbonamenti
    def percAbbonamentiPartite(self):
        if len(self.abbonamenti) > 0:
            # %maschi e femmine
            contAbbonamenti = 0
            contPartite = 0

            if len(self.ricevute) > 0:
                for ricevuta in self.ricevute:
                    if (ControlloreRicevuta(ricevuta).getTipo() == "Abbonamento"):
                        contAbbonamenti += 1
                    elif (ControlloreRicevuta(ricevuta).getTipo() == "Partita"):
                        contPartite += 1

            percAbbonamenti = (contAbbonamenti / len(self.ricevute)) * 100
            percPartite = (contPartite / len(self.ricevute)) * 100

            percAbbonamenti = round(percAbbonamenti, 2)
            percPartite = round(percPartite, 2)

            return percAbbonamenti, percPartite
        else:
            return 0,0

    #incasso totale
    def incasso(self):
        if len(self.abbonamenti) > 0:
            incasso = 0
            if len(self.ricevute) > 0:
                for ricevuta in self.ricevute:
                    incasso += ControlloreRicevuta(ricevuta).getImporto()
            return incasso
        else:
            return 0


    #partite totali fatte
    def partiteAttive(self):
        return len(self.partite)

    #tempo medio di una partita
    def primaPartita(self):
        if len(self.partite) > 0:
            date = []
            for partita in self.partite:
                date.append((ControllorePartita(partita).getOraInizio()))
            return min(date).strftime("%H:%M:%S")
        else:
            return 0
