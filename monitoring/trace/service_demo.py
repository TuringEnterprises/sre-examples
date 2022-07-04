from requests import get
from flask import Flask
from random import random
from time import sleep
from os import environ
from opentelemetry import trace
tracer = trace.get_tracer(__name__)


app = Flask(__name__)
service = environ.get("SVC_NAME", "a").lower()

def sleep_with_context():
    sleep_sec = random()
    with tracer.start_as_current_span("sleep_time") as sleep_span:  
        sleep(sleep_sec)
        sleep_span.set_attribute("sleep_seconds", sleep_sec)
    # sleep(sleep_sec)


@app.route("/")
def hello():
    if service == "a":
        sleep_with_context()
        get("http://b")
        get("http://c")
    elif service == "b":
        get("http://d")
    elif service == "c":
        get("http://e")
        sleep_with_context()
        get("http://f")
    else:
        sleep_with_context()
    return f"returing from service: {service} "
