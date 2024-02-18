import os
import pickle

from Cliente.controller.controllore_cliente import ControlloreCliente
from Scarpa.model.Scarpa import Scarpa
from GruppoClienti.controller.controllore_gruppo_clienti import ControlloreGruppoClienti


class ControlloreScarpa():
    def __init__(self, scarpa=None):
        self.model = scarpa

    def creaScarpa(self, disponibilita, id, taglia):
        nuovaScarpa = Scarpa().creaScarpa(
            disponibilita=disponibilita,
            id=id,
            taglia=taglia,
             )

        return nuovaScarpa

    def getIdScarpa(self):
        return self.model.getIdScarpa()

    def getDisponibilitaScarpa(self):
        return self.model.getDisponibilitaScarpa()

    def getTagliaScarpa(self):
        return self.model.getTaglia()


    def ricercaScarpaId(self, id):
        scarpe = []
        if os.path.isfile('Scarpa/data/scarpe.pickle'):
            with open('Scarpa/data/scarpe.pickle', 'rb') as f:
                scarpe = pickle.load(f)
        if len(scarpe) > 0:
            for scarpa in scarpe:
                if str(scarpa.getIdScarpa()) == id:
                    return scarpa
            return None
        else:
            return None

    def getScarpa(self):
        return self.model.getScarpa()

    def visualizzaScarpe(self):
        return Scarpa().getScarpe()

    def setDisponibilitaScarpa(self, bool, id):
        self.model.setDisponibilitaScarpa(bool, id)

    #torna False se la scarpa selezionata non corrisponde con la taglia richiesta dal cliente
    def assegnaScarpa(self,gruppoSelezionato, clienteSelezionato, idScarpa):

        if gruppoSelezionato is not None:
            #scorre i membri del gruppo
            for cliente in ControlloreGruppoClienti(gruppoSelezionato).getMembri():
                cf = cliente.split("codice fiscale: ")[1].strip()
                # se trovo corrispondenza con cliente al quale sto assegnando la scarpa
                if cf == clienteSelezionato.getCodiceFiscale():
                    #se la taglia della scarpa coincide con la richiesta
                    self.setDisponibilitaScarpa(False, idScarpa)  # rendiamo la scarpa non più disponibile
                    # associa dentro l'attributo del cliente l'id della scarpa
                    clienteIstanza = ControlloreCliente().ricercaClienteCodiceFiscale(cf)

                    cfCliente = ControlloreCliente(clienteIstanza).getCodiceFiscale()

                    ControlloreCliente(clienteIstanza).setIdScarpa(idScarpa, cfCliente)

                    return True
        return False

    def controllaTaglia(self, taglia, clienteSelezionato):
        if clienteSelezionato.getTagliaScarpe() == taglia:
            return True
        else:
            return False


