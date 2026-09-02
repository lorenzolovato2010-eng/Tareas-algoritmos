/* 
1. Crear un formulario con tres botones con las leyendas "1", "2" y "3".
Mostrar un mensaje indicando qué botón se presionó.
*/

function numero1(){
let boton1=document.getElementById("boton1")
boton1.addEventListener("click", function()
{
    alert("Se eligio 1")
});
}

function numero2(){
let boton2=document.getElementById("boton2")
boton2.addEventListener("click", function()
{
    alert("Se eligio 2")
});
}

function numero3(){
let boton3=document.getElementById("boton3")
boton3.addEventListener("click", function()
{
    alert("Se eligio 3")
});
}

numero1()
numero2()
numero3()