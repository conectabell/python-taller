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
print "Puerto 22: " + nm['127.0.0.1'].has_tcp(22)
print "Puerto 23:" + nm['127.0.0.1'].has_tcp(23)
#nm['127.0.0.1']['tcp'][22]
#nm['127.0.0.1'].tcp(22)