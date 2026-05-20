# 3. Realizar un programa que solicite la carga por teclado de dos números, si el
# primero es mayor al segundo informar su suma y diferencia, en caso
# contrario informar el producto y la división del primero respecto al segundo.

num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
suma=num1+num2
diferencia=num1-num2
producto=num1*num2
division= num1/num2
if num1>num2:
   print("La suma de los numeros es:")
   print (suma)
   print("La diferencia es de:")
   print(diferencia)
   
else:
   print("El producto de los numeros es:")
   print(producto)
   print("La division del primer numero respecto al segundo es:")
   print(division)

