#3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
#más posiciones en la lista)
lista = []

for x in range(5):
    valor = int(input("Ingrese su elemento: "))
    lista.append(valor)

mayor = lista[0]

for x in range(5):
    if lista[x] > mayor:
        mayor = lista[x]

contador = 0

for i in lista:
    if i == mayor:
        contador += 1

print("El mayor es:", mayor)

if contador >= 2:
    print("El mayor se repite en la lista", contador, "veces")