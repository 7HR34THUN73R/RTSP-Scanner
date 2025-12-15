import socket
from rtsp.paths import RTSP_PATHS
from utils.constants import TIMEOUT




def rtsp_available(host):
try:
s = socket.socket()
s.settimeout(TIMEOUT)
s.connect((host, 554))
s.send(b"OPTIONS rtsp://%b/ RTSP/1.0\r\nCSeq: 1\r\n\r\n" % host.encode())
data = s.recv(1024)
s.close()
return b"RTSP" in data
except:
return False




def probe_paths(host):
found = []
for path in RTSP_PATHS:
try:
s = socket.socket()
s.settimeout(TIMEOUT)
s.connect((host, 554))
req = f"DESCRIBE rtsp://{host}{path} RTSP/1.0\r\nCSeq: 2\r\n\r\n"
s.send(req.encode())
resp = s.recv(1024)
s.close()
if b"200 OK" in resp:
found.append(path)
except:
pass
return found
