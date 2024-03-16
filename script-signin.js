//controles
let btnSignin = document.getElementById("btnSignin");
let usr = document.getElementById("username");
let psw = document.getElementById("password");
let error = document.getElementById("error");

//local storage
const usuarioMem = JSON.parse(localStorage.getItem("USUARIO"));
//eventos
btnSignin.addEventListener("click", () => Signin());

//funciones
function Signin() {
  let rta = validacion();
  if (rta.b) {
    const USUARIO = { username: usr.value, password: psw.value };
    localStorage.setItem("USUARIO", JSON.stringify(USUARIO));
    window.location.href = "login.html";
  } else {
    error.textContent = rta.ex;
  }
}
function validacion() {
  if (isNullOrEmpty(usr.value) || isNullOrEmpty(psw.value)) {
    return { b: false, ex: "Hay campos sin completar." };
  }
  if ("admin" == usr.value) {
    return { b: false, ex: "Ese nombre de usuario ya se encuentra en uso." };
  }
  if(usuarioMem && usr.value.toString() == usuarioMem.username.toString()){
    return { b: false, ex: "Ese nombre de usuario ya se encuentra en uso." };
  }
  return { b: true, ex: "" };
}
function isNullOrEmpty(str) {
  return !str || str.trim().length === 0;
}
