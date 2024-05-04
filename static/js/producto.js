$(document).ready(function () {
    $('.miniatura_ajax').click(function (e) { 
        e.preventDefault();
        const id_miniatura = e.target.id;
        const src_miniatura = e.target.src;

        $('.miniatura_ajax').removeClass('miniatura-select');
        $(`#${id_miniatura}`).addClass('miniatura-select');


        $('#expositor').attr('src', src_miniatura);
    });

    $('#preguntar').click(function(e) { 
        e.preventDefault();
        let parametros = new URLSearchParams(window.location.search);
        parametros = parametros.values();
        parametros.forEach(p => {
            id = p[0]
        });
        
        pregunta = document.getElementById('pregunta').value;
        if (pregunta != ''){
            url = e.target.baseURI;
            query = `?id_producto=${id}&pregunta=${pregunta}&url=${url}`;
            window.location.href = '/preguntar' + query;
        }
        else{
            alert('Debe escribir algo')
        }
    });

    
    $('.producto-ajax').hide();
    $('#especificaciones').show();
    $('.btn-menu-producto').removeClass('btn-menu-producto-selected');
    $('#btn-especificaciones').addClass('btn-menu-producto-selected');

    $('#btn-especificaciones').click(function(e) { 
        e.preventDefault();
        $('.producto-ajax').hide();
        $('#especificaciones').show();
        
        $('.btn-menu-producto').removeClass('btn-menu-producto-selected');
        $('#btn-especificaciones').addClass('btn-menu-producto-selected');
    });
    $('#btn-preguntas').click(function(e) { 
        e.preventDefault();
        $('.producto-ajax').hide();
        $('#preguntas').show();

        $('.btn-menu-producto').removeClass('btn-menu-producto-selected');
        $('#btn-preguntas').addClass('btn-menu-producto-selected');
    });
});