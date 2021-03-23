#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack

import config as conf
interfas = conf.interfas
checklib = conf.checklib
StartupAutomac = conf.StartupAutomac
import sys, os, time
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def instala_lib():
	print("")
	print(color.BLUE + "INFO:" + color.END + " Comenzando comprobacion de Librerias...")
	system('sudo pip install QtWidgets QtGui QtCore QApplication QMainWindow QLineEdit QLabel QComboBox QComboBox QPushButton QtGui')
	
    
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
def no_adaptador():
	if interfas == "COLOCA_TU_ADAPTADOR_A_AQUI":
		print("")
		print(color.PURPLE + ".. INSTRUCCIONES de Configuracion: .." + color.END)
		print("")
		print(color.BLUE + " 1)" + color.END + " En terminal escriba {" + color.RED + color.BOLD + "[ifconfig], [iw dev] o [nmcli d]" + color.END + "}, sin parentesis y Ejecute.")
		print(" Busque su Adaptador de red: " + color.YELLOW + color.BOLD + "wlan0, eth0, enp0, lo, etc" + color.END + ".")
		print(" El nombre es importante para poder cambiar la MAC.")
		print("")
		print("* Ejemplo: Si es Wifi. Deberia aparecer algo asi... {" + color.RED + color.BOLD + "wlx5632g1276004" + color.END +"}")
		print("")
		print(color.BLUE + " 2)" + color.END + " Copie el Nombre {" + color.RED + color.BOLD + "wlx5632g1276004" + color.END + "}, sin los parentesis")
		print(color.BLUE + " 3)" + color.END + " Abra el archivo {" + color.RED + color.BOLD + "config.py" + color.END + "} con un editor de TEXTO.")
		print(color.BLUE + " 4)" + color.END + " Busque la LINEA 18 y remplace {" + color.RED + color.BOLD + "COLOCA_TU_ADAPTADOR_A_AQUI" + color.END + "} por el nombre que copiaste.")
		print(color.BLUE + " 5)" + color.END + " Graba, y ejecuta el programa como Admin {" + color.YELLOW + color.BOLD + "sudo python3 mymac.py" + color.END + "}")
		print("")
		print("El programa verificara e instalara de ser necesario MacChanger. (Configurable en config.py)")
		print("")
		exit(0)

def getmac():
    print("")
    print(color.BLUE + "INFO:" + color.END + " Procederemos a Installar Complementos necesarios: GetMac" + color.END)
    system('sudo pip install getmac')
    #system('getmac')
    print("")
    print(color.YELLOW + "NOTA:" + color.END + " Ahora puedes usar el comando [" + color.RED + color.BOLD + "getmac" + color.END + "] en el terminal para conocer tu MAC de una forma sensilla.")		
    print(color.YELLOW + "NOTA:" + color.END + " Si usted esta con VPN de forma ACTIVA su MAC sera mostrada como [" + color.RED + color.BOLD + "00:00:00:00:00:00" + color.END + "] Cuando ejecute [" + color.RED + color.BOLD + "getmac" + color.END + "].")		
    print("")

def macchanger32():
	print("")
	print(color.BLUE + "INFO:" + color.END + " Comenzando comprobacion de Recursos...")     
	system('sudo apt-get install macchanger')
	clear()   

def wifi_down():
	clear()
	print(color.BLUE + "INFO:" + color.END + " Estamos " + color.RED + color.BOLD + "Apagando" + color.END + " su conector de Internet [" + interfas + "]")
	print("")	
	system('nmcli networking off') 

def wifi_up():
	clear()
	print(color.BLUE + "INFO:" + color.END + " Estamos " + color.YELLOW + color.BOLD + "Encendiendo" + color.END + " su conector de Internet [" + color.RED + color.BOLD + interfas + color.END+ "]")
	print("")	
	system('nmcli networking on') 

def cambia_mac():
	clear()
	print(color.BLUE + "INFO:" + color.END + " Cambiando MAC de [" + color.RED + color.BOLD + interfas + color.END + "]")
	print("")
	system('sudo macchanger -r ' + interfas)

def chequea_libreria():
    if checklib == "si" or checklib == "SI" or checklib == "Si" or checklib == "s" or checklib == "S" or checklib == "y" or checklib == "yes" or checklib == "Y" or checklib == "YES":
        instala_lib()
        getmac()
        macchanger32()
    else:
        pass

def startUpMac():
    if StartupAutomac == "si" or StartupAutomac == "SI" or StartupAutomac == "Si" or StartupAutomac == "s" or StartupAutomac == "S" or StartupAutomac == "y" or StartupAutomac == "yes" or StartupAutomac == "YES" or StartupAutomac == "Y":
        wifi_down()
        time.sleep(1)
        cambia_mac()
        time.sleep(1)
        wifi_up()
        time.sleep(1)
    else:
        pass
        
def programa():
    no_adaptador()
    chequea_libreria()	
    wifi_down()
    startUpMac()
    clear()
    print("")	
    print(color.BLUE + "INFO: " + color.END + color.UNDERLINE + "Estado actual de la MAC" + color.END+ ":")
    system('sudo macchanger -s ' + interfas)
    print("")	

