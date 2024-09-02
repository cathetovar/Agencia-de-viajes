#Importar funciones 
from origenydestino import validarorigenydestino
from paquetes import paquetesListado, printpaquete
from precio import choose
from gestion_reserva import datosPasajeros, reserva, confirmarReserva
from constantes import *
from fechas_viajes import fechasViajes

while True:
    # Consultar origen y destino
    origendestino = validarorigenydestino()
    #Arreglo apra guardar el origen y destino ingresados por el cliente
    destino = origendestino[1]

    # Ingresar fechas para el viaje
    fechasReserva = fechasViajes()

    # Buscar paquetes disponibles al usuario de acuerdo al destino ingresado
    paquetes = paquetesListado(destino)

    # Imprimir los paquetes correspondientes
    printpaquete(paquetes)

    # Seleccionar y calcular precio
    precioPaquete = choose(paquetes,fechasReserva)

    # Consultar los datos de los pasajeros
    pasajeros = datosPasajeros(precioPaquete[1])

    # Gestión de reserva
    reservaOut = reserva(origendestino, precioPaquete, ciudades, pasajeros, fechasReserva)
    print("¿Es correcta su reserva?")

    if confirmarReserva(precioPaquete[0]):
        break
