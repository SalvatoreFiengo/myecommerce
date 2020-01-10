$(window).on('load resize', function(){
    newWidth = Math.floor($('#products').width()/250)
    console.log(newWidth)
    $('.products-wrapper').css({'width' : (254*newWidth)+"px"})
})

$(document).ready(function(){
    $(window).on('load resize', function(){
        newWidth = Math.floor($('#products').width()/250)
        console.log(newWidth)
        $('.products-wrapper').css({'width' : (254*newWidth)+"px"})
    })
    
    $("#close-messages-modal").on('click', function(){
        $("#messages-modal").removeClass('show')

    })
})