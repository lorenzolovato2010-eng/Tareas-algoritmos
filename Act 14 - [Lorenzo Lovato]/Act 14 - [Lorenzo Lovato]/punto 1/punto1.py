#1. Definir una lista que almacene por asignación los nombres de 5 personas.
#Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.
nombres=["Lorenzo", "Pablo", "Marzo", "Abril"]
contador=0
for x in nombres:
    if len(x)>5:
        contador+=1
        print("el nombre",x," tiene mas de 5 caracteres")
print("la cantidad de nombres con  caracteres o mas es:", contador)