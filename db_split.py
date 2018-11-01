from sys import stdin
import json
#EXCEPTION MIQUNI IS VALID - TIPO FACET VS KOREA - TRIDON VS DIAMON - MATORCRAFT - JIU JIU - NEW ERA - AMERICAN EAGLE - AUTO BULB VEK TRA - MASTER POWER INJECTIONS
brands = ["HELLA" , "GAUGE", "T.BOSCH", "IFC", "HIBARI", "AHT", "NEWSUN" , "TORICA", "ICHIBAN", "FV", "FIC", "DT", "NPC", "YWK", "BOSCH", "SANKEI", "NARVA", "DIAMOND", "KOYO", "TOYOPOWER", "OSIS", "BTK", "AUTO BULB VEK TRA", "NAPCO", "SNR", "EXACT", "OSK", "RENAULT", "DODUCO", "AISAN", "TSK", "NAKAMOTO", "HERKO", "AIRTEX", "RIK", "VALEO", "TOTO", "FAE", "AWP", "RAON", "BISSC", "DEUSIC", "MOBIS", "GM", "EKKO", "LOCTITE", "MIQUINI", "JIU JIU", "BGF", "A1", "TP", "PERFECT", "BROSOL", "I&R", "SHIBUMI", "NEW ERA", "FACET", "ASIA-INC", "INFAC", "CHAIN", "KOS", "NTN", "FAG", "TW", "KOSYN", "COGEFA", "NECCO", "AUTOLITE", "AMERICAN EAGLE", "NATSUKI", "SUN", "REVVSUN", "NOK", "DAIDO", "BRIKE", "MOTORCRAFT", "KYOSAN", "NGK", "NGK", "ECLIPSE", "CENTURY", "CONTITECH", "DAEWHA", "MASTER POWER INJECTIONS", "TRIDON", "NEW COO", "GMB", "TAMA", "GEN", "PUNTO ROJO", "TRANSPO", "NAGARES", "DENSO", "KMC", "MANDO", "NPW", "NAMCCO", "NACHI", "PHOENIX", "SOFABEX", "IRAUTO", "REGITAR", "NPR", "GATES", "GENUINE PARTS", "YEC", "YSK", "JGK", "DIAMON", "ASHIMORI", "NSK"]
#EXCEPTION INSTALACION DE ALTA - REPARACION, REP -> KIT REPARACION - BOMBA -> AGUA, GASOLINA *COMBUSTIBLE ACEITE CLUTCH - IF NARVA -> BOMBILLO - MEDIA LUNA - BASE * BASE Y PUNZON - BUJIAS - DISCRO FRENO - CAJA CAJA DIRECCION - KIT - KIT DE REPARACION
types = ["CHICLER", "CORNETAS", "INSTALACION", "PITO", "CORNETA", "MOTOVENTILADOR", "SWITCH", "CRUCETA", "REPARACION", "BOBINA", "CADENA", "IMPULSADOR", "RODAMIENTO", "RETEN", "BIELETA", "BOMBILLO", "CORREA", "PISTONES", "CASQUETES", "ROTOR", "MEDIA LUNA", "TENSOR", "VALVULA", "RADIADOR", "GUIA", "BOCIN", "PLATINO", "GUAYA", "INYECTOR", "ANILLOS", "TERMOSTATO", "PERA", "MODULO", "ELEVADOR", "CONDENSADOR", "BUJIA", "BALINERA", "SENSOR", "PUNZON", "FILTRO", "PUNTA", "SILICONA", "MOTOR", "AMORTIGUADOR", "PLUMILLAS", "SOPORTE", "DISCO", "MUNECO", "CAJA", "DISYUNTOR", "PINON", "TIJERA", "FLASHER", "MANDO", "CAUCHOS", "TAPA", "CIGUENAL"]
#EXCEPTION TROOP -> TROOPER - R-4 R-12 R-9 R-18 -> RENAULT - GRAND VITARA -> CHEVROLET - TOY. - M323 MAZ. 323 ALEGRO 626-> MAZDA - SUZ ->SUZUKI - DAE -> DAEWOO
cars = ["FORD", "LUV", "KIA", "ESTEEM", "TOYOTA", "DAEWOO", "" ]
#Creates files inputs
inv_orig = open("inventario", "r")
inv_aux = open("inventario_aux", "r")
with open('preciosJSON.json') as json_data:
    jeisson_data = json.load(json_data)

