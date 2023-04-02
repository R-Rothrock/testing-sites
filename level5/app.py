#!/usr/bin/python3

from flask import Flask, render_template, redirect, Response, request

import sqlite3

connection = sqlite3.connect("./templates/sqlite.db", check_same_thread=False)
cursor = connection.cursor()

def authenticate(password: str) -> int:
    global cursor
    command = f"SELECT true \
              FROM Users \
              WHERE username=\"admin\" \
              AND password=\"{password}\";"
    try:
        ret = cursor.execute(command).fetchone()[0]
    except TypeError:
        return -1
    if ret == 1:
        return 0
    return 1

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("login")
        match authenticate(password):
            case 0:
                return redirect("/admin", code=302)
            case -1:
                return "Internal Server Error", 500
    return render_template("admin_login.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)

