/*Ejercicio 05: Control de Temperatura
Diseñar una página con un campo de texto para ingresar una temperatura y un botón
“Verificar”.
Cuando el usuario haga clic:
 Si la temperatura es menor a 10, mostrar en el documento el mensaje “Hace
frío” en azul.
 Si está entre 10 y 25, mostrar “Clima agradable” en verde.
 Si es mayor a 25, mostrar “Hace calor” en rojo.
Además, cada verificación debe registrarse en consola con la fecha y hora
exacta (usando Date()).*/


let textoInput = document.getElementById("areadetexto");

let boton=document.getElementById("boton")
boton.addEventListener("click", function()
{

        let texto = textoInput.value.trim();
    let producto = document.createElement("li");
    if (texto<10){
    producto.textContent = "Hace frio";
    lista.appendChild(producto);
    textoInput.value = '';}

    else if (texto>10 && texto<25){
    producto.textContent = "Clima agradable";
    lista.appendChild(producto);
    textoInput.value = '';}

        else {
    producto.textContent = "Hace calor";
    lista.appendChild(producto);
    textoInput.value = '';}

});
