#!/usr/bin/python3
# -*- coding: utf-8 -*-
#By Neo-Jack

#=================Instrucciones===============================
#------En Terminal ejecute "ifconfig" o "iw dev" o "nmcli d"
#y remplace el valor de "interfas" en la linea 18 de esta pantalla por el nombre de su adaptador.
# EJ:
# Si es RED: "eth0" --> interfas = "eth0"
# Si es WIFI: "wlx4343452289" --> interfas = "wlx4343452289"
#
# Si su dispositivo es Ethernet el Adaptador (DIVICE) se mostrara como: 
# * eth0, enp0 , etc
# Si su disposivo es WIFi el Adaptador (DIVICE) se mostrara como:
# * wlan , wlx88450065 , etc
#
#=================CONFIGURACIONES===============================
interfas = "COLOCA_TU_ADAPTADOR_A_AQUI" #Este campto es OBLIGATORIO para el correcto funcionamiento de la APP
#------------------Configuraciones-------------------------------
checklib = "si"       # Verificar Instalacion de: Librerias, GetMac, MacChanger. Al iniciar Aplicacion.
StartupAutomac = "si" # Cambiar Mac al iniciar programa. 
#=================================================================
