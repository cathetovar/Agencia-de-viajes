from utilities import diasTotales


#Elegir paquete y numero de personas y precio total
def choose(paquetes, fechasReserva):
    while True:
        try:
            paqueteIndex = int(input("\nIngrese el número correspondiente al paquete que desea: ")) - 1
            if paqueteIndex < 0 or paqueteIndex >= len(paquetes):
                raise ValueError("Índice de paquete fuera de rango.")
            break
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente de nuevo.")

    while True:
        try:
            numPersonas = int(input("Digite la cantidad de personas que adquirirán el paquete: "))
            if numPersonas <= 0:
                raise ValueError("El número de personas debe ser mayor que cero.")
            break
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente de nuevo.")

    paquete = paquetes[paqueteIndex]
    precioUnitario = int(paquete[6].replace(".", ""))
    precioUnitarioTotalYDias = calcularPrecioUnitarioTotal(precioUnitario, fechasReserva)
    precioFinal = precioUnitarioTotalYDias[0] * numPersonas

    precioFormateado = "{:,}".format(precioFinal).replace(",", ".")

    print("El precio a pagar por los "+str(precioUnitarioTotalYDias[1])+f" sería de: ${precioFormateado}\n")
    return [precioFormateado, numPersonas, paquete]

def calcularPrecioUnitarioTotal(precioPorNoche, fechasReserva):
    # Calcular la diferencia de días entre las fechas
    diferenciaDias = diasTotales(fechasReserva)

    # Calcular el precio total
    precioTotal = precioPorNoche * diferenciaDias

    return [precioTotal,diferenciaDias]
