////////////////////////
// JavaScript for posts page
////////////////////////

$(function() {
    // Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        $(this).next().toggle();
    })
})