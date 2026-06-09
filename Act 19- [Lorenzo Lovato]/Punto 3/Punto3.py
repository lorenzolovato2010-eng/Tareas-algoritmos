"""
3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto.
"""

def enteros(a1, a2, a3=0, a4=0,a5=0):
    return a1+a2+a3+a4+a5

print(enteros(2,4))
print(enteros(2,4,6))
print(enteros(2,4,6,8))
print(enteros(2,4,6,8,10))
