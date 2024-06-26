from flask import render_template, g, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import *
from functools import wraps

db = SQL("sqlite:///src/database/database.sqlite3")

def error(mensaje, error=400):
    return render_template("error.html", error=error, mensaje=mensaje), error

def moneda(value):
    return f"$ {value:,.0f}".replace(",", ".")

def max_len(value, max_caracteres = 89):
    if len(value) > max_caracteres:
        return value[:max_caracteres] + "..."
    else:
        return value

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('id_usuario') is None:
            return redirect(url_for('index', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def val_login(form):
    username = form.get("username")
    password = username + form.get("password")
    
    if not username or not form.get("password"):
        return (False, "Campos sin completar")
    
    res = db.execute("SELECT u.id, hash, nombre FROM usuarios AS u JOIN personas AS p ON u.id_persona = p.id WHERE username=?", username)
    if (len(res) != 1):
        return (False, "Usuario o contraseña incorrecto.")

    hash_psw = res[0]['hash']
    if not check_password_hash(hash_psw, password):
        return (False, "Usuario o contraseña incorrecto.")
    
    id = res[0]['id']
    nombre = res[0]['nombre']

    return (True, id, nombre)

def val_register(form):
        name = form.get("name")
        username = form.get("username")
        password = form.get("password")
        password2 = form.get("password2")

        if not name or not username or not password or not password2:
            return (False, "Campos sin completar")
        
        if password != password2:
            return (False, "Las contraseñas deben ser iguales")

        res = db.execute("SELECT * FROM usuarios WHERE username=?", username)
        if (len(res) != 0):
            return (False, "El nombre de usuario se encuentra en uso")
        
        hash_psw = generate_password_hash(username + password)
        id_persona = db.execute("INSERT INTO personas(nombre) VALUES (?)", name)
        db.execute("INSERT INTO usuarios(username, hash, id_persona) VALUES (?, ?, ?)", username, hash_psw, id_persona)
        return (True, "")

def eventos():
    res = db.execute("SELECT * FROM eventos")
    return res

def ultimos_productos(limite=20, precio=False, desc=True, marca=-1):
    if desc:
        desc = 'DESC'
    else:
        desc = 'ASC'

    if precio:
        precio = 'precio'
    else:
        precio = 'id'

    if marca == -1:
        res = db.execute(f"SELECT * FROM (SELECT * FROM productos ORDER BY id DESC LIMIT ?) ORDER BY {precio} {desc}", limite)
    else:
        res = db.execute(f"SELECT * FROM (SELECT * FROM productos WHERE id_marca=? ORDER BY id DESC LIMIT ?) ORDER BY {precio} {desc}", marca, limite)

    return res

def consultar_producto_id(id):
    res = db.execute("""
                    SELECT p.id, p.nombre, precio, imagen, cantidad_imagenes, c.nombre AS [categoria], sc.nombre AS [subcategoria], m.nombre AS [marca], sc.id AS [id_subcategoria]
                     FROM productos AS p
                     JOIN subcategorias AS sc ON p.subcategoria = sc.id
                     JOIN categorias AS c ON c.id = sc.id_categoria
                     JOIN marcas AS m ON m.id = p.id_marca
                     WHERE p.id=?
                    """, id)
    return res

def buscar_producto(query, precio=False, desc=True ):
    q = f"%{query}%";

    if desc:
        desc = 'DESC';
    else:
        desc = 'ASC';

    if precio:
        precio = 'p.precio';
    else:
        precio = 'p.id';

    res = db.execute(f"""
                    SELECT p.id, p.nombre, precio, imagen
                     FROM productos AS p
                     JOIN subcategorias AS sc ON p.subcategoria = sc.id
                     JOIN categorias AS c ON c.id = sc.id_categoria
                     JOIN marcas AS m ON m.id = p.id_marca
                     WHERE p.nombre LIKE ? OR sc.nombre LIKE ? OR c.nombre LIKE ? OR m.nombre LIKE ?
                     ORDER BY {precio} {desc}
                    """, q, q, q, q)
    return res

def consultar_productos_subcat(id, precio=False, desc=True, marca=-1):
    if desc:
        desc = 'DESC'
    else:
        desc = 'ASC'

    if precio:
        precio = 'precio'
    else:
        precio = 'id'
        
    if marca == -1:
        res = db.execute(f"SELECT * FROM productos WHERE subcategoria=? ORDER BY {precio} {desc}", id)
    else:
        res = db.execute(f"SELECT * FROM productos WHERE subcategoria=? AND id_marca=? ORDER BY {precio} {desc}", id, marca)
    return res

def consultar_productos_armatupc_subcat(subcat):
    res = db.execute("SELECT p.id, p.nombre, p.precio, p.imagen, sc.id AS subcat FROM productos AS p JOIN subcategorias AS sc ON p.subcategoria = sc.id WHERE subcategoria=? ORDER BY precio asc", subcat)
    return res

def consultar_productos_armatupc_cat(cat):
    res = db.execute("SELECT p.id, p.nombre, p.precio, p.imagen, sc.id AS subcat FROM productos AS p JOIN subcategorias AS sc ON p.subcategoria = sc.id WHERE id_categoria=? ORDER BY precio asc", cat)
    return res

def consultar_faqs():
    res = db.execute("SELECT * FROM faqs")
    return res

def consultar_preguntas(id_producto):
    res = db.execute("SELECT * FROM preguntas WHERE id_producto=? ORDER BY id desc", id_producto)
    return res

def insertar_pregunta(pregunta, id_producto):
    db.execute(f"INSERT INTO preguntas(pregunta, id_producto) VALUES(?,?)", pregunta, id_producto)


def traer_info_paso(paso):
    res = db.execute("SELECT * FROM pasos WHERE paso=?", paso)
    return res


# CARGA

def traer_cats():
    res = db.execute("SELECT * FROM categorias")
    return res

def traer_subcats(id):
    res = db.execute("SELECT * FROM subcategorias WHERE id_categoria = ? ORDER BY nombre ASC", id)
    return res
def traer_marcas():
    res = db.execute("SELECT * FROM marcas ORDER BY nombre ASC")
    return res

def insert_producto(form):
    nombre = form.get('nombre', False)
    subcat = form.get('subcat', False)
    precio = form.get('precio', False)
    marca = form.get('marca', False)
    imagenes = form.get('imagenes', False)

    if not nombre or not subcat or not precio or not imagenes or not marca:
        return False

    id = db.execute("""
            INSERT INTO productos
             (nombre, subcategoria, precio, cantidad_imagenes, id_marca)
             VALUES (?,?,?,?,?);
            """, nombre, subcat, precio, imagenes, marca)
    foto = f'static\\image\\productos\\{id}\\'
    db.execute("""
            UPDATE productos
             SET imagen = ?
             WHERE id=?;
            """, foto, id)
    return True

def traer_categorias():
    res = db.execute("SELECT * FROM categorias ORDER BY nombre ASC")
    return res

def traer_subcategorias():
    res = db.execute("SELECT * FROM subcategorias ORDER BY nombre ASC")
    return res

def orderby_ultimos(orderby, limit=20, marca=-1):
    if orderby == 'mayoramenor':
        res = ultimos_productos(limit, True, True, marca)
    elif orderby == 'menoramayor':
        res = ultimos_productos(limit, True, False, marca)
    else:
        res = ultimos_productos(limit, False, True, marca)
        
    return res

def orderby_cat(id, orderby, marca=-1):
    if orderby == 'mayoramenor':
        res = consultar_productos_subcat(id, True, True, marca)
    elif orderby == 'menoramayor':
        res = consultar_productos_subcat(id, True, False, marca)
    else:
        res = consultar_productos_subcat(id, False, True, marca)
        
    return res
def orderby_query(query, orderby):
    if orderby == 'mayoramenor':
        res = buscar_producto(query, True, True)
    elif orderby == 'menoramayor':
        res = buscar_producto(query, True, False)
    else:
        res = buscar_producto(query)
        
    return res
