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