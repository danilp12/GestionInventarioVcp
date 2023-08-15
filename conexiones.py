
import sqlite3
from datetime import datetime as dt
from statistics import mode
from PyQt5.QtCore import QDate


# Aca definimos todas las funciones relacionadas con la base de datos


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
    conexion.execute("INSERT INTO 'Case' (marca,modelo,serie,garantia,fecha,TipoHardware,Estado) VALUES(?,?,?,?,?,?,?)",(marca,modelo,serie,garantia,fecha,tipohard,estado))
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
def guardarPeriferico(Nombre,Modelo,TipoPeriferico,Serie,Voltaje,TipoConexion,estado):
    conexion = sqlite3.connect('Inventario.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO Perifericos (Nombre,Modelo,TipoPeriferico,Serie,Voltaje,TipoConexion,Estado) VALUES (?,?,?,?,?,?,?)',(Nombre,Modelo,TipoPeriferico,Serie,Voltaje,TipoConexion,estado))
    conexion.commit()
    conexion.close()

#   Actualizacion de Datos
def modMother(cod,tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute(f"Update Motherboard set marca='{marca}' ,modelo='{modelo}',chipset='{chipset}',socket='{socket}',serie='{serie}',video='{video}',audio='{audio}',garantia='{garantia}',fecha='{fecha}',TipoHardware='{tipohard}' where ID={cod}")
    conexion.commit()
    conexion.close()
    print("Mother Actualizada")
    return True

def modRam(cod,tipohard,marca,modelo,capacidad,frecuencia,serie,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute(f"Update Ram set marca='{marca}' ,modelo='{modelo}',capacidad='{capacidad}',frecuencia='{frecuencia}',serie='{serie}',garantia='{garantia}',fecha='{fecha}',TipoHardware='{tipohard}' where ID={cod}")
    conexion.commit()
    conexion.close()
    print("Ram Actualizada")
    return True

def modCPU(cod,tipohard,marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute(f"Update Cpu set TipoHardware='{tipohard}', marca='{marca}', modelo='{modelo}', nucleos='{nucleo}', hilos='{hilos}',frecuencia='{frecuencia}', socket='{socket}',cache='{cache}',serie='{serie}',garantia='{garantia}',fecha='{fecha}' where ID={cod}")
    conexion.commit()
    conexion.close()
    print("Cpu Actualizado")
    return True


def modFuente(cod,tipohard,marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute(f"Update Fuente set TipoHardware='{tipohard}',marca='{marca}',modelo='{modelo}',potencia='{potencia}',certificacion='{certificacion}',voltaje='{voltaje}',serie='{serie}',garantia='{garantia}',fecha='{fecha}' where ID='{cod}'")
    conexion.commit()
    conexion.close()
    print("Fuente Actualizado")
    return True
    
def modCase(cod,tipohard,marca,modelo,serie,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute(f"Update 'Case' set TipoHardware='{tipohard}',marca='{marca}',modelo='{modelo}',serie='{serie}',garantia='{garantia}',fecha='{fecha}' where ID='{cod}'")
    conexion.commit()
    conexion.close()
    print("Case Actualizado")
    return True
    
def modDisco(cod,tipohard,marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha):
    conexion = sqlite3.connect('Inventario.db')
    conexion.execute(f"Update Disco set TipoHardware='{tipohard}',marca='{marca}',modelo='{modelo}',capacidad='{capacidad}',tipodisco='{tipodisco}',cache='{cache}',buffer='{buffer}',serie='{serie}', garantia='{garantia}',fecha='{fecha}' where ID='{cod}'")
    conexion.commit()
    conexion.close()
    print("Disco Actualizado")
    return True
    

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
