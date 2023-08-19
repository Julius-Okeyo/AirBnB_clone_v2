#!/usr/bin/python3
'''
script that starts a Flask web application
'''
from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes = False)
def hello_hbnb(environment, response):
    """Displays 'Hello HBNB!'"""
    status = "200 OK"
    headers = [('Content-Type', 'text/html')]
    response(status, headers)
    return [b'Hello HBNB!']

if __name__ == "__main__":
    try:
        print('* Serving Flask app "0-hello_route" (lazy loading)')
        print("* Environment: production")
        print("  WARNING: Do not use the development server in a production environment.")
        print("  Use a production WSGI server instead.")
        print("* Debug mode: off")
        print("* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)")
        httpd = make_server('0.0.0.0', 5000, hello_hbnb)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
