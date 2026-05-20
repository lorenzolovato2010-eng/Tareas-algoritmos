#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más
#|altas que el promedio y cuántas más bajas.
lista = []

for x in range(5):
    altura = float(input("Ingrese la altura: "))
    lista.append(altura)


suma = 0

for i in lista:
    suma += i

promedio = suma / 5


mas_altas = 0
mas_bajas = 0

for i in lista:
    if i > promedio:
        masAltas += 1
    elif i < promedio:
        masBajas += 1

print("El promedio de alturas es:", promedio)
print("Personas más altas que el promedio:", masAltas)
print("Personas más bajas que el promedio:", masBajas)