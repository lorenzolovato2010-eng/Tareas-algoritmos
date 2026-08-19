/*Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = [&quot;Boca&quot;, &quot;River&quot;, &quot;Racing&quot;] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8). */

function debeIntercambiar(puntos, diferencia, i, j){

    if(puntos[j] > puntos[i]){
        return true;
    }

    if(puntos[j] == puntos[i] &&
       diferencia[j] > diferencia[i]){

        return true;
    }

    return false;
}


function intercambiar(equipos, puntos, diferencia, i, j){

    let aux = equipos[i];
    equipos[i] = equipos[j];
    equipos[j] = aux;

    aux = puntos[i];
    puntos[i] = puntos[j];
    puntos[j] = aux;

    aux = diferencia[i];
    diferencia[i] = diferencia[j];
    diferencia[j] = aux;
}


function ordenar(equipos, puntos, diferencia){

    for(let i = 0; i < equipos.length - 1; i++){

        for(let j = i + 1; j < equipos.length; j++){

            if(debeIntercambiar(puntos, diferencia, i, j)){
                intercambiar(equipos, puntos, diferencia, i, j);
            }
        }
    }
}


function mostrarTabla(equipos, puntos, diferencia){

    for(let i = 0; i < equipos.length; i++){

        console.log(
            i + 1,
            equipos[i],
            puntos[i],
            "DG:",
            diferencia[i]
        );
    }
}


let equipos = ["Boca", "River", "Racing"];
let puntos = [12, 15, 12];
let diferencia = [8, 5, 10];

ordenar(equipos, puntos, diferencia);

mostrarTabla(equipos, puntos, diferencia);