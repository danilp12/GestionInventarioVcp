from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont,QPixmap
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, QDate
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
from Registro_Hardware import Registro_Hardware
from conexiones import Cursor, conexion

### CLASE INVENTARIO (QDIALOG) 
    ### ATRIBUTOS:
    ###     -NuevoHardware (Boton)
    ###     -DetalleHardware (Boton)
    ###     -EliminarHardware (Boton)
    ###     -Buscar (Boton)
    ###     -BuscarID (Campo de Texto)
    ###     -TablaHardware (TableWidget)

    ### METODOS:
    ###     -modificar_hardware:
    ###         primero se carga el objeto Registro_Hardware luego
    ###         esta funcion toma el texto de la tabla de la interfaz de la columna Tipo de hardware
    #           luego busca con el id y tipo de hard en la bd y rellena la interfaz para realizar la modificacion
    #       -detalle_hardware:
    #           primero se carga el objeto Registro_Hardware luego
    #           esta funcion toma el texto de la tabla de la interfaz de la columna Tipo de hardware
    #           luego busca con el id y tipo de hard en la bd y rellena la interfaz para mostrar los detelles
    #       -bloqueodebotones:
    #           esta funcion bloquea los botones de la interfaz de registro de hardware
    #       -nuevo_hardware:
    #           esta funcion carga el objeto Registro_Hardware y la ejecuta para registrar el nuevo hardware
    #       -cargarhard:
    #           esta funcion carga todos los hardware de la bd y los lista en la tabla de la interfaz
    ###     -darbajahard:
    #           esta funcion se le da de baja al hardware seleccionado en la tabla de interfaz
    #           al igual que modificar hardware esta funcion lee el id y tipo de hard de la tabla de interfaz y luego
    #           busca en la bd con esos datos para realizar la baja. el elemento no se elimina, se cambia el estado a "Descontinuado"



