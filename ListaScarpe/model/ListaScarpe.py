import json
import pickle
import os.path
from Scarpa.model.Scarpa import Scarpa


class ListaScarpe():
    def __init__(self):
        self.lista_scarpe = []
        if os.path.isfile('ListaScarpe/data/lista_scarpe_salvata.pickle'):          #se esiste il file leggi la lista
            with open('ListaScarpe/data/lista_scarpe_salvata.pickle', 'rb') as f:
                self.lista_scarpe = pickle.load(f)
        else:                                                                       #se non esiste il file leggi la lista di scarpe inziale preinserita
            with open('ListaScarpe/data/lista_scarpe.json', 'r') as f:
                lista_scarpe = json.load(f)
                for scarpa in lista_scarpe:
                    self.aggiungiScarpa(
                        Scarpa(scarpa["id"],
                               scarpa["taglia"],
                               scarpa["disponibilita"]
                               )
                    )

    def aggiungiScarpa(self, scarpa):
        self.lista_scarpe.append(scarpa)

    def saveData(self):
        with open('lista_scarpe/data/lista_scarpe_salvata.pickle', 'wb') as handle: #a file handle indicates where data should be read or put into the file
            pickle.dump(self.lista_scarpe, handle, pickle.HIGHEST_PROTOCOL)