import time
class Abbonamento():
    def __int__(self, dataFine, dataValidazione, id, pagamentoRidotto, partiteGratuite):
        self.dataFine = dataFine
        self.dataValidazione = dataValidazione
        self.id = id
        self.pagamentoRidotto = False
        self.partiteGratuite = 15

    def is_PagamentoRidotto(self):
        return self.pagamentoRidotto
    def scadenzaAbbonamento(self):
        timestamp = int(time.time())
        return timestamp > self.dataFine
    def verificaPartiteMassime(self):
        return self.partiteGratuite > 0
    #SE QUESTO METODO RITORNA FALSE ALLORA BISOGNA IMPOSTARE IL PAGAMENTO RIDOTTO A TRUE

