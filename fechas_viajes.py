import datetime

# Ingresar fechas de viaje
def fechasViajes():
    while True:
        print("\nIngresa las fechas en las que quieres viajar en formato DD/MM/YYYY")
        fechaSalida = input("Fecha de salida (DD/MM/YYYY): ")
        fechaRegreso = input("Fecha de regreso (DD/MM/YYYY): ")

        try:
            # Convertir las fechas de string a objetos datetime
            fechaSalidaDt = datetime.datetime.strptime(fechaSalida, "%d/%m/%Y")
            fechaRegresoDt = datetime.datetime.strptime(fechaRegreso, "%d/%m/%Y")
            fechaActual = datetime.datetime.now()

            # Verificar que la fecha de salida sea posterior a la fecha actual
            if fechaSalidaDt <= fechaActual:
                print("La fecha de salida debe ser posterior a la fecha actual. Por favor, intente de nuevo.")
                continue

            # Verificar que la fecha de salida sea anterior a la fecha de regreso
            if fechaSalidaDt >= fechaRegresoDt:
                print("La fecha de salida debe ser anterior a la fecha de regreso. Por favor, intente de nuevo.")
                continue

            print("\nSu fecha de salida es: ", fechaSalida)
            print("Su fecha de regreso es: ", fechaRegreso)
            print("\nDías de viaje: ", (fechaRegresoDt - fechaSalidaDt).days)
            print("\n¿Las fechas seleccionadas son correctas?\n1. Si\n2. No")
            eleccion = int(input("\nDigite el número correspondiente: "))

            if eleccion == 1:
                fechasReserva = [fechaSalida, fechaRegreso]
                break
            elif eleccion == 2:
                print("Comencemos de nuevo")
            else:
                print("Digitaste un carácter no válido, pero igual comencemos de nuevo")
        except ValueError:
            print("Formato de fecha no válido. Por favor, use el formato DD/MM/YYYY.")

    return fechasReserva
