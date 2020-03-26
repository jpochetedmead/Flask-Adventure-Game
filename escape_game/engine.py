import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def base():
    return render_template('base.html', message='Welcome to Escape The Curse Of Chucky game!')

@bp.route('/hello', methods=('GET', 'POST'))
def hello():
    return render_template('game/hello.html', message='Hello, World!')

@bp.route('/index', methods=('GET', 'POST'))
def index():
    return render_template('game/index.html')

@bp.route('/menu', methods=('GET', 'POST'))
def menu():
    return render_template('game/menu.html')  # TO-DO werkzeug.routing.BuildError:

@bp.route('/guide', methods=('GET', 'POST'))
def guide():
    return render_template('game/guide.html')

@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    return render_template('game/profile.html')
