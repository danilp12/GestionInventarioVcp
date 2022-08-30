from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer
from PyQt5 import QtWidgets, uic,QtCore 
from datetime import datetime as dt
from PyQt5.QtCore import pyqtProperty

from conexiones import guardarPeriferico


class Registro_Perifericos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Perifericos.ui',self)
        self.setWindowTitle('Registro Perifericos')
        self.setWindowIcon(QIcon('icon.png'))
        self.Guardar.clicked.connect(self.guardar)
        self.Cancelar.clicked.connect(self.cancelar)
        self.TipoPeriferico.addItems(['Mouse','Teclado','Monitor','Impresora','Otro'])
        self.Voltaje.addItems(['3V','5V','12V','24V','110V','220V','380V','USB','Otro'])
        self.TipoConexion.addItems(['USB','Paralelo','Serial','Wifi','Bluetooth','Otro'])
        
    def guardar(self):
        
        guardarPeriferico(self.Nombre.text(),self.Modelo.text(),self.TipoPeriferico.currentText(),self.Serie.text(),self.Voltaje.currentText(),self.TipoConexion.currentText())
        
        self.close()
    def cancelar(self):
        self.close()