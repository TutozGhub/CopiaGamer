from flask import Flask, render_template, request, session, redirect, jsonify, url_for
from flask_session import Session

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
    if request.method == "POST":
        print("post")
        return redirect('/')

    id = request.args.get("id")
    producto = consultar_producto_id(id)
    
    if len(producto) == 0:
        return error("Producto inexistente", 404)
    
    producto = producto[0]

    imagenes = []
    for i in range(1, int(producto['cantidad_imagenes']) + 1):
        imagenes.append(f'{producto['imagen']}{i}.png')

    return render_template('producto.html', fondo="#fff", producto=producto, imgs=imagenes)
    
@app.route('/productos', methods=['POST', 'GET'])
def productos():
    categorias = traer_categorias()
    subcategorias = traer_subcategorias()
    _scat = request.args.get('subcategoria', False)
    search = request.args.get('search', False)
    orderby = request.args.get('orderby', 'todos')
    id_scat = None
    id_cat = None
    orders =[
        {'value': 'todos', 'text': 'Todos'},
        {'value': 'mayoramenor', 'text': 'Mayor precio'},
        {'value': 'menoramayor', 'text': 'Menor precio'}
    ]

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
            productos = orderby_ultimos(orderby, 20)
        else:
            productos = orderby_cat(int(_scat), orderby)
    else:
        productos = orderby_query(search, orderby)


    return render_template('productos.html',orderby=orderby, orders=orders, id_scat=id_scat,id_cat=id_cat, scat=scat, cats=categorias, subcats=subcategorias, productos=productos)





# CARGA -----------------------------------
if app.debug:
    @app.route('/cargar', methods=['POST', 'GET'])
    def carga():
        if request.method == "POST":
            insert_producto(request.form)

        cat = request.args.get("cat")
        categorias = traer_cats()

        if not cat:
            cat_form = request.form.get("categoria")
            if cat_form:
                return redirect(f'/cargar?cat={cat_form}')
            return render_template('carga de productos.html', categorias=categorias)
        
        subcategorias = traer_subcats(cat)
        marcas = traer_marcas()
            
        return render_template('carga de productos.html', categorias=categorias, subcategorias=subcategorias, marcas=marcas)