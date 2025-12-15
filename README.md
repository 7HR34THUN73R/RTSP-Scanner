# RTSP Camera Scanner (Advanced)
📡 RTSP Camera Scanner – Advanced Network & Camera Discovery Tool
An advanced Python-based RTSP camera scanner designed for network discovery, security assessment, and research.
The project focuses on clean modular architecture, separating network scanning from RTSP intelligence, making it ideal for pentesting labs, blue-team analysis, and learning protocol-level enumeration.

## ✨ Features
## 🔍 TCP & UDP port scanning
## 🎥 RTSP service detection (OPTIONS / DESCRIBE)
## 🛣️ Known RTSP path probing
## 🏷️ Camera vendor fingerprinting (Hikvision, Dahua, etc.)
## ⚡ Multi-threaded scanning engine
## 📤 JSON export of results
## 🧱 Clean, extensible modular design

🚀 Usage
```bash
pip install -r requirements.txt
python3 main.py 192.168.1.0/24 --json results/scan.json
