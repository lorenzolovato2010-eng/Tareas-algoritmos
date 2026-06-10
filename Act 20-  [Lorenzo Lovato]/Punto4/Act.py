"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""

def cargar_datos():
    lista = []
    for x in range(5):
        edad=int(input("Ingrese edad:"))
        lista.append(edad)
    return lista

def mayores(edades):
    contador=0
    for edad in edades:
         if edad >= 18:
             contador= contador+1
    return contador

serie_edad = cargar_datos()
cantidad= mayores(serie_edad)
print("la cantidad de edades mayores o iguales a 18 son:", cantidad)

