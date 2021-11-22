#Dependencias

dependencias() {

	clear
	printf "\e[1;93mInstalando dependencias\e[0m\n"
	printf "\n\e[1;91mXterm\e[0m\n"
	sudo apt-get install -y xterm
	printf "\n\e[1;34mAircrack-ng\e[0m\n"
	sudo apt-get install aircrack-ng
	printf "\n\e[1;92mWifite\e[0m\n"
	sudo apt-get install wifite

}

dependencias
