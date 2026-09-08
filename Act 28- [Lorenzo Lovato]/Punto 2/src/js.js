/*
2. Confeccionar una página de visitas a un sitio, solicitar ingresar el nombre de una
persona, su mail y los comentarios (TEXTAREA). Mostrar luego llamando a la función
alert los datos ingresados.
*/
function mostrarDatos() {
    let nom = document.getElementById('nombre').value;
    let mail = document.getElementById('mail').value;
    let com = document.getElementById('comentarios').value;
    alert('Nombre: ' + nom + ' \nMail: ' + mail + ' \nComentarios: ' + com);
}