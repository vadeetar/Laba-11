import time
import os

DATA_DIR = "/data"
os.makedirs(DATA_DIR, exist_ok=True)

while True:
    with open(f"{DATA_DIR}/shared.txt", "a") as f:
        f.write(f"Writer: {time.ctime()}\n")
    print(f"[Writer] Записано в {time.ctime()}")
    time.sleep(5)