// Update quantity on click
$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function (e) {
    // Retrieves item Id and prepares the remove URL
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/cart/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken
    };

    // Post removal URL
    $.post(url, data)
        .done(function () {
            location.reload();
        });
})