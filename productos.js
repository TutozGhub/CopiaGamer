let productos = [];

function generarNombreEImagen(id) {
  const nombres = [
    "Ryzen 3",
    "Intel Core i5",
    "GTX 1660",
    "RX 580",
    "RTX 2080 Ti",
  ];
  const imagenes = [
    "https://www.venex.com.ar/products_images/1655397661_dfgdfg.jpg",
    "https://diamondsystemar.vtexassets.com/arquivos/ids/159275/513400_1.jpg?v=638246077990100000",
    "https://images.start.com.ar/VDO0524-3.jpg",
    "https://m.media-amazon.com/images/I/61ocO85sqBL._AC_UF894,1000_QL80_.jpg",
    "https://asset.msi.com/resize/image/global/product/product_1_20180919185540_5ba22b2ce7ec4.png62405b38c58fe0f07fcef2367d8a9ba1/1024.png",
  ];

  const indice = Math.floor(Math.random() * nombres.length);
  const producto = {
    ID: id + 1563,
    nombre: nombres[indice],
    imagen: imagenes[indice],
    precio: generarPrecio(),
  };
  return producto;
}

// Método para generar un precio aleatorio
function generarPrecio() {
  return Math.floor(Math.random() * 500000) + 50000; 
}

function generarRegistrosAleatorios() {
  for (let i = 0; i < 20; i++) {
    const producto = generarNombreEImagen(i);
    productos.push(producto);
  }
}

generarRegistrosAleatorios();
