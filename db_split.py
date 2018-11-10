from sys import stdin
import json
import sys 

reload(sys)  
sys.setdefaultencoding('utf8')

#PRODUCTS ARRAY
products = []

#EXCEPTION MIQUNI IS VALID - TIPO FACET VS KOREA - TRIDON VS DIAMON - MATORCRAFT - JIU JIU - NEW ERA - AMERICAN EAGLE - AUTO BULB VEK TRA - MASTER POWER INJECTIONS
brands = ["HELLA" , "GAUGE", "T.BOSCH", "IFC", "HIBARI", "AHT", "NEWSUN" , "TORICA", "ICHIBAN", "FV", "FIC", "DT", "NPC", "YWK", "BOSCH", "SANKEI", "NARVA", "DIAMOND", "KOYO", "TOYOPOWER", "OSIS", "BTK", "AUTO BULB VEK TRA", "NAPCO", "SNR", "EXACT", "OSK", "RENAULT", "DODUCO", "AISAN", "TSK", "NAKAMOTO", "HERKO", "AIRTEX", "RIK", "VALEO", "TOTO", "FAE", "AWP", "RAON", "BISSC", "DEUSIC", "MOBIS", "GM", "EKKO", "LOCTITE", "MIQUINI", "JIU JIU", "BGF", "A1", "TP", "PERFECT", "BROSOL", "I&R", "SHIBUMI", "NEW ERA", "FACET", "ASIA-INC", "INFAC", "CHAIN", "KOS", "NTN", "FAG", "TW", "KOSYN", "COGEFA", "NECCO", "AUTOLITE", "AMERICAN EAGLE", "NATSUKI", "SUN", "REVVSUN", "NOK", "DAIDO", "BRIKE", "MOTORCRAFT", "KYOSAN", "NGK", "NGK", "ECLIPSE", "CENTURY", "CONTITECH", "DAEWHA", "MASTER POWER INJECTIONS", "TRIDON", "NEW COO", "GMB", "TAMA", "GEN", "PUNTO ROJO", "TRANSPO", "NAGARES", "DENSO", "KMC", "MANDO", "NPW", "NAMCCO", "NACHI", "PHOENIX", "SOFABEX", "IRAUTO", "REGITAR", "NPR", "GATES", "GENUINE PARTS", "YEC", "YSK", "JGK", "DIAMON", "ASHIMORI", "NSK"]
#EXCEPTION INSTALACION DE ALTA - REPARACION, REP -> KIT REPARACION - BOMBA -> AGUA, GASOLINA *COMBUSTIBLE ACEITE CLUTCH - IF NARVA -> BOMBILLO - MEDIA LUNA - BASE * BASE Y PUNZON - BUJIAS - DISCRO FRENO - CAJA CAJA DIRECCION - KIT - KIT DE REPARACION
types = ["CHICLER", "CORNETAS", "INSTALACION", "PITO", "CORNETA", "MOTOVENTILADOR", "SWITCH", "CRUCETA", "BOBINA", "CADENA", "IMPULSADOR", "RODAMIENTO", "RETEN", "BIELETA", "BOMBILLO", "CORREA", "PISTONES", "CASQUETES", "ROTOR", "MEDIA LUNA", "TENSOR", "VALVULA", "RADIADOR", "GUIA", "BOCIN", "PLATINO", "GUAYA", "INYECTOR", "ANILLOS", "TERMOSTATO", "PERA", "MODULO", "ELEVADOR", "CONDENSADOR", "BUJIA", "BALINERA", "SENSOR", "PUNZON", "FILTRO", "PUNTA", "SILICONA", "MOTOR", "AMORTIGUADOR", "PLUMILLAS", "SOPORTE", "DISCO", "MUNECO", "CAJA", "DISYUNTOR", "PINON", "TIJERA", "FLASHER", "MANDO", "CAUCHOS", "TAPA", "CIGUENAL"]
#EXCEPTION TROOP -> TROOPER - R-4 R-12 R-9 R-18 -> RENAULT - GRAND VITARA LUV ESTEEM-> CHEVROLET - TOY. - M323 MAZ. 323 ALEGRO 626 -> MAZDA - SUZ ->SUZUKI - DAE -> DAEWOO -> NUBIRA - HYUNDAI - ELANTRA VERNA ACCENT GYRO TERRACAN GETZ VISION GRAND STAREX TUCSON SPORTAGE ATOS  - NISSAN -> X-TRAIL X-TERRA MURANO 
cars = ["FORD", "RENAULT", "MAZDA", "SUZUKI", "DAEWOO", "HYUNDAI", "NISSAN", "TOYOTA", "FORD", "KIA", "MITSUBISHI", "HONDA", "SKODA", "DODGE", "CHEVROLET", "ISUZU", "PULSAR", "DAIHATSU" ]
#EXCEPTION GRAND
models = {"DAIHATSU": ["TERIOS", "DELTA", "F20"], "RENAULT": ["MEGANE", "R-4", "R-12", "R-6", "R-9", "R-18", "DUSTER", "KOLEOS", "LOGAN", "SYMBOL", "TWINGO", "CLIO", "SANDERO" ], "CHEVROLET": ["TROOPER","SPARK", "D-MAX", "OPTRA", "CAPTIVA","AVEO","GRAND-VITARA", "LUV", "LUV-1.6", "LUV-2.3", "LUV-2.2", "ESTEEM", "N200", "N300", "TRACKER", "SWIFT", "SPRINT", "ALTO", "SONIC", "SUPER-CARRY", "CORSA", "LANOS", "DMAX", "WAGON", "SONIC", "L200", "CRUZE", "SAIL", "AVEO"] , "MAZDA": ["MATSURI", "323", "ALLEGRO", "626", "ASAHI", "B2.2", "B2.0", "6", "B2600", "BT-50"] ,"SUZUKI": ["JIMNY", "SAMURAI"] , "DAEWOO": ["NUBIRA", "RACER", "TICO", "MATIZ"] , "HYUNDAI": ["ELANTRA", "VERNA", "ACCENT", "GYRO", "TERRACAN", "GETZ", "VISION", "VITARA", "STAREX", "TUCSON", "ATOS", "I10", "XCITE", "EXCELL", "SANTA-FE", "VERNA", "H100"] ,"NISSAN": ["URBAN","TIIDA","X-TRAIL", "X-TERRA", "MURANO", "SENTRA", "PATROL", "VANETTE", "FRONTIER"] ,"TOYOTA": ["COROLLA", "PRADO", "HILUX", "YARIS", "4RUNNER", "LAND-CRUISER", "CAMPERO", "VIGO", "FORTUNER"] ,"FORD": ["FIESTA", "ESCAPE", "ECOSPORT", "FOCUS", "FERTIVA"] ,"KIA": ["SPORTAGE", "RIO", "CERATO", "SOUL", "SEPHIA", "PICANTO", "ION"] ,"MITSUBISHI": ["SPACE", "WAGON", "LANCER", "L2000", "PAJERO", "MONTERO", "HART", "L300", "V6"] ,"HONDA": ["CRV", "CIVIC"] , "PEUGEOT": ["106", "406", "306", "206", "307", "207"] ,"SKODA": ["FABIA"] ,"DODGE": ["JOURNEY"] }

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
    reference_orig = ''
    brand = ''
    type = ''
    car = ''
    model = ''
    quantity = ''
    price = 0
    

    def __init__(self, ide, ref_o, ref, brand, type, car, qty, price, model):
        self.ide = ide
        self.reference_orig = ref_o
        self.reference = reference
        self.brand = brand
        self.type = type
        self.car = car
        self.model = model
        self.quantity = qty
        self.price = price
        

