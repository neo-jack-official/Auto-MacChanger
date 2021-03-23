Imagen: Auto-MacChanger "mymac.py")
![alt text](https://raw.githubusercontent.com/neo-jack-official/Auto-MacChanger/master/ex.png)

# AUto-MacChanger for Python 3 (mymac.py)
Small program to make you life easy. 
How many time you start your linux os and you take notice your mac did not change as you set up.
well this program solve that issu.
Also have a small grafical interface. To do it manual, in order left to rigth: Network: ON/OFF MAC Addres: Random/Show
Have a Configuration menu on "config.py":
1) Variable "interfas" you will need the name of your network DIVACE, instructions INCLUDED (sp).
  *You can get it from you terminal with: "ifconfig" or "iw dev" or "nmcli d"
  *Just copy the name and remplace in "config.py" line 18 ."COLOCA_TU_ADAPTADOR_A_AQUI"  for the name of your divace 
3) Let you check for the necesary libraries, Macchanger programa, and Getmac programa. instalation. (firs time let ir work, then you can turn it off) variable name "checklib"
4) give you the alternative to change automatic your mac at the first time you run the program on "config.py" variable name "StartupAutomac "

NOTE: The program its fully in SPANISH, so if you speak ENLGISH this can help you a lot.

NOTE: Works with Command "SUDO",if you have other distribution, just remplace every SUDO for one you linux USE


## TESTED on: Ubuntu, Kali.

# How to RUN it??
*python3 mymac.py 
*sudo python3 mymac.py

# Requirements :
*Set on config.py your DIVICE NETWORK name.
