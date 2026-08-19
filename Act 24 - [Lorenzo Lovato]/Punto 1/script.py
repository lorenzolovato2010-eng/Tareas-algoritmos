"""
 Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes
 de dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
 monitoreo (ej: "San Telmo") y el Valor sea una lista de flotantes que represente
 las últimas 3 lecturas de contaminación tomadas en el día.
 Desarrollar las siguientes funciones:
 1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
    una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
 2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada barrio.
 3. Alerta ambiental: Mostrar en pantalla una alerta roja de "Protocolo de Emergencia"
    únicamente para las estaciones cuyo promedio de contaminación supere las 400 ppm."""


def cargar():
    senso = {}

    for i in range(3):
        estacion = input(f"Ingrese el nombre de estación {i + 1}: ")
        lecturas = []

        for j in range(3):
            lectura = float(
                input(
                    f"Ingrese la lectura {j + 1} de CO2 para {estacion} (ppm): "
                )
            )
            lecturas.append(lectura)

        senso[estacion] = lecturas

    return senso


def reportar_promedios(senso):
    promedios = {}

    for estacion, lecturas in senso.items():
        suma = 0
        for l in lecturas:
            suma = suma + l

        promedio = suma / len(lecturas)
        promedios[estacion] = promedio
        print("Promedio de", estacion, ":", promedio, "ppm")

    return promedios


def alerta_ambiental(promedios):

    for estacion, promedio in promedios.items():
        if promedio > 400:
            print(
                "Alerta roja en:",
                estacion,
                "con",
                promedio,
                "ppm",
            )


senso = cargar()
promedios = reportar_promedios(senso)
alerta_ambiental(promedios)