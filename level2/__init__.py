#!/usr/bin/python3

from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

comments = [
    "Lorem ipsum dolor sit amet.",
    "consetetur apidiscing elit.",
    "Nam quid quo cicero erunt.",
    "Itaque Romani partem Gallos occiderunt."
]

@app.route("/")
def index():
    with open("./templates/index.html", "r") as stream:
        return render_template_string(stream.read(), comments=comments)

@app.route("/nameyouwouldntguess.js")
def index_js():
    with open("index.js", "r") as stream:
        return stream.read()

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        comment.append(request.form["comment"])
    return render_template("submit.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
