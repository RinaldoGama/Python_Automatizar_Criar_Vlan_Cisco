##Script Python criar Vlan no Switch Cisco

import getpass
import telnetlib

HOST = "10.10.2.1"
user = input("Entre com seu nome de usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf\n")
tn.write(b"vlan 100\n")
tn.write(b"name USUARIOS\n")

tn.write(b"vlan 101\n")
tn.write(b"name TELEFONIA_IP\n")

tn.write(b"vlan 103\n")
tn.write(b"name EQUIP_REDES\n")

tn.write(b"vlan 104\n")
tn.write(b"name IMPRESSORAS\n")


tn.write(b"vlan 113\n")
tn.write(b"name RADIOS_DEPARTAMENTOS\n")

tn.write(b"vlan 114\n")
tn.write(b"name CONTROLE DE ACESSO\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
