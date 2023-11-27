import json

from Cliente.model import Cliente


class ControllerCliente():
    def __init__(self):
        self.model = Cliente

    def carica_clienti_da_file(self, file_path):
        with open(file_path, 'rb') as file:
            dati_clienti = json.load(file)

        clienti = []
        for dati_cliente in dati_clienti:
            cliente = Cliente(**dati_cliente)
            clienti.append(cliente)

        return clienti

# esempio di utilizzo:


controller_cliente = ControllerCliente()
file_path = 'C:\Users\matte\OneDrive\Desktop\Unilif3\Ingegneria Del Software\Gestione Bowling\Cliente\Data\dati_cliente.json'
clienti_caricati = controller_cliente.carica_clienti_da_file(file_path)
