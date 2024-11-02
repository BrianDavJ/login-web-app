const wrapper = document.querySelector('.wrapper');
const signupLink = document.querySelector('.signup-link');
const registerLink = document.querySelector('.register-link');
const registerButton = document.getElementById('register-btn');
const loginButton = document.getElementById('login-btn');

 import { checkLogin } from "./login-signup.js";
 import { registerUser } from "./login-signup.js";

registerLink.addEventListener('click',()=> {
    wrapper.classList.add('active');
})
signupLink.addEventListener('click',()=> {
    wrapper.classList.remove('active');
})

console.log("Adding event listeners");
loginButton.addEventListener('click',(event)=>{
    event.preventDefault();
    const email=document.getElementById('login-email').value;
    const psw=document.getElementById('login-psw').value;
    checkLogin(email,psw );
})

registerButton.addEventListener('click',(event)=>{
    event.preventDefault();
    const email=document.getElementById('login-email').value;
    const psw=document.getElementById('login-psw').value;
    registerUser(email,psw)
})