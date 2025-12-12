#!/usr/bin/env python3
recv_socket.settimeout(1)


recv_socket.bind(("", 33434))
send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
send_socket.sendto(b"Hello", (target, 33434))


try:
data, addr = recv_socket.recvfrom(512)
print(f"Hop {ttl}: {addr[0]}")
if addr[0] == target:
print("Reached target!")
break
except socket.timeout:
print(f"Hop {ttl}: * timeout *")


finally:
recv_socket.close()
send_socket.close()


# Main


def main():
parser = argparse.ArgumentParser(description="Advanced Python Network Scanner")
parser.add_argument("ip", help="Target IP address")
parser.add_argument("--threads", type=int, default=50, help="Number of threads")
parser.add_argument("--save", action="store_true", help="Save results to JSON file")


args = parser.parse_args()


ip = args.ip
ports = Queue()


# Add ports 1–1024
for port in range(1, 1025):
ports.put(port)


print(f"
[+] Scanning {ip} with {args.threads} threads...")


threads = []
for _ in range(args.threads):
t = threading.Thread(target=worker, args=(ip, ports))
t.daemon = True
t.start()
threads.append(t)


ports.join()


# Show results
print(f"
[+] Open Ports:")
for entry in open_ports:
print(f" - Port {entry['port']}: Banner -> {entry['banner']}")


# Save report
if args.save:
save_report(ip)


# Run traceroute
traceroute(ip)


if __name__ == "__main__":
main()
