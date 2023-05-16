from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, QDate
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
from Registro_Hardware import Registro_Hardware
from conexiones import Cursor, conexion

class NuevaReparaciones(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Nueva_Reparacion.ui',self)
        self.setWindowTitle('Nueva Reparacion')
        self.setWindowIcon(QIcon('icon.png'))
