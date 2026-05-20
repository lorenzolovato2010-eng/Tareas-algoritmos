# 1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
# informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
mayores=0
menores=0
notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    if nota>=7:
        mayores=mayores+1
    else:
        menores=menores+1
    
print("La cantidad de notas mayores o iguales a 7 son:")
print(mayores)
print("La cantidad de notas menores a 7 son:")
print(menores)
