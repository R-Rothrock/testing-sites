#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open("./static/index.html", "r") as stream:
        return stream.read()

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=False)
