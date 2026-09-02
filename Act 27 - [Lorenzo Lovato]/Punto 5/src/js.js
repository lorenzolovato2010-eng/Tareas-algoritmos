/*
5. Generar un presupuesto de un equipo de computación a partir de tres
objetos de tipo SELECT que nos permiten seleccionar:
Procesador (Intel I3 - $400, Intel I5 $600, Intel I7 $800).
Monitor (Samsung 20&#39; - $250, Samsung 22&#39; - $350, Samsung 26&#39; - $550)
Disco Duro(500 Gb - $300, 1 Tb - $440, 3 Tb - $500)
Para cada característica indicamos string a mostrar (Ej. Intel I3) y el
valor asociado a dicho string (Ej. 400).
Al presionar un botón &quot;Calcular&quot; mostrar el presupuesto en un objeto de
tipo TEXT.
*/
function calcularPresupuesto(){
   let selProc = document.getElementById("procesador");
   let valProc = parseInt(selProc.options[selProc.selectedIndex].value) ;

   let selMon = document.getElementById("monitor");
   let valMon = parseInt(selMon.options[selMon.selectedIndex].value) ;

   let selDisco = document.getElementById("disco");
   let valDisco = parseInt(selDisco.options[selDisco.selectedIndex].value) ;

   let Total = valProc + valMon + valDisco;

   document.getElementById("resultado").value = "$" + Total;
}


