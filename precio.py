import datetime

#funciones utilitarias
#imprimir listas

def printList(inLista):
    for lista in inLista:
            for elemento in lista:
                print(elemento, end=" ")
            print()  # Salto de línea después de cada lista

#imprimir lista como un solo string
def printSingleList(inLista):
     print(" ".join(inLista))

#imprimir datos de pasajeros
def printPasajeros(pasajeros):
    i=0
    print("\nDatos de los pasajeros: ")
    for pasajero in pasajeros:
        i=i+1
        print("Pasajero ",i)
        print("Nombre: ",pasajero[0])
        print("Apello: ",pasajero[1])
        print(pasajero[2]+": "+pasajero[3])
        print("Email: ",pasajero[4])
        print()

def diasTotales(fechasReserva):
    # Convertir las fechas de string a objetos datetime
    fechaSalida = datetime.datetime.strptime(fechasReserva[0], "%d/%m/%Y")
    fechaLlegada = datetime.datetime.strptime(fechasReserva[1], "%d/%m/%Y")

    # Calcular la diferencia de días entre las fechas
    diferenciaDias = (fechaLlegada - fechaSalida).days

    return diferenciaDias
