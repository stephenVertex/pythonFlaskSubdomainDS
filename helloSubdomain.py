from flask import Flask
import platform
from flask import request
app = Flask(__name__)


@app.route("/", subdomain="<subdomain>")
def hello_subdomain(subdomain):
    print(request)
    x = "<h1><p>Hello, there!</p></h1><h2>Your subdomain:</h2> " + subdomain
    return x

@app.route("/")
def hello_regular():
    print(request)
    print("MY URL: " + request.base_url)
    my_url = request.base_url.replace("http://", "")
    x = f"<h1><p>Hello, there!</p></h1><h2>{my_url}</h2> " 
    return x
    