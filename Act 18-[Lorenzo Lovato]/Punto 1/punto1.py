"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""

# Definición de la función

def cargar():
 
    print("--- Carga de tres números enteros ---")
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    
    if valor1 <= valor2 and valor1 <= valor3:
        menor = valor1
    elif valor2 <= valor3:
        menor = valor2
    else:
        menor = valor3
        
    print("El menor de los tres valores ingresados es:", menor)


cargar()
cargar()
