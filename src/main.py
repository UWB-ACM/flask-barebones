"""
PaaS Puns as a Service

Uses the power of Python Flask to deliver puns through the internet.

"""

from flask import Flask, send_from_directory, render_template, jsonify
from pun.pun import BP as pun_route

def create_app():
    """
    Creates a new Flask application
    """
    app = Flask(__name__, static_url_path='')
    # blueprints allow our logic to be separated among different files
    app.register_blueprint(pun_route)
    return app

APP = create_app()

@APP.route("/index.html")
@APP.route("/")
def index():
    """
    /
    /index.html

    Responds with the "Hello World" page for the default endpoint.
    """
    return send_from_directory("static", filename="hello.html")

@APP.route("/test")
def testing():
    """
    A really simple route
    """
    return "Hello Flask!"

@APP.route("/json")
def testing_json():
    """
    An example of a route that returns JSON
    """
    return jsonify({
        "wow": "You can use Flask to return JSON!",
        "howCoolIsJSON": 9001
    })

@APP.route('/static/<path:path>')
def serve_static(path):
    """
    Serves files that are contained under the static folder
    """
    return send_from_directory('static', path)

@APP.route('/hello')
@APP.route('/hello/<name>')
def hello(name = "Anonymous"):
    """
    /hello
    /hello/Chris

    Responds with the rendered name.html page
    which includes your name, if specified as part of the route.
    """ 
    return render_template('name.html', name=name)

if __name__ == '__main__':
    """
    main

    When run directly, starts the debug server.
    """
    APP.run(debug=True, host='0.0.0.0')
