class ControlloreScarpa():
    def __init__(self, scarpa):
        self.model = scarpa

    def getIdScarpa(self):
        return self.model.id

    def getTagliaScarpa(self):
        return self.model.taglia

    def getDisponibilitaScarpa(self):
        return self.model.disponibilita