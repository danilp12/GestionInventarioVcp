
import sqlite3
from datetime import datetime as dt

def conexion():
    conexion = sqlite3.connect('Inventario.db')
    return conexion

def Cursor():
    conexion = sqlite3.connect('Inventario.db')
    cursor = conexion.cursor()
    return cursor

def guardarPeriferico(Nombre,Modelo,TipoPeriferico,Serie,Voltaje,TipoConexion):
    conexion = sqlite3.connect('Inventario.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO Perifericos (Nombre,Modelo,TipoPeriferico,Serie,Voltaje,TipoConexion) VALUES (?,?,?,?,?,?)',(Nombre,Modelo,TipoPeriferico,Serie,Voltaje,TipoConexion))
    conexion.commit()
    conexion.close()
def instanciarbd():
    conexion = sqlite3.connect('Inventario.db')
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE "Perifericos" (
	"ID"	INTEGER,
	"Nombre"	TEXT,
	"Modelo"	TEXT,
	"TipoPeriferico"	TEXT,
	"Serie"	TEXT,
	"Voltaje"	TEXT,
	"TipoConexion"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
""")
    conexion.commit()
    conexion.close()