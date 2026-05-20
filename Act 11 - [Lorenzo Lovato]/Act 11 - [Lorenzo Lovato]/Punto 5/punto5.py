# 5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
# el número es positivo, negativo o nulo (es decir cero)

num1=int(input("Ingrese primer valor:"))

if num1 > 0:
    print("El numero es positivo")
elif num1 < 0:
    print("El numero es negativo")
else:
    print("El numero es nulo")


