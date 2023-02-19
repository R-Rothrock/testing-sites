#!/usr/bin/python3

from flask import Flask, request, render_template

app = Flask(__name__)

comments = [
    "Lorem ipsum dolor sit amet.",
    "consetetur apidiscing elit.",
    "Nam quid quo cicero erunt.",
    "Itaque Romani partem Gallos occiderunt."
]

@app.route("/")
def index():
    return render_template("./static/index.html", comments=comments)

@app.route("/nameyouwouldntguess.js")
def index_js():
    with open("./static/index.js", "r") as stream:
        return stream.read()

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        comment.append(request.form["comment"])
    with open("./static/submit.html", "r") as stream:
        return stream.read()

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
