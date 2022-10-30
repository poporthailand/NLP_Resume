
$(document).ready(function(){
    

    var checkscroll = true
    console.log($(document).height())

    $('.scrollTobuttom').click(function(){
        checkscroll = false

        
        $('html,body').animate({scrollTop: $(document).height()}, 1);

        $(".scrollToup").attr("hidden",checkscroll);

        $("#tableResult").attr("hidden" , checkscroll);
        return false
    })

    $('.scrollToup').click(function(){
        checkscroll = true

        $('html,body').animate({scrollTop: 0}, 1);
        
        $(".scrollToup").attr("hidden",checkscroll);
        return false
    })

    $('#btnBack').click(function(){
        checkscroll = true
        
        $('html,body').animate({scrollTop: 0}, 1);
        
        // $(".scrollToup").attr("hidden",checkscroll);

        // $("#tableResult").attr("hidden" , checkscroll);
        return false
    })

    $('.btnLoad').click(function(){
        $('.btnLoad').html("<div class='loader'></div>")
        
        setTimeout(() =>{
            $('.btnLoad').html("COMPLETE")
            $('.btnLoad').css("background-color" , "green")
        },2000)
    })

    $('.btnClear').click(function(){
        $('.btnLoad').html("UPLOAD")
        
        $('.btnLoad').css("background-color" , "#ffc404")
    })
})