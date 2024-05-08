$(document).ready(function () {
    $('.armapc-paso').click(function (e) {
        const value = e.target.getAttribute("value");
        $(location).attr('href', editarQuery('paso', value, '/armatupc')[0]);
    });
    $('.btn-tipo-armado').click(function (e) {
        const value = e.target.getAttribute("value");
        $(location).attr('href', editarQuery('tipo', value, '/armatupc', '')[0]);
    });
    $('.armapc-producto').click(function (e) {
        const value = e.target.getAttribute("value");
        let paso = parseInt(e.target.getAttribute("paso"));
        let url = editarQuery(`productoPaso${paso}`, value, '/armatupc')[1];
        if (paso == 1 || paso == 2){
            let tipo = parseInt(e.target.getAttribute("tipo"));

            if (tipo == 13) tipo = 10;
            if (tipo == 14) tipo = 11;

            url = editarQuery(`tipo`, tipo, '/armatupc', url)[1];
        }
        $(location).attr('href', editarQuery('paso', paso + 1, '/armatupc', url)[0]);
    });
});

function editarQuery(parametro, valor, urlOut, urlIn=window.location.search){
    let parametros = new URLSearchParams(urlIn);
    parametros = parametros.entries();
    let query = '?';
    let add = true;

    parametros.forEach((p) => {
        if (p[0] == parametro){
            query += `${p[0]}=${valor}&`;
            add = false;
        }
        else{
            query += `${p[0]}=${p[1]}&`;
        }
    });
    if (add){
        query += `${parametro}=${valor}&`;
    }
    return [urlOut + query, query];
}