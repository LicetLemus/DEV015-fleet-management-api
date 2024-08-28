from flask import Blueprint

bp_main = Blueprint("main", __name__)

@bp_main.route('/')
def handle_main():
    return '<h1>¡Hola, mundo!</h1>'