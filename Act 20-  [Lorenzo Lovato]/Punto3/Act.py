"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def cargar():
    lista=[]
    for x in range(10):
        num=int(input("Ingrese elemento:"))
        lista.append(num)
    return lista

def generar_listas(lista):
    positivos=[]
    negativos=[]

    for num in lista:
          if num >=0:
           positivos.append(num)
          else:
           negativos.append(num)
    return positivos, negativos

def imprimir(positivo, negativo):
   print("valores positivos:", positivo)
   print("valores negaivos:", negativo)

lista_principal= cargar()
lista_positiva, lista_negativa= generar_listas(lista_principal)        
imprimir(lista_positiva, lista_negativa)