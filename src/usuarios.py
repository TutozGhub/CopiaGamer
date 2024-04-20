import conn_sqlite3

db = conn_sqlite3.conn

usuarios = db.execute("SELECT * FROM usuarios")

usuarios = usuarios.fetchall()

for r in usuarios:
    print(r)