from datetime import datetime




def log(message: str):
ts = datetime.utcnow().strftime("%H:%M:%S")
print(f"[{ts}] {message}")
