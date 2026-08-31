import sqlite3

DATABASE = "bima.db"

def get_connexion() :
    connexion = sqlite3.connect(DATABASE)
    return connexion

def creer_table() :
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS kim(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            text TEXT NOT NULL,
            photo TEXT
        )
    """)   

def inserer_info(email,text,photo) :
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO kim(email,text,photo) VALUES(?,?,?)",(email,text,photo))
    connexion.commit()
    connexion.close()

def recuperer_info() :
    pass