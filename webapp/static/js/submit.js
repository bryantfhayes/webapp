$(function() {
    $('#btnSubmit').click(function() {
 
        $.ajax({
            url: '/submitPost',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $('#btnSubmit').html("success!");
            },
            error: function(error) {
                $('#btnSubmit').html("error!");
            }
        });
    });
});