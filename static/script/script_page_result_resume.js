$(document).ready(function () {
    var data_length = $('#data_length').text()
    $('table').css({
        'cursor' : 'default'
    })

    for (let index = 0; index < data_length; index++) {
        text_pdf = '#text_pdf_' + index
        $(text_pdf).val(index) 
    }

    for (let index = 0; index < data_length; index++) {
        text_gmail= '#text_gmail_' + index
        $(text_gmail).val(index)   
    }
    
});