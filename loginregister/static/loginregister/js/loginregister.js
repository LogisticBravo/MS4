var transitionButton = document.getElementById("transition");

var ltr = document.getElementById("ltr");
var rtl = document.getElementById("rtl");

// Adds and removes animation classes dependant on which class is active to allow for the transition of the left and right cards
transitionButton.onclick = function transition() {
  if (ltr.classList.contains("ltr") == true) {
    ltr.classList.remove("ltr");
    ltr.classList.add("ltr-reverse");
    ltr.classList.remove("drop-shadow-green");
    ltr.classList.add("drop-shadow-pink");
  }
  else if (ltr.classList.contains("ltr-reverse") == true || ltr.classList.contains("ltr") == false) {
    ltr.classList.remove("ltr-reverse");
    ltr.classList.add("ltr");
    ltr.classList.add("drop-shadow-green");
    ltr.classList.remove("drop-shadow-pink");
  }
  if (rtl.classList.contains("rtl") == true) {
    rtl.classList.remove("rtl");
    rtl.classList.add("rtl-reverse");
  }
  else if (rtl.classList.contains("rtl-reverse") == true || rtl.classList.contains("rtl") == false) {
    rtl.classList.add("rtl");
    rtl.classList.remove("rtl-reverse");
  }

  var signupForm = document.getElementById("signup_form");
  var loginForm = document.getElementById("login_form");
  var loginHeader = document.getElementById("signin_h1");
  var signupHeader = document.getElementById("createacc_h1");

  // adds and removes classes so that the right content is shown respective of the active card panel
  if (signupForm.classList.contains("d-none") == true) {
    setTimeout(function () {
      loginForm.classList.add("d-none", "disabled");
      ltr.classList.remove("bg-colorgradient");
      signupForm.classList.remove("d-none", "disabled");
      signupHeader.classList.remove("d-none");
      loginHeader.classList.add("d-none");
      transitionButton.textContent = "Sign In";
      transitionButton.classList.add("btn-outline-green");
      transitionButton.classList.remove("btn-outline-pink");
      signupHeader.nextElementSibling.classList.add("text-white");
      transitionButton.parentNode.firstElementChild.innerText = "Welcome Back";
      transitionButton.parentNode.firstElementChild.classList.add("text-white");
      transitionButton.parentNode.firstElementChild.style.borderBottom = "none";
      transitionButton.parentNode.firstElementChild.classList.remove("text-light-blue");
      transitionButton.parentElement.children[1].classList.add("d-none");
      transitionButton.parentElement.children[2].classList.remove("d-none");
    }, 500);
  }
  else {
    setTimeout(function () {
      signupForm.classList.add("d-none", "disabled");
      loginForm.classList.remove("d-none", "disabled");
      ltr.classList.add("bg-colorgradient");
      loginHeader.classList.remove("d-none");
      signupHeader.classList.add("d-none");
      transitionButton.textContent = "Sign Up";
      transitionButton.classList.remove("btn-outline-green");
      transitionButton.classList.add("btn-outline-pink");
      signupHeader.nextElementSibling.classList.remove("text-white");
      transitionButton.parentNode.firstElementChild.innerText = "Hello, Friend!";
      transitionButton.parentNode.firstElementChild.classList.add("text-light-blue");
      transitionButton.parentNode.firstElementChild.style.borderBottom = "";
      transitionButton.parentNode.firstElementChild.classList.remove("text-white");
      transitionButton.parentElement.children[2].classList.add("d-none");
      transitionButton.parentElement.children[1].classList.remove("d-none");
    }, 500);
  }
};