programa()
print(color.YELLOW + "NOTA:" + color.END + " Todo parece en Orden, puede minimizar esta ventana. o cerrar la aplicacion. No afectara en su Mac.")
print("\n" + color.YELLOW + "NOTA:" + color.END + " En Espera ...")


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QComboBox, QPushButton, QToolButton
from PyQt5.QtGui import *
import sys, os, time
from os import system, name


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()        
        self.setGeometry(1000, 30, 205, 68) 
        self.initUI() 
        
    def button_net_on(self): 
        clear()        
        os.system('nmcli networking on')
        time.sleep(.1)
        print(color.BLUE + "INFO:" + color.END + " Network: Activada.")
        time.sleep(3)
        print("\n" + color.YELLOW + "NOTA:" + color.END + " En Espera ...")
      
    def button_net_off(self):
        clear()        
        os.system('nmcli networking off')
        time.sleep(.1)
        print(color.BLUE + "INFO:" + color.END + " Network: Desactivada.")
        time.sleep(1)
        print("\n" + color.YELLOW + "NOTA:" + color.END + " En Espera ...")
        
    def button_mac_r(self):
        clear()
        print(color.BLUE + "INFO:" + color.END + " Desactivando Network...")
        os.system('nmcli networking off')
        print("")        
        time.sleep(.5)        
        print(color.BLUE + "INFO:" + color.END + " Cambiando Direccion MAC..\n")  
        os.system('sudo macchanger ' + interfas + ' -r') 
        print("")
        time.sleep(.5)
        print(color.BLUE + "INFO:" + color.END + " Activando Network...")
        os.system('nmcli networking on')
        time.sleep(3)
        print("\n" + color.BLUE + "INFO:" + color.END + color.RED + " Esperando Finalizar Tarea..." + color.END)
        time.sleep(2)
        print("\n" + color.BLUE + "INFO:" + color.END + " LISTO...")
        time.sleep(.2)
        print("\n" + color.YELLOW + "NOTA:" + color.END + " En Espera ...") 
        
    def button_mac_s(self):
        clear()
        print(color.BLUE + "INFO:" + color.END + " Mostrando MAC ADDRESS..\n")          
        os.system('sudo macchanger ' + interfas + ' -s')
        time.sleep(2)
        print("\n" + color.YELLOW + "NOTA:" + color.END + " En Espera ...") 

    def initUI(self):		
        self.setFixedSize(205, 68) 
        self.setWindowTitle("Auto-MacChanger")         
        txt_Wifi = QtWidgets.QLabel(self) 
        txt_Wifi.setGeometry(QtCore.QRect(10, 0, 67, 17))
        txt_Wifi.setText("Network") 
        txt_Wifi.setStyleSheet("color: black")             
        txt_Wifi.move(15,0) 
        txt_Wifi.setObjectName("network")    
        txt_Mac = QtWidgets.QLabel(self) 
        txt_Mac.setGeometry(QtCore.QRect(10, 0, 150, 17))    
        txt_Mac.setText("MacChanger")
        txt_Mac.setStyleSheet("color: black")                
        txt_Mac.move(113,0)
        txt_Mac.setObjectName("mac") 
        txt_Mac = QtWidgets.QLabel(self) 
        txt_Mac.setGeometry(QtCore.QRect(10, 0, 150, 17))    
        txt_Mac.setText("By Neo-Jack 2021")        
        txt_Mac.setStyleSheet("font: 8pt;color: black")         
        txt_Mac.move(50,50)
        txt_Mac.setObjectName("mac")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)      
        self.net_on = QtWidgets.QToolButton(self)
        self.net_on.setGeometry(QtCore.QRect(5, 20, 41, 31)) 
        self.net_on.setStyleSheet("background-color: rgb(115, 210, 22);") 
        self.net_on.setIcon(icon2) 
        self.net_on.setIconSize(QtCore.QSize(32, 32)) 
        self.net_on.setCheckable(False)
        self.net_on.setChecked(False)
        self.net_on.setObjectName("net_on") 
        self.net_on.clicked.connect(self.button_net_on)      
        self.net_off = QtWidgets.QToolButton(self)
        self.net_off.setGeometry(QtCore.QRect(50, 20, 41, 31))
        self.net_off.setStyleSheet("background-color: rgb(204, 0, 0);") 
        self.net_off.setIcon(icon2) 
        self.net_off.setIconSize(QtCore.QSize(32, 32)) 
        self.net_off.setCheckable(False)
        self.net_off.setObjectName("net_off") 
        self.net_off.clicked.connect(self.button_net_off)  
        self.random = QtWidgets.QToolButton(self)
        self.random.setGeometry(QtCore.QRect(110, 20, 41, 31))
        self.random.setStyleSheet("background-color: rgb(115, 210, 22);")         
        self.random.setIcon(icon1)
        self.random.setIconSize(QtCore.QSize(32, 32))
        self.random.setObjectName("random") 
        self.random.clicked.connect(self.button_mac_r)       
        self.ojo = QtWidgets.QToolButton(self)
        self.ojo.setGeometry(QtCore.QRect(160, 20, 41, 31))
        self.ojo.setStyleSheet("background-color: rgb(237, 212, 0);")  
        self.ojo.setIcon(icon3)
        self.ojo.setIconSize(QtCore.QSize(32, 32))
        self.ojo.setCheckable(False)
        self.ojo.setChecked(False)
        self.ojo.setObjectName("ver") 
        self.ojo.clicked.connect(self.button_mac_s) 
    


    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
