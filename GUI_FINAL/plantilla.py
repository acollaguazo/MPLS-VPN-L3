# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantilla.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
import configuracionBasica
import funciones2
import funciones_com
import paramiko


class Ui_Plantilla(object):
    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla"""
    def showConfiguracionBasica(self,Form,remote_conn):
        self.configuracionBasica = QtWidgets.QDialog()
        self.ui = configuracionBasica.Ui_ConfiguracionBasica()
        self.ui.setupUi(self.configuracionBasica,remote_conn)
        self.configuracionBasica.show()
        Form.close()

    def verificarIP(self, txt_1,txt_2,txt_3,txt_4):
        if (txt_1.text()!="" or txt_2.text()!="" or txt_3.text()!="" or txt_4.text()!=""):
            if txt_1.text().isnumeric() and (int(txt_1.text()) < 256):
                if txt_2.text().isnumeric() and (int(txt_2.text()) < 256):
                    if txt_3.text().isnumeric() and (int(txt_3.text()) < 256):
                        if txt_4.text().isnumeric() and (int(txt_4.text()) < 256):
                            ip = txt_1.text() + "." + txt_2.text() + "." + txt_3.text() + "." + txt_4.text()
                            return True
                        else:
                            ctypes.windll.user32.MessageBoxW(0, "Error en el cuarto octeto", "Error", 1)
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "Error en el tercer octeto", "Error", 1)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Error en el segundo octeto", "Error", 1)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Error en el primer octeto", "Error", 1)

    """Primero valido todos los campos de ingreso de texto. Si los campos necesarios (hostname y domain name) no están
    completos o no validados la función lanza un mensaje de alerta. Los campos opcionales (dns1,dns2) se validan y se
    incluyen en la configuración siempre y cuando se detecte contenido en su campo de texto, caso contrario se omiten de
    la configuración."""
    def configurar(self,Form,remote_conn):
        hostname = self.txt_hostname.text()
        domainName = self.txt_domainName.text()
        if (self.verificarIP(self.txt_dns1_1,self.txt_dns1_2,self.txt_dns1_3,self.txt_dns1_4)):
            dns1 = self.txt_dns1_1.text()+"."+self.txt_dns1_2.text()+"."+self.txt_dns1_3.text()+"."+self.txt_dns1_4.text()
        else:
            dns1=""
            ctypes.windll.user32.MessageBoxW(0, "No se configurará DNS1", "Alerta", 0)
        if (self.verificarIP(self.txt_dns2_1,self.txt_dns2_2,self.txt_dns2_3,self.txt_dns2_4)):
            dns2 = self.txt_dns2_1.text()+"."+self.txt_dns2_2.text()+"."+self.txt_dns2_3.text()+"."+self.txt_dns2_4.text()
        else:
            dns2=""
            ctypes.windll.user32.MessageBoxW(0, "No se configurará DNS2", "Alerta", 0)

        tipo_ssh = "paramiko"
        #tipo_ssh = "<paramiko.Channel 0 (open) window=1004 -> <paramiko.Transport at 0x7546c70 (cipher aes128-cbc, 128 bits) (active; 1 open channel(s))>>"

        print(type(remote_conn) is paramiko.channel.Channel)
        if type(remote_conn) is paramiko.channel.Channel:
            if len(hostname)>0 and len(domainName)>0:
                funciones2.conf_plantilla(remote_conn, hostname, domainName, dns1, dns2)
                ctypes.windll.user32.MessageBoxW(0, "Configuración realizada con éxito",
                                                 "Done", 0)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Llene los campos necesarios para la configuración (*)",
                                                 "Error", 0)
            print("Entro por REMOTE")
        else:
            print("Entro por LOCAL")
            funciones_com.conf_plantilla(remote_conn, hostname, domainName, dns1, dns2)


    def atras(self,Form,remote_conn):
        self.showConfiguracionBasica(Form,remote_conn)
        Form.close()


    def setupUi(self, Plantilla,remote_conn):
        Plantilla.setObjectName("Plantilla")
        Plantilla.resize(410, 312)
        self.label = QtWidgets.QLabel(Plantilla)
        self.label.setGeometry(QtCore.QRect(50, 50, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Plantilla)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Plantilla)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Plantilla)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 61, 16))
        self.label_4.setObjectName("label_4")
        self.txt_hostname = QtWidgets.QLineEdit(Plantilla)
        self.txt_hostname.setGeometry(QtCore.QRect(170, 50, 161, 22))
        self.txt_hostname.setObjectName("txt_hostname")
        self.txt_domainName = QtWidgets.QLineEdit(Plantilla)
        self.txt_domainName.setGeometry(QtCore.QRect(170, 100, 161, 22))
        self.txt_domainName.setObjectName("txt_domainName")
        self.txt_dns1_1 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns1_1.setGeometry(QtCore.QRect(140, 150, 41, 22))
        self.txt_dns1_1.setMaxLength(3)
        self.txt_dns1_1.setObjectName("txt_dns1_1")
        self.txt_dns2_1 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns2_1.setGeometry(QtCore.QRect(140, 200, 41, 22))
        self.txt_dns2_1.setMaxLength(3)
        self.txt_dns2_1.setObjectName("txt_dns2_1")
        self.btn_configurar = QtWidgets.QPushButton(Plantilla)
        self.btn_configurar.setGeometry(QtCore.QRect(90, 260, 93, 28))
        self.btn_configurar.setObjectName("btn_configurar")
        self.btn_atras = QtWidgets.QPushButton(Plantilla)
        self.btn_atras.setGeometry(QtCore.QRect(250, 260, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.txt_dns1_2 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns1_2.setGeometry(QtCore.QRect(200, 150, 41, 22))
        self.txt_dns1_2.setMaxLength(3)
        self.txt_dns1_2.setObjectName("txt_dns1_2")
        self.txt_dns1_3 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns1_3.setGeometry(QtCore.QRect(260, 150, 41, 22))
        self.txt_dns1_3.setMaxLength(3)
        self.txt_dns1_3.setObjectName("txt_dns1_3")
        self.txt_dns1_4 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns1_4.setGeometry(QtCore.QRect(320, 150, 41, 22))
        self.txt_dns1_4.setMaxLength(3)
        self.txt_dns1_4.setObjectName("txt_dns1_4")
        self.txt_dns2_2 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns2_2.setGeometry(QtCore.QRect(200, 200, 41, 22))
        self.txt_dns2_2.setMaxLength(3)
        self.txt_dns2_2.setObjectName("txt_dns2_2")
        self.txt_dns2_3 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns2_3.setGeometry(QtCore.QRect(260, 200, 41, 22))
        self.txt_dns2_3.setMaxLength(3)
        self.txt_dns2_3.setObjectName("txt_dns2_3")
        self.txt_dns2_4 = QtWidgets.QLineEdit(Plantilla)
        self.txt_dns2_4.setGeometry(QtCore.QRect(320, 200, 41, 22))
        self.txt_dns2_4.setMaxLength(3)
        self.txt_dns2_4.setObjectName("txt_dns2_4")
        self.label_5 = QtWidgets.QLabel(Plantilla)
        self.label_5.setGeometry(QtCore.QRect(190, 160, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Plantilla)
        self.label_6.setGeometry(QtCore.QRect(250, 160, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Plantilla)
        self.label_7.setGeometry(QtCore.QRect(190, 210, 16, 10))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Plantilla)
        self.label_8.setGeometry(QtCore.QRect(250, 210, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Plantilla)
        self.label_9.setGeometry(QtCore.QRect(310, 210, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Plantilla)
        self.label_10.setGeometry(QtCore.QRect(310, 160, 16, 16))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Plantilla)
        QtCore.QMetaObject.connectSlotsByName(Plantilla)

        ################################################################
        self.btn_configurar.clicked.connect(lambda : self.configurar(Plantilla,remote_conn))
        self.btn_atras.clicked.connect(lambda : self.atras(Plantilla,remote_conn))


    def retranslateUi(self, Plantilla):
        _translate = QtCore.QCoreApplication.translate
        Plantilla.setWindowTitle(_translate("Plantilla", "Form"))
        self.label.setText(_translate("Plantilla", "Hostname *"))
        self.label_2.setText(_translate("Plantilla", "Domain name *"))
        self.label_3.setText(_translate("Plantilla", "Dns1"))
        self.label_4.setText(_translate("Plantilla", "Dns2"))
        self.btn_configurar.setText(_translate("Plantilla", "Configurar"))
        self.btn_atras.setText(_translate("Plantilla", "Atras"))
        self.label_5.setText(_translate("Plantilla", "."))
        self.label_6.setText(_translate("Plantilla", "."))
        self.label_7.setText(_translate("Plantilla", "."))
        self.label_8.setText(_translate("Plantilla", "."))
        self.label_9.setText(_translate("Plantilla", "."))
        self.label_10.setText(_translate("Plantilla", "."))

