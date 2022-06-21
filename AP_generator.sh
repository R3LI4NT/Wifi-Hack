#!/bin/bash


read -p $' Nombre de AP (max=16): ' AP_name
read -p $' Nombre del diccionario: ' wordlist_name
printf " Número de AP's: 100\n"
printf " Diccionario creado con exito >\e[1;32m $(pwd)/$wordlist_name\e[0m\n"

for i in {1..100};
do 
	echo "$AP_name-$i"; 
done > $wordlist_name