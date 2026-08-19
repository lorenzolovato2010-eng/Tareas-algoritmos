"""1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo."""

def cargar_temperaturas():
    temperaturas = []
    for i in range(6):
        temp = float(input(f"Ingrese la temperatura máxima de la hora {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def procesar_extremos(temperaturas):
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
    return max_temp, min_temp


if __name__ == "__main__":
    temperaturas = cargar_temperaturas()
    maxima, minima = procesar_extremos(temperaturas)
    print(f"La temperatura máxima registrada es: {maxima}°C")
    print(f"La temperatura mínima registrada es: {minima}°C")

