import os
import pickle

from Ricevuta.model.Ricevuta import Ricevuta
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from Cliente.controller.controllore_cliente import ControlloreCliente
from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento


class ControlloreRicevuta():
    def __init__(self, ricevuta=None):
        self.model = ricevuta

    def getId(self):
        return self.model.getId()

    def getDataEmissione(self):
        return self.model.getDataEmissione()

    def getTipo(self):
        return self.model.getTipo()

    def getImporto(self):
        return self.model.getImporto()

    def getOraEmissione(self):
        return self.model.getOraEmissione()

    def getMembri(self):
        return self.model.getMembri()

    def calcolaImportoPartita(self, idGruppo):
        importo = 0.0
        gruppo = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
        numPartite = ControlloreGruppoClienti(gruppo).getNumeroPartite()
        for membro in ControlloreGruppoClienti(gruppo).getMembri():
            if ControlloreCliente(membro).getAbbonato() is False:
                importo += (5*numPartite)
            elif ControlloreCliente(membro).getAbbonato() is True:
                abbonamento = ControlloreAbbonamento().ricercaAbbonamentoCfCliente(
                    ControlloreCliente(membro).getCodiceFiscale())
                partiteDaPagare = ControlloreAbbonamento(abbonamento).getPartiteDaPagareAbbonamento()
                if partiteDaPagare > 0:
                    importo += 0
                    importo += (3*partiteDaPagare)
                else:
                    if ControlloreAbbonamento(abbonamento).getPagamentoRidotto() is False:
                        importo += 0
                    else:
                        importo += (3*numPartite)
        return importo



    def creaRicevuta(self, dataEmissione, id, importo, oraEmissione, membri, tipo):
        nuovaRicevuta = Ricevuta().creaRicevuta(
            dataEmissione=dataEmissione,
            id=id,  # preferibilimente lo stesso della classe partita
            importo=importo,
            oraEmissione=oraEmissione,
            membri=membri,
            tipo = tipo)

        return nuovaRicevuta

    def rimuoviRicevuta(self, ricevuta):
        if isinstance(ricevuta, Ricevuta):
            ricevuta.eliminaRicevuta()
            return True
        else:
            return False


    def ricercaRicevutaId(self, id):
        ricevute = []
        ricevuteCercate=[]
        if os.path.isfile('Ricevuta/data/ricevute.pickle'):
            with open('Ricevuta/data/ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        if len(ricevute) > 0:
            for ricevuta in ricevute:
                if ricevuta.id == id:
                    ricevuteCercate.append(ricevuta)
            if len(ricevuteCercate) > 0:
                return ricevuteCercate
            else:
                return None
        else:
            return None

    def ricercaRicevutaIdOra(self, id, ora):
        ricevute = []
        if os.path.isfile('Ricevuta/data/ricevute.pickle'):
            with open('Ricevuta/data/ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        if len(ricevute) > 0:
            for ricevuta in ricevute:
                oraFormat = (ricevuta.oraEmissione).strftime("%H:%M:%S")
                if ricevuta.id == id and oraFormat == ora:
                    return ricevuta
        else:
            return None

    def visualizzaRicevute(self):
        return Ricevuta().getRicevute()

