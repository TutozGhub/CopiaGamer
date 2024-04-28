$(document).ready(function () {
    $('#orderby').click(function (e) { 
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "/productos",
            data: "data",
            dataType: "dataType",
            success: function (response) {
                alert(data.orderby)
                window.location.href = '/productos'
                
            }
        });
    });
});