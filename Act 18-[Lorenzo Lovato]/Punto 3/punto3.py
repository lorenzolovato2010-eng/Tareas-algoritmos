"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una supreficie mayor.
"""

def retornar_superficie(lado1, lado2):
    return lado1 * lado2
Lado1rectangulo1 = float(input("Ingrese el lado 1 del rectángulo 1: "))
Lado2rectangulo1 = float(input("Ingrese el lado 2 del rectángulo1: "))
Lado1rectangulo2 = float(input("Ingrese el lado 1 del rectángulo 2: "))
Lado2rectangulo2 = float(input("Ingrese el lado 2 del rectángulo   2: "))
superficie_rectangulo1 = retornar_superficie(Lado1rectangulo1, Lado2rectangulo1)
superficie_rectangulo2 = retornar_superficie(Lado1rectangulo2, Lado2rectangulo2)

if superficie_rectangulo1 > superficie_rectangulo2:
    print("El rectángulo 1 tiene una superficie mayor: ", superficie_rectangulo1)
if superficie_rectangulo2 > superficie_rectangulo1:
    print("El rectángulo 2 tiene una superficie mayor: ", superficie_rectangulo2)
else:
    print("Ambos rectángulos tienen la misma superficie: ", superficie_rectangulo1)
    

