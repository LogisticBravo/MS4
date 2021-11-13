/* 
sets up a session to track if the cookie consent toast was agreed to. The session 'value'
is set by appending a random number from between 0 and d.getTime() to the string 'user'
*/
window.onload = function () {
    let d = new Date();
    let uid = Math.floor(Math.random() * d.getTime());
    let cookie = document.getElementById("cookie");
    let cookieConsent = document.getElementById("accept");
    if (window.sessionStorage.length != 1) {
        cookie.classList.add("show");
    }
    cookieConsent.onclick = function () {
        window.sessionStorage.setItem("cookieconsent", "user" + uid);
        cookie.classList.remove("show");
    };
};