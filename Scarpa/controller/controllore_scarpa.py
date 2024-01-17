import os
import pickle

from Cliente.controller.controllore_cliente import ControlloreCliente
from Scarpa.model.Scarpa import Scarpa
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti


class ControlloreScarpa():
    def __init__(self, scarpa=None):
        self.model = scarpa

    # def creaScarpa(self, disponibilita, id, taglia):
    #     nuovaScarpa = Scarpa().creaScarpa(
    #         disponibilita=disponibilita,
    #         id=id,
    #         taglia=taglia,
    #          )
    #
    #     return nuovaScarpa

    def getIdScarpa(self):
        return self.model.getIdScarpa()

    def getDisponibilitaScarpa(self):
        return self.model.getDisponibilitaScarpa()

    def getTagliaScarpa(self):
        return self.model.getTaglia()

    def ricercaScarpaTaglia(self, taglia):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
        if len(scarpe) > 0:
            for scarpa in scarpe:
                if scarpa.getTagliaScarpa() == taglia:
                    return scarpa
        else:
            return None

    def ricercaScarpaId(self, id):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
        if len(scarpe) > 0:
            for scarpa in scarpe:
                if scarpa.getIdScarpa() == id:
                    return scarpa
        else:
            return None

    def getScarpa(self):
        return self.model.getScarpa()

    def visualizzaScarpe(self):
        return Scarpa().getScarpe()

    def setDisponibilitaScarpa(self, bool, id):
        self.model.setDisponibilitaScarpa(bool, id)

    def assegnaScarpa(self,gruppoSelezionato, cliente, id):
        self.model.setDisponibilitaScarpa(False, id) #rendiamo la scarpa non più disponibile
        #far scorrere i gruppi di clienti e cercare al loro interno i clienti partecipanti
        if gruppoSelezionato is not None:
            for cliente in ControlloreGruppoClienti(gruppoSelezionato).getMembri():
                nome = cliente.split("nome: ")[1].split(",")[0].strip()
                cognome = cliente.split("cognome:")[1].split(",")[0].strip()
                if nome == cliente.getNome() and cognome == cliente.getCognome():
                    # appena trovo corrispondenza con cliente
                    # associa dentro data di gruppiClienti l'id della scarpa al gruppo trovato
                    pass#parte da rivedere, meglio associare un attributo

        #quando si andrà ad eliminare il gruppo di Clienti si fa una ricerca della scarpa
        #in base all'id per poter settare nuovamente la disponibilità a True