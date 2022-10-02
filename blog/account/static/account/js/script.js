var edit_btn = document.getElementById('edit');
var form_div = document.getElementById('form');

var state = false;
form_div.style.display = "none";

edit_btn.addEventListener('click', function() {
    console.log('hi')
    state = !state;
    if (state) {
        form_div.style.display = "block";
    } else {
        form_div.style.display = "none";
    }
})