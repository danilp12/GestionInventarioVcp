
from time import strftime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
import sys
from Inventario import Inventario
from Ordenes import Ordenes

timer = QTimer()
def hora ():
    return dt.now().strftime('%H:%M:%S')  


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle('Sistema de Tickets')
        self.setWindowIcon(QIcon('icon.png'))
        self.Fecha.setText(strftime('%d/%m/%Y'))
        self.Hora.setText(self.actualizar_tiempo())
        self.inventario = Inventario()
        self.ordenes = Ordenes()
        self.Inventario.clicked.connect(self.inventario.show)
        self.Ordenes.clicked.connect(self.ordenes.show)
        
    def actualizar_tiempo(self):
        timer.start(1000)
        timer.timeout.connect(self.set_tiempo)
    def set_tiempo(self):
        self.Hora.setText(hora())
    
        
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())