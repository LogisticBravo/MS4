var logo = document.getElementById("flick");

logo.onmouseover = function(){
this.classList.remove("flicker");
this.classList.remove("no-flicker");
this.classList.add("flickering");
};

logo.onmouseout = function(){
this.classList.remove("flickering");
this.classList.add("no-flicker");
};
