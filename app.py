from flask import Flask, render_template, request, session, redirect, jsonify, url_for
from flask_session import Session
from json import load

from metodos import *


app = Flask(__name__)

app.jinja_env.filters["M"] = moneda
app.jinja_env.filters["Tmax"] = max_len

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    res = eventos()
    productos = ultimos_productos(10)
    return render_template('index.html', fondo="#fff", images=res, productos=productos)

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        res = val_login(request.form)

        if res[0]:
            app.logger.debug("Logeado")
            session["id_usuario"] = res[1]
            session["nombre"] = res[2]
            return jsonify({'success' : True, 'message' : ''})
        
        else:
            app.logger.debug("Error al logear")
            return jsonify({'success': False, 'message': res[1]})

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        res = val_register(request.form)
        if res[0]:
            return jsonify({'success': res[0], 'message': ''})
        else:
            return jsonify({'success': res[0], 'message': res[1]})
        
@app.route('/producto', methods=['POST', 'GET'])
def producto():
    id = request.args.get("id")
    producto = consultar_producto_id(id)
    
    if len(producto) == 0:
        return error("Producto inexistente", 404)
    
    producto = producto[0]

    imagenes = []
    dir_imagenes = producto['imagen']
    
    for i in range(1, int(producto['cantidad_imagenes']) + 1):
        imagenes.append(f'{dir_imagenes}{i}.png')

    especificaciones = load(open('static/jsons/Especificaciones.json',encoding="utf8"))
    preguntas = consultar_preguntas(id)

    return render_template('producto.html', fondo="#fff", producto=producto, imgs=imagenes, especificaciones=especificaciones, preguntas=preguntas)

@app.route('/preguntar', methods=['POST', 'GET'])
def preguntar():
    id = request.args.get("id_producto", False)
    pregunta = request.args.get("pregunta", False)
    url = request.args.get("url", '/')
    print(id)

    if not id or not pregunta:
        return error("Error al enviar pregunta")
    
    insertar_pregunta(pregunta, id)
    return redirect(url)

@app.route('/productos', methods=['POST', 'GET'])
def productos():
    categorias = traer_categorias()
    subcategorias = traer_subcategorias()
    _scat = request.args.get('subcategoria', False)
    search = request.args.get('search', False)
    orderby = request.args.get('orderby', 'todos')
    marca = request.args.get('marca', -1)
    id_scat = None
    id_cat = None
    orders =[
        {'value': 'todos', 'text': 'Todos'},
        {'value': 'mayoramenor', 'text': 'Mayor precio'},
        {'value': 'menoramayor', 'text': 'Menor precio'}
    ]
    marcas = traer_marcas()

    if not _scat:
        scat = 'novedades'
    else:
        found = False
        for sc in subcategorias:
            if int(_scat) == int(sc['id']):
                id_scat = sc['id']
                id_cat = sc['id_categoria']
                scat = sc['nombre']
                found = True
                break;
        
        if not found:
            return redirect('/productos')
    
    if not search:
        if not _scat:
            productos = orderby_ultimos(orderby, 20, marca)
        else:
            productos = orderby_cat(int(_scat), orderby, marca)
    else:
        productos = orderby_query(search, orderby)

    return render_template('productos.html', search=search, marcas=marcas, orderby=orderby, orders=orders, id_scat=id_scat,id_cat=id_cat, scat=scat, cats=categorias, subcats=subcategorias, productos=productos)


@app.route('/carro', methods=['POST', 'GET'])
def carro():
    productos = session.get('productos_carro', False)
    total = 0
    
    if productos:
        for p in productos:
            total += p['precio'] * p['cantidad']

    return render_template('carro.html', productos=productos, total=total)

@app.route('/add', methods=['GET'])
def add_carro():
    id = request.args.get('id', False)
    url = request.args.get('url', False)
    if not id or not url:
        return redirect('/')
    
    productos = session.get('productos_carro', [])
    found = False
    for p in productos:
        if str(p['id']) == str(id):
            p['cantidad'] += 1
            found = True
            break
    if not found and len(consultar_producto_id(id)) == 1:
        producto = consultar_producto_id(id)[0]
        producto = {
            'id': producto['id'],
            'nombre': producto['nombre'],
            'precio': int(producto['precio']),
            'imagen': producto['imagen'],
            'cantidad': 1
        }
        productos.append(producto)
    
    session['productos_carro'] = productos

    if not session.get('productos_carro_count', False):
        session['productos_carro_count'] = 1
    else:
        session['productos_carro_count'] += 1
    

    return redirect(url)

@app.route('/delete', methods=['GET'])
def delete_carro():
    id = request.args.get('id', False)
    if not id:
        return redirect('/')
    
    productos = session.get('productos_carro', [])
    carro_count = session.get('productos_carro_count', 0)
    print('p:',len(productos))

    for i in range(len(productos)):
        if str(productos[i]['id'] ) == str(id):
            carro_count -= int(productos[i]['cantidad'])
            productos.pop(i)
            break
    print('c:', productos)
    
    session['productos_carro'] = productos
    session['productos_carro_count'] = carro_count

    return redirect('/carro')

@app.route('/comprar', methods=['POST', 'GET'])
def comprar():
    session['productos_carro'] = []
    session['productos_carro_count'] = 0
    return redirect('/')

@app.route('/ayuda', methods=['GET'])
def ayuda():
    faqs = consultar_faqs()
    return render_template('ayuda.html', faqs=faqs)


# CARGA -----------------------------------
if app.debug:

    @app.route('/cargar', methods=['POST', 'GET'])
    def carga():
        if request.method == "POST":
            insert_producto(request.form)

        cat = int(request.args.get("cat", False))
        categorias = traer_cats()

        if not cat:
            cat_form = request.form.get("categoria")
            if cat_form:
                return redirect(f'/cargar?cat={cat_form}')
            return render_template('carga de productos.html', categorias=categorias)
        
        subcategorias = traer_subcats(cat)
        marcas = traer_marcas()
            
        return render_template('carga de productos.html', categoria=cat, categorias=categorias, subcategorias=subcategorias, marcas=marcas)