class Inventario_Hardware(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('Inventario-Hardware.ui',self)
        self.setWindowTitle('Inventario Hardware')
        self.setWindowIcon(QIcon('icon.png'))
        self.Logo.setPixmap(QPixmap("logo.jpg"))
        self.NuevoHardware.clicked.connect(self.nuevo_hardware)
        self.DetallesHardware.clicked.connect(self.detelle_hardware)
        self.EliminarHardware.clicked.connect(self.darbajahard)
        self.ModificarHardware.clicked.connect(self.modificar_hardware)
        self.cargarhard()
        
    
    

    
            
    def redimensionarcabecera(self,tabla):
        header = tabla.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)     #ResizeToContents  
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)   #Stretch
    def modificar_hardware(self):
        if self.validarseleccion():
            self.det = Registro_Hardware()
            self.det.setWindowTitle('Modificar Hardware')
            self.det.Modificar.setEnabled(True)
            tipohard = self.TablaHardware.item(self.TablaHardware.currentRow(),2).text()
            cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
            self.det.Modificar.clicked.connect(lambda:self.det.actualizar(cod))
            cursor = Cursor()
            if tipohard == "Motherboard":
                self.det.stackedW.setCurrentIndex(0)
                cursor.execute(f"SELECT * From Motherboard WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Mother.date().fromString(listado[0][9])
                self.det.Marca_Mother.setText(listado[0][1])
                self.det.Modelo_Mother.setText(listado[0][2])
                self.det.Chipset_Mother.setText(listado[0][3])
                self.det.Socket_Mother.setText(listado[0][4])
                self.det.Serie_Mother.setText(listado[0][5])
                self.det.Video_Mother.addItems([listado[0][6]])
                self.det.Audio_Mother.addItems([listado[0][7]])
                self.det.Garantia_Mother.setText(listado[0][8])
                self.det.Fecha_Mother.setDate(fecha)
            if tipohard == "Ram":
                self.det.stackedW.setCurrentIndex(1)
                cursor.execute(f"SELECT * From Ram WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Ram.date().fromString(listado[0][7])
                self.det.Marca_Ram.setText(listado[0][1])
                self.det.Modelo_Ram.setText(listado[0][2])
                self.det.Capacidad_Ram.setText(listado[0][3])
                self.det.Frecuencia_Ram.setText(listado[0][4])
                self.det.Serie_Ram.setText(listado[0][5])
                self.det.Garantia_Ram.setText(listado[0][6])
                self.det.Fecha_Ram.setDate(fecha)
            if tipohard == "CPU":
                self.det.stackedW.setCurrentIndex(2)
                cursor.execute(f"SELECT * From Cpu WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][10])
                self.det.Marca_Cpu.setText(listado[0][1])
                self.det.Modelo_Cpu.setText(listado[0][2])
                self.det.Nucleos_Cpu.setText(listado[0][3])
                self.det.Hilos_Cpu.setText(listado[0][4])
                self.det.Frecuencia_Cpu.setText(listado[0][5])
                self.det.Socket_Cpu.setText(listado[0][6])
                self.det.Cache_Cpu.setText(listado[0][7])
                self.det.Serie_Cpu.setText(listado[0][8])
                self.det.Garantia_Cpu.setText(listado[0][9])
                self.det.Fecha_Cpu.setDate(fecha)

            if tipohard == "Fuente":
                self.det.stackedW.setCurrentIndex(3)
                cursor.execute(f"SELECT * From Fuente WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][8])
                self.det.Marca_Fuente.setText(listado[0][1])
                self.det.Modelo_Fuente.setText(listado[0][2])
                self.det.Potencia_Fuente.setText(listado[0][3])
                self.det.Certificacion_Fuente.addItems([listado[0][4]])
                self.det.Voltaje_Fuente.addItems([listado[0][5]])
                self.det.Serie_Fuente.setText(listado[0][6])
                self.det.Garantia_Fuente.setText(listado[0][7])
                self.det.Fecha_Fuente.setDate(fecha)
            if tipohard == "Case":
                self.det.stackedW.setCurrentIndex(4)
                cursor.execute(f"SELECT * From 'Case' WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][5])
                self.det.Marca_Case.setText(listado[0][1])
                self.det.Modelo_Case.setText(listado[0][2])
                self.det.Serie_Case.setText(listado[0][3])
                self.det.Garantia_Case.setText(listado[0][4])
                self.det.Fecha_Case.setDate(fecha)
            if tipohard == "Disco":
                self.det.stackedW.setCurrentIndex(5)
                cursor.execute(f"SELECT * From Disco WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][9])
                self.det.Marca_Disco.setText(listado[0][1])
                self.det.Modelo_Disco.setText(listado[0][2])
                self.det.Capacidad_Disco.setText(listado[0][3])
                self.det.TipoDisco.addItems([listado[0][4]])
                self.det.Cache_Disco.setText(listado[0][5])
                self.det.Buffer_Disco.setText(listado[0][6])
                self.det.Serie_Disco.setText(listado[0][7])
                self.det.Garantia_Disco.setText(listado[0][8])
                self.det.Fecha_Disco.setDate(fecha)
            self.bloqueodebotones()
            
            self.cargarhard()     
    def detelle_hardware(self):
        if self.validarseleccion():
            self.det = Registro_Hardware()
            self.det.setWindowTitle('Detalle Hardware')
            self.det.Exportar.setEnabled(True)
            tipohard = self.TablaHardware.item(self.TablaHardware.currentRow(),2).text()
            cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
            cursor = Cursor()
            if tipohard == "Motherboard":
                self.det.stackedW.setCurrentIndex(0)
                cursor.execute(f"SELECT * From Motherboard WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Mother.date().fromString(listado[0][9])
                self.det.Marca_Mother.setText(listado[0][1])
                self.det.Modelo_Mother.setText(listado[0][2])
                self.det.Chipset_Mother.setText(listado[0][3])
                self.det.Socket_Mother.setText(listado[0][4])
                self.det.Serie_Mother.setText(listado[0][5])
                self.det.Video_Mother.addItems([listado[0][6]])
                self.det.Audio_Mother.addItems([listado[0][7]])
                self.det.Garantia_Mother.setText(listado[0][8])
                self.det.Fecha_Mother.setDate(fecha)

                self.det.Marca_Mother.setReadOnly(True)
                self.det.Modelo_Mother.setReadOnly(True)
                self.det.Chipset_Mother.setReadOnly(True)
                self.det.Socket_Mother.setReadOnly(True)
                self.det.Serie_Mother.setReadOnly(True)
                self.det.Video_Mother.setEditable(False)
                self.det.Audio_Mother.setEditable(False)
                self.det.Garantia_Mother.setReadOnly(True)
            if tipohard == "Ram":
                self.det.stackedW.setCurrentIndex(1)
                cursor.execute(f"SELECT * From Ram WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Ram.date().fromString(listado[0][7])
                self.det.Marca_Ram.setText(listado[0][1])
                self.det.Modelo_Ram.setText(listado[0][2])
                self.det.Capacidad_Ram.setText(listado[0][3])
                self.det.Frecuencia_Ram.setText(listado[0][4])
                self.det.Serie_Ram.setText(listado[0][5])
                self.det.Garantia_Ram.setText(listado[0][6])
                self.det.Fecha_Ram.setDate(fecha)
            if tipohard == "CPU":
                self.det.stackedW.setCurrentIndex(2)
                cursor.execute(f"SELECT * From Cpu WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][10])
                self.det.Marca_Cpu.setText(listado[0][1])
                self.det.Modelo_Cpu.setText(listado[0][2])
                self.det.Nucleos_Cpu.setText(listado[0][3])
                self.det.Hilos_Cpu.setText(listado[0][4])
                self.det.Frecuencia_Cpu.setText(listado[0][5])
                self.det.Socket_Cpu.setText(listado[0][6])
                self.det.Cache_Cpu.setText(listado[0][7])
                self.det.Serie_Cpu.setText(listado[0][8])
                self.det.Garantia_Cpu.setText(listado[0][9])
                self.det.Fecha_Cpu.setDate(fecha)

            if tipohard == "Fuente":
                self.det.stackedW.setCurrentIndex(3)
                cursor.execute(f"SELECT * From Fuente WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][8])
                self.det.Marca_Fuente.setText(listado[0][1])
                self.det.Modelo_Fuente.setText(listado[0][2])
                self.det.Potencia_Fuente.setText(listado[0][3])
                self.det.Certificacion_Fuente.addItems([listado[0][4]])
                self.det.Voltaje_Fuente.addItems([listado[0][5]])
                self.det.Serie_Fuente.setText(listado[0][6])
                self.det.Garantia_Fuente.setText(listado[0][7])
                self.det.Fecha_Fuente.setDate(fecha)
            if tipohard == "Case":
                self.det.stackedW.setCurrentIndex(4)
                cursor.execute(f"SELECT * From 'Case' WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][5])
                self.det.Marca_Case.setText(listado[0][1])
                self.det.Modelo_Case.setText(listado[0][2])
                self.det.Serie_Case.setText(listado[0][3])
                self.det.Garantia_Case.setText(listado[0][4])
                self.det.Fecha_Case.setDate(fecha)
            if tipohard == "Disco":
                self.det.stackedW.setCurrentIndex(5)
                cursor.execute(f"SELECT * From Disco WHERE ID ={cod}")
                listado = cursor.fetchall()
                fecha = self.det.Fecha_Cpu.date().fromString(listado[0][9])
                self.det.Marca_Disco.setText(listado[0][1])
                self.det.Modelo_Disco.setText(listado[0][2])
                self.det.Capacidad_Disco.setText(listado[0][3])
                self.det.TipoDisco.addItems([listado[0][4]])
                self.det.Cache_Disco.setText(listado[0][5])
                self.det.Buffer_Disco.setText(listado[0][6])
                self.det.Serie_Disco.setText(listado[0][7])
                self.det.Garantia_Disco.setText(listado[0][8])
                self.det.Fecha_Disco.setDate(fecha)
            self.bloqueodebotones()      
    def bloqueodebotones(self):
        self.det.Mother.setEnabled(False)
        self.det.Ram.setEnabled(False)
        self.det.Cpu.setEnabled(False)
        self.det.Fuente.setEnabled(False)
        self.det.Case.setEnabled(False)
        self.det.Disco.setEnabled(False)
        self.det.Guardar.setEnabled(False) 

        self.det.exec_()
    def nuevo_hardware(self):
        self.reg = Registro_Hardware()
        self.reg.exec_()
        self.cargarhard()
    def cargarhard(self):
        cursor = Cursor()
        cursor.execute("SELECT * FROM Motherboard")
        listado = cursor.fetchall()
        self.TablaHardware.setRowCount(0)
        self.redimensionarcabecera(self.TablaHardware)
        for fila in listado:
            self.TablaHardware.insertRow(self.TablaHardware.rowCount())
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,1,QTableWidgetItem(str(fila[1]+"-"+fila[2])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,2,QTableWidgetItem(str(fila[10])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,3,QTableWidgetItem(str(fila[5])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,4,QTableWidgetItem(str(fila[9])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,5,QTableWidgetItem(str(fila[8])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,6,QTableWidgetItem(str(fila[11])))
        cursor.execute("SELECT * FROM Ram")
        listado = cursor.fetchall()
        for fila in listado:
            self.TablaHardware.insertRow(self.TablaHardware.rowCount())
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,1,QTableWidgetItem(str(fila[1]+"-"+fila[2])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,2,QTableWidgetItem(str(fila[8])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,3,QTableWidgetItem(str(fila[5])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,4,QTableWidgetItem(str(fila[7])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,5,QTableWidgetItem(str(fila[6])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,6,QTableWidgetItem(str(fila[9])))
        cursor.execute("SELECT * FROM Cpu")
        listado = cursor.fetchall()
        for fila in listado:
            self.TablaHardware.insertRow(self.TablaHardware.rowCount())
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,1,QTableWidgetItem(str(fila[1]+"-"+fila[2])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,2,QTableWidgetItem(str(fila[11])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,3,QTableWidgetItem(str(fila[8])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,4,QTableWidgetItem(str(fila[10])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,5,QTableWidgetItem(str(fila[9])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,6,QTableWidgetItem(str(fila[12])))
        cursor.execute("SELECT * FROM Fuente")
        listado = cursor.fetchall()
        for fila in listado:
            self.TablaHardware.insertRow(self.TablaHardware.rowCount())
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,1,QTableWidgetItem(str(fila[1]+"-"+fila[2])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,2,QTableWidgetItem(str(fila[9])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,3,QTableWidgetItem(str(fila[6])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,4,QTableWidgetItem(str(fila[8])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,5,QTableWidgetItem(str(fila[7])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,6,QTableWidgetItem(str(fila[10])))
        cursor.execute("SELECT * FROM 'Case'")
        listado = cursor.fetchall()
        for fila in listado:
            self.TablaHardware.insertRow(self.TablaHardware.rowCount())
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,1,QTableWidgetItem(str(fila[1]+"-"+fila[2])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,2,QTableWidgetItem(str(fila[6])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,3,QTableWidgetItem(str(fila[3])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,4,QTableWidgetItem(str(fila[5])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,5,QTableWidgetItem(str(fila[4])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,6,QTableWidgetItem(str(fila[7])))
        cursor.execute("SELECT * FROM Disco")
        listado = cursor.fetchall()
        for fila in listado:
            self.TablaHardware.insertRow(self.TablaHardware.rowCount())
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,0,QTableWidgetItem(str(fila[0])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,1,QTableWidgetItem(str(fila[1]+"-"+fila[2])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,2,QTableWidgetItem(str(fila[10])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,3,QTableWidgetItem(str(fila[7])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,4,QTableWidgetItem(str(fila[9])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,5,QTableWidgetItem(str(fila[8])))
            self.TablaHardware.setItem(self.TablaHardware.rowCount()-1,6,QTableWidgetItem(str(fila[11])))
    def darbajahard(self):
        if self.validarseleccion():
            if QMessageBox.question(self,"Esta seguro ?","Esta seguro que desea eliminar el hardware seleccionado?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No) == QMessageBox.Yes:
                tipohard = self.TablaHardware.item(self.TablaHardware.currentRow(),2).text()
                if tipohard == "Motherboard":
                    cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
                    cursor = conexion()
                    cursor.execute(f"UPDATE Motherboard set Estado='Descontinuado' WHERE ID ={cod}")
                    cursor.commit()
                    cursor.close()
                if tipohard == "Ram":
                    cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
                    cursor = conexion()
                    cursor.execute(f"UPDATE Ram set Estado='Descontinuado' WHERE ID ={cod}")
                    cursor.commit()
                    cursor.close()
                if tipohard == "Cpu":
                    cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
                    cursor = conexion()
                    cursor.execute(f"UPDATE Cpu set Estado='Descontinuado' WHERE ID ={cod}")
                    cursor.commit()
                    cursor.close()
                if tipohard == "Fuente":
                    cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
                    cursor = conexion()
                    cursor.execute(f"UPDATE Fuente set Estado='Descontinuado' WHERE ID ={cod}")
                    cursor.commit()
                    cursor.close()
                if tipohard == "Case":
                    cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
                    cursor = conexion()
                    cursor.execute(f"UPDATE 'Case' set Estado='Descontinuado' WHERE ID ={cod}")
                    cursor.commit()
                    cursor.close()
                if tipohard == "Disco":
                    cod = self.TablaHardware.item(self.TablaHardware.currentRow(),0).text()
                    cursor = conexion()
                    cursor.execute(f"UPDATE Disco set Estado='Descontinuado' WHERE ID ={cod}")
                    cursor.commit()
                    cursor.close()
        self.cargarhard()
    def validarseleccion(self):
        if self.TablaHardware.currentRow() != -1:
            return True
        else:
            QMessageBox.information(self,"Error de Seleccion","Debe seleccionar un elemento de la Tabla")
            return False