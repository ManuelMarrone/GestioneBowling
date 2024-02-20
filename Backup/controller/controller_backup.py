import pickle
import time

import schedule

from Abbonamento.controller.controllore_abbonamento import ControlloreAbbonamento
from Amministratore.controller.controllore_amministratore import ControlloreAmministratore
from Cliente.controller.controllore_cliente import ControlloreCliente
from Dipendente.controller.controllore_dipendente import ControlloreDipendente
from Partita.controller.controllore_partita import ControllorePartita
from Pista.controller.controllore_pista import ControllorePista
from Scarpa.controller.controllore_scarpa import ControlloreScarpa
from Ricevuta.controller.controllore_ricevuta import ControlloreRicevuta


class Backup:

    def __init__(self):
        self.gestoreAbbonamenti = ControlloreAbbonamento()
        self.gestoreAmministratore = ControlloreAmministratore()
        self.gestoreClienti = ControlloreCliente()
        self.gestoreDipendenti = ControlloreDipendente()
        self.gestorePartite = ControllorePartita()
        self.gestorePiste = ControllorePista()
        self.gestoreScarpe = ControlloreScarpa()
        self.gestoreRicevute = ControlloreRicevuta()

        self.backup_daily()

    def eseguiBackup(self):
        self.abbonamenti = self.gestoreAbbonamenti.visualizzaAbbonamenti()
        self.amministratore = self.gestoreAmministratore.getAmministratore()
        self.clienti = self.gestoreClienti.visualizzaClienti()
        self.dipendenti = self.gestoreDipendenti.visualizzaDipendenti()
        self.partite = self.gestorePartite
        self.piste = self.gestorePiste.visualizzaPiste()
        self.scarpe = self.gestoreScarpe.visualizzaScarpe()
        self.ricevute = self.gestoreRicevute.visualizzaRicevute()

        with open('Backup/data/backup.pickle', "wb") as f:
            pickle.dump((self.abbonamenti,
                            self.amministratore,
                            self.clienti,
                            self.dipendenti,
                            self.partite,
                            self.piste,
                            self.scarpe,
                            self.ricevute), f)
    def backup_daily(self):
        schedule.every().day.at("07:00").do(self.eseguiBackup)
        while True:
            schedule.run_pending()
            time.sleep(1)
