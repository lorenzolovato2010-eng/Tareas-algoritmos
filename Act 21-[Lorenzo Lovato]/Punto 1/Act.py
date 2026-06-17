"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

def cargar():
    lista=[]
    for x in range(5):
        num=int(input("Ingrese un valor:"))
        lista.append(num)
    return lista

def mayor_menor(lista):
    may=lista[0]
    men=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
        if elemento<men:
            men=elemento

    return (may,men)


lista= cargar()

val_mayor, val_menor= mayor_menor(lista)

print("El mayor de la lista es:",val_mayor)
print("El menor de la lista es:",val_menor)
