jQuery(document).ready(function($) {
    $(".statement-list").sortable();
    $(".statement-list").disableSelection();
    $('#rank_statements').bind('submit', function() {
        var sort_data;
        $('.statement-list').each(function() {
            sort_data += $(this).sortable("serialize");
        });
        console.log(sort_data)
        return false;
    });
});
