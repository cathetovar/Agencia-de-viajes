from utilities import *

#datos de los pasajeros
def datospasajeros(number):
    pasajeros=[]
    for i in range(number):
        a=i+1
        print("Ingresa los datos del pasajero ",a, ":")
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        tipo=input("Tipo de documento (TI, CC, PP): ")
        id=input("Numero de documento: ")
        telefono=input("Telefono: ")
        correo=input("Correo electronico: ")

        # Usar append para añadir el pasajero a la lista
        pasajeros.append([nombre, apellido, tipo, id, telefono, correo])
    return pasajeros
#imprimir y almacenar el resumen la reserva 
def reserva(origendestino,precionumberpaquete,ciudades,pasajeros,fechasReserva):
    origen=ciudades[origendestino[0]-1]
    destino=ciudades[origendestino[1]-1]
    print("\n")
    print("Su reserva seria: ")
    print("Origen:", origen, "\nDestino: ", destino)
    print("\nLas fechas de su reserva son")
    print("Fecha de salida: ",fechasReserva[0])
    print("Fecha de llegada: ",fechasReserva[1])
    paquete=precionumberpaquete[2]
    print("\nPaquete: ")
    printSingleList(paquete)
    precioc=precionumberpaquete[0]
    print("\nPrecio total: ",precioc)
    printPasajeros(pasajeros)
    reservaUsuario=[origendestino,precionumberpaquete,ciudades,pasajeros]
    return reservaUsuario