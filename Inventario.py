from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont,QPixmap
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
import sys,sqlite3,os,pickle ,datetime, json
from Inventario_Equipos import Inventario_Equipos
from Inventario_Perifericos import Inventario_Perifericos
from Inventario_Hardware import Inventario_Hardware
from Reparaciones import Reparaciones

timer = QTimer()
def hora ():
    return dt.now().strftime('%H:%M:%S')  



class Inventario(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('Inventario.ui', self)
        self.setWindowTitle('Inventario')
        self.setWindowIcon(QIcon('icon.png'))
        self.Logo.setPixmap(QPixmap("logo.jpg"))
        self.Fecha.setText(strftime('%d/%m/%Y'))
        self.Hora.setText(self.actualizar_tiempo())
        self.Inventario_Equipos.clicked.connect(self.inv_equipos)
        self.Inventario_Hardware.clicked.connect(self.inv_hardware)
        self.Inventario_Perifericos.clicked.connect(self.inv_perifericos)
        self.Reparaciones.clicked.connect(self.reparaciones)
    def reparaciones(self):
        self.reparaciones = Reparaciones()
        self.reparaciones.exec_()
    def actualizar_tiempo(self):
        timer.start(1000)
        timer.timeout.connect(self.set_tiempo)
    def set_tiempo(self):
        self.Hora.setText(hora())
    def inv_equipos(self):
        self.inv = Inventario_Equipos()
        self.inv.exec_()
    def inv_hardware(self):
        self.inv = Inventario_Hardware()
        self.inv.exec_()
    def inv_perifericos(self):
        self.inv = Inventario_Perifericos()
        self.inv.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Inventario()
    ventana.show()
    sys.exit(app.exec_())