from ListaScarpe.model.ListaScarpe import ListaScarpe


class ControllerListaScarpe():

    def __init__(self):
        self.model = ListaScarpe()

    def saveData(self):
        self.model.saveData()
