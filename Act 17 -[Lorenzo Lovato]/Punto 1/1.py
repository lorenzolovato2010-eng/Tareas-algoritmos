"""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50
del primer elemento de "lista";.
Volver a imprimir la lista.
"""
aux=0
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
listaAux=[]

print("Lista")
print(lista)
print("--------")
i=0
x=0

posicion=0


for x in range(len(lista)):
    nuevaAux=[]
    for i in lista[x]:
        if i > 50:
            listaAux.append(i)
        else:
            nuevaAux.append(i)
    lista[x]=nuevaAux

lista[0]=listaAux

print(lista)
    
