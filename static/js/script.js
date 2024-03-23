// Scroll to top on products.html
$('.btt-link').click(function(e) {
    window.scrollto(0,0)
})

// products.html product arrangement by sort type and direction
$('#sort-selector').change(function() {
var selector = $(this);
var currentUrl = new URL(window.location)
var selectedVal = selector.val();

if(selectedVal != "reset"){
    var sort = selectedVal.split("_")[0];
    var direction = selectedVal.split("_")[1];
    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);

    window.location.replace(currentUrl);
} else {
    currentUrl.searchParams.delete("sort", sort);
    currentUrl.searchParams.delete("direction", direction);

    window.location.replace(currentUrl);
}
})


// Disable +/- buttons outside 1-99 range on product_detail.html
// and cartview.html
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});


// On click Update items from cartview.html
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// On click Remove items from cartview.html
// https://youtu.be/0rRNZa7BR_Y 08:59
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId =$(this).attr('id').split('remove_')[1];
    var size = $(this).data('size');
    var url = `/cartview/remove/${itemId}`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};

    $.post(url, data)
     .done(function() {
        location.reload();
    });
    
})