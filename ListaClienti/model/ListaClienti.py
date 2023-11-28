import json
import pickle
import os.path

from Cliente.model.Cliente import Cliente

#FINIRE DI VEDERE TUTTO QUI SOTTO
class ListaClienti():
    def __init__(self):
        self.model = Cliente

    def carica_clienti_da_file(self, file_path):
        with open(file_path, 'r') as file:
            dati_clienti = json.load(file)

        clienti = []
        for dati_cliente in dati_clienti:
            cliente = Cliente(**dati_cliente)
            clienti.append(cliente)

        return clienti

# esempio di utilizzo:

controller_cliente = ListaClienti()
file_path = 'ListaClienti/data/dati_cliente.json'  #C:\Users\matte\OneDrive\Desktop\Unilif3\Ingegneria Del Software\Gestione Bowling\Cliente\Data\dati_cliente.json
clienti_caricati = controller_cliente.carica_clienti_da_file(file_path)