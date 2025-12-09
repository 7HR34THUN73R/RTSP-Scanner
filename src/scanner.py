import threading
from netaddr import IPNetwork
from utils.rtsp_check import check_rtsp
from utils.exporter import save_text, save_json
from utils.colors import G, R, Y

class Scanner:
    def __init__(self, network, timeout=2, verbose=False, json_out=False):
        self.network = network
        self.timeout = timeout
        self.verbose = verbose
        self.json_out = json_out
        self.found = []

    def worker(self, ip):
        result = check_rtsp(str(ip), self.timeout)
        if result:
            print(f"{G}[OPEN]{Y} RTSP Found → {ip}")
            self.found.append(str(ip))
        elif self.verbose:
            print(f"{R}[CLOSED]{Y} {ip}")

    def run(self):
        threads = []
        for ip in IPNetwork(self.network):
            t = threading.Thread(target=self.worker, args=(ip,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

        save_text(self.found)
        if self.json_out:
            save_json(self.found)

        print(f"\nCompleted. Found {len(self.found)} RTSP hosts.")