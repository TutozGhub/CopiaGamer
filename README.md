# COPIA GAMER
#### Página web:  [Copia Gamer](http://tutoz.pythonanywhere.com/)
Copia Gamer es un sitio web de “Compra” de componentes y periféricos para computadora, además de permitir al usuario “hacer un pedido” de un conjunto de componentes ensamblados en un ordenador. El sitio es una réplica de [Compra Gamer](https://compragamer.com.ar/index.php), una web de Argentina.

Copia Gamer fue hecho usando tecnologías adquiridas en CS50 y otras adquiridas de forma externa
> [!NOTE]
> Tecnologías
> 
>HTML5, SASS, BOOTSTRAP, JavaScript, JQurey, Python, Flask, SQLite.

La página no es una copia 1:1 ya que la idea es simplemente crear una réplica parcialmente funcional. Tiene sus limitaciones, pero, esencialmente con unos retoques podría perfectamente ser una página 100% utilizable con fines comerciales.

### Dentro de todas las paginas podemos encontrar el HEADER, el menú y el FOOTER con los que podemos movernos por el sitio.

En el HEADER tenemos
*	El buscador, el cual podemos usar para buscar cualquier producto en la página.
*	El login, el se despliega en la misma pagina donde nos encontremos y también nos da la posibilidad de registrarnos.
*	El carrito, el cual nos redirecciona a nuestros productos en el carro de compra.
  
En el menú tenemos
* Productos, el cual nos redirige hacia el catálogo de productos.
* Armá tu pc, que nos redirecciona al apartado del mismo nombre.
* Ayuda, que nos redirecciona al apartado de ayuda.
* Marcas sponsor, que despliega una lista de sponsors del sitio, los cuales podemos clickear para que nos redireccione a sus respectivos sitios web.

En el FOOTER tenemos
* Slider de marcas, donde podemos ver las marcas de los productos que “vende” el sito.
* Información legal.
* Otro botón de ayuda.
* Botón de arrepentimiento (Decorativo).
* Términos y condiciones (Decorativo).
* Botones a mis redes sociales.
* Trabaja con nosotros (Decorativo).


# El sitio se compone por 6 páginas principales.

### Página principal
### Productos
### Producto
### Armá tu pc
### Carrito
### Ayuda

## La página principal
Es de donde podemos movernos a otros lugares de la página y ver los últimos productos en el catálogo, aquí tenemos 2 secciones principales:

### Promociones del sitio y Últimas novedades
-	Promociones del sitio, un slider de banners donde podemos ver, colaboraciones, sorteos y/o cualquier cosa que el sitio desee mostrar a sus visitantes.
-	Últimas novedades, aquí podemos ver los últimos productos añadidos al catalogo de la tienda.

## Productos
Es donde podemos buscar, filtrar y encontrar todos los productos para encontrar lo que deseamos “comprar”, aquí tenemos 4 secciones principales:

### Categorías, Filtro, Orden y Productos.
-	En las categorías podemos elegir el tipo de producto que buscamos mediante un sistema de categorías y subcategorías. Por ejemplo, si quisiéramos comprar un microprocesador ryzen 5 podemos ir al apartado de categorías, buscar y desplegar la categoría de “Procesadores” y dentro seleccionar la subcategoría “Procesadores AMD”.
-	En el apartado de filtro podemos filtrar los productos por los de una marca en concreto, por ejemplo, si hubiéramos entrado a la categoría de motherboards podríamos filtrar, si así lo quisiéramos, solo las motherboards de la marca “Asus”.
-	En el apartado de orden, podemos seleccionar si queremos que los productos se ordenen por defecto, de menor a mayor o de mayor a menor.
-	El apartado de productos es donde vemos reflejados los productos en base a nuestros filtros de búsqueda y orden. Aquí podemos apreciar una imagen del producto, su nombre, precio y un botón que nos permite sumarlo al carrito de compras. Al dar click en el nombre, o la imagen alguno de los productos este nos redireccionara al apartado Producto.

## Producto
Es donde podemos ver en detalle cualquiera de los productos del sitio, aquí tenemos 4 secciones principales:

### Imágenes, Información, Especificaciones y Preguntas.
-	Imágenes, imágenes que muestran el producto y/o partes de este.
-	Información, aquí podemos ver, el nombre del producto, su categoría y subcategoría, id, precio, cuotas, datos de la garantía, stock y envío. Además de un botón para sumar el producto al carrito de compras. 
-	Especificaciones, en este apartado DECORATIVO podemos ver las características detalladas del producto. En esté caso todos los productos tienen la misma carta de especificaciones por una cuestión de lo exhaustivo de tener que cargar una hoja personalizada para cada producto. Pese a eso con una pequeña modificación se podría dar especificaciones únicas a cada producto sin problema.
-	Preguntas, en este apartado podemos ver las preguntas hechas por los usuarios, y, en caso de estar logueados, podemos hacer preguntas sobre el producto.

## Arma tu pc
Aquí podemos seleccionar una serie de componentes de modo que al finalizar tengamos un pc completo armado, luego estos componentes se enviaran al carrito de compras junto con un “producto” llamado como “Armado de pc”, por lo cual estaríamos comprando un ordenador completo ya armado con los componentes seleccionados por nosotros, aquí tenemos 3 secciones principales:

### Selector de paso, Controles e información, Productos/ Resumen
-	 Selector de paso, tenemos los 10 pasos aquí podemos elegir que paso del armado queremos ir ya sea para añadir un nuevo producto al armado o para modificar un paso anterior.
-	Controles e información, aquí podemos ver, los watts teóricos que consumirá nuestro ordenador, el precio total de los componentes seleccionados y tendremos dos botones, uno para retroceder al paso anterior y uno para avanzar al siguiente. Este ultimo en caso de estar en el paso 10 semostrara como “Terminar” para pasar al Resumen, y en caso de estar en el resumen se mostrara como “Ir al carrito” que añadira los productos al carrito y nos redireccionara allí mismo.
-	Productos/ Resumen, este apartado nos mostrara los productos del paso actual los cuales podremos seleccionar. En caso de estar en el paso 1, tendremos una opción adicional, la cual es elegir el tipo de ordenador que armaremos, aquí decidiremos si estamos armando una computadora Intel o AMD. Y en caso de estar en el paso 11 (el resumen), en lugar de productos veremos el resumen de todos los productos seleccionados mas el armado, con su precio.

## Carrito
Es donde veremos los productos que seleccionamos y donde podremos efectuar la “compra” de estos, aquí tenemos 3 secciones principales:

### Productos, Opciones de pago, Botón de compra.
-	Productos, aquí podremos observar un resumen de los productos con: una imagen, su nombre, la cantidad de productos, el precio del producto por la cantidad, y un botón para eliminarlo del carrito.
-	Opciones de pago, este es un apartado DECORATIVO que simplemente nos deja seleccionar el método de pago y nos muestra el total de todos los productos.
-	Botón de compra, en caso de estar logueado podremos efectuar la “compra” lo que nos mostrara un mensaje en pantalla de que la compra fue realizada, limpiara el carrito y nos redireccionara a la pagina principal.

## Ayuda
Es donde veremos las preguntas comunes sobre el sitio, como este opera y maneja los productos y envíos, no hay apartados relevantes es solo información general.

