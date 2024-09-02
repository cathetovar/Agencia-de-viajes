
#paquetes disponibles
def paquetesListado(ciudadId):

    bogota = [["1. Vuelos ida y regreso +", "Hotel Decameron +", "por noche", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:", "$", "900.000 "],
              ["2. Vuelos ida y regreso +", "Hotel hilton +", "por noche", "incluye: Desayuno y almuerzo +", "Precio por persona:", "$", "1.200.000"],
              ["3. Vuelos ida y regreso +", "Hotel Dann Carton +", "por noche", "Incluye: Desayuno y cena +", "Precio por persona:", "$", "850.000"]
             ]
    medellin = [["1. Vuelos ida y regreso +", "Hotel Decameron +", "por noche", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:", "$", "1.000.000 "],
                ["2. Vuelos ida y regreso +", "Hotel hilton +", "por noche", "incluye: Desayuno y almuerzo +", "Precio por persona:", "$", "1.000.000"],
                ["3. Vuelos ida y regreso +", "Hotel Dann Carton +", "por noche", "Incluye: Desayuno y cena +", "Precio por persona:", "$", "750.000"]
               ]
    cartagena = [["1. Vuelos ida y regreso +", "Hotel Dubai +", "por noche", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:", "$", "700.000"],
                 ["2. Vuelos ida y regreso +", "Hotel hilton +", "por noche", "incluye: Desayuno y almuerzo +", "Precio por persona:", "$", "950.000"],
                 ["3. Vuelos ida y regreso +", "Hotel Decameron +", "por noche", "Incluye: Desayuno y cena +", "Precio por persona:", "$", "1.000.000"]
                ]
    barranquilla = [["1. Vuelos ida y regreso +", "Hotel Decameron +", "por noche", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:", "$", "900.000"],
                    ["2. Vuelos ida y regreso +", "Hotel hilton +", "por noche", "incluye: Desayuno y almuerzo +", "Precio por persona:", "$", "1.200.000"],
                    ["3. Vuelos ida y regreso +", "Hotel Dann Carton +", "por noche", "Incluye: Desayuno y cena +", "Precio por persona:", "$", "850.000"]
                   ]
    cali = [["1. Vuelos ida y regreso +", "Hotel intercontinental +", "por noche", "Incluye: Desayuno, almuerzo y cena +", "Precio por persona:", "$", "1.500.000"],
            ["2. Vuelos ida y regreso +", "Hotel hilton +", "por noche", "incluye: Desayuno y almuerzo +", "Precio por persona:", "$", "1.200.000"],
            ["3. Vuelos ida y regreso +", "Hotel Dann Carton +", "por noche", "Incluye: Desayuno y cena +", "Precio por persona:", "$", "900.000"]
           ]

    paquetes = [bogota,medellin,cartagena,barranquilla,cali]

    return paquetes[ciudadId-1]
#imprimir paquetes
def printpaquete(paquetes):
    print("\nRecuerde que nuestros paquetes están disponibles todo el año")
    print("Los paquetes disponibles son:")
    for lista in paquetes:
            for elemento in lista:
                print(elemento, end=" ")
            print()  # Salto de línea después de cada lista

