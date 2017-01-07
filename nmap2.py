# -*- coding: utf-8 -*-
import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443')
nm.command_line()
nm.scaninfo()
print "hostname" + nm['127.0.0.1'].hostname()
print ("Estado", nm['127.0.0.1'].state())
print nm['127.0.0.1'].all_protocols()
print nm['127.0.0.1']['tcp'].keys()

for x in range(22, 443):
    nmh = nm['127.0.0.1'].has_tcp(x)
    if nmh is True:
        print "Puerto " + str(x) + ": " + str(nmh)

#nm['127.0.0.1']['tcp'][22]
#nm['127.0.0.1'].tcp(22)