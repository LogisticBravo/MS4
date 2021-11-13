// adapated from ci walkthrough project for boutique ado
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})