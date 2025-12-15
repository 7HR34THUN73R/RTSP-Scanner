# RTSP Camera Scanner
📡 RTSP Camera Scanner – Network & Camera Discovery Tool
An advanced Python-based RTSP camera scanner designed for network discovery, security assessment, and research.
The project focuses on clean modular architecture, separating network scanning from RTSP intelligence, making it ideal for pentesting labs, blue-team analysis, and learning protocol-level enumeration.

### ✨ Features
#### •🔍 TCP & UDP port scanning
#### •🎥 RTSP service detection (OPTIONS / DESCRIBE)
#### •🛣️ Known RTSP path probing
#### •🏷️ Camera vendor fingerprinting (Hikvision, Dahua, etc.)
#### •⚡ Multi-threaded scanning engine
#### •📤 JSON export of results
#### •🧱 Clean, extensible modular design

### 🧠 Architecture Philosophy
- scanner/ handles hosts, ports, threading
- rtsp/ handles RTSP protocol logic only
- utils/ provides shared infrastructure
- main.py orchestrates everything

This design avoids monolithic scripts and enables easy future extensions such as ONVIF discovery, authentication checks, snapshots, or plugins.

### ⚠️ Legal Notice

This tool is intended ONLY for:
- Networks you own
- Environments you have explicit permission to test

Unauthorized scanning of networks or devices is illegal.

### 🚀 Usage
```bash
pip install -r requirements.txt
python3 main.py 192.168.1.0/24 --json results/scan.json
