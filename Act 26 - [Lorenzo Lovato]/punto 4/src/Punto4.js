/*Ejercicio 04: Lista de Compras Dinámica

Confeccionar una página con un campo de texto y un botón “Agregar”.
Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
a una lista (&lt;ul&gt;).
Además:
 La lista debe permitir eliminar un producto haciendo clic sobre él.
 En consola debe mostrarse en todo momento la cantidad de productos
actuales en la lista.*/
let textoInput = document.getElementById("areadetexto");

let boton=document.getElementById("boton")
boton.addEventListener("click", function()
{
    let texto = textoInput.value.trim();
    let producto = document.createElement("li");
    producto.textContent = texto;
    lista.appendChild(producto);
    textoInput.value = '';
});

