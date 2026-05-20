"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""

ele=[]

for i in range(5):
     elementos =float(input ("Ingrese elemento de la primera lista: "))
     ele.append(elementos)



for k in range(4):
    for x in range(4-k):
        if ele[x]>ele[x+1]:
             aux=ele[x]
             ele[x]=ele[x+1]
             ele[x+1]=aux


print("Lista de elementos ordenados de menor a mayor:")
print(ele)

for k in range(4):
    for x in range(4-k):
        if ele[x]<ele[x+1]:
             aux=ele[x]
             ele[x]=ele[x+1]
             ele[x+1]=aux
print("Lista de elementos ordenados de mayor a menor:")
print(ele)



