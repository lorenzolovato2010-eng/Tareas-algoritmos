#2. cargar por teclado Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas.
mañana = []
tarde = []


for x in range(4):
    sueldo = float(input("Ingrese sueldo del turno mañana: "))
    mañana.append(sueldo)


for x in range(4):
    sueldo = float(input("Ingrese sueldo del turno tarde: "))
    tarde.append(sueldo)

print("Sueldos turno mañana:", mañana)
print("Sueldos turno tarde:", tarde)

