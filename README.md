# Gestor de Reservas de Viajes
Aplicacion para realizas desr y gestionar reservas de viajes en diferentetinos.

#tags #python #Agenciadeviajes

## Tabla de Contenido
- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Estructura del Código](#estructura-del-código)
- [Guía de Uso](#guía-de-uso)

## Descripción
Esta aplicación permite a los usuarios realizar reservas de viajes, seleccionar su paquete de viaje y gestionar sus reservas.

## Características
- Validación de origen y destino.
- Selección de fechas de viaje.
- Listado e impresión de paquetes de viaje disponibles.
- Cálculo del precio del paquete seleccionado.
- Gestión de datos de pasajeros y reservas.
- Gestión de pagos.

## Requisitos
- **Python v3.X.X**

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/gestor_de_reservas_de_viajes.git
    ```
2. Navegar al directorio del proyecto:
    ```bash
    cd Agencia-de-viajes-Panchito
    ```
## Ejecución
1. Ejecutar el script principal:
    ```bash
    python main.py
    ```
2. Sigue las instrucciones en pantalla para ingresar el origen y destino, fechas de viaje, seleccionar paquetes y gestionar la reserva.

## Estructura del Código
- `main.py`: Script principal que ejecuta la aplicación.
- `origenydestino.py`: Funciones para validar el origen y destino.
- `paquetes.py`: Funciones para listar e imprimir paquetes disponibles.
- `precio.py`: Función para seleccionar y calcular el precio del paquete.
- `gestion_reserva.py`: Funciones para gestionar los datos de los pasajeros y la reserva.
- `constantes.py`: Constantes utilizadas en el proyecto.
- `fechas_viajes.py`: Funciones para ingresar y validar las fechas de viaje.
- `gestion_pagos.py`: Función para gestionar el pago de la reserva.

## Guía de Uso
1. Al ejecutar `main.py`, se te pedirá que ingreses el origen y destino de tu viaje.
2. Luego, deberás ingresar las fechas de tu viaje.
3. La aplicación listará los paquetes de viaje disponibles para el destino ingresado.
4. Selecciona un paquete de viaje y la aplicación calculará el precio.
5. Ingresa los datos de los pasajeros.
6. Confirma la reserva y selecciona una opción de pago.
7. Recibirás una confirmación de tu compra por teléfono y correo electrónico.
