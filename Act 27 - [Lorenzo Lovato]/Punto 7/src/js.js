/*7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió.*/

boton1=""
boton2=""
boton3=""


function Calcular(){
    if (document.getElementById("checkbox1").checked)
{
boton1="Futbol"
}
    if (document.getElementById("checkbox2").checked)
{
boton2="Basquet"
}
    if (document.getElementById("checkbox3").checked)
{
boton3="Tenis"
}
alert(`Jugas a: ${boton1}  ${boton2} ${boton3}`)

}