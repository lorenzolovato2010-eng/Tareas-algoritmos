"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""
def ordenar(a, b, c):
    if a < b and a < c:
        if b < c:
            return a, b, c
        else:
            return a, c, b
    else:
        if b < a and b < c:
            if a < c:
                return b, a, c
            else:
                return b, c, a
        else:
            if a < b:
                return c, a, b
            else:
                return c, b, a
def cargar():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    return ordenar(valor1, valor2, valor3)
print("Los valores ordenados de menor a mayor son: ", cargar())
