from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)


from random import random
from time import sleep

app = Flask(__name__)


provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)

@app.route("/")
@tracer.start_as_current_span("/")
def hello():
    sleep_sec=random()
    with tracer.start_as_current_span("sleep_time") as sleep_span:  
        sleep(sleep_sec)
        sleep_span.set_attribute("sleep_seconds", sleep_sec)
    return f"sleeped {sleep_sec} seconds"
