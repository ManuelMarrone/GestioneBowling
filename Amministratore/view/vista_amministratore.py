from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic
from PyQt6.QtWidgets import *

from Amministratore.view.vista_gestione_dipendenti import VistaGestioneDipendenti
from Statistiche.controller.controllore_statistiche import ControlloreStatistiche

"from Statistiche.controller.controllore_statistiche import ControlloreStatistiche"

class VistaAmministratore(QWidget):
    closed = pyqtSignal()
    def __init__(self, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        uic.loadUi('Amministratore/view/amministratoreMain.ui', self)

        # Ottieni le dimensioni dello schermo principale
        desktop = QApplication.primaryScreen().geometry()

        # Imposta il posizionamento al centro dello schermo
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2-50
        self.move(x, y)

        self.gestioneDipendentiButton.clicked.connect(self.goDipendenti)
        self.esciButton.clicked.connect(self.chiudiFinestra)

        self.resetComboBox()
        self.statComboBox.activated.connect(self.statistiche)

    def statistiche(self):
        selezione = self.statComboBox.currentText()
        if selezione == "":
            self.etichetta1.setText("")
            self.testo1.setText("")
            self.etichetta2.setText("")
            self.testo2.setText("")
            self.etichetta3.setText("")
            self.testo3.setText("")
            self.etichetta4.setText("")
            self.testo4.setText("")
            self.etichetta5.setText("")
            self.testo5.setText("")
            self.etichetta6.setText("")
            self.testo6.setText("")
            self.etichetta7.setText("")
            self.testo7.setText("")
        if selezione == "Dipendenti":
            etaMediaDipendenti,totDipendenti = ControlloreStatistiche().etaMediaDipendenti()
            percCassieri,percMagazzinieri = ControlloreStatistiche().percRuoliDipendenti()
            percUomo,percDonna,percAltro = ControlloreStatistiche().percSessoDipendenti()
            self.etichetta1.setText("Totale dipendenti: ")
            self.testo1.setText(str(totDipendenti))
            self.etichetta2.setText("Età media: ")
            self.testo2.setText(str(etaMediaDipendenti)+" anni")
            self.etichetta3.setText("Percentuale di cassieri: ")
            self.testo3.setText(str(percCassieri) + "%")
            self.etichetta4.setText("Percentuale di magazzinieri: ")
            self.testo4.setText(str(percMagazzinieri) + "%")
            self.etichetta5.setText("Percentuale di donne")
            self.testo5.setText(str(percDonna) + "%")
            self.etichetta6.setText("Percentuale di uomini")
            self.testo6.setText(str(percUomo) + "%")
            self.etichetta7.setText("Percentuale di altro")
            self.testo7.setText(str(percAltro) + "%")
        if selezione == "Clienti":
            percAbbonati,clientiTot = ControlloreStatistiche().percClientiAbbonati()
            tagliaPiuFrequente, numeroOccorrenze = ControlloreStatistiche().statisticaTaglieScarpe()
            percClientiUomo, percClientiDonna, percClientiAltro = ControlloreStatistiche().percSessoClienti()
            self.etichetta1.setText("Totale clienti: ")
            self.testo1.setText(str(clientiTot))
            self.etichetta2.setText("Percentuale di abbonati: ")
            self.testo2.setText(str(percAbbonati) + "%")
            self.etichetta3.setText("Taglia di scarpe più richiesta: ")
            self.testo3.setText(str(tagliaPiuFrequente))
            self.etichetta4.setText("Richiesta: ")
            self.testo4.setText(str(numeroOccorrenze) + " volte")
            self.etichetta5.setText("Percentuale di donne")
            self.testo5.setText(str(percClientiDonna) + "%")
            self.etichetta6.setText("Percentuale di uomini")
            self.testo6.setText(str(percClientiUomo) + "%")
            self.etichetta7.setText("Percentuale di altro")
            self.testo7.setText(str(percClientiAltro) + "%")
        if selezione == "Abbonamenti":
            numeroAbbonamentiAttivi = ControlloreStatistiche().numeroAbbonamentiAttivi()
            clientiSenzaPartiteGratuite = ControlloreStatistiche().clientiSenzaPartiteGratutite()
            clientiConPartiteGratuite = numeroAbbonamentiAttivi - clientiSenzaPartiteGratuite
            mediaPartiteDaGiocare = ControlloreStatistiche().mediaPartiteGratuite()
            dataPrimoAbbonamento = ControlloreStatistiche().dataPrimoAbbonamento()

            self.etichetta1.setText("Abbonamenti attivi: ")
            self.testo1.setText(str(numeroAbbonamentiAttivi))
            self.etichetta2.setText("Clienti con partite gratuite terminate: ")
            self.testo2.setText(str(clientiSenzaPartiteGratuite))
            self.etichetta3.setText("Clienti con delle partite gratuite da giocare: ")
            self.testo3.setText(str(clientiConPartiteGratuite))
            self.etichetta4.setText("Media delle partite gratuite rimanenti: ")
            self.testo4.setText(str(mediaPartiteDaGiocare))
            self.etichetta5.setText("Data del primo abbonamento effettuato: ")
            self.testo5.setText(str(dataPrimoAbbonamento))
            self.etichetta6.setText("")
            self.testo6.setText("")
            self.etichetta7.setText("")
            self.testo7.setText("")
        if selezione == "Ricevute":
            numeroRicevute = ControlloreStatistiche().numeroRicevute()
            percAbbonamenti,percPartite = ControlloreStatistiche().percAbbonamentiPartite()
            incasso = ControlloreStatistiche().incasso()

            self.etichetta1.setText("Numero di ricevute: ")
            self.testo1.setText(str(numeroRicevute))
            self.etichetta2.setText("Percentuale di ricevute per abbonamenti: ")
            self.testo2.setText(str(percAbbonamenti)+"%")
            self.etichetta3.setText("Percentuale di ricevute per partite: ")
            self.testo3.setText(str(percPartite)+"%")
            self.etichetta4.setText("Somma degli incassi: ")
            self.testo4.setText(str(incasso) + "€")
            self.etichetta5.setText("")
            self.testo5.setText("")
            self.etichetta6.setText("")
            self.testo6.setText("")
            self.etichetta7.setText("")
            self.testo7.setText("")

        if selezione == "Partite":
            numeroPartite = ControlloreStatistiche().partiteAttive()
            data = ControlloreStatistiche().primaPartita()

            self.etichetta1.setText("Numero totale di partite all'attivo: ")
            self.testo1.setText(str(numeroPartite))
            self.etichetta2.setText("Prima partita creata presente nel database: ")
            self.testo2.setText(str(data))
            self.etichetta3.setText("")
            self.testo3.setText("")
            self.etichetta4.setText("")
            self.testo4.setText("")
            self.etichetta5.setText("")
            self.testo5.setText("")
            self.etichetta6.setText("")
            self.testo6.setText("")
            self.etichetta7.setText("")
            self.testo7.setText("")

    def goDipendenti(self):
        VistaAmministratore.close(self)
        self.vista_gestione_dipendenti = VistaGestioneDipendenti()
        self.vista_gestione_dipendenti.closed.connect(self.show)
        self.vista_gestione_dipendenti.closed.connect(self.resetComboBox)
        self.vista_gestione_dipendenti.show()

    def resetComboBox(self):
        self.statComboBox.setCurrentIndex(0)
        self.statistiche()
    def chiudiFinestra(self):
        self.closed.emit()
        self.close()

