"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""

vendedores=[]
ventas=[]


for i in range(5):
    nom=input("Ingrese el nombre del vendedor: ")
    venta=float(input("Ingrese el total vendido: "))
    
    vendedores.append(nom)
    ventas.append(venta)


for k in range(4):
    for x in range(4-k):
        if ventas[x] < ventas[x+1]:
            aux=ventas[x]
            ventas[x]=ventas[x+1]
            ventas[x+1]=aux
            
            aux=vendedores[x]
            vendedores[x]=vendedores[x+1]
            vendedores[x+1]=aux


print("Lista ordenada de vendedores:")
for i in range(5):
    print(vendedores[i], ventas[i])


print("El empleado que menos vendió fue:")
print(vendedores[4], ventas[4])
