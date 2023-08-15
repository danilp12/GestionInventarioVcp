from time import strftime
from turtle import pos
from PyQt5.QtGui import QIcon,QColor,QFont,QPixmap
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer
from PyQt5 import QtWidgets, uic,QtCore 
from datetime import datetime as dt
from PyQt5.QtCore import pyqtProperty
from conexiones import *

class Registro_Hardware(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Hardware.ui',self)
        self.setWindowTitle('Registro Hardware')
        self.setWindowIcon(QIcon('icon.png'))
        self.Logo.setPixmap(QPixmap("logo.jpg"))
        self.Mother.clicked.connect(lambda: self.cambiar(0))
        self.Ram.clicked.connect(lambda: self.cambiar(1))
        self.Cpu.clicked.connect(lambda: self.cambiar(2))
        self.Fuente.clicked.connect(lambda: self.cambiar(3))
        self.Case.clicked.connect(lambda: self.cambiar(4))
        self.Disco.clicked.connect(lambda:self.cambiar(5))
        self.Video_Mother.addItems(['HDMI','DVI','VGA','DVI','Otro'])
        self.Audio_Mother.addItems(['Estereo','Mono','Otro','Placa Externa'])
        self.Certificacion_Fuente.addItems(['Gold','Silver','Bronce','Sin Certificacion'])
        self.Voltaje_Fuente.addItems(['110V','220V','380V','Otro'])
        self.TipoDisco.addItems(['SSD','HDD','M2','Otro'])
        self.GarantiaBox_Mother.addItems(["Dias","Semanas","Meses","Años"])
        self.GarantiaBox_Disco.addItems(["Dias","Semanas","Meses","Años"])
        self.GarantiaBox_Case.addItems(["Dias","Semanas","Meses","Años"])
        self.GarantiaBox_Ram.addItems(["Dias","Semanas","Meses","Años"])
        self.GarantiaBox_Cpu.addItems(["Dias","Semanas","Meses","Años"])
        self.GarantiaBox_Fuente.addItems(["Dias","Semanas","Meses","Años"])
        self.Guardar.clicked.connect(self.guardar)
        self.Cancelar.clicked.connect(self.cancelar)
        
        self.checkBox_Mother.stateChanged.connect(self.cambiargarantia)
        self.checkBox_Ram.stateChanged.connect(self.cambiargarantia)
        self.checkBox_Cpu.stateChanged.connect(self.cambiargarantia)
        self.checkBox_Fuente.stateChanged.connect(self.cambiargarantia)
        self.checkBox_Case.stateChanged.connect(self.cambiargarantia)
        self.checkBox_Disco.stateChanged.connect(self.cambiargarantia)

                                               
### CLASE Registro_Hardware (QDIALOG) 
    ### ATRIBUTOS:
    ###     -Mother (Boton)
    ###     -Ram (Boton)
    ###     -Cpu (Boton)
    ###     -Fuente (Boton)
    ###     -Case (Boton)
    ###     -Disco (Boton)
    ###     -Video_Mother (Boton)
    ###     -Audio_Mother (Boton)
    ###     -Certificacion_Fuente (Boton)
    ###     -Voltaje_Fuente (Boton)
    ###     -TipoDisco (ComboBox)
    ###     -Guardar (Boton)
    ###     -Cancelar (Boton)

    ### METODOS:
    ###     -cambiar:
    #           funcion para cambiar las pantallas de hardware 
    #       -cancelar:
    #           funcion para cerrar la ventana
    #       -guardar:
    #           funcion para guardar el nuevo hardware
    #           la funcion toma la posicion en la que se llenaron los datos e inserta en la tabla correspondiente
    #       -actualizar:
    #           funcion para actualizar los datos del hardware. esta funcion es parecida al de guardar, solo que hace un update en la base de datos
    #       -mother:
    #           funcion para guardar los datos en la BD
    #       -ram:
    #           funcion para guardar los datos en la BD
    #       -cpu:
    #           funcion para guardar los datos en la BD
    #       -fuente:
    #           funcion para guardar los datos en la BD
    #       -case:
    #           funcion para guardar los datos en la BD
    #       -disco:
    #           funcion para guardar los datos en la BD
    #       -actualizarMother:
    #           funcion para actualizar los datos del mother
    #       -actualizarRam:
    #           funcion para actualizar los datos del ram
    #       -actualizarCpu:
    #               funcion para actualizar los datos del cpu
    #       -actualizarFuente:
    #               funcion para actualizar los datos de la fuente
    #       -actualizarCase:
    #               funcion para actualizar los datos del case
    #       -actualizarDisco:
    #               funcion para actualizar los datos del disco
    def calculargarantia(self,fechainicial,garantia,duracion):
        if duracion == "Dias":
            duracion = 1
        elif duracion == "Semanas":
            duracion = 7
        elif duracion == "Meses":
            duracion = 30
        else:
            duracion = 365
        diasgarantia = int(garantia) * duracion
        fechaestimada = fechainicial.addDays(diasgarantia) 
        return fechaestimada
    def cambiar(self,tipo):
        self.stackedW.setCurrentIndex(tipo)
    def cancelar(self):
        self.close()
    def guardar(self):
        posicion = self.stackedW.currentIndex()
        if posicion == 0:
            if self.validar_Mother():
                self.mother()
            else:
                QMessageBox.information(self,"Error","No pueden quedar campos vacios")
        elif posicion == 1:
            if self.validar_Ram():
                self.ram()
            else:
                QMessageBox.information(self,"Error","No pueden quedar campos vacios")
        elif posicion == 2:
            if self.validar_Cpu():
                self.cpu()
            else:
                QMessageBox.information(self,"Error","No pueden quedar campos vacios")
        elif posicion == 3:
            if self.validar_Fuente():
                self.fuente()
            else:
                QMessageBox.information(self,"Error","No pueden quedar campos vacios")
        elif posicion == 4:
            if self.validar_Case():
                self.case()
            else:
                QMessageBox.information(self,"Error","No pueden quedar campos vacios")
        elif posicion == 5:
            if self.validar_Disco():
                self.disco()
            else:
                QMessageBox.information(self,"Error","No pueden quedar campos vacios")
    def actualizar(self,cod):
        posicion = self.stackedW.currentIndex()
        if posicion == 0:
            self.actualizarMother(cod)
        elif posicion == 1:
            self.actualizarRam(cod)
        elif posicion == 2:
            self.actualizarCpu(cod)
        elif posicion == 3:
            self.actualizarFuente(cod)
        elif posicion == 4:
            self.actualizarCase(cod)
        elif posicion == 5:
            self.actualizarDisco(cod)
    def mother(self):
        tipohard = "Motherboard"
        marca = self.Marca_Mother.text()
        modelo = self.Modelo_Mother.text()
        chipset = self.Chipset_Mother.text()
        socket = self.Socket_Mother.text()
        serie = self.Serie_Mother.text()
        video = self.Video_Mother.currentText()
        audio = self.Audio_Mother.currentText()
        if self.checkBox_Mother.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Mother.text() != "":
                garantia = self.calculargarantia(self.Fecha_Mother.date(),self.Garantia_Mother.text(),self.GarantiaBox_Mother.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Mother.date().toString()
        estado = "Sin Asignar"
        print(tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,estado)
        if guardarMother(tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha,estado):
            QMessageBox.information(self,"Guardar","Motherboard Guardada Correctamente")
            self.close()
        else:
            QMessageBox.information(self,"Guardar","Ocurrio un error al guarda, comprobar datos")
    def ram(self):
        tipohard = "Ram"
        marca = self.Marca_Ram.text()
        modelo = self.Modelo_Ram.text()
        capacidad = self.Capacidad_Ram.text()
        frecuencia = self.Frecuencia_Ram.text()
        serie = self.Serie_Ram.text()
        if self.checkBox_Ram.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Ram.text()!= "":
                garantia = self.calculargarantia(self.Fecha_Ram.date(),self.Garantia_Ram.text(),self.GarantiaBox_Ram.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Ram.date().toString()
        estado = "Sin Asignar"
        print(tipohard,marca,modelo,capacidad,frecuencia,serie,garantia,fecha,estado)
        if guardarRam(tipohard,marca,modelo,capacidad,frecuencia,serie,garantia,fecha,estado):
            QMessageBox.information(self,"Guardar","Ram Guardada Correctamente")
            self.close()
        else:
            QMessageBox.information(self,"Guardar","Ocurrio un error al guarda, comprobar datos")
    def cpu(self):
        tipohard = "CPU"
        marca = self.Marca_Cpu.text()
        modelo = self.Modelo_Cpu.text()
        nucleo = self.Nucleos_Cpu.text()
        hilos = self.Hilos_Cpu.text()
        frecuencia = self.Frecuencia_Cpu.text()
        socket = self.Socket_Cpu.text()
        cache = self.Cache_Cpu.text()
        serie = self.Serie_Cpu.text()
        if self.checkBox_Cpu.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Cpu.text() != "":
                garantia = self.calculargarantia(self.Fecha_Cpu.date(),self.Garantia_Cpu.text(),self.GarantiaBox_Cpu.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Cpu.date().toString()
        estado = "Sin Asignar"
        print(tipohard,marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha,estado)
        if guardarCpu(tipohard,marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha,estado):
            QMessageBox.information(self,"Guardar","Cpu Guardada Correctamente")
            self.close()    
    def fuente(self):
        tipohard = "Fuente"
        marca = self.Marca_Fuente.text()
        modelo = self.Modelo_Fuente.text()
        potencia = self.Potencia_Fuente.text()
        certificacion = self.Certificacion_Fuente.currentText()
        voltaje = self.Voltaje_Fuente.currentText()
        serie = self.Serie_Fuente.text()
        if self.checkBox_Fuente.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Fuente.text()!="":
                garantia = self.calculargarantia(self.Fecha_Fuente.date(),self.Garantia_Fuente.text(),self.GarantiaBox_Fuente.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Fuente.date().toString()
        estado = "Sin Asignar"
        print(tipohard,marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha,estado)
        if guardarFuente(tipohard,marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha,estado):
            QMessageBox.information(self,"Guardar","Fuente Guardada Correctamente")
            self.close()
    def case(self):
        tipohard = "Case"
        marca = self.Marca_Case.text()
        modelo = self.Marca_Case.text()
        serie = self.Serie_Case.text()
        if self.checkBox_Case.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Case.text() !="":
                garantia = self.calculargarantia(self.Fecha_Case.date(),self.Garantia_Case.text(),self.GarantiaBox_Case.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Case.date().toString()
        estado = "Sin Asignar"
        print(tipohard,marca,modelo,serie,garantia,fecha,estado)
        if guardarCase(tipohard,marca,modelo,serie,garantia,fecha,estado):
            QMessageBox.information(self,"Guardar","Case Guardado Correctamente")
            self.close()
    def disco(self):
        tipohard = "Disco"
        marca = self.Marca_Disco.text()
        modelo = self.Modelo_Disco.text()
        capacidad = self.Capacidad_Disco.text()
        tipodisco = self.TipoDisco.currentText()
        cache = self.Cache_Disco.text()
        buffer = self.Buffer_Disco.text()
        serie = self.Serie_Disco.text()
        if self.checkBox_Disco.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Disco.text() != "" :
                garantia = self.calculargarantia(self.Fecha_Disco.date(),self.Garantia_Disco.text(),self.GarantiaBox_Disco.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Disco.date().toString()
        estado = "Sin Asignar"
        print(tipohard,marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha,estado)
        if guardarDisco(tipohard,marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha,estado):
            QMessageBox.information(self,"Guardar","Disco Guardado Correctamente")
            self.close()
#Modificaciones

    def actualizarMother(self,cod):
        tipohard = "Motherboard"
        marca = self.Marca_Mother.text()
        modelo = self.Modelo_Mother.text()
        chipset = self.Chipset_Mother.text()
        socket = self.Socket_Mother.text()
        serie = self.Serie_Mother.text()
        video = self.Video_Mother.currentText()
        audio = self.Audio_Mother.currentText()
        if self.checkBox_Mother.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Mother.text() != "":
                garantia = self.calculargarantia(self.Fecha_Mother.date(),self.Garantia_Mother.text(),self.GarantiaBox_Mother.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Mother.date().toString()
        if modMother(cod,tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha):
            QMessageBox.information(self,"Actualizar","Motherboad Actualizada")
            self.close()
            return True
        else:
            return False
    def actualizarRam(self, cod):
        tipohard = "Ram"
        marca = self.Marca_Ram.text()
        modelo = self.Modelo_Ram.text()
        capacidad = self.Capacidad_Ram.text()
        frecuencia = self.Frecuencia_Ram.text()
        serie = self.Serie_Ram.text()
        if self.checkBox_Ram.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Ram.text()!= "":
                garantia = self.calculargarantia(self.Fecha_Ram.date(),self.Garantia_Ram.text(),self.GarantiaBox_Ram.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Ram.date().toString()
        if modRam(cod,tipohard,marca,modelo,capacidad,frecuencia,serie,garantia,fecha):
            QMessageBox.information(self,"Actualizar","Ram Actualizada")
            self.close()
    def actualizarCpu(self, cod):
        tipohard = "CPU"
        marca = self.Marca_Cpu.text()
        modelo = self.Modelo_Cpu.text()
        nucleo = self.Nucleos_Cpu.text()
        hilos = self.Hilos_Cpu.text()
        frecuencia = self.Frecuencia_Cpu.text()
        socket = self.Socket_Cpu.text()
        cache = self.Cache_Cpu.text()
        serie = self.Serie_Cpu.text()
        if self.checkBox_Cpu.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Cpu.text() != "":
                garantia = self.calculargarantia(self.Fecha_Cpu.date(),self.Garantia_Cpu.text(),self.GarantiaBox_Cpu.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Cpu.date().toString()   
        if modCPU(cod, tipohard,marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha):
            QMessageBox.information(self,"Actualizar","Cpu Actualizado")
            self.close()
    def actualizarFuente(self, cod):
        tipohard = "Fuente"
        marca = self.Marca_Fuente.text()
        modelo = self.Modelo_Fuente.text()
        potencia = self.Potencia_Fuente.text()
        certificacion = self.Certificacion_Fuente.currentText()
        voltaje = self.Voltaje_Fuente.currentText()
        serie = self.Serie_Fuente.text()
        if self.checkBox_Fuente.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Fuente.text()!="":
                garantia = self.calculargarantia(self.Fecha_Fuente.date(),self.Garantia_Fuente.text(),self.GarantiaBox_Fuente.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Fuente.date().toString()
        if modFuente(cod, tipohard,marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha):
            QMessageBox.information(self,"Actualizar","Fuente Actualizado")
            self.close()
    def actualizarCase(self, cod):
        tipohard = "Case"
        marca = self.Marca_Case.text()
        modelo = self.Marca_Case.text()
        serie = self.Serie_Case.text()
        if self.checkBox_Case.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Case.text() !="":
                garantia = self.calculargarantia(self.Fecha_Case.date(),self.Garantia_Case.text(),self.GarantiaBox_Case.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Case.date().toString()
        if modCase(cod, tipohard,marca,modelo,serie,garantia,fecha):
            QMessageBox.information(self,"Actualizar","Case Actualizado")
            self.close()
    def actualizarDisco(self, cod):
        tipohard = "Disco"
        marca = self.Marca_Disco.text()
        modelo = self.Modelo_Disco.text()
        capacidad = self.Capacidad_Disco.text()
        tipodisco = self.TipoDisco.currentText()
        cache = self.Cache_Disco.text()
        buffer = self.Buffer_Disco.text()
        serie = self.Serie_Disco.text()
        if self.checkBox_Disco.isChecked():
            garantia = "Sin Garantia"
        else:
            if self.Garantia_Disco.text() != "" :
                garantia = self.calculargarantia(self.Fecha_Disco.date(),self.Garantia_Disco.text(),self.GarantiaBox_Disco.currentText())
                garantia = garantia.toString()
            else: 
                QMessageBox.information(self,"Garantia","La Garantia no puede quedar vacia")
                return False
        fecha = self.Fecha_Disco.date().toString()
        if modDisco(cod, tipohard,marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha):
            QMessageBox.information(self,"Actualizar","Disco Actualizado Correctamente")
            self.close()

#   Validaciones
# 
    def validar_Mother(self):
        if self.Marca_Mother.text() != "" and self.Modelo_Mother.text()!="" and self.Chipset_Mother.text()!="" and self.Socket_Mother.text()!=""and self.Serie_Mother.text()!="":
            return True
        else:
            return False
    def validar_Ram(self):
        if self.Marca_Ram.text()!="" and self.Modelo_Ram.text()!="" and self.Capacidad_Ram.text()!="" and self.Frecuencia_Ram.text()!="" and self.Serie_Ram.text()!="":
            return True
        else:
            return False
    def validar_Cpu(self):
        if self.Marca_Cpu.text()!="" and self.Modelo_Cpu.text()!="" and self.Nucleos_Cpu.text()!="" and self.Hilos_Cpu.text()!="" and self.Frecuencia_Cpu.text()!="" and self.Socket_Cpu.text() !="" and self.Cache_Cpu.text()!="" and self.Serie_Cpu.text() !="":
            return True
        else:
            return False
    def validar_Fuente(self):
        if self.Marca_Fuente.text()!="" and self.Modelo_Fuente.text()!="" and self.Potencia_Fuente.text()!="" and self.Serie_Fuente.text()!="":
            return True
        else:
            return False
    def validar_Case(self):
            if self.Marca_Case.text()!="" and self.Modelo_Case.text()!="" and self.Serie_Case.text()!="" :
                return True
            else:
                return False
    def validar_Disco(self):
        if self.Marca_Disco.text()!="" and self.Modelo_Disco.text()!="" and self.Capacidad_Disco.text()!="" and self.Cache_Disco.text()!="" and self.Buffer_Disco.text()!="" and self.Serie_Disco.text()!="":
            return True
        else:
            return False
    def cambiargarantia(self):
        if self.checkBox_Mother.isChecked():
            self.Garantia_Mother.setEnabled(False)
            self.GarantiaBox_Mother.setEnabled(False)
        elif self.checkBox_Ram.isChecked():
            self.Garantia_Ram.setEnabled(False)
            self.GarantiaBox_Ram.setEnabled(False)
        elif self.checkBox_Cpu.isChecked():
            self.Garantia_Cpu.setEnabled(False)
            self.GarantiaBox_Cpu.setEnabled(False)
        elif self.checkBox_Fuente.isChecked():
            self.Garantia_Fuente.setEnabled(False)
            self.GarantiaBox_Fuente.setEnabled(False)
        elif self.checkBox_Case.isChecked():
            self.Garantia_Case.setEnabled(False)
            self.GarantiaBox_Case.setEnabled(False)
        elif self.checkBox_Disco.isChecked():
            self.Garantia_Disco.setEnabled(False)
            self.GarantiaBox_Disco.setEnabled(False)
        
        else:
            self.Garantia_Mother.setEnabled(True)
            self.GarantiaBox_Mother.setEnabled(True)
            self.Garantia_Ram.setEnabled(True)
            self.GarantiaBox_Ram.setEnabled(True)
            self.Garantia_Cpu.setEnabled(True)
            self.GarantiaBox_Cpu.setEnabled(True)
            self.Garantia_Fuente.setEnabled(True)
            self.GarantiaBox_Fuente.setEnabled(True)
            self.Garantia_Case.setEnabled(True)
            self.GarantiaBox_Case.setEnabled(True)
            self.Garantia_Disco.setEnabled(True)
            self.GarantiaBox_Disco.setEnabled(True)

