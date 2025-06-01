$(document).ready(function () {
    var table = $('#tabla').DataTable({
        responsive: true,
        "language": {
            url: "/static/js/location/es_ES.json"
        }
    });
});
function eliminar() {
    var x = confirm("Desea Eliminar?");
    if (x)
        return true;
    else
        return false;
}