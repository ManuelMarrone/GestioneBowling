import time
import os
import pickle
idIncrementale = 0
class Abbonamento():

    idIncrementale = 0
    id_disponibili = set()
    def __init__(self):
        self.dataFine = ""
        self.dataValidazione = ""
        self.id = ""
        self.pagamentoRidotto = ""
        self.partiteGratuite = ""

    def get_id(self):
        return self.id

    def creaId(self):
        # Riutilizzo degli id delle istanze cancellate
        if Abbonamento.id_disponibili:  # Se ci sono ID disponibili nell'insieme
            self.id = Abbonamento.id_disponibili.pop()  # Prendi un ID disponibile
        else:
            Abbonamento.idIncrementale += 1
            self.id = Abbonamento.idIncrementale

        return self.id
    def creaAbbonamento(self, dataFine, dataValidazione, id, pagamentoRidotto, partiteGratuite):
        self.dataFine = dataFine
        self.dataValidazione = dataValidazione
        self.id = self.creaId()
        self.pagamentoRidotto = False
        self.partiteGratuite = 15
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', "rb") as f:
                abbonamenti = pickle.load(f)
            abbonamenti.append(self)
            with open('Abbonamento/data/ListaAbbonamenti.pickle', "wb") as f:
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
        return self
#MODIFICARE QUI SOTTO I PATH
    def rimuoviAbbonamento(self):
        Abbonamento.id_disponibili.add(self.id)  # Aggiungi l'ID dell'istanza eliminata agli ID disponibili
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                daRimuovere = next((cliente for cliente in clienti if cliente.id == self.id), None)
                clienti.remove(daRimuovere)
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        del self

    def is_PagamentoRidotto(self):
        return self.pagamentoRidotto
    def scadenzaAbbonamento(self):
        timestamp = int(time.time())
        return timestamp > self.dataFine
    def verificaPartiteMassime(self):
        return self.partiteGratuite > 0
    #SE QUESTO METODO RITORNA FALSE ALLORA BISOGNA IMPOSTARE IL PAGAMENTO RIDOTTO A TRUE

