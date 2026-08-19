"""4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente."""


def cargar_inventario():
    inventario = []
    for i in range(5):
        nombre_articulo = input(f"Ingrese el nombre del artículo {i + 1}: ")
        precio = float(input(f"Ingrese el precio del artículo {nombre_articulo}: "))
        stock = int(input(f"Ingrese el stock del artículo {nombre_articulo}: "))
        inventario.append((nombre_articulo, precio, stock))
    return inventario

def imprimir_listado(inventario):
    print("\nListado de artículos:")
    for nombre_articulo, precio, stock in inventario:
        print(f"Artículo: {nombre_articulo}, Precio: {precio:.2f}, Stock: {stock}")

def valor_inventario(inventario):
    valor_total = sum(precio * stock for _, precio, stock in inventario)
    print(f"\nValor total del inventario: {valor_total:.2f}")

def alerta_reposicion(inventario):
    print("\nArtículos con stock menor o igual a 10 unidades:")
    for nombre_articulo, _, stock in inventario:
        if stock <= 10:
            print(f"Artículo: {nombre_articulo}, Stock: {stock}")



if __name__ == "__main__":
    inventario = cargar_inventario()
    imprimir_listado(inventario)
    valor_inventario(inventario)
    alerta_reposicion(inventario)

