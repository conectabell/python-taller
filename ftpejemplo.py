# -*- coding: utf-8 -*-
import ftplib

#ip = "192.168.1.123"
#f = FTP(ip)
#f.login("taller2", "taller2")

ftp = ftplib.FTP('192.168.1.123', 'taller2', 'taller2')
print "Lista de archivos: "
files = ftp.dir()
print files
ftp.cwd("/pub/unix")
