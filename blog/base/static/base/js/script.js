
let aside = document.querySelector('aside');
let icon = aside.querySelector('.menu-icon');
let li = aside.getElementsByClassName('nav-item');
let list_it = document.getElementById('list-mm');
let change = document.getElementById('change');
let state = false;

icon.onclick = ()=>{
    aside.classList.toggle('expand');
}
for(let i of li){
    i.onclick = activeLi;
}
function activeLi(){
    const list =Array.from(li);
    list.forEach(e=>e.classList.remove('active'));
    this.classList.add('active');
 
}
// let btn =document.querySelector("btn");
// let sidebar = document.querySelector('.side-bar');
// let searchbtn = aside.getElementsByClassName('.bx-search');

// btn.onclick  = function(){
//     sidebar.classList.toggle("active")
// }
// searchbtn.onclick  = function(){
//     sidebar.classList.toggle("active")
// }


// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}