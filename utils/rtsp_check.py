import socket

def check_rtsp(ip, timeout=2):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, 554))
        s.close()
        return True
    except:
        return False