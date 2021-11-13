/* 
Auto shows the sidebar shopping bag when products are added 
dismissis it automatically after a few seconds
*/
let addButton = document.getElementById("addToBag");
let shoppingBag = document.getElementById("shoppingBag")

if($(document.body.childNodes).hasClass("toast-container")){
    shoppingBag.setAttribute('Role','Dialog');
    shoppingBag.style = "Visibility: visible";
    shoppingBag.classList.add("show");
    setTimeout(function(){
        shoppingBag.setAttribute('Role','');
        shoppingBag.style = "Visibility: hidden";
        shoppingBag.classList.remove("show");
    }, 2000)
};