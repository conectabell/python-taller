# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

#import os, sys
from ftplib import FTP, error_perm
import re
#import os
#import sys

#Defino aqui los contenedores de datos provisionalmente
#Colores
rojo = str('\033[01;31m')
verde = str('\033[01;92m')
azul = str('\033[01;94m')
amarillo = str('\033[01;93m')
rese = str('\033[00m')
#Regex que localiza uno o varios espacios
regs = "\s*"
#Patrones para directorio o archivo
patron_dir = re.compile("^d[r|w|x|t|\-]{9}$")
patron_arch = re.compile("^\-[\-|r|w|x|t]{9}$")
#Almacen final de archivos y directorios
dirsdisc = []
filesdisc = []


#Funcion mejorada para el crawling
#usa dir para obtener los directorios, los parsea y los manda a listadirs
def run_dir(f, dirpath):
    #Donde se almacenaran todas la rutas
    listadirs = []
    original_dir = f.pwd()
    try:
        f.cwd(dirpath)
    except error_perm as e:
        return "Error" + str(e)
    f.dir(dirpath, listadirs.append)
    for i, dire in enumerate(listadirs):
        desc = re.split(regs, dire)
        if patron_dir.match(desc[0]):
            ruta = (dirpath + "/" + desc[8])
            #print (("RUTA: " + ruta))
            if ruta not in dirsdisc:
                append_dir(f, ruta, desc)
    f.cwd(original_dir)


def append_dir(f, ruta, desc):
    try:
        if f.cwd(ruta):
            dirsdisc.append([desc[0], desc[2], desc[3], ruta])
            run_dir(f, ruta)
            #listadirs[i] += " " + ruta
            #print "indice: " + str(i)
            #print "DIRE: " + dire
            #print "RUTA: " + ruta
    except Exception:
        #print e
        return None


#Saca los archivos de la lista de directorios descubiertos (dirdisc)
def chk_files_dir(f):
    for d in dirsdisc:
        lsaloc = []
        f.dir(d[3], lsaloc.append)
        for i, dire in enumerate(lsaloc):
            descu = re.split(regs, dire)
            if patron_arch.match(descu[0]):
                ruta = (d[3] + "/" + descu[8])
                ap = [descu[0],descu[2], descu[3], ruta]
                filesdisc.append(ap)


# lista los directorios
def listdirs2():
    for d in dirsdisc:
        print verde, d[0], " ", d[1], " ", d[2], " ", d[3], rese


# lista los archivos
def listfiles2():
    for d in filesdisc:
        print verde, d[0], " ", d[1], " ", d[2], " ", d[3], rese

#ip = raw_input(str("Introduzca la dirección IP >>> ").decode("utf-8"))
#us = raw_input(str("Introduzca el nombre de usuario >>> ").decode("utf-8"))
#pa = raw_input(str("Introduzca la contraseña >>>").decode("utf-8"))
ip = "192.168.1.206"
f = FTP(ip)
#f.login("anonymous", "")
print ((">>> " + azul + "Conectado con " + rese + amarillo + ip + rese + "\n\n"))
f.login("taller2", "taller2")
print ((">>> " + azul + "LOGIN OK" + rese + "\n\n"))
run_dir(f, "")
print ((">>> " + azul + "LISTADO OK" + rese + "\n\n"))
print (("\n>>> " + azul + "Listado de archivos encontrados" + rese))
print (("-------------------------------------------------\n"))
chk_files_dir(f)
listfiles2()
print (("\n>>> " + azul + "Listado de directorios encontrados" + rese))
print (("-------------------------------------------------\n"))
listdirs2()
f.quit()