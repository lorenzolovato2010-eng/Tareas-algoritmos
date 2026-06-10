"""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def cargar_datos():
    nombre=[]
    precio=[]
    for x in range(5):
        valor1=input("Ingrese el nombre del articulo:")
        nombre.append(valor1)
        valor2=int(input("Ingrese el precio del articulo:"))
        precio.append(valor2)
    return nombre, precio

def imprimir(nombre, precio):
    print("---Lista de Articulos---")
    for x in range(len(nombre)):
        print("Articulo", nombre[x] ,"|", "Precio", precio[x])

def mas_caro(nombre, precio):
    caro=precio[0]
    posicion_mayor=0
    for x in range(1,len(precio)):

        if precio[x]>caro:
            caro=precio[x]
            posicion_mayor = x
    print("El articulo mas caro es¨:", nombre[posicion_mayor])

def importe(nombre, precio):
    limite= int(input("Ingrese un importe"))
    for i in range(5):
        if precio[i]<= limite:
         print("Articulos con precio menor o igual", nombre[i])
        

lista_nombres, lista_precios = cargar_datos()

imprimir(lista_nombres, lista_precios)
mas_caro(lista_nombres, lista_precios)
importe(lista_nombres, lista_precios)