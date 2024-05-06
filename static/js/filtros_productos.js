$(document).ready(function () {
    $('#orderby').change(function (e) {

        let parametros = new URLSearchParams(document.location.search);
        parametros = parametros.entries();
        let query = '?';
        let add = true;

        parametros.forEach((p, i) => {
            if (p[0] == 'orderby'){
                query += `${p[0]}=${e.target.value}&`;
                add = false;
            }
            else{
                query += `${p[0]}=${p[1]}&`;
            }
        });
        if (add){
            query += `orderby=${e.target.value}`
        }
        document.location.href = '/productos' + query;
    });
    $('#marca_filtro').change(function (e) {
        let parametros = new URLSearchParams(document.location.search);
        parametros = parametros.entries();
        let query = '?';
        let add = true;

        parametros.forEach((p, i) => {
            if (p[0] == 'marca'){
                query += `${p[0]}=${e.target.value}&`;
                add = false;
            }
            else{
                query += `${p[0]}=${p[1]}&`;
            }
        });
        if (add){
            query += `marca=${e.target.value}`
        }
        document.location.href = '/productos' + query;
    });
});