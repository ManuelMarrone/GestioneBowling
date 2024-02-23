from Amministratore.model.Amministratore import Amministratore


class ControlloreAmministratore:
    def __init__(self, amministratore=None):
        self.model = amministratore

    def getEmail(self):
        return self.model.getEmail()

    def getPassword(self):
        return self.model.getPassword()

    def getAmministratore(self):
        return Amministratore().getAmministratore()
