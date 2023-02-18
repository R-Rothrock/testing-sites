#!/usr/bin/python3
# app.py

from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_in = request.form["in"]
    else:
        user_in = "Say hey to the form!"
    with open("index.html", "r") as stream:
        return render_template_string(stream.read() % (user_in))

@app.route("/index.js")
def inde_js():
    with open("./index.js", "r") as stream:
        return stream.read()

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=False)
