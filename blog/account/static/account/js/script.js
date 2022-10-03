var edit_btn = document.getElementById('edit');
var form_div = document.getElementById('form');

var state = false;
form_div.style.display = "none";

edit_btn.addEventListener('click', function() {
    state = !state;
    if (state) {
        form_div.style.display = "block";
        edit_btn.textContent = 'hide edit'
    } else {
        form_div.style.display = "none";
        edit_btn.textContent = 'edit profile';
    }
})