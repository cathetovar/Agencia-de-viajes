
def paquetesListado(ciudadId):

    bogota=[["1. Hotel Decameron ", "5 dias y 4 noches ", "Incluye: Desayuno, almuerzo y cena ", "Precio: $900.000 "],["2. Hotel hilton ", "3 dias y 2 noches ", "incluye: Desayuno y almuerzo ", "Precio: $1.200.000 "], ["3. Hotel Dann Carton ", "4 dias y 3 noches ", "Incluye: Desayuno y cena", "Precio: $850.000  "]]
    medellin=[["1. Hotel Decameron ", "5 dias y 4 noches ", "Incluye: Desayuno, almuerzo y cena ", "Precio: $1.000.000 "],["2. Hotel hilton ", "3 dias y 2 noches ", "incluye: Desayuno y almuerzo ", "Precio: $1.000.000 "], ["3. Hotel Dann Carton ", "4 dias y 3 noches ", "Incluye: Desayuno y cena", "Precio: $750.000  "]]
    cartagena=[["1. Hotel Dubai ", "4 dias y 3 noches ", "Incluye: Desayuno, almuerzo y cena ", "Precio: $700.000 "],["2. Hotel hilton ", "3 dias y 2 noches ", "incluye: Desayuno y almuerzo ", "Precio: $950.000 "], ["3. Hotel Decameron ", "5 dias y 4 noches ", "Incluye: Desayuno y cena", "Precio: $1.000.000  "]]
    barranquilla=[["1. Hotel Decameron ", "3 dias y 2 noches ", "Incluye: Desayuno, almuerzo y cena ", "Precio: $900.000 "],["2. Hotel hilton ", "3 dias y 2 noches ", "incluye: Desayuno y almuerzo ", "Precio: $1.200.000 "], ["3. Hotel Dann Carton ", "4 dias y 3 noches ", "Incluye: Desayuno y cena", "Precio: $850.000  "]]
    cali=[["1. Hotel intercontinental ", "5 dias y 4 noches ", "Incluye: Desayuno, almuerzo y cena ", "Precio: $1.500.000 "],["2. Hotel hilton ", "3 dias y 2 noches ", "incluye: Desayuno y almuerzo ", "Precio: $1.200.000 "], ["3. Hotel Dann Carton ", "4 dias y 3 noches ", "Incluye: Desayuno y cena", "Precio: $900.000  "]]

    paquetes = [bogota,medellin,cartagena,barranquilla,cali]    

    paquetes1=paquetes[ciudadId-1]
    #print(response)

    return paquetes1