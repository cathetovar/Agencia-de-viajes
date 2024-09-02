#Funcion de Registro
# Función común de validación para origen y destino
def validarLocacion(prompt):
    while True:
        try:
            location = int(input(prompt))
            if 1 <= location <= 5:
                return location
            else:
                print("Por favor, introduce un número válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

#orquestación origen y destino
def validarorigenydestino():
    print("-----------------------------------------------------------\n")
    print("Bienvenido a la agencia de viajes Panchito, la mejor agencia de viajes en Colombia. A continuación se mostrarán las ciudades donde estamos ubicados:")
    print(" 1. Bogotá \n 2. Medellín \n 3. Cartagena \n 4. Barranquilla \n 5. Cali")

    while True:
        origen = validarLocacion("\nDigite el número de su lugar de partida: ")
        destino = validarLocacion("\nDigite el número de lugar de llegada: ")

        if origen != destino:
            return [origen, destino]
        else:
            print("El destino y el origen no pueden ser iguales.")
