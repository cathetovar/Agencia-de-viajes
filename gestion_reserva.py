from gestion_pagos import mostrarOpcionesPago
from utilities import *

# Datos de los pasajeros
def datosPasajeros(number):
    pasajeros = []
    for i in range(number):
        a = i + 1
        print("Ingresa los datos del pasajero ", a, ":")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        tipo = input("Tipo de documento (TI, CC, PP): ")
        documentoId = input("Número de documento: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")

        # Usar append para añadir el pasajero a la lista
        pasajeros.append([nombre, apellido, tipo, documentoId, telefono, correo])
    return pasajeros

# Imprimir y almacenar el resumen de la reserva
def reserva(origenDestino, precioNumberPaquete, ciudades, pasajeros, fechasReserva):
    origen = ciudades[origenDestino[0] - 1]
    destino = ciudades[origenDestino[1] - 1]
    print("---------------------------------------\n")
    print("Su reserva sería: ")
    print("Origen:", origen, "\nDestino: ", destino)
    print("\nLas fechas de su reserva son")
    print("Fecha de salida: ", fechasReserva[0])
    print("Fecha de llegada: ", fechasReserva[1])
    paquete = precioNumberPaquete[2]
    print("\nPaquete: ")
    printSingleList(paquete)
    precioC = precioNumberPaquete[0]
    print("\nPrecio total: $", precioC)
    printPasajeros(pasajeros)
    reservaUsuario = [origenDestino, precioNumberPaquete, ciudades, pasajeros]
    return reservaUsuario

def confirmarReserva(precioPaquete):
    while True:
        confirmReserva = input("Confirma tu reserva (1 para confirmar, 2 para reiniciar): ")
        if confirmReserva.isdigit():
            confirmReserva = int(confirmReserva)
            if confirmReserva == 1:
                mostrarOpcionesPago(precioPaquete)
                break
            elif confirmReserva == 2:
                print("Muy bien, volvamos a empezar")
                return False
            else:
                print("No ingresaste un carácter válido, pero igual volvamos a empezar.")
        else:
            print("Entrada no válida. Por favor, ingresa un número.")
    return True
