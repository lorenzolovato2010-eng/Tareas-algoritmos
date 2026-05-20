# 4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a. La cantidad de valores ingresados negativos.
# b. La cantidad de valores ingresados positivos.
# c. La cantidad de múltiplos de 15.
# d. El valor acumulado de los números ingresados que son pares.
negativos=0
positivos=0 
multiplos=0
acumulado=0
for i in range(10):
    valor=int(input(f"Ingrese el valor {i+1}:"))

    if valor<0:
        negativos+=1
    elif valor>0:
        positivos+=1
    if valor%15==0:
        multiplos+=1
    if valor%2==0:
        acumulado+=valor
print(f"La cantidad de valores ingresados negativos es: {negativos}")
print(f"La cantidad de valores ingresados positivos es: {positivos}")
print(f"La cantidad de múltiplos de 15 es: {multiplos}")
print(f"El valor acumulado de los números ingresados que son pares es: {acumulado}")  
