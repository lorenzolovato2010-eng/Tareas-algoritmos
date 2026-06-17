"""
3-

Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:

empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] , etc. ]
"""


def cargar_empleados():
    lista_empleados=[]
    
    for i in range(5):
        nombre=input(f"Ingrese el nombre del empleado:")

        sueldo1=float(input(f"Sueldo 1:"))
        sueldo2=float(input(f"Sueldo 2:"))
        sueldo3=float(input(f"Sueldo 3:"))

        sueldos_tuplas=(sueldo1,sueldo2,sueldo3)

        lista_empleados.append([nombre, sueldos_tuplas])
        

        return lista_empleados
    
def imprimir_monto_total(lista_empleados):

    for empleado in lista_empleados:
        nombre= empleado[0]
        sueldos= empleado[1]

        total_cobrado= sum(sueldos)
        print(f"Empleado:", nombre,"| total cobrado:", total_cobrado)

def imprimir_ingreso_mayor_diezmil(lista_empleados):
    hubo_empleados= False

    for empleado in lista_empleados:
        nombre=empleado[0]
        sueldos= empleado[1]
        total_trimestral= sum(sueldos)

        if total_trimestral > 10000:
            print(nombre,"Ingreso:",total_trimestral)
            hubo_empleados=True
        
        if not hubo_empleados:
            print("Ningun empleado supero los 10000 en el trimestre")


empleados= cargar_empleados()

imprimir_monto_total(empleados)
imprimir_ingreso_mayor_diezmil(empleados)

