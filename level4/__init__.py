#!/usr/bin/python3

# If you have a FileNotFoundError running this script,
# you need to install `host` which is used for DNS and rDNS.
# Debian/Ubuntu/Mint/Kali/Parrot/Kubuntu/many more:
# ~$ sudo apt install dnsutils
# Arch/Manjaro
# ~$ sudo pacman -S bind

from flask import Flask, render_template, request
import subprocess
import time
import threading

dns_ret = "waiting for input"

def get_output(cmd: str, shell="/bin/bash") -> str:
    """
    This code is horrible. But it should work for you :)
    I programmed this on a Saturday morning, don't blame me.
    """

    cmd = cmd.encode("utf-8")

    process = subprocess.Popen(shell, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE)

    process.stdin.write(cmd)
    process.stdin.flush()

    ret = str()

    activator = False

    def timer(sec: int):
        """ Small threading timer functionality. Waits for sleep """
        nonlocal activator
        time.sleep(sec)
        activator = True

    threading.Thread(target=timer, args=(5,)).start()

    while not activator:
        ret += process.stdout.read(1)

    return ret

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
