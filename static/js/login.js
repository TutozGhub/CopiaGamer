$(document).ready(function() {
    error_message('#login-form', '/login', '', '#login-error')
    error_message('#register-form', '/register', '', '#register-error')
});

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