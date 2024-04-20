import sqlite3

class conn:
    def execute(query, select=True):
        res = None
        try:
            conn = sqlite3.connect("database/database.sqlite3")
            db = conn.cursor()

            if select:
                res = db.execute(query)
            elif not select:
                res = db.executescript(query)
            
            conn.close
        except Exception as ex:
            print("error:", ex)

        return res