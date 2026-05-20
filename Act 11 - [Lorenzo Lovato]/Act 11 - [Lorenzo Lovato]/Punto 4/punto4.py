# 4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un
# número entero)

num1=int(input("Ingrese primer valor:"))
if num1<10:
    print("El numero tiene 1 digito:")
else:
    print("El numero tiene 2 digitos:")