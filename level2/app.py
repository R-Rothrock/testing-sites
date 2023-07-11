#!/usr/bin/python3

from flask import Flask, request, render_template

app = Flask(__name__)

comments = [
    "Lorem ipsum dolor sit amet.",
    "consetetur apidiscing elit.",
    "Nam quid quo cicero erunt.",
    "Itaque Romani partem princepes Gallos occiderunt."
]

@app.route("/")
def index():
    with open("./templates/index.html", "r") as stream:
        return render_template("index.html", comments=comments)

@app.route("/index.js")
def index_js():
    return render_template("index.js")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        print(request.form)
        comments.append(request.form["submit"])
    return render_template("submit.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
