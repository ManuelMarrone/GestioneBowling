import os
import pickle

from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti
from Pista.controller.controllore_pista import ControllorePista


class CodaPiste():
    def __init__(self):
        self.idGruppo = ""
        self.oraInizioCoda = None

    def getIdGruppo(self):
        return self.idGruppo
    def getOraInizioCoda(self):
        return self.oraInizioCoda

    def aggiungiInCoda(self, idGruppo, oraInizioCoda):
        self.idGruppo = idGruppo
        self.oraInizioCoda = oraInizioCoda
        codaGruppi = []
        if os.path.isfile('CodaPiste/data/codaPiste.pickle'):
            with open('CodaPiste/data/codaPiste.pickle', "rb") as f:
                codaGruppi = pickle.load(f)
            codaGruppi.append(self)
            with open('CodaPiste/data/codaPiste.pickle', "wb") as f:
                pickle.dump(codaGruppi, f, pickle.HIGHEST_PROTOCOL)
        return self


    def rimuoviDaCoda(self, id):
        if os.path.isfile('CodaPiste/data/codaPiste.pickle'):
            with open('CodaPiste/data/codaPiste.pickle', 'rb') as f:
                codaGruppi = pickle.load(f)
                daRimuovere = next((Gruppo for Gruppo in codaGruppi if str(Gruppo.idGruppo) == str(id)), None)
                codaGruppi.remove(daRimuovere)
            with open('CodaPiste/data/codaPiste.pickle', 'wb') as f:
                pickle.dump(codaGruppi, f, pickle.HIGHEST_PROTOCOL)
        del self

    def visualizzaGruppiCoda(self):
        if os.path.isfile('CodaPiste/data/codaPiste.pickle'):
            with open('CodaPiste/data/codaPiste.pickle', 'rb') as f:
                self.codaGruppi = pickle.load(f)
            return self.codaGruppi

    # def liberaCoda(self, pista):
    #         self.codaGruppi = self.visualizzaElementi()
    #         if len(self.codaGruppi) != 0:
    #             for idGruppo in self.codaGruppi:
    #                 gruppo = ControlloreGruppoClienti().ricercaGruppoId(idGruppo)
    #
    #                 if ControllorePista(pista).getId() is not None:
    #                     if int(ControlloreGruppoClienti(gruppo)) == int(
    #                             ControlloreScarpa(scarpa).getTagliaScarpa()):
    #                         # se la scarpa liberata corrisponde con quella del cliente in coda allora procedi
    #                         # libera il cliente in coda
    #                         self.rimuoviDaCoda(clienteCoda)
    #                         self.setNotifica(True)