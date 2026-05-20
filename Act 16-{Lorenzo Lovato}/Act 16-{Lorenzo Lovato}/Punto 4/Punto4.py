"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""
docentes=[]
puntajes=[]


for i in range(6):
    nom=input("Ingrese el nombre del docente: ")
    nota=float(input("Ingrese el puntaje del docente: "))
    
    docentes.append(nom)
    puntajes.append(nota)


mayor=puntajes[0]
menor=puntajes[0]

posmayor=0
posmenor=0

for i in range(6):
    if puntajes[i] > mayor:
        mayor=puntajes[i]
        posmayor=i
        
    if puntajes[i] < menor:
        menor=puntajes[i]
        posmenor=i

print("Docente con mejor calificación:")
print(docentes[posmayor], mayor)

print("Docente con peor calificación:")
print(docentes[posmenor], menor)


for k in range(5):
    for x in range(5-k):
        if puntajes[x] < puntajes[x+1]:
            aux=puntajes[x]
            puntajes[x]=puntajes[x+1]
            puntajes[x+1]=aux
            
            aux=docentes[x]
            docentes[x]=docentes[x+1]
            docentes[x+1]=aux


print("Lista ordenada de docentes:")

for i in range(6):
    print(docentes[i], puntajes[i])


aprobados=0
desaprobados=0

for i in range(6):
    if puntajes[i] >= 6:
        aprobados=aprobados+1
    else:
        desaprobados=desaprobados+1

print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)
