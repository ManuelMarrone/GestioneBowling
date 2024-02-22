import os
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
    #     ControlloreCliente(cliente).setAssegnato(val=False)
    # for pista in ControllorePista().visualizzaPiste():
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

























