import os
import pickle
from Abbonamento.model.Abbonamento import Abbonamento
import schedule
import time
from threading import Thread
from datetime import datetime
from Cliente.controller.controllore_cliente import ControlloreCliente
class ControlloreAbbonamento():
    def __init__(self, abbonamento=None):
        self.model = abbonamento

        # Pianifica l'avvio del controllo delle scadenze ogni giorno alle 00:00
        schedule.every().day.at("22:09").do(self.controllo_scadenze)

        # Thread per eseguire la pianificazione in background
        self.thread_schedule = Thread(target=self.schedule_thread)
        self.thread_schedule.start()

    def controllo_scadenze(self):
        print("il controllo viene richiamato")
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
        if len(abbonamenti) > 0:
            data_corrente = datetime.now()
            for abbonamento in abbonamenti:
                print(abbonamento.getDataFine()," > ", data_corrente.strftime("%Y-%m-%d %H:%M"))
                if abbonamento.getDataFine() >= data_corrente.strftime("%Y-%m-%d %H:%M"):
                    self.rimuoviAbbonamento(abbonamento)
                    print(abbonamento.cfCliente)

    def schedule_thread(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def getDataFine(self):
        return self.model.getDataFine()
    def getDataValidazione(self):
        return self.model.getDataValidazione()
    def getPartiteGratuite(self):
        return self.model.getPartiteGratuite()
    def getPagamentoRidotto(self):
        return self.model.getPagamentoRidotto()
    def getCfCliente(self):
        return self.model.getCfCliente()
    def creaAbbonamento(self, dataFine, dataValidazione, partiteGratuite, pagamentoRidotto, cfCliente):
        abbonamento = self.ricercaAbbonamentoCfCliente(cfCliente)
        if isinstance(abbonamento, Abbonamento):  # se l'abbonamento già esiste
            return None
        else:
            nuovoAbbonamento = Abbonamento().creaAbbonamento(
              dataFine=dataFine,
              dataValidazione=dataValidazione,
              partiteGratuite=partiteGratuite,
              pagamentoRidotto=pagamentoRidotto,
              cfCliente=cfCliente
             )

        return nuovoAbbonamento
    def ricercaAbbonamentoCfCliente(self, cf):
        abbonamenti = []
        if os.path.isfile('Abbonamento/data/ListaAbbonamenti.pickle'):
            with open('Abbonamento/data/ListaAbbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
        if len(abbonamenti) > 0:
            for abbonamento in abbonamenti:
                if abbonamento.getCfCliente() == cf:
                    return abbonamento
        else:
            return None

    def rimuoviAbbonamento(self, abbonamento):
        if isinstance(abbonamento, Abbonamento):
            abbonamento.rimuoviAbbonamento()
            ControlloreCliente().setAbbonato(abbonamento.cfCliente, val=False)
            return True
        else:
            return False