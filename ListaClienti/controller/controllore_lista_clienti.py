from ListaClienti.model.ListaClienti import ListaClienti
class ControllerListaClienti():
    def __init__(self):
        self.model = ListaClienti()
    def getListaClienti(self):
        return self.model.getListaClienti()
    def getClienteByIndex(self, index):
        return self.model.getClienteByIndex(index)
    def saveData(self):
        self.model.saveData()