//#region Controles
//#region Botones
let btnCarro = document.getElementById("buylist");
let btnAñadir = document.getElementById("add");
let btnLogin = document.getElementById("login");
let btnLogout = document.getElementById("logout");
let btnSignin = document.getElementById("signin");
//#endregion
//#region Otros
let carro = document.getElementById("products");
let msg = document.getElementById("user");
//#endregion

//local storage
const carroMem = localStorage.getItem("carro");
const usernameMem = localStorage.getItem("usernameMem");
let loged = localStorage.getItem("loged");
//#endregion

//#region Eventos
document.addEventListener("DOMContentLoaded", () => Load());
btnAñadir.addEventListener("click", () => SumarAlCarro());
btnCarro.addEventListener("click", () => LimpiarCarro());
btnLogin.addEventListener("click", () => IrAlLogin());
btnSignin.addEventListener("click", () => IrAlSignin());
btnLogout.addEventListener("click", () => LogOut());
//#endregion

//#region Funciones
function Load() {
  cargarCarro();
  cargarUser();
  configBtns();
}
function SumarAlCarro() {
  let i = parseInt(carro.textContent);
  i++;
  carro.textContent = i.toString();
  localStorage.setItem("carro", i);
}
function LimpiarCarro() {
  carro.textContent = 0;
  localStorage.setItem("carro", 0);
}
function cargarCarro() {
  if (carroMem) {
    carro.textContent = parseInt(carroMem);
  } else {
    carro.textContent = 0;
  }
}
function cargarUser() {
  if (usernameMem) {
    msg.textContent = "Bienvenido " + usernameMem;
  } else {
    msg.textContent = "Bienvenido, por favor inicie sesión.";
  }
}
function IrAlLogin() {
  window.location.href = "login.html";
}
function IrAlSignin() {
  window.location.href = "signin.html";
}
function LogOut() {
  localStorage.removeItem("usernameMem");
  localStorage.setItem("loged", 0);
  IrAlLogin();
}
function configBtns() {
  if (loged) {
    if (loged == 1) {
      btnLogin.style.display = "none";
      btnSignin.style.display = "none";
    } else if (loged == 0) {
      {
        btnLogout.style.display = "none";
      }
    } else {
      localStorage.setItem("loged", 0);
      loged = localStorage.getItem("loged");
      configBtns();
    }
  }
}

//#endregion
