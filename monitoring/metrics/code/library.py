from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from random import randint,random
from time import sleep

# Create an app
app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def hello():
    return "hello"

@app.route("/slow")
def slow():
    sec = randint(1,3)
    sleep(sec)
    return f"slept for {sec} seconds"