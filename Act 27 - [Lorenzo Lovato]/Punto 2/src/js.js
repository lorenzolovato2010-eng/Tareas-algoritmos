/*
2. Cargar un nombre y un apellido en dos text. Al presionar un botón,
concatenarlos y mostrarlos en un tercer text (Tener en cuenta que
podemos modificar la propiedad value de un objeto TEXT cuando ocurre
un evento).
*/

function sumar(idPrimero, idSegundo) {

    let boton1 = document.getElementById("sumar"); 
    boton1.addEventListener("click", function() {
       
        let input1 = document.getElementById(idPrimero);
        let input2 = document.getElementById(idSegundo);    
        let total = input1.value + " " + input2.value;
        
        alert("El resultado es: " + total);
    });
}

sumar("primera", "segunda");

