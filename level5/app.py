#!/usr/bin/python3

from flask import Flask, render_template, redirect, request
import sqlite3

connection = sqlite3.connect("./templates/sqlite.db", check_same_thread=False)
cursor = connection.cursor()

authenticated  = False

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form['login']
        global authenticated
        authenticated  = cursor.execute(
            f"SELECT true FROM Users" +
            " WHERE username=\"admin\"" +
            " AND password=\"{password}\";"
        ).fetchone()
    if authenticated:
        return redirect("/admin.html", code=302)
    return render_template("admin_login.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)

