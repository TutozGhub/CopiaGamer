$(document).ready(function () {
    $('.miniatura_ajax').click(function (e) { 
        e.preventDefault();
        const id_miniatura = e.target.id;
        const src_miniatura = e.target.src;

        $('.miniatura_ajax').removeClass('miniatura-select');
        $(`#${id_miniatura}`).addClass('miniatura-select');


        $('#expositor').attr('src', src_miniatura);
    });
});