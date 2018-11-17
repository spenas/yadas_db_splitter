from sys import stdin
import sys 
import csv



#clients array
clients = []
ides = []

#open output file
output = open("output.txt", "w+")


class Client:

    ide = 0
    name = ""
    city = ""
    zone = ""
    email = ""
    telephone = 0
    address = ""

    def __init__(self, ide, name, city, zone, email, telephone, addr):
        self.ide = ide
        self.name = name
        self.city = city
        self.zone = zone
        self.email = email
        self.telephone = telephone
        self.address = addr


def make_product(ide, name, city, zone, email, telephone, address):
    client = Client(ide, name, city, zone, email, telephone, address)
    return client

with open("nombres.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    cont= 0
    for row in reader:
        if cont != 0:
            if row["Terceros_Propiedades"] == "Cliente;":
                seq = (row["Primer_Nombre"],row["Segundo_Nombre"], row["Primer_Apellido"], row["Segundo_Apellido"])
                aux = " ".join(seq)    
                name_tot = aux.strip()
                city = row["Ciudad"]
                zone = row["ZonaUno"]
                ide = row["Terceros_Identificacion"]
                client = make_product(ide,name_tot, city, zone, "", "", "")
                clients.append(client)
                ides.append(ide)
        else:
            cont +=1

with open("detalles.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    cont = 0
    for row in reader:
        if cont != 0:
            if row["Identificacion"] in ides:
                clients[ides.index(row["Identificacion"])].telephone = row["Telefonos"]
                clients[ides.index(row["Identificacion"])].email = row["EMail"]
                clients[ides.index(row["Identificacion"])].address = row["Direccion"]
        else:
            cont += 1       

for i in clients:
    output.write("[" + i.ide + "," +  "'" + i.name + "'" + "," + "'" + i.city + "'" + "," + "'" + i.address + "'" + "," + "'" + i.zone + "'" + "," + i.telephone + "," + "'" + i.email + "'" +"]" + "," + "\n")    
