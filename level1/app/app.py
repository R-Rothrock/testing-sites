#!/usr/bin/python3
# app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    pass

if __name__ == "__main__":
    app.run()
