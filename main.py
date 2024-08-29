from origenydestino import validarorigenydestino
from paquetes import paquetesListado

#consultar origen y destino
origenDestino=validarorigenydestino()

destino=origenDestino[1]
#mostrar paquetes disponibles al usuario
paquete=paquetesListado(destino)

print("Los paquetes disponibles son: ")
for lista in paquete:
        for elemento in lista:
           print(elemento, end=" ")
        print()  # Salto de línea después de cada lista

