from time import strftime
from turtle import pos
from PyQt5.QtGui import QIcon,QColor,QFont
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
        self.Mother.clicked.connect(lambda: self.cambiar(0))
        self.Ram.clicked.connect(lambda: self.cambiar(1))
        self.Cpu.clicked.connect(lambda: self.cambiar(2))
        self.Fuente.clicked.connect(lambda: self.cambiar(3))
        self.Case.clicked.connect(lambda: self.cambiar(4))
        self.Disco.clicked.connect(lambda:self.cambiar(5))
        self.Video_Mother.addItems(['HDMI','DVI','VGA','DVI','Otro'])
        self.Audio_Mother.addItems(['Estereo','Mono','Otro','Placa Externa'])
        self.Certificacion_Fuente.addItems(['Gold','Silver','Bronce'])
        self.Voltaje_Fuente.addItems(['110V','220V','380V','Otro'])
        self.TipoDisco.addItems(['SSD','HDD','M2','Otro'])
        self.Guardar.clicked.connect(self.guardar)
        self.Cancelar.clicked.connect(self.cancelar)
    def cambiar(self,tipo):
        self.stackedW.setCurrentIndex(tipo)
    def cancelar(self):
        self.close()
    def guardar(self):
        posicion = self.stackedW.currentIndex()
        if posicion == 0:
            self.mother()
        elif posicion == 1:
            self.ram()
        elif posicion == 2:
            self.cpu()
        elif posicion == 3:
            self.fuente()
        elif posicion == 4:
            self.case()
        elif posicion == 5:
            self.disco()
    def mother(self):
        tipohard = "Motherboard"
        marca = self.Marca_Mother.text()
        modelo = self.Modelo_Mother.text()
        chipset = self.Chipset_Mother.text()
        socket = self.Socket_Mother.text()
        serie = self.Serie_Mother.text()
        video = self.Video_Mother.currentText()
        audio = self.Audio_Mother.currentText()
        garantia = self.Garantia_Mother.text()
        fecha = self.Fecha_Mother.date().toString()
        print(tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha)
        if guardarMother(tipohard,marca,modelo,chipset,socket,serie,video,audio,garantia,fecha):
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
        garantia = self.Garantia_Ram.text()
        fecha = self.Fecha_Ram.date()
        print(tipohard,marca,modelo,capacidad,frecuencia,serie,garantia,fecha)
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
        garantia = self.Garantia_Cpu.text()
        fecha = self.Fecha_Cpu.date()
        print(tipohard,marca,modelo,nucleo,hilos,frecuencia,socket,cache,serie,garantia,fecha)
    def fuente(self):
        tipohard = "Fuente"
        marca = self.Marca_Fuente.text()
        modelo = self.Modelo_Fuente.text()
        potencia = self.Potencia_Fuente.text()
        certificacion = self.Certificacion_Fuente.currentText()
        voltaje = self.Voltaje_Fuente.currentText()
        serie = self.Serie_Fuente.text()
        garantia = self.Garantia_Fuente.text()
        fecha = self.Fecha_Fuente.date()
        print(tipohard,marca,modelo,potencia,certificacion,voltaje,serie,garantia,fecha)
    def case(self):
        tipohard = "Case"
        marca = self.Marca_Case.text()
        modelo = self.Marca_Case.text()
        serie = self.Serie_Case.text()
        garantia = self.Garantia_Case.text()
        fecha = self.Fecha_Case.date()
        print(tipohard,marca,modelo,serie,garantia,fecha)
    def disco(self):
        tipohard = "Disco"
        marca = self.Marca_Disco.text()
        modelo = self.Modelo_Disco.text()
        capacidad = self.Capacidad_Disco.text()
        tipodisco = self.TipoDisco.currentText()
        cache = self.Cache_Disco.text()
        buffer = self.Buffer_Disco.text()
        serie = self.Serie_Disco.text()
        garantia = self.Garantia_Disco.text()
        fecha = self.Fecha_Disco.date()
        print(tipohard,marca,modelo,capacidad,tipodisco,cache,buffer,serie,garantia,fecha)