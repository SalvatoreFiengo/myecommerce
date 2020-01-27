$(window).on('load resize', function () {
    maxLiCount = Math.floor($('#products').width() / 270) || Math.floor($('#user-products').width() / 270)
    ulMaxWidth = 278 * maxLiCount;
    if (maxLiCount == 1) {
        ulMaxWidth = 250;
    }
    $('.custom-media-list-products').css({
        'max-width': (ulMaxWidth) + "px",
        'min-width': "250px"
    })
});

$(document).ready(function () {

    // messages-modal
    $(".close-modal").on('click', function () {
        $(".opened").removeClass('show')
    })
    // prev and next buttons in user products modal form
    $("#add-product-page-2, #add-product-prev, #user-product-submit").hide()

    $("#add-product-prev").on("click", function () {
        $("#add-product-page-1, #add-product-next").show()
        $("#add-product-page-2, #add-product-prev, #user-product-submit").hide()
    })
    $("#add-product-next").on("click", function () {
        $("#add-product-page-1, #add-product-next").hide()
        $("#add-product-page-2, #add-product-prev, #user-product-submit").show()
    })
    // cart plus minus 
    $('.plus').on('click', function () {
        input = $(this).siblings("input")
        max = input.attr('max');
        id = input.attr('data-id');
        inputValue = input.val();
        if (inputValue < max) {
            inputValue++;
        }
        input.val(inputValue);
        $("#adjust-cart-" + id).submit();
    })
    $('.minus').on('click', function () {
        input = $(this).siblings("input")
        min = input.attr('min');

        id = input.attr('data-id')
        inputValue = input.val();
        if (inputValue > min) {
            inputValue--;
        }
        input.val(inputValue);
        $("#adjust-cart-" + id).submit();
    })
    // add a product in user prodducts
    $('#add-product-image-link').on('click', function () {
        $('#add-product-via-img').submit();
    })
    //Edit Profile is vendor checkbox behaviour
    $("#id_reseller").on('change', function () {
        if (this.checked) {
            $('#is_vendor').text('No').removeClass('btn-success').addClass('btn-danger');
        } else (
            $('#is_vendor').text('Yes').removeClass('btn-danger').addClass('btn-success')
        )
    });
})