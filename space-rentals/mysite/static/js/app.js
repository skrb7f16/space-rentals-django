let burger = document.getElementById('burger');
let overlay = document.getElementById('overlay')
let type = document.querySelectorAll('.type')

function showNav() {
    burger.style.width = "0"
    overlay.style.height = "60vh"
}

function closeNav() {
    burger.style.width = "50px"
    overlay.style.height = "0"
}

let i = 0
function showHeading() {
    if (i < 5) {
        type[i].style.height = "40px";
        type[i].style.width = "90%";
        i++;
        setTimeout(showHeading, 2000)
    }
    else{
        i=0;
        type.forEach(element=>{
            element.style.height="0"
            element.style.width="0"
        })
        setTimeout(showHeading,1000)
    }
}

if(document.getElementById('home')!=null){
    showHeading()
}


function showSignup(){
    document.getElementById('form-1').classList.add('selected-form')
    document.getElementById('form-2').classList.remove('selected-form')
    loginForm.style.display="none"
    signupForm.style.display="flex"
}

function showLogin(){
    document.getElementById('form-1').classList.remove('selected-form')
    document.getElementById('form-2').classList.add('selected-form')
    loginForm.style.display="flex"
    signupForm.style.display="none"
}