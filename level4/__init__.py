#!/usr/bin/python3

# If you have a FileNotFoundError running this script,
# you need to install `host` which is used for DNS and rDNS.
# Debian/Ubuntu/Mint/Kali/Parrot/Kubuntu/many more:
# ~$ sudo apt install dnsutils
# Arch/Manjaro
# ~$ sudo pacman -S bind

from flask import Flask, render_template, request
import subprocess

dns_ret = "waiting for input"

def get_output(cmd: str) -> str:
    """
    Gets output of command.
    """
    stream = subprocess.run(cmd, capture_output=True, shell=True)
    return stream.stdout.decode()

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_in = request.form["submit"]
        global dns_ret
        dns_ret = get_output(f"host {user_in}")
        print(dns_ret)
    return render_template("index.html", dns_ret=dns_ret)

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=False)
