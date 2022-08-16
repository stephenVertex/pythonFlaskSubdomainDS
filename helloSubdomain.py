from flask import Flask
import platform
app = Flask(__name__)


@app.route("/", subdomain="<subdomain>")
def hello_subdomain(subdomain):
    x = "<h1><p>Hello, there!</p></h1><h2>Your subdomain:</h2> " + subdomain
    return x

@app.route("/")
def hello_regular():
    x = "<h1><p>Hello, there!</p></h1><h2>No subdomain.</h2> " 
    return x
    