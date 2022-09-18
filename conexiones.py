
import sqlite3
from datetime import datetime as dt
from PyQt5.QtCore import QDate

def conexion():
    conexion = sqlite3.connect('Inventario.db')
    return conexion

def Cursor():
    conexion = sqlite3.connect('Inventario.db')
    cursor = conexion.cursor()
    return cursor
def guardarMother(tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into Motherboard (marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,TipoHardware) Values (?,?,?,?,?,?,?,?,?,?)",(marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,tipohard) )
    conexion.commit()
    conexion.close()
    print("Mother Guardada")
    return True
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