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
    // prev and next buttons in user products modal form
    $("#add-product-page-2, #add-product-prev, #user-product-submit").hide()

    $("#add-product-prev").on("click", function(){
        $("#add-product-page-1, #add-product-next").show()
        $("#add-product-page-2, #add-product-prev, #user-product-submit").hide()
    })
    $("#add-product-next").on("click", function(){
        // check validation name and description. 
        // submit error due to validation (change model then js or manual focus?)
        $("#add-product-page-1, #add-product-next").hide()
        $("#add-product-page-2, #add-product-prev, #user-product-submit").show()      
    })
})