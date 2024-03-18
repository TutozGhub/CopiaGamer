//#region Controles
//#region Botones
let btnCarro = document.getElementById("buylist");
let btnLogin = document.getElementById("login");
let btnLogout = document.getElementById("logout");
let btnSignin = document.getElementById("signin");
//#endregion
//#region Otros
let carro = document.getElementById("products");
let msg = document.getElementById("user");
const contenedorProductos = document.getElementById('products');
//#endregion

//local storage
const carroMem = localStorage.getItem("carro");
const usernameMem = localStorage.getItem("usernameMem");
let loged = localStorage.getItem("loged");
//#endregion

//#region Eventos
document.addEventListener("DOMContentLoaded", () => Load());
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
  generarTarjetas();
}
function SumarAlCarro(id, nombre, precio) {
  if (loged == 1){
    let i = parseInt(carro.textContent);
    i++;
    carro.textContent = i.toString();
    localStorage.setItem("carro", i);
    alert(`ID: ${id}\nNombre: ${nombre}\nPrecio: ${precio}\nAñadido al carrito.`);
  }
  else{
    alert(`Debe iniciar sesion para poder usar el carrito de compras.`);
  }
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
function generarTarjetas() {
  const contenedorProductos = document.getElementById("contenedorProductos");
  contenedorProductos.innerHTML = "";

  productos.forEach(producto => {
      const card = document.createElement("div");
      card.classList.add("card");

      const imagen = document.createElement("img");
      imagen.src = producto.imagen;
      imagen.alt = producto.nombre;
      imagen.title = producto.nombre;

      const nombre = document.createElement("h3");
      nombre.textContent = producto.nombre;

      const precio = document.createElement("p");
      precio.textContent = `$ ${producto.precio}`;

      const boton = document.createElement("button")
      boton.id = "add"
      boton.type = "button"
      boton.textContent = "Añadir a la cesta"
      boton.addEventListener("click", () => SumarAlCarro(producto.ID, nombre.textContent, precio.textContent));
      
      card.appendChild(imagen);
      card.appendChild(nombre);
      card.appendChild(precio);
      card.appendChild(boton);

      contenedorProductos.appendChild(card);
  });
}
//#endregion