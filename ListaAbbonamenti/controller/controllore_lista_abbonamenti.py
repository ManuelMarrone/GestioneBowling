from ListaAbbonamenti.model.ListaAbbonamenti import ListaAbbonamenti
class ControllerListaAbbonamenti():
    def __init__(self):
        self.model = ListaAbbonamenti()
    def getListaAbbonamenti(self):
        return self.model.getListaAbbonamenti()
    def getAbbonamentoByIndex(self, index):
        return self.model.getAbbonamentoByIndex(index)
    def saveData(self):
        self.model.saveData()