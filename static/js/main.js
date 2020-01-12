$(window).on('load resize', function(){
    maxLiCount = Math.floor($('#products').width()/250)

    $('.custom-media-list-products').css({
        'max-width' : (250*maxLiCount)+"px"})
});

$(document).ready(function(){
    $(window).on('load resize', function(){
        maxLiCount = Math.floor($('#products').width()/250)

        $('.custom-media-list-products').css({
            'max-width' : (250*maxLiCount)+"px"})
    }).trigger("resize");
    
    $("#close-messages-modal").on('click', function(){
        $("#messages-modal").removeClass('show')

    })
})