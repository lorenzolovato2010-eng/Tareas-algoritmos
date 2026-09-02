/*
3. Disponer dos campos de texto tipo password. Cuando se presione un
botón mostrar si las dos claves ingresadas son iguales o no (es muy
común solicitar al operador el ingreso de dos veces de su clave para
validar si las escribió correctamente, esto se hace cuando se crea una
password para el ingreso a un sitio o para el cambio de una existente).
Tener en cuenta que podemos emplear el operador == para ver si dos
string son iguales.
*/

function verificar(idPrimero, idSegundo) {

    let boton1 = document.getElementById("verificar"); 
    boton1.addEventListener("click", function() {
       
        let input1 = document.getElementById(idPrimero);
        let input2 = document.getElementById(idSegundo);    
       
        if(input1.value == input2.value){
            alert("La contraseña es correcta")
        }
       
        else{
            alert("La contrasela es incorrecta")
        }
    });
}

verificar("primera", "segunda");

