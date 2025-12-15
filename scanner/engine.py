import ipaddress
from concurrent.futures import ThreadPoolExecutor
from scanner.host import scan_host
from utils.constants import MAX_THREADS




def run_scan(target):
results = []
net = ipaddress.ip_network(target, strict=False)


with ThreadPoolExecutor(max_workers=MAX_THREADS) as pool:
for res in pool.map(scan_host, [str(ip) for ip in net.hosts()]):
results.append(res)


return results
