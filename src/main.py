'''
PaaS - Puns as a Service
'''

from flask import Flask, send_from_directory
from pun.pun import BP as pun_route


def create_app():
    app = Flask(__name__, static_url_path='')

    app.register_blueprint(pun_route)

    return app


APP = create_app()


@APP.route('/')
def hello_world():
    return 'Hello World!'

from flask import Flask, send_from_directory

APP = Flask(__name__, static_url_path='')

@APP.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
