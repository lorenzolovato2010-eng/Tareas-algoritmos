/*Ejercicio 5: Gestión de Triaje en Guardia Médica (Prioridad)
Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
(Crítico).
Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
[[&quot;Paciente&quot;, Prioridad], ...]. Crear la función atender_siguiente(cola_espera) que seleccione
al próximo paciente en ser atendido.
Requisitos:
● Buscar al paciente que posea la prioridad más alta (mayor número).
● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
la guardia (criterio FIFO).
● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
indicando su nombre y nivel de urgencia.
Ejemplo de Entrada: [[&quot;Carlos&quot;, 1], [&quot;Ana&quot;, 3], [&quot;Roberto&quot;, 2], [&quot;Lucía&quot;, 3]] Salida
Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
la siguiente será Lucía (Nivel 3). */
function atenderSiguiente(cola){

    let mayor=0;

    for(let i=1;i<cola.length;i++){
        if(cola[i][1]>cola[mayor][1]){
            mayor=i;
        }
    }

    let paciente=cola.splice(mayor,1);

    console.log("Atiende primero:",paciente[0][0]);
    console.log("Nivel:",paciente[0][1]);
}

let cola=[
    ["Carlos",1],
    ["Ana",3],
    ["Roberto",2],
    ["Lucia",3]
];

atenderSiguiente(cola);

console.log(cola);