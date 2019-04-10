import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QTableWidget, QTableWidgetItem

from source.coneccion import *
from source.AppMain import *


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("firts/GUI/login.ui",self)
        self.boton_ingresar.clicked.connect(self.login)

       
    def login(self):

        nom_usu = self.usuario.text()
        pass_usu = self.contrasena.text()
        
        sql_val = "SELECT * FROM usuarios WHERE nom_usuarios = '%s' and pass_usuarios = '%s' " % (nom_usu, pass_usu)
            
        cursor.execute(sql_val)

        if cursor.fetchone():        
                
            self.main = MainPage()
            self.main.show()
            self.close()

            pass

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("firts/GUI/app_main.ui",self)
        self.ingresar_usuarios.clicked.connect(funciones.ingresar_usuario)
        funciones.cargar_usuarios(self.tabla_usuarios)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
