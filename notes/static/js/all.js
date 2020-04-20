// Side bar effects
$('#sidebar-link').hover(
    function () {
        $(this).addClass('animated');
        $(this).addClass('flipInX');
    }

)


// Main editor
CKEDITOR.replace('editor');
