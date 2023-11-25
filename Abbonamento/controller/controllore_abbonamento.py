class controllereAbbonamento():
    def __init__(self, abbonamento):
        self.model = abbonamento
    def getDataFine(self):
        return self.model.dataFine
    def getDataValidazione(self):
        return self.model.dataValidazione
    def getId(self):
        return self.model.id
    def getPartiteGratuite(self):
        return self.model.partiteGratuite