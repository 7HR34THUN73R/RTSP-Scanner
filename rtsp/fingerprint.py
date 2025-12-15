def detect_vendor(paths):
joined = " ".join(paths).lower()
if "realmonitor" in joined:
return "Dahua"
if "streaming/channels" in joined:
return "Hikvision"
return "Unknown"
