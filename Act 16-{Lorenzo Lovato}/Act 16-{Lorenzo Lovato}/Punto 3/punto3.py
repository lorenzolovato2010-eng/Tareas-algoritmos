"""
3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio. 
"""

atletas=[]
tiempos=[]


for i in range(5):
    nom=input("Ingrese el nombre del atleta: ")
    tiempo=float(input("Ingrese el tiempo en segundos: "))
    
    atletas.append(nom)
    tiempos.append(tiempo)


suma=0
for i in range(5):
    suma=suma+tiempos[i]

promedio=suma/5

print("Promedio de tiempos:", promedio)


menor=tiempos[0]
mayor=tiempos[0]

posmenor=0
posmayor=0

for i in range(5):
    if tiempos[i] < menor:
        menor=tiempos[i]
        posmenor=i
        
    if tiempos[i] > mayor:
        mayor=tiempos[i]
        posmayor=i

print("Mejor tiempo:")
print(atletas[posmenor], menor)

print("Peor tiempo:")
print(atletas[posmayor], mayor)


print("Atletas que superaron el promedio:")

for i in range(5):
    if tiempos[i] < promedio:
        print(atletas[i], tiempos[i])