//controles
let btnLogin = document.getElementById("btnLogin");
let usr = document.getElementById("username");
let psw = document.getElementById("password");
let error = document.getElementById("error");

//local storage
const usuarioMem = JSON.parse(localStorage.getItem("USUARIO"));

//eventos
btnLogin.addEventListener("click", () => Login());

//funciones
function Login() {
  let rta = validacion();
  if (rta.b) {
    error.textContent = "";
    localStorage.setItem("usernameMem", usr.value.toString());
    localStorage.setItem("loged", 1);
    window.location.href = "main.html";
  } else {
    error.textContent = rta.ex;
  }
}
function validacion() {
  let usuario = usr.value;
  let contraseña = psw.value;
  let usrs = ["admin"];
  let psws = ["admin"];
  if (usuarioMem){
    usrs.push(usuarioMem.username)
    psws.push(usuarioMem.password)
  }
  if (isNullOrEmpty(usuario) || isNullOrEmpty(contraseña)) {
    return { b: false, ex: "Hay campos sin completar." };
  }
  if (usrs.includes(usuario)) {
    if (psws[usrs.indexOf(usuario)] != contraseña){
      return { b: false, ex: "Nombre de usuario o contraseña incorrecto." };
    }
  } else {
    return { b: false, ex: "Nombre de usuario o contraseña incorrecto." };
  }
  return { b: true, ex: "" };
}
function isNullOrEmpty(str) {
  return !str || str.trim().length === 0;
}
