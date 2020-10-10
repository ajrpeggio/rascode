#/usr/bin/env python3
from flask import Flask, redirect, url_for


server = Flask(__name__)


@server.route("/")
def root():
    return redirect(url_for('home'))


@server.route("/home")
def home():
    return "Homepage! "


if __name__ == "__main__":
   server.run(host='0.0.0.0')
