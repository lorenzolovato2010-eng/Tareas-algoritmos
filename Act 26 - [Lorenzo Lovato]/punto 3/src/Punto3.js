/* Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”.*/

let Lolo=0
let Pablo=0
let Santi=0


let boton1=document.getElementById("boton1")
boton1.addEventListener("click", function()
{
    Lolo=Lolo+1
    alert("Se añadio voto a Lolo")
    let LoloVotos=document.getElementById("Lolo")
    LoloVotos.innerHTML=("Votos a Lolo",Lolo)
    if(Lolo>Pablo && Lolo>Santi){
        console.log("Lolo esta ganando")
    }
        else{
        console.log("Hay un empate")
    }
});


let boton2=document.getElementById("boton2")
boton2.addEventListener("click", function()
{
    Pablo=Pablo+1
    alert("Se añadio voto a Pablo")
    let PabloVotos=document.getElementById("Pablo")
    PabloVotos.innerHTML=("Votos a Pablo",Pablo)
    if(Pablo>Lolo && Pablo>Santi){
        console.log("Pablo esta ganando")
    }
    else{
        console.log("Hay un empate")
    }
});

let boton3=document.getElementById("boton3")
boton3.addEventListener("click", function()
{
    Santi=Santi+1
    alert("Se añadio voto a Santi")
    let SantiVotos=document.getElementById("Santi")
    SantiVotos.innerHTML=("Votos a Santi",Santi)
    if(Santi>Lolo && Santi>Pablo){
        console.log("Santi esta ganando")
    }
    else{
        console.log("Hay un empate")
    }
});