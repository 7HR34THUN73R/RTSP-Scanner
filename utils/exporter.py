import json


def save_text(found):
    with open("results.txt", "w") as f:
        for ip in found:
            f.write(ip + "\n")


def save_json(found):
    with open("export.json", "w") as f:
        json.dump(found, f, indent=2)