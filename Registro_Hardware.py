from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer
from PyQt5 import QtWidgets, uic,QtCore 
from datetime import datetime as dt
from PyQt5.QtCore import pyqtProperty


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
        pass
