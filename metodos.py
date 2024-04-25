from flask import render_template
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import *

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

def ultimos_productos():
    res = db.execute("SELECT * FROM productos ORDER BY id DESC LIMIT 10")
    return res

def consultar_producto(id):
    res = db.execute("""
                    SELECT p.id, p.nombre, precio, imagen, c.nombre AS [categoria], sc.nombre AS [subcategoria], m.nombre AS [marca]
                     FROM productos AS p
                     JOIN subcategorias AS sc ON p.subcategoria = sc.id
                     JOIN categorias AS c ON c.id = sc.id_categoria
                     JOIN marcas AS m ON m.id = p.id_marca
                     WHERE p.id=?
                    """, id)
    return res