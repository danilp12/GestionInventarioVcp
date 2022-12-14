from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
from Perifericos import Registro_Perifericos
from conexiones import Cursor, conexion

class Inventario_Perifericos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Inventario-Perifericos.ui',self)
        self.setWindowTitle('Inventario Perifericos')
        self.setWindowIcon(QIcon('icon.png'))
        self.NuevoPeriferico.clicked.connect(self.nuevo)
        self.ModificarPeriferico.clicked.connect(self.modificar)
        self.EliminarPeriferico.clicked.connect(self.eliminar)
        self.listar()
    def modificar(self):
        if self.ListaPerifericos.currentRow() != -1:
            self.mod =Registro_Perifericos()
            self.mod.setWindowTitle("Modificar Perifericos")
            cod = self.ListaPerifericos.item(self.ListaPerifericos.currentRow(),0).text()
            cursor = Cursor()
            cursor.execute(f"Select * from Perifericos where ID={cod}")
            listado = cursor.fetchall()
            self.mod.Nombre.setText(listado[0][1])
            self.mod.Modelo.setText(listado[0][2])
            self.mod.TipoPeriferico.addItems([listado[0][3]])
            self.mod.Serie.setText(listado[0][4])
            self.mod.Voltaje.addItems([listado[0][5]])
            self.mod.TipoConexion.addItems([listado[0][6]])
            self.mod.exec_()
    def nuevo(self):
        nuevoperiferico = Registro_Perifericos()
        nuevoperiferico.exec_()
        self.listar()
    def eliminar (self):
        if self.ListaPerifericos.currentRow() != -1:
            if QMessageBox.question(self,"Esta seguro ?","Esta seguro que desea eliminar el periferico seleccionado?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No) == QMessageBox.Yes:
                cod = self.ListaPerifericos.item(self.ListaPerifericos.currentRow(),0).text()
                cursor = conexion()
                cursor.execute(f"UPDATE Perifericos set Estado='Descontinuado' WHERE ID ={cod}")
                cursor.commit()
                cursor.close()
            self.listar()
    def listar(self):
        cursor = Cursor()
        cursor.execute("SELECT * FROM perifericos")
        filas = cursor.fetchall()
        self.ListaPerifericos.setRowCount(0)
        for fila in filas:
            self.ListaPerifericos.insertRow(self.ListaPerifericos.rowCount())
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,1,QTableWidgetItem(str(fila[1])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,2,QTableWidgetItem(str(fila[2])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,3,QTableWidgetItem(str(fila[3])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,4,QTableWidgetItem(str(fila[4])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,5,QTableWidgetItem(str(fila[5])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,6,QTableWidgetItem(str(fila[6])))
            self.ListaPerifericos.setItem(self.ListaPerifericos.rowCount()-1,7,QTableWidgetItem(str(fila[7])))
        