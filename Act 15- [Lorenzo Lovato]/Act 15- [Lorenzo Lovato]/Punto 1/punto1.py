"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o
igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot;
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
"""

nombre=[]
notas=[]

for i in range(5):
    nom=input ("Ingrese el nombre del alumno: ")
    nota=float(input ("Ingrese la nota del alumno: "))
    nombre.append(nom)
    notas.append(nota)
print("Listado de alumnos:")
for i in range(5):
    if notas[i]>=8:
        print(nombre[i],notas[i],"Muy Bueno")
    else:
        if notas[i]>=4 and notas[i]<8:
            print(nombre[i],notas[i],"Bueno")
        else:

            print(nombre[i],notas[i],"Insuficiente")
contador=0
for i in range(5):
    if notas[i]>=8:
        contador+=1 
print("Cantidad de alumnos con 'Muy Bueno':",contador)
