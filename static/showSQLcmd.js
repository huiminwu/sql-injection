//INFORMATION PAGE HOVER OVER
var consequenceuno = document.getElementById("consequence-1");
var consequencedos = document.getElementById("consequence-2");
var consequencetres = document.getElementById("consequence-3");
var consequencecuatro = document.getElementById("consequence-4");
var consequencecinco = document.getElementById("consequence-5");
var consequenceseis = document.getElementById("consequence-6");

// THE DEMO
var username = document.getElementById("user");
var password = document.getElementById("pass");
var usernameinput = document.getElementById("usernameinput");
var passwordinput = document.getElementById("passwordinput");

usernameinput.addEventListener("input", function(e){
    console.log(e);
    username.innerHTML = usernameinput.value
});

passwordinput.addEventListener("input", function(e){
    password.innerHTML = passwordinput.value
});
