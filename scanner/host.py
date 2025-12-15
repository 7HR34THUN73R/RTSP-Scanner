from scanner.ports import tcp_open, udp_probe
from rtsp.protocol import rtsp_available, probe_paths
from rtsp.fingerprint import detect_vendor
from utils.constants import TCP_PORTS, UDP_PORTS




def scan_host(host):
open_tcp = [p for p in TCP_PORTS if tcp_open(host, p)]
open_udp = [p for p in UDP_PORTS if udp_probe(host, p)]


rtsp = False
paths = []
vendor = None


if 554 in open_tcp:
rtsp = rtsp_available(host)
if rtsp:
paths = probe_paths(host)
vendor = detect_vendor(paths)


return {
"host": host,
"tcp": open_tcp,
"udp": open_udp,
"rtsp": rtsp,
"paths": paths,
"vendor": vendor,
}
