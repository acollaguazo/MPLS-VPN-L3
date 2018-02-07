# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\carlo\Desktop\ProyectoCE\GUI\login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
from local import Ui_local
from remote import Ui_Remote
import sqlite3


class Ui_Dialog(object):

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showRemoteWindow(self):
        self.remoteWindow = QtWidgets.QDialog()
        self.ui = Ui_Remote()
        self.ui.setupUi(self.remoteWindow)
        self.remoteWindow.show()


    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla. 
    Actualmente este código no se ejecuta ya que la conexión por puerto COM esta deshabilitado en esta versión de MPLStudio."""
    def showlocalWindow(self):
        self.localWindow = QtWidgets.QDialog()
        self.ui = Ui_local()
        self.ui.setupUi(self.localWindow)
        self.localWindow.show()

    """Esta función verifica los datos ingresados en el cuadro de texto de login para la aplicación. Realiza conexión
    con la base de datos bajo SQL y una vez que los datos estén validados muestra la pantalla correspondiente al tipo
    de conexión. Por defecto en esta versión del aplicativo automáticamente entra a showRemoteWindow()"""
    def ingresar(self):
        username = self.txt_usuario.text()
        password = self.txt_contrasena.text()
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND CONTRASENA = ?", (username, password))
        if (len(result.fetchall()) > 0):
            print("Usuario encontrado ! ")
            loginWindow.close()
            if self.chk_remote.checkState():
                self.showRemoteWindow()
            else:
                self.showlocalWindow()
        else:
            print("Usuario no encontrado !")
            ctypes.windll.user32.MessageBoxW(0, "Credenciales invalidas",
                                             "Error", 0)
        connection.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(293, 391)
        Dialog.setMinimumSize(QtCore.QSize(293, 391))
        Dialog.setMaximumSize(QtCore.QSize(293, 391))
        self.btn_ingresar = QtWidgets.QPushButton(Dialog)
        self.btn_ingresar.setGeometry(QtCore.QRect(100, 290, 93, 28))
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Networking.png"))
        self.label.setObjectName("label")
        self.txt_usuario = QtWidgets.QLineEdit(Dialog)
        self.txt_usuario.setGeometry(QtCore.QRect(30, 190, 221, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txt_usuario.setMaxLength(20)
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_contrasena = QtWidgets.QLineEdit(Dialog)
        self.txt_contrasena.setGeometry(QtCore.QRect(30, 240, 221, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_contrasena.sizePolicy().hasHeightForWidth())
        self.txt_contrasena.setSizePolicy(sizePolicy)
        self.txt_contrasena.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txt_contrasena.setMaxLength(20)
        self.txt_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_contrasena.setObjectName("txt_contrasena")
        self.chk_remote = QtWidgets.QCheckBox(Dialog)
        self.chk_remote.setGeometry(QtCore.QRect(110, 340, 81, 20))
        self.chk_remote.setObjectName("chk_remote")
        self.chk_remote.setChecked(True)
        self.chk_remote.setEnabled(False)
        self.chk_remote.setVisible(False)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ##########################################################
        self.btn_ingresar.clicked.connect(self.ingresar)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ingreso al Sistema"))
        self.btn_ingresar.setText(_translate("Dialog", "Ingresar"))
        self.txt_usuario.setPlaceholderText(_translate("Dialog", "usuario"))
        self.txt_contrasena.setPlaceholderText(_translate("Dialog", "contraseña"))
        self.chk_remote.setText(_translate("Dialog", "Remote"))

"""Este es el llamado a la acción MAIN que se ejecuta al momento de abrir la aplicación. Carga la ventana de login"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
