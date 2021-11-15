filter = document.getElementById("filter");
sonyFilter = document.getElementById("sonyFilter");
msFilter = document.getElementById("msFilter");
nintendoFilter = document.getElementById("nintendoFilter");
segaFilter = document.getElementById("segaFilter");
nvidiaFilter = document.getElementById("nvidiaFilter");
specialsFilter = document.getElementById("specialsFilter");

//filterLink and changeLink functions used to manipulate the href for the filter checkboxes to work.
function filterLink(category){
    var tempArray = filter.href.split(",");
    var index = tempArray.indexOf(category);
    tempArray.pop(index);
    tempArray.join(',');
    tempArray.toString();
    filter.href = tempArray;
}

function changeLink(checkbox, category){
    checkbox.addEventListener('change', function(){
        if (this.checked){
            filter.href += ','+category;
        }
        else {
            filterLink(category);
        };
    })
}

changeLink(sonyFilter,'sony');
changeLink(msFilter,'microsoft');
changeLink(nintendoFilter,'nintendo');
changeLink(segaFilter,'sega');
changeLink(nvidiaFilter,'nvidia');
changeLink(specialsFilter,'specials');

sortSelector = document.getElementById("sort-selector");

// code adapted from boutique ado milestone project
sortSelector.addEventListener('change', function(){
    var selector = this;
    var currentUrl = new URL(window.location);

    var selectedVal = selector.value;
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})

//Back to top button functionality. Shows the button on scroll down and hides it when at the top of a page. 
let backToTopButton = document.getElementById("btt");

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    backToTopButton.classList.add("d-block");
    backToTopButton.classList.remove("d-none");
  } else {
    backToTopButton.classList.add("d-none");
    backToTopButton.classList.remove("d-remove");
  }
}

backToTopButton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

//Implements a FA star for each of the ratings on the product page. Rounds the rating to the nearest integer.
var rating = document.querySelectorAll('[id^="rating-"]')

for (let i = 0; i < rating.length; i++) {
  let value = parseFloat(rating[i].innerText);
  Math.round(value)
  for (let j = 0; j < value; j++){
    rating[i].insertAdjacentHTML('afterbegin', '<i class="fas fa-star"></i>')
  }
}