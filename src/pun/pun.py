import random


from flask import Blueprint


BP = Blueprint('pun', __name__, url_prefix='/pun')


def get_quotes(fpath):
    '''Gets the list of quotes from a local file'''
    with open(fpath) as quotey_boi:
        quotes_file = quotey_boi.read()
        quotes = quotes_file.splitlines()
        return quotes


QUOTES = get_quotes('punlist.txt')


@BP.route('/')
def get_pun():
    return 'Punishment'


# consider rate limiting this endpoint?
@BP.route('/quote', methods=['GET'])
def quote():
    '''
    /quote endpoint
    Returns a random quote
    Only works with the GET method
    :return:
    '''

    # debug
    print('got', len(QUOTES), 'lines')

    return QUOTES[random.randint(0, len(QUOTES)-1)]