#open output file
output = open("output.txt", "w+")

#Creating object class
class Product(object):
    ide = 0
    reference = ''
    name = ''
    brand = ''
    type = ''
    car = ''
    model = ''
    quantity = ''
    price = 0
    taiwan = False
    description = ''

    def __init__(self, ide, ref, name, brand, type, car, qty, price, tw, dcr):
        self.ide = ide
        self.reference = ref
        self.name = name
        self.brand = brand
        self.type = type
        self.car = car
        self.quantity = qty
        self.price = price
        self.taiwan = tw
        self.description = dcr

def make_product(ref, ide, name, brand, type, car, qty, price, tw, dcr):
    product = Product(ref, ide, name, brand, type, car, qty, price, tw, dcr)
    return product

def search_references(arr):
    ret_arr = []
    for i in range(len(arr)):
        if "(" in arr[i]:
            ret_arr.append(arr[i])
            break
    if  not not ret_arr:
        return ''.join(ret_arr),i
    else:
        return '', -1

#method for search brands
def brand_search(line):
    exceptions = {"JIU":"JIU JIU", "NEW": "NEW ERA", "AMERICAN": "AMERICAN EAGLE", "AUTO": "AUTO BULB VEK TRA", "MASTER": "MASTER POWER INJECTION"}
    brand = ''
    for i in range(len(line)):
        if line[i] in brands:
            return line[i], i
        else:
            if line[i] in exceptions.keys():
                return exceptions[line[i]], i 
    return "",-1

#search for product types
def type_search(line):
    exceptions = {"COMANDO": "COMANDO LUCES", "EJE": "EJE DE LEVAS", "INSTALACION": "INSTALACION DE ALTA", "REPARACION": "KIT DE REPARACION", "REP.": "KIT DE REPRACION", "KIT": "KIT DE REPARACION", "MEDIA": "MEDIA LUNA", "FRENO": "DISCO FRENO", "CAJA": "CAJA DE DIRECCION"}
    p_type = ''
    for i in range(len(line)):
        if line[i] in types:
            return line[i], i
        else:
            if line[i] in exceptions.keys():
                return exceptions[line[i]], i
            elif line[i] == "BOMBA":
                if "AGUA" in line:
                    return "BOMBA DE AGUA", i
                elif "ACEITE" in line:
                    return "BOMBA DE ACEITE", i
                elif "GASOLINA" in line or "COMBUSTIBLE" in line:
                    return "BOMBA DE GASOLINA", i
                elif "CLUTCH" in line:
                    return "BOMBA DE CLUTCH", i
    return "", -1

         


n_line = 2895
#start searching for data, splitting values and asign them into the correct object fields
for _ in range (n_line):
    
    line_aux = inv_aux.readline().split()
    del line_aux[0]
    reference_orig = ' '.join(line_aux)
    line = inv_orig.readline().split()
    ide = line[0]
    del line[0]
    reference = line[0]
    del line[0]
    
    add_ref, num = search_references(line)
    if num == -1:
        total_ref = reference
    else:
        total_ref = str(reference) + " " + add_ref
        del line[num]
  
    #Add brand
    brand,num = brand_search(line)
    if num != -1:
        del line[num]

    #Add type 
    p_type, num = type_search(line)
    if num != -1:
        del line[num]

    output.write(p_type + "\n")
    #output.write(brand + "\n")
    #output.write(' '.join(line) + "\n")
