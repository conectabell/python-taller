from metasploit.msfrpc import MsfRpcClient

#msfrpcd -U msf -P test -f
cli = MsfRpcClient(username="msf", password="test")
lista = cli.modules.exploits
for m in lista:
    if "windows" in m:
        if "smb" in m:
            print m
