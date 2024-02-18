from Amministratore.model.Amministratore import Amministratore


class ControlloreAmministratore:
    def __init__(self, amministratore=None):
        self.model = amministratore

    def getEmail(self):
        return self.model.email

    def getPassword(self):
        return self.model.password

    def getAmministratore(self):
        return Amministratore().getAmministratore()
