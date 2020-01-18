$(window).on('load resize', function(){
    maxLiCount = Math.floor($('#products').width()/270) || Math.floor($('#user-products').width()/270) || Math.floor($('#user-cart').width()/270);
    ulMaxWidth = 270*maxLiCount;
    if (maxLiCount == 1) {
        ulMaxWidth = 250;
    }
    $('.custom-media-list-products').css({
        'max-width' : (ulMaxWidth)+"px",
        'min-width':"250px"})
});

$(document).ready(function(){

    // messages-modal
    $(".close-modal").on('click', function(){
        $(".opened").removeClass('show')
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