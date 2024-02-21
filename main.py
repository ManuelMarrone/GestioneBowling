#import os
import pprint
import pickle
import sys
from PyQt6.QtWidgets import QApplication

from Backup.controller.controller_backup import Backup
from Cliente.controller.controllore_cliente import ControlloreCliente
from Login.view.VistaLogin import VistaLogin
from Cliente.view.vista_lista_clienti import VistaGestioneClienti
from Pista.controller.controllore_pista import ControllorePista
from Scarpa.controller.controllore_scarpa import ControlloreScarpa
from GruppoClienti.model.GruppoClienti import GruppoClienti
from Dipendente.view.vista_cassiere import VistaCassiere
from Dipendente.view.vista_magazziniere import VistaMagazziniere

if __name__ == "__main__":

    # pista1 = ControllorePista().creaPista(
    #      disponibilita=True,
    #      id=1
    # )
    # pista2 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=2
    # )
    # pista3 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=3
    # )
    # pista4 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=4
    # )
    # pista5 = ControllorePista().creaPista(
    #     disponibilita=True,
    #     id=5
    # )
    # with open('Pista/data/piste.pickle', 'rb') as f:
    #     piste = pickle.load(f)
    #
    # print(piste)

    # with open('Pista/data/piste.pickle', 'wb') as f:
    #     pickle.dump([],f,pickle.HIGHEST_PROTOCOL)

    # app = QApplication(sys.argv)
    # vista_mag = VistaMagazziniere()
    # vista_mag.show()
    # sys.exit(app.exec())

    # app = QApplication(sys.argv)
    # vista_cassiere = VistaCassiere()
    # vista_cassiere.show()
    # sys.exit(app.exec())


    app = QApplication(sys.argv)
    VistaLogin = VistaLogin()
    VistaLogin.show()
    sys.exit(app.exec())

    #SVUOTA I GRUPPI, LE PARTITE E RISETTA I CLIENTI A NON ASSEGNATI (FALSE)
    # with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
    #     pickle.dump([], f, pickle.HIGHEST_PROTOCOL)
    # with open('Partita/data/partite.pickle', 'wb') as f:
    #     pickle.dump([], f, pickle.HIGHEST_PROTOCOL)
    # for cliente in ControlloreCliente().visualizzaClienti():
    #     print(ControlloreCliente(cliente).getCodiceFiscale(), "Settato")
    #     ControlloreCliente(cliente).setAssegnato(val=False)
    # for pista in ControllorePista().visualizzaPiste():
    #     print(ControllorePista(pista).getId(), "Libera")
    #     ControllorePista(pista).setDisponibilita(occupata=False)
    # with open('CodaPiste/data/codaPiste.pickle', 'wb') as f:
    #     pickle.dump([], f, pickle.HIGHEST_PROTOCOL)

    #RESET PICKLE DI CLIENTI E GRUPPO CLIENTI

    # with open('GruppoClienti/data/GruppoClienti.pickle', 'wb') as f:
    #     pickle.dump([],f,pickle.HIGHEST_PROTOCOL)
    #
    # with open('Cliente/data/ListaClienti.pickle', 'wb') as f:
    #     pickle.dump([],f,pickle.HIGHEST_PROTOCOL)
    #
    # with open('Abbonamento/data/ListaAbbonamenti.pickle', 'wb') as f:
    #     pickle.dump([],f,pickle.HIGHEST_PROTOCOL)

    #RESET RICEVUTE
    # with open('Ricevuta/data/ricevute.pickle', 'wb') as f:
    #   pickle.dump([],f,pickle.HIGHEST_PROTOCOL)
    #


    #RESET DISPONIBILITA SCARPE

    # with open('Scarpa/data/scarpe.pickle', 'rb') as f:
    #         scarpe = pickle.load(f)
    #         for scarpa in scarpe:
    #             scarpa.disponibilita=True
    #
    # with open('Scarpa/data/scarpe.pickle', 'wb') as f:
    #    pickle.dump(scarpe,f,pickle.HIGHEST_PROTOCOL)

    #RESET DISPONIBLITA PISTE

    # with open('Pista/data/piste.pickle', 'rb') as f:
    #     piste = pickle.load(f)
    #     for pista in piste:
    #        pista.disponibilita=False
    #
    # with open('Pista/data/piste.pickle', 'wb') as f:
    #    pickle.dump(piste,f,pickle.HIGHEST_PROTOCOL)

























