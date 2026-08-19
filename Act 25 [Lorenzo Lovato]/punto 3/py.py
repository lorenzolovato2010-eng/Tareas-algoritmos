"""3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ [&quot;Franco&quot;, (78.5, 77.2, 79.1)], [&quot;Lewis&quot;, (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece."""

def cargar_pilotos():

    pilotos = []
    for i in range(4):
        nombre = input(f"Ingrese el nombre del piloto {i + 1}: ")
        tiempos = []
        for j in range(3):
            tiempo = float(input(f"Ingrese el tiempo de la vuelta {j + 1} para {nombre}: "))
            tiempos.append(tiempo)
        pilotos.append([nombre, tuple(tiempos)])
    return pilotos


def calcular_promedios(pilotos):
    for piloto in pilotos:
        nombre = piloto[0]
        tiempos = piloto[1]
        promedio = sum(tiempos) / len(tiempos)
        print(f"El promedio de tiempos de {nombre} es: {promedio:.2f} segundos")

def mejor_vuelta(pilotos):
    mejor_tiempo = float('inf')
    piloto_mejor = ""
    for piloto in pilotos:
        nombre = piloto[0]
        tiempos = piloto[1]
        tiempo_minimo = min(tiempos)
        if tiempo_minimo < mejor_tiempo:
            mejor_tiempo = tiempo_minimo
            piloto_mejor = nombre
    print(f"La mejor vuelta de toda la clasificación es de {piloto_mejor} con un tiempo de {mejor_tiempo:.2f} segundos")

if __name__ == "__main__":
    pilotos = cargar_pilotos()
    calcular_promedios(pilotos)
    mejor_vuelta(pilotos)

    