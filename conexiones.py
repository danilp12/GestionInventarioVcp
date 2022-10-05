
import re
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
def guardarMother(tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,estado):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into Motherboard (marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,TipoHardware,Estado) Values (?,?,?,?,?,?,?,?,?,?,?)",(marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,tipohard,estado) )
    conexion.commit()
    conexion.close()
    print("Mother Guardada")
    return True
def guardarRam(tipohard,marca,modelo,capacidad,frecuencia,serie,garantia,fecha,estado):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into Ram (marca,modelo,capacidad,frecuencia,serie,garantia,fecha,TipoHardware,Estado) VALUES(?,?,?,?,?,?,?,?,?)",(marca,modelo,capacidad,frecuencia,serie,garantia,fecha,tipohard,estado))
    conexion.commit()
    conexion.close()
    print("Ram Guardada")
    return True
def guardarCpu(tipohard,marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha,estado):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into Cpu (marca,modelo,nucleos,hilos,frecuencia,socket,cache,serie,garantia,fecha,TipoHardware,Estado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha,tipohard,estado))
    conexion.commit()
    conexion.close()
    print("Cpu Guardada")
    return True
def guardarFuente(tipohard,marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha,estado):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into Fuente (marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha,TipoHardware,Estado) VALUES(?,?,?,?,?,?,?,?,?,?)",(marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha,tipohard,estado))
    conexion.commit()
    conexion.close()
    print("Fuente Guardada")
    return True
def guardarCase(tipohard,marca,modelo,serie,garantia,fecha,estado):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into 'Case' (marca,modelo,serie,garantia,fecha,TipoHardware,Estado) VALUES(?,?,?,?,?,?,?)",(marca,modelo,serie,garantia,fecha,tipohard,estado))
    conexion.commit()
    conexion.close()
    print("Case Guardado")
    return True
def guardarDisco(tipohard,marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha,estado):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute("insert into Disco(marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha,TipoHardware,Estado) Values(?,?,?,?,?,?,?,?,?,?,?)",(marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha,tipohard,estado))
    conexion.commit()
    conexion.close()
    print("Disco Guardado")
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