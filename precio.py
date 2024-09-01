
#Elegir paquete y numero de personas y precio total 
def choose (paquetes):
    choose=int(input("\nIngrese el numero correspondiente al paquete que desea: "))
    number=int(input("Digite la cantidad de personas que adquiriran el paquete: "))
    paquete=paquetes[choose-1]
    salidachoose=[]
    valor= paquete[6]
    #Eliminar los puntos 
    valorc=valor.replace(".","")
    precio=int(valorc)*number
    #volver a agregar los puntos
    precioc="{:,}".format(precio).replace(",", ".")
        
    print("El precio a pagar seria de: $", precioc)
    print()
    salidachoose=[precioc,number, paquete]
    return salidachoose     

