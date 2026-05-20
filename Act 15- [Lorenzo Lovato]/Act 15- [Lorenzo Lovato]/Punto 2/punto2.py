"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""
lista1=[]
lista2=[]
lista3=[]

for i in range(4):
     uno =float(input ("Ingrese elemento de la primera lista: "))
     dos =float(input ("Ingrese elemento de la segunda lista: "))
     lista1.append(uno)
     lista2.append(dos)
     print("LISTA DE ELEMENTOS")


for x in range (4) :
     tres = lista1[x] + lista2[x]
     lista3.append(tres)

print("LISTA 3")
print(lista3)