import os
import pickle
idIncrementale = 0
class Cliente():
    def __init__(self):
        self.abbonato = ""
        self.codiceFiscale = ""
        self.id = ""
        self.cognome = ""
        self.email = ""
        self.nome = ""
        self.sesso = ""
        self.tagliaScarpe = ""
        self.assegnato = False

    class MyClass:
        idIncrementale = 0
        id_disponibili = set()

        def __init__(self):
            if MyClass.id_disponibili:  # Se ci sono ID disponibili nell'insieme
                self.id = MyClass.id_disponibili.pop()  # Prendi un ID disponibile
            else:
                MyClass.idIncrementale += 1
                self.id = MyClass.idIncrementale

        def delete_instance(self):
            MyClass.id_disponibili.add(self.id)  # Aggiungi l'ID dell'istanza eliminata agli ID disponibili
            # Qui puoi fare altre operazioni necessarie per eliminare l'istanza

        def get_id(self):
            return self.id

    def creaId(self, nome, cognome):
        global idIncrementale
        idIncrementale += 1
        idGenerato = nome[0:2] + cognome[0:2] + str(idIncrementale)
        return idGenerato

    def creaCliente(self, abbonato, codiceFiscale, cognome, email, nome, sesso, tagliaScarpe, assegnato):
        self.abbonato = abbonato
        self.codiceFiscale = codiceFiscale
        self.id = self.creaId(nome, cognome)
        self.cognome = cognome
        self.email = email
        self.nome = nome
        self.sesso = sesso
        self.tagliaScarpe = tagliaScarpe
        self.assegnato = assegnato
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', "rb") as f:
                clienti = pickle.load(f)
            clienti.append(self)
            with open('Cliente/data/ListaClienti.pickle', "wb") as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        return self

    def modificaCliente(self,id, nuovoAbbonato, nuovoCodiceFiscale, nuovoCognome, nuovaEmail, nuovoNome,
                        nuovoSesso, nuovaTagliaScarpe):
        self.abbonato = nuovoAbbonato
        self.codiceFiscale = nuovoCodiceFiscale
        self.cognome = nuovoCognome
        self.email = nuovaEmail
        self.nome = nuovoNome
        self.sesso = nuovoSesso
        self.tagliaScarpe = nuovaTagliaScarpe

        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if cliente.id == id), None)
                cliente.abbonato = nuovoAbbonato
                cliente.codiceFiscale = nuovoCodiceFiscale
                cliente.cognome = nuovoCognome
                cliente.email = nuovaEmail
                cliente.nome = nuovoNome
                cliente.sesso = nuovoSesso
                cliente.tagliaScarpe = nuovaTagliaScarpe
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:  # se ti sovrascriverà cambia wb con ab
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviCliente(self):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                daRimuovere = next((cliente for cliente in clienti if cliente.id == self.id), None)
                clienti.remove(daRimuovere)
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:  # riscrive i cassieri sena l'eliminato
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        del self

    def isAbbbonato(self):
        return self.abbonato

    def getNome(self):
        return self.nome

    def getCliente(self):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                return clienti[self.id]

    def getClienti(self):
        clienti = []
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                    clienti = pickle.load(f)
            return clienti
        else:
            return None


    def setAssegnato(self, x, id):
        if os.path.isfile('Cliente/data/ListaClienti.pickle'):
            with open('Cliente/data/ListaClienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                cliente = next((cliente for cliente in clienti if cliente.id == id), None)
                cliente.assegnato = x
            with open('Cliente/data/ListaClienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return  "abbonato: " + self.abbonato + "\n" + \
                "Codice Fiscale: " + self.codiceFiscale + "\n" + \
                "Id: " + self.id + "\n" + \
                "Cognome: " + self.cognome + "\n" + \
                "Email: " + self.email + "\n" + \
                "Nome: " + self.nome + "\n" + \
                "Sesso: " + self.sesso + "\n" + \
                "Taglia Scarpe: " + self.tagliaScarpe + "\n" + \
                "assegnat: " + self.assegnato
