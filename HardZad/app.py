import os
import sys
import importlib.util

# Загружаем Rust-расширение
spec = importlib.util.spec_from_file_location("myapp", "./myapp.so")
myapp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(myapp)

from flask import Flask

app = Flask(__name__)
port = int(os.environ.get("PORT", 8000))

@app.route('/')
def hello():
    return f"Rust says: {myapp.hello()}"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"{a} + {b} = {myapp.add(a, b)}"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)