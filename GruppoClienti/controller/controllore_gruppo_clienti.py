import os
import pickle

from GruppoClienti.model.GruppoClienti import GruppoClienti


class ControlloreGruppoClienti():
    def __init__(self, gruppoClienti=None):
        self.model = gruppoClienti

    def getId(self):
        return self.model.getId()

    def getMembri(self):
        return self.model.getMembri()

    def getCounterPartito(self):
        return self.model.getCounterPartito()

    def setCounterPartito(self, id, bool):
        self.model.setCounterPartito(id, bool)

    def getNumeroPartite(self):
        return self.model.getNumeroPartite()

    def getPistaOccupata(self):
        return self.model.getPistaOccupata()

    def modificaGruppoClienti(self, id, nuovoMembri, nuovoNumeroPartite, nuovoPistaOccupata):
        GruppoClienti().modificaGruppoClienti(id=id,
                                              nuovoMembri=nuovoMembri,
                                              nuovoNumeroPartite=nuovoNumeroPartite,
                                              nuovoPistaOccupata=nuovoPistaOccupata
                                              )
        return True

    def rimuoviGruppo(self, id):
        if isinstance(self.model, GruppoClienti):
            self.model.rimuoviGruppoClienti(id)
            return True
        else:
            return False

    def getGruppo(self):
        return self.model.getGruppo()

    def visualizzaGruppi(self):
        return GruppoClienti().getGruppoClienti()

    def ricercaGruppoId(self, id):
        gruppi = []
        if os.path.isfile('GruppoClienti/data/GruppoClienti.pickle'):
            with open('GruppoClienti/data/GruppoClienti.pickle', 'rb') as f:
                gruppi = pickle.load(f)
        if len(gruppi) > 0:
            for gruppo in gruppi:
                if gruppo.id == id:
                    return gruppo
        else:
            return None

    def creaGruppoClienti(self, id, membri, numeroPartite, counterPartito):
        gruppo = self.ricercaGruppoId(id)
        if isinstance(gruppo, GruppoClienti):
            return None
        else:
            nuovoGruppoclienti = GruppoClienti().creaGruppoClienti(
                id=id,
                membri=membri,
                numeroPartite=numeroPartite,
                counterPartito=counterPartito
            )

        return nuovoGruppoclienti
