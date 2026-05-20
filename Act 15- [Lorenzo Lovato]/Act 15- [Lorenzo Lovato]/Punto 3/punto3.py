"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""
sueldos=[]
cantidad=int(input("Ingrese la cantidad de empleados:"))
for x in range(cantidad):
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    sueldos.append(sueldo)
print("Lista de sueldos ordenados de menor a mayor:")
print(sueldos)

for k in range(cantidad-1):
    for x in range(cantidad-1-k):
         if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
        
print(sueldos)