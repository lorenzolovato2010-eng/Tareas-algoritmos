/*
3. Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
onBlur)
*/
function validarClave() {
    let clv = document.getElementById('clave').value;
    if (clv.length < 7 || clv.length > 20) {
        alert('La clave debe tener entre 7 y 20 caracteres.');
    }
}