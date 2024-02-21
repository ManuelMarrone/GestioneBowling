import os
import pickle

from CodaPiste.model.CodaPiste import CodaPiste
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti

class ControlloreCodaPiste():
    def __init__(self, codaGruppi=None):
        self.model = codaGruppi

    def getIdGruppo(self):
        return self.model.getIdGruppo()
    def getOraInizioCoda(self):
        return self.model.getOraInizioCoda()
    def aggiungiInCoda(self, idGruppo, oraInizioCoda):
        if ControlloreGruppoClienti().ricercaGruppoId(idGruppo) is not None:
            nuovoGruppoCoda = CodaPiste().aggiungiInCoda(
                idGruppo=idGruppo,
                oraInizioCoda=oraInizioCoda
            )
            return nuovoGruppoCoda
        else:
            return None
    def rimuoviDaCoda(self, id):
        CodaPiste().rimuoviDaCoda(id)
    def visualizzaGruppiCoda(self):
        return CodaPiste().visualizzaGruppiCoda()
    def ricercaGruppoInCoda(self, id):
        codaGruppi = []
        if os.path.isfile('CodaPiste/data/codaPiste.pickle'):
            with open('CodaPiste/data/codaPiste.pickle', 'rb') as f:
                codaGruppi = pickle.load(f)
        if len(codaGruppi) > 0:
            for gruppo in codaGruppi:
                if gruppo.idGruppo == id:
                    return gruppo
        else:
            return None


