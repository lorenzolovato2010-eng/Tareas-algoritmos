"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""

nombre=[]
notas=[]


for i in range(6):
    nom=input("Ingrese el nombre del alumno: ")
    nota=float(input("Ingrese la nota del alumno: "))
    
    nombre.append(nom)
    notas.append(nota)


maxima = max(notas)
minima = min(notas)


print("Alumnos con la nota más alta:")
for i in range(6):
    if notas[i] == maxima:
        print(nombre[i], "-", notas[i])

print("Alumnos con la nota más baja:")
for i in range(6):
    if notas[i] == minima:
        print(nombre[i], "-", notas[i])


contador_max = 0
for i in range(6):
    if notas[i] == maxima:
        contador_max += 1

if contador_max > 1:
    print("Hay", contador_max, "estudiantes con la nota máxima.")


contador_min = 0
for i in range(6):
    if notas[i] == minima:
        contador_min += 1

if contador_min > 1:
    print("Hay", contador_min, "estudiantes con la nota mínima.")