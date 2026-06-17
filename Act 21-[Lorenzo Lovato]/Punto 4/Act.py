"""
4-
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""

def cargar_candidatos():
    lista_candidatos=[]
    
    print("--Carga de votos por candidato--")

    for i in range(3):
        nombre= input("Ingrese nombre del candidato:")
        lista_provincias=[]

        cant_provincias = int(input(f"¿Cuantas provincias queres cargar para "+ nombre+"?"))
        for j in range(cant_provincias):
            provincia= input(f"Nombre de la provincia:")
            votos= int(input(f"Cantidad de votos en "+provincia+":"))

            lista_provincias.append((provincia,votos))
        
        lista_candidatos.append([nombre, lista_provincias])

    return lista_candidatos

def imprimir_total_votos(lista_candidatos):
    print("--Resultados Totales--")
    for candidato in lista_candidatos:      
        nombre=candidato[0]
        provincias_votos= candidato[1]

        total_votos=0
        for elemento in provincias_votos:
            total_votos += elemento[1]
        
        print(f"Candidato:",nombre,"| Votos totales", total_votos)

candidatos = cargar_candidatos()
imprimir_total_votos(candidatos)