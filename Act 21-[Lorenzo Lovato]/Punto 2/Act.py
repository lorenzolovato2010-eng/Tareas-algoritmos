"""
2-
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos
valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos
de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y
seguidamente llamar a la función que muestra el nombre de empleado con sueldo
mayor.
# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""

def cargar_empleado():
    nombre=(input("Ingrese el nombre del empleado:"))
    sueldo=float(input(f"Ingrese el sueldo:"))
    return(nombre, sueldo)

def mayor_sueldo(emp1, emp2):
    if emp1[1]>emp2[1]:
        print(f"El empleado con mayor sueldo es",emp1[0],"(sueldo:",emp1[1],")")
    elif emp2[1]>emp1[1]:
        print(f"El empleado con mayor sueldo es",emp2[0],"(sueldo:",emp2[1],")")
    else:
        print(f"Ambos empleados tienen el mismo sueldo:",emp1[1])

empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)