/*
4. Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma.
*/

function precio(){
    let seleccion = document.getElementById("selectPizza");
    let precioSeleccionado = seleccion.options[seleccion.selectedIndex].value;
    document.getElementById("textPrecio").value=precioSeleccionado;
    
}