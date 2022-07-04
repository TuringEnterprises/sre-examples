from flask import Flask
from opentelemetry import trace

from random import random
from time import sleep

app = Flask(__name__)

tracer = trace.get_tracer(__name__)

@app.route("/")
def hello():
    sleep_sec=random()
    with tracer.start_as_current_span("sleep_time") as sleep_span:  
        sleep(sleep_sec)
        sleep_span.set_attribute("sleep_seconds", sleep_sec)
    return f"sleeped {sleep_sec} seconds"
