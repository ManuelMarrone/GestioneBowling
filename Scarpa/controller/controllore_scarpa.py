import os
import pickle

from Scarpa.model.Scarpa import Scarpa


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
        return self.model.id

    def getDisponibilitaScarpa(self):
        return self.model.disponibilita

    def getTagliaScarpa(self):
        return self.model.taglia

    def ricercaScarpaTaglia(self, taglia):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
        if len(scarpe) > 0:
            for scarpa in scarpe:
                if scarpa.taglia == taglia:
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
                if scarpa.id == id:
                    return scarpa
        else:
            return None

    def getScarpa(self):
        return self.model.getScarpa()

    def visualizzaScarpe(self):
        return Scarpa().getScarpe()

    def setDisponibilitaScarpa(self, bool):
        self.model.setDisponibilitaScarpa(bool)
        #aggiungi modifica nel pickle

    def assegnaScarpa(self, cliente):
        self.model.setDisponibilitaScarpa(False) #rendiamo la scarpa non più disponibile
        #far scorrere i gruppi di clienti e cercare al loro interno i clienti partecipanti
        #appena trovo corrispondenza con cliente
        #associa dentro data di gruppiClienti l'id della scarpa al gruppo trovato
        #quando si andrà ad eliminare il gruppo di Clienti si fa una ricerca della scarpa
        #in base all'id per poter settare nuovamente la disponibilità a True