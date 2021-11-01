filter = document.getElementById("filter");
sonyFilter = document.getElementById("sonyFilter");
msFilter = document.getElementById("msFilter");
nintendoFilter = document.getElementById("nintendoFilter");
segaFilter = document.getElementById("segaFilter");
nvidiaFilter = document.getElementById("nvidiaFilter");
specialsFilter = document.getElementById("specialsFilter");

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

// $('#sort-selector').change(function() {
//     var selector = $(this);
//     var currentUrl = new URL(window.location);

//     var selectedVal = selector.val();
//     if(selectedVal != "reset"){
//         var sort = selectedVal.split("_")[0];
//         var direction = selectedVal.split("_")[1];

//         currentUrl.searchParams.set("sort", sort);
//         currentUrl.searchParams.set("direction", direction);

//         window.location.replace(currentUrl);
//     } else {
//         currentUrl.searchParams.delete("sort");
//         currentUrl.searchParams.delete("direction");

//         window.location.replace(currentUrl);
//     }
// })