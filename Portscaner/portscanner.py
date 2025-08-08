import socket
from IPy import IP

ipaddress = input('[+] Enter Target to scan ')
port = 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print('[-] Port 80 Is Open')
except:
    print('[-] Port 80 Is Closed')
