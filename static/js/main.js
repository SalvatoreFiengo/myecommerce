$(window).on('load resize', function(){
    maxLiCount = Math.floor($('#products').width()/250) || Math.floor($('#user-products').width()/250)
    $('.custom-media-list-products').css({
        'max-width' : (250*maxLiCount)+"px",
        'min-width':"250px"})
});

$(document).ready(function(){

    // messages-modal
    $("#close-messages-modal").on('click', function(){
        $("#messages-modal").removeClass('show')
    })
})