import time
import os

DATA_FILE = "/data/shared.txt"

while True:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            lines = f.readlines()
            if lines:
                print(f"[Reader] Последняя строка: {lines[-1].strip()}")
    else:
        print("[Reader] Файл ещё не создан")
    time.sleep(3)