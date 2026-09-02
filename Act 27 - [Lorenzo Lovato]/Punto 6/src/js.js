/*
6. Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT)
*/
function corregir(){
    let correctas = 0;
    let incorrectas = 0;

    let r1 = document.getElementById("p1").value;
    let r2 = document.getElementById("p2").value;
    let r3 = document.getElementById("p3").value;
    let r4 = document.getElementById("p4").value;

    let respuestas = [r1, r2, r3, r4];

    respuestas.forEach(function(resp){
        if (resp == "correcta") {
            correctas++;
        } else {
            incorrectas++;
        }
    });

    document.getElementById("cantCorrectas").value = correctas;
    document.getElementById("cantIncorrectas").value = incorrectas;
}
