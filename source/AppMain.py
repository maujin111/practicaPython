import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtSql import *

from source.coneccion import *
from app import *


class Ingresar_Usuario_UI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("firts/GUI/ingresar_usuario.ui",self)
        self.guardar_usuario.clicked.connect(self.guardar)
        pass

    def guardar(self):
        
        nom_usu = self.usuario.text()
        pass_usu = self.password.text()

        sql = "INSERT INTO usuarios (nom_usuarios, pass_usuarios) VALUES ('%s', '%s')" % (nom_usu, pass_usu)

        cursor.execute(sql)
        db.commit()
        db.close()


        Dguardado = guardado()
        Dguardado.show()
        app.show()

        pass

class guardado(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("firts/GUI/dialogo_exito.ui", self)


class funciones():
    def ingresar_usuario():
        ex2 = Ingresar_Usuario_UI()
        ex2.show()
        app.show()
        pass
    
    def cargar_usuarios(Tabla):
        tabla_usuarios = Tabla
        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        result = cursor.fetchall()
        tabla_usuarios.setRowCount(len(result))
        tabla_usuarios.setColumnCount(3)
        print(result[0][2])

        for r in range(0,len(result)):
            print(r) 
            for c in range(0,3):
                print(c)
                tabla_usuarios.setItem(r, c, QTableWidgetItem(result[r][c]))