from flask import Flask, render_template, request, session, redirect, jsonify
from flask_session import Session

from metodos import *

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    res = eventos()
    productos = ultimos_productos()

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
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect('/')

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

    id = request.args.get("id")
    producto = consultar_producto(id)
    
    if len(producto):
        error("Producto inexistente", 404)

    return render_template('producto.html', fondo="#fff", producto=producto[0])