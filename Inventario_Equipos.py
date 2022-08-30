from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt

class Inventario_Equipos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Inventario-Equipos.ui',self)
        self.setWindowTitle('Inventario Equipos')
        self.setWindowIcon(QIcon('icon.png'))