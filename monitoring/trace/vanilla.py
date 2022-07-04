from flask import Flask
from random import random
from time import sleep

app = Flask(__name__)

@app.route("/")
def hello():
    sleep_sec=random()
    sleep(sleep_sec)
    return f"sleeped {sleep_sec} seconds"

