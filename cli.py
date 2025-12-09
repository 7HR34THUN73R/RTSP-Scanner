import argparse
from scanner import Scanner
from banner import print_banner

parser = argparse.ArgumentParser(description="RTSP Scanner")
parser.add_argument("--network", required=True)
parser.add_argument("--timeout", type=int, default=2)
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--json", action="store_true")
args = parser.parse_args()

print_banner()
scanner = Scanner(args.network, args.timeout, verbose=args.verbose, json_out=args.json)
scanner.run()