from metasploit.msfrpc import MsfRpcClient
#import time

#msfrpcd -U msf -P test -f
cli = MsfRpcClient(username="msf", password="test")
lista = cli.modules.exploits
exploit = cli.modules.use('exploit', 'windows/smb/ms08_067_netapi')
print exploit.description
print exploit.required
