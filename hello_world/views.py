from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

msg = "Hello World!"

@app.route('/')
def index():
    moje_imie = "Natalia"
    # here we want to get the value of user (i.e. ?name=some-value)
    # brak imienia - moje imie domyslne
    output = request.args.get('output')
    name = request.args.get('name')

    if 'name' in request.args:
        moje_imie = name

    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
