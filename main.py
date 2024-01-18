#import os
import pprint
import pickle
import sys
from PyQt6.QtWidgets import QApplication
from Login.view.VistaLogin import VistaLogin
#from Dipendente.view.vista_lista_clienti import VistaGestioneClienti
from Pista.controller.controllore_pista import ControllorePista
from Scarpa.controller.controllore_scarpa import ControlloreScarpa
from GruppoClienti.model.GruppoClienti import GruppoClienti

if __name__ == "__main__":

    """pista1 = ControllorePista().creaPista(
         disponibilita=False,
         id=1
    )
    pista2 = ControllorePista().creaPista(
         disponibilita=True,
         id=2
    )
    pista3 = ControllorePista().creaPista(
         disponibilita=False,
         id=3
    )
    pista4 = ControllorePista().creaPista(
         disponibilita=True,
         id=4
    )
    pista5 = ControllorePista().creaPista(
         disponibilita=False,
         id=5
    )
    piste = [pista1, pista2, pista3, pista4, pista5]

    with open('Pista/data/piste.pickle', 'wb') as file_pickle:
        pickle.dump(piste, file_pickle)

    with open('Pista/data/piste.pickle', 'rb') as file_pickle:
        piste_caricate = pickle.load(file_pickle)

    pprint.pprint(piste_caricate)"""
    #
    app = QApplication(sys.argv)
    VistaLogin = VistaLogin()
    VistaLogin.show()
    sys.exit(app.exec())
    #
    # with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
    #     pickle.dump([],f,pickle.HIGHEST_PROTOCOL)



    # with open('Scarpa/data/scarpe.pickle', 'rb') as f:
    #     scarpe = pickle.load(f)
    #     for scarpa in scarpe:
    #         scarpa.disponibilita=True
    #
    # with open('Scarpa/data/scarpe.pickle', 'wb') as f:
    #      pickle.dump(scarpe,f,pickle.HIGHEST_PROTOCOL)

    # app = QApplication(sys.argv)
    # vistaclienti = VistaGestioneClienti()
    # vistaclienti.show()
    # sys.exit(app.exec())

