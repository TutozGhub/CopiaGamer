$(document).ready(function () {
    $('.armapc-paso').click(function (e) {
        const value = e.target.getAttribute("value");
        window.location.href = editarQuery('paso', value, '/armatupc')[0];
    });
    $('.btn-tipo-armado').click(function (e) {
        const value = e.target.getAttribute("value");
        window.location.href = editarQuery('tipo', value, '/armatupc')[0];
    });
    $('.armapc-producto').click(function (e) {
        const value = e.target.getAttribute("value");
        let paso = parseInt(e.target.getAttribute("paso"));
        const url = editarQuery(`productoPaso${paso}`, value, '/armatupc')[1];
        console.log(url);
        console.log(paso);
        window.location.href = editarQuery('paso', paso + 1, '/armatupc', url)[0]
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
            console.log(valor == p[1]);
        }
        else{
            query += `${p[0]}=${p[1]}&`;
        }
    });
    if (add){
        query += `${parametro}=${valor}`;
    }
    return [urlOut + query, query];
}