# 6. De un operario se conoce su sueldo y los años de antigüedad. Se pide
# confeccionar un programa que lea los datos de entrada e informe:
# a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
# años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10
# años, otorgarle un aumento de 5 %.
# c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
# cambios.


num1 = int(input("Ingrese su sueldo: "))
num2 = int(input("Ingrese los años de antigüedad: "))

if num1<500 and num2>=10:
    aumento = num1 * 0.20
    sueldoFinal = num1 + aumento
    print("El sueldo a pagar es:")
    print(sueldoFinal)
elif num1<500 and num2<10:
    aumento = num1 * 0.05
    sueldoFinal = num1 + aumento
    print("El sueldo a pagar es:",)
    print(sueldoFinal)

elif num1 >= 500:
    print("El sueldo a pagar es:")
    print(num1)