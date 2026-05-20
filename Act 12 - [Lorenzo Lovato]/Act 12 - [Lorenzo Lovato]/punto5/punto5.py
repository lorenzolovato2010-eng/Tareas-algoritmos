# 5. Realizar un programa que lea los lados de n triángulos, e informar:
# a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
# iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b. Cantidad de triángulos de cada tipo.

cant= int(input("Ingrese la cantidad de triángulos"))
equilatero=0
isosceles=0
escaleno=0
for i in range(cant):
    lado1=int(input(f"Ingrese el lado 1 del triángulo {i+1}:"))
    lado2=int(input(f"Ingrese el lado 2 del triángulo {i+1}:"))
    lado3=int(input(f"Ingrese el lado 3 del triángulo {i+1}:"))

    if lado1==lado2 and lado2==lado3:
        print("El triángulo es equilátero")
        equilatero+=1
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        print("El triángulo es isósceles")
        isosceles+=1
    else:
        print("El triángulo es escaleno")
        escaleno+=1

print(f"Cantidad de triángulos equiláteros: {equilatero}")
print(f"Cantidad de triángulos isósceles: {isosceles}")
print(f"Cantidad de triángulos escalenos: {escaleno}")