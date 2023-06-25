from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, QDate
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
from conexiones import Cursor, conexion

class Registro_Equipos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Registro_Equipos.ui',self)
        self.setWindowTitle('Registro de Equipos')
        self.setWindowIcon(QIcon('icon.png'))
        self.Notebook.clicked.connect(lambda: self.cambiar(0))
        self.Allinone.clicked.connect(lambda: self.cambiar(1))
        self.Escritorio.clicked.connect(lambda: self.cambiar(2))
        self.Otro.clicked.connect(lambda: self.cambiar(3))
        self.Cancelar.clicked.connect(self.close)
        self.Guardar.clicked.connect(self.guardar)
    def cambiar(self,tipo):
        self.stackedW.setCurrentIndex(tipo)
    def guardar(self):
        posicion = self.stackedW.currentIndex()
        if posicion == 0:
            self.notebook()
        if posicion == 1:
            self.allinone()
        if posicion == 2:
            self.escritorio()
        if posicion == 3:
            self.otro()
    def notebook(self):
        pass
    def allinone(self):
        pass
    def escritorio(self):
        pass
    def otro(self):
        pass
