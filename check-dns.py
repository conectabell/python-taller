# -*- coding: utf-8 -*-
import socket
#import os
from dns import reversename
#from dns import resolver

direccion = "217.160.132.34"


def fromip(direccion):
    name, alias, addresslist = socket.gethostbyaddr(direccion)
    rev = reversename.from_address(direccion)
    #print "DnsLib: " + str(resolver.query(addr, "PTR")[0])
    print "Dirección IP: ", direccion
    print "Nombre: ", name
    print "Alias: ", alias
    print "Reverse Address: ", rev