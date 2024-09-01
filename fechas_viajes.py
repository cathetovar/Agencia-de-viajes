
#Ingresar fechas de viaje
def fechasViajes():
    while True:
        print("\nIngresa las fechas en las que quieres viajar en formato DD/MM/YYYY")
        fechaSalida=input("Fecha de salida (DD/MM/YYYY): ")
        fechaLlegada=input("Fecha de llegada (DD/MM/YYYY): ")
        print("\nSu fecha de salida es: ", fechaSalida)
        print("Su fecha de llegada es: ",fechaLlegada)
        print("\n¿Las fechas seleccionadas son correctas?\n1. Si\n2. No")
        eleccion=int(input("\nDigite el numero correspondiente: "))
        if eleccion == 1:
            fechasReserva=[fechaSalida,fechaLlegada]
            break
        elif eleccion == 2:
            print("Comencemos de nuevo")
        else:
            print("Digitaste un caracter no valido, pero igual Comencemos de nuevo")
    return fechasReserva
    

    