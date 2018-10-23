var $div_check = $(".checkbox");
$div_check.addClass("form-check");
var $label = $(".form-check label");
console.log(typeof $label);
$label.each(function(){
    var $input = $(this).children(":first");
    var text =  $(this).text();
    $(this).text("");
    $(this).append($input);
    $(this).append("<span class='label-text'>" + text + "</span>");
});
