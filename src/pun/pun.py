"""
Endpoints for the PaaS application which are specific to serving puns
"""

import random

from flask import Blueprint, send_from_directory, abort

# all of the routes defined in this file will be under /pun
BP = Blueprint('pun', __name__, url_prefix='/pun')

def get_puns(fpath):
    """
    Gets the list of puns from a file
    """
    with open(fpath) as punny_boi:
        puns_file = punny_boi.read()
        puns = puns_file.splitlines()
        return puns

puns = get_puns('punlist.txt')

@BP.route('/', methods=['GET'])
@BP.route('index.html', methods=['GET'])
def root():
    """
    Serves the homepage.
    """
    # the home page for /pun is under static/pun_home.html
    return send_from_directory('static', filename="pun_home.html")

@BP.route('/random', methods=['GET'])
def random_pun():
    """
    /pun/random

    Returns a random pun from the entire list of puns
    """
    return puns[random.randint(0, len(puns)-1)]

@BP.route('/<int:id>', methods=['GET'])
def pun_by_id(id: int):
    """
    /pun/<id>

    Gets a pun by the ID.
    Invalid IDs respond with a 404 Not Found error.
    """
    # check if id is in valid range
    if 0 <= id < len(puns):
        # valid, return the pun
        return puns[id]
    # else return a 404
    return abort(404)
