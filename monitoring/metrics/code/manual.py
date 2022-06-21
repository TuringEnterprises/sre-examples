from crypt import methods
from flask import Flask, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

# Create an app
app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

from prometheus_client import Counter

c = Counter('hits', 'number of hits', ['method', 'endpoint'])

@app.route("/", methods=["GET", "POST", "PUT", "HEAD"])
def hello():
    c.labels(endpoint="/", method = request.method).inc()
    return "hello"