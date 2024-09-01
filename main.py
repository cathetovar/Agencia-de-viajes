#Importar funciones 
from origenydestino import validarorigenydestino
from paquetes import paquetesListado, printpaquete
from precio import choose
from gestion_reserva import datospasajeros, reserva
from constantes import *
from fechas_viajes import fechasViajes
from gestion_pagos import gestionarPago

while True:
    #consultar origen y destino
    origendestino=validarorigenydestino()
    #Arreglo apra guardar el origen y destino ingresados por el cliente
    destino=origendestino[1]

    #Ingresar fechas para el viaje
    fechasReserva=fechasViajes()

    #Buscar paquetes disponibles al usuario de acuerdo al destino ingresado
    paquetes=paquetesListado(destino)

    #Imprimir los paquetes correspondientes
    printpaquete(paquetes)

    #seleccionar y Calcular precio
    precionumberpaquete=choose(paquetes)

    #Se consulta los datos de los pasajeros.
    pasajeros=datospasajeros(precionumberpaquete[1])

    #Gestion de reserva
    reservaOut=reserva(origendestino,precionumberpaquete,ciudades,pasajeros,fechasReserva)
    print("¿Es correcta su reserva?")
    confirmReserva=input("1. SI\n2. NO\nDigite el numero correspondiente: ")

    if int(confirmReserva) == 1:
        print("\nGracias por confirmar, estas son nuestras opciones de pago")
        gestionarPago(precionumberpaquete[0])
        print("\nGracias por comprar con nosotros, pronto te llegara a tu telefono y correo la confirmacion de tu compra. \nTen un viaje espectacular.\n")
        break
    elif int(confirmReserva)==2:
        print("Muy bien volvamos a empezar")
    else:
        print("No ingresaste un caracter valido, pero igual volvamos a empezar.")

