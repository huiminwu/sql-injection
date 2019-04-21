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
