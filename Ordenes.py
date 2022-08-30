from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
import sys,sqlite3,os,pickle ,datetime, json

timer = QTimer()
def hora ():
    return dt.now().strftime('%H:%M:%S')  


class Ordenes(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('Ordenes.ui', self)
        self.setWindowTitle('Ordenes de Trabajo')
        self.setWindowIcon(QIcon('icon.png'))
        self.Fecha.setText(strftime('%d/%m/%Y'))
        self.Hora.setText(self.actualizar_tiempo())
        
    def actualizar_tiempo(self):
        timer.start(1000)
        timer.timeout.connect(self.set_tiempo)
    def set_tiempo(self):
        self.Hora.setText(hora())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ordenes()
    ventana.show()
    sys.exit(app.exec_())