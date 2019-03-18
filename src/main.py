'''
PaaS - Puns as a Service
'''

from flask import Flask
from pun.pun import BP as pun_route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pun_route)

    return app


APP = create_app()


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
