var username = document.getElementById("user");
var password = document.getElementById("pass");
var usernameinput = document.getElementById("usernameinput");
var passwordinput = document.getElementById("passwordinput");

usernameinput.addEventListener("oninput", function(e){
    console.log(e);
    username.innerHTML = 'y'
});
			       
passwordinput.addEventListener("oninput", function(e){
    password.innerHTML = 'y';
});

var button = document.getElementById("but")
button.addEventListener("onclick", function(e){
    console.log(e)
});
