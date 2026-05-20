"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""
paises=[]
habitantes=[]
for i in range(5):
    pais=input ("Ingrese el nombre del país: ")
    hab=int(input ("Ingrese la cantidad de habitantes del país: "))
    paises.append(pais)
    habitantes.append(hab)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
             aux=paises[x]
             paises[x]=paises[x+1]
             paises[x+1]=aux
             aux=habitantes[x]
             habitantes[x]=habitantes[x+1]
             habitantes[x+1]=aux    
print("Lista de países ordenados alfabéticamente:")
for i in range(5):
    print(paises[i],habitantes[i])
for k in range(4):  
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
             aux=paises[x]
             paises[x]=paises[x+1]
             paises[x+1]=aux
             aux=habitantes[x]
             habitantes[x]=habitantes[x+1]
             habitantes[x+1]=aux
print("Lista de países ordenados por cantidad de habitantes (de mayor a menor):")
for i in range(5):
    print(paises[i],habitantes[i])

        