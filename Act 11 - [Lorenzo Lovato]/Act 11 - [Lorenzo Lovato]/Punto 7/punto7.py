# 7. Escribir un programa en el cual: dada una lista de tres valores numéricos
# distintos se calcule e informe su rango de variación (debe mostrar el mayor
# y el menor de ellos)

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1 > num2 and num1 > num3:
    print("El numero mayor es:")
    print(num1)
if num2 > num1 and num2 > num3:
    print("El numero mayor es:")
    print(num2)
if num3 > num1 and num3 > num2:
    print("El numero mayor es:")
    print(num3)
if num1 < num2 and num1 < num3:
    print("El numero menor es:")
    print(num1)
if num2 < num1 and num2 < num3:
    print("El numero menor es:")
    print(num2)
if num3 < num1 and num3 < num2:
    print("El numero menor es:")
    print(num3)
