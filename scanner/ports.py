import socket
from utils.constants import TIMEOUT




def tcp_open(host, port):
try:
s = socket.socket()
s.settimeout(TIMEOUT)
s.connect((host, port))
s.close()
return True
except:
return False




def udp_probe(host, port):
try:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(TIMEOUT)
s.sendto(b"\x00", (host, port))
s.recvfrom(1024)
return True
except:
return False
