#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/robots.txt")
def robots():
    return render_template("robots.txt")

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=False)
