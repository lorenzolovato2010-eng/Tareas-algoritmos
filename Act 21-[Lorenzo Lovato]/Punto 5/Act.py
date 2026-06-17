"""
5-Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

def cargarDatos():
    productos = []
    for numeroProducto in range(5):
        nombreProducto = input(f"Ingrese el nombre del producto n{numeroProducto +1}: ")
        precio = int(input("Ingrese el precio: "))
        productos.append((nombreProducto, precio))
    return productos

def listarProductos(productos):
    print("Lista de productos:")
    for producto in productos:
        print("Producto:", producto[0], "- Precio:", producto[1])

def productosEntre(productos):
    print("Los productos con precios entre 10 y 15 son:")
    for producto in productos:
        nombreProducto = producto[0]
        precio = producto[1]
        if precio >= 10 and precio <= 15:
            print(nombreProducto,":", precio)

productos = cargarDatos()
listarProductos(productos)
productosEntre(productos)