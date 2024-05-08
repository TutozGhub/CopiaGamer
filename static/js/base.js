$(document).ready(function() {
    error_message('#login-form', '/login', '', '#login-error')
    error_message('#register-form', '/register', '', '#register-error')

    $('#search').keypress(function (e) {
    if (e.keyCode == 13){
            query = e.target.value;
            window.location.href = '/productos?search=' + query;
        }
    });
    $('#search').focus(function (e) { 
        $('#buscar-img').removeClass('nav__buscar--logo');
    });
    $('#search').focusout(function (e) { 
        $('#buscar-img').addClass('nav__buscar--logo');
    });
    $('.sumar-carro-ajax').click(function (e) { 
        e.preventDefault();
        window.location.href = `/add?id=${e.target.value}&url=${e.target.baseURI}`
    })

    $('#comprar').click(function (e) { 
        e.preventDefault();
        alert('¡¡Productos comprados!!')
        window.location.href = `/comprar`
    });
    
});

var sponsors = new Swiper(".mySwiperSponsors", {
    slidesPerView: 'auto',
    spaceBetween: 100,
    centeredSlides: true,
    loop: true,
    speed: 3000,
    autoplay: {
        delay: 1000,
        disableOnInteraction: false,
    },
});
sponsors.allowTouchMove = false;

function error_message(ID_form, RUTA, RUTA_SALIDA, ID_error){

    // codigo de chat gpt, yo lo adapte para hacerlo reutilizable
    $(ID_form).submit(function(e) {
        e.preventDefault();

        const formData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: RUTA,
            data: formData,
            success: function(response) {
                if (response.success){
                    window.location.href = RUTA_SALIDA;
                }
                else{
                    $(ID_error).html(`
                    <div class="alert alert-danger alert-dismissible fade show" role="alert">
                        ${response.message}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                    `);
                }
            },
            error: function(xhr, status, error) {
            }
        });
    });
}