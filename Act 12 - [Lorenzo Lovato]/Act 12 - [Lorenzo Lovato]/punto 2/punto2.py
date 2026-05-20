# 2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
# altura promedio de las personas.

cant= int(input("Ingrese la cantidad de alturas"))
suma=0
promedio=0
for i in range(cant):
    alturas=int(input(f"Ingrese la altura {i+1}:"))

    suma+=alturas
promedio=suma/cant
print("La altura promedio de las personas es:")
print(promedio)