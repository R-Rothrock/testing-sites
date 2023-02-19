#!/usr/bin/python3
# app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_in = request.form["in"]
    else:
        user_in = "Say hey to the form!"
    with open("./app/index.html", "r") as stream:
        return stream.read() % (user_in))

@app.route("/index.js")
def index_js():
    with open("./app/index.js", "r") as stream:
        return stream.read()

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=False)