def make_product(ide, ref_o, ref, brand, type, car, qty, price, model):
    product = Product(ide, ref_o, ref, brand, type, car, qty, price, model)
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
        return "nil", -1

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
    return "nil",-1

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
    return "nil", -1

#search models and brands
def search_models(line):
    types = []
    brands = []
    for i in range(len(line)):
        for e in models.keys():
            if line[i] in models[e]:
                types.append(line[i])
                if not e in brands:
                    brands.append(e)
        if not brands or not types:
            if line[i] in cars:
                brands.append(line[i]) 
    return brands, types        

#creation of a chimbo array
prices= [-1]*2895


n_line = 2895
arr_ref = []

#variable qty temporary set to 0
qty = 0
#start searching for data, splitting values and asign them into the correct object fields
for _ in range (n_line):
    
    line_aux = inv_aux.readline().split()
    del line_aux[0]
    reference_orig = ' '.join(line_aux)
    arr_ref.append(reference_orig.split())
    line = inv_orig.readline().split()
    ide = int(line[0])
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

    #add models and brands
    brand, model = search_models(line)
    #output.write(str(brand) + "," + str(model)+ "\n")

    #make product object with the parameters except price and qty
    product = make_product(ide, reference_orig, total_ref, brand, p_type, brand, qty, -1, model)
    products.append(product)
    #output.write(' '.join(line) + "\n")



for i in jeisson_data:
    if i["IdInventario"].split() in arr_ref:
        pos = arr_ref.index(i["IdInventario"].split())
        if "," in i["Precio1"]:
            precio = str(i["Precio1"]).replace(",","")
        products[pos].price = float(precio)

"""
ides = []
ref_orig = []
ref =[]
brands = []
types = []
cars = []
models = []
quantities = [0] * 2895
prices = []
"""


for i in products:
    
    output.write("["+str(i.ide) + "," + "'" +i.reference + "'" + "," +"'"+ i.reference_orig + "'" + ","+ str(i.brand) + "," +"'"+ i.type + "'" +"," + str(i.car) + "," + str(i.model) + "," + str(i.price) + "]" + "," +"\n")


   