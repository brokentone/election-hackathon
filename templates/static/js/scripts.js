jQuery(document).ready(function($) {
    $(".statement-list").sortable();
    $(".statement-list").disableSelection();
    $('#rank_statements').bind('submit', function() {
        $('.statement-list').each(function() {
            console.log($(this).sortable("serialize"));
        });
    });
});
