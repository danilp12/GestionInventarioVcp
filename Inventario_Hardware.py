from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
from Inventario_Perifericos import Inventario_Perifericos
from Registro_Hardware import Registro_Hardware

class Inventario_Hardware(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Inventario-Hardware.ui',self)
        self.setWindowTitle('Inventario Hardware')
        self.setWindowIcon(QIcon('icon.png'))
        self.ConsultarPerifericos.clicked.connect(self.consultar_perifericos)
        self.NuevoHardware.clicked.connect(self.nuevo_hardware)
    def consultar_perifericos(self):
        self.inv = Inventario_Perifericos()
        self.inv.exec_()
    def nuevo_hardware(self):
        self.reg = Registro_Hardware()
        self.reg.exec_()