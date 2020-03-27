import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('engine', __name__)

# Simple Hello World Page
@bp.route('/hello', methods=('GET', 'POST'))
def hello():
    return render_template('game/hello.html', message='Hello, World!')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if (request.method == 'POST'):
        # form was sent
        name = request.form['user_name']

        if name == "":
            return render_template('game/index.html', error="Sorry, but you didn't enter a name")
        else:
            return render_template('game/menu.html', person=name)
    else:
        # first view of page
        return render_template('game/index.html', message="Welcome to 'Escape The Curse Of Chucky'!")

@bp.route('/menu/<name>')
def menu(name):
    return render_template('game/menu.html', person=name)

#@bp.route('/menu', methods=('GET', 'POST'))
#def menu():
#    return render_template('game/menu.html')  # TO-DO werkzeug.routing.BuildError:

#@bp.route('/guide', methods=('GET', 'POST'))
#def guide():
#    return render_template('game/guide.html')

@bp.route('/guide/<name>')
def guide(name):
    return render_template('game/guide.html', person=name)

@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    return render_template('game/profile.html')

@bp.route('/room', methods=('GET', 'POST'))
def room():
    return render_template('game/room.html')

@bp.route('/room1', methods=('GET', 'POST'))
def room1():
    return render_template('game/room1.html')

@bp.route('/room2', methods=('GET', 'POST'))
def room2():
    return render_template('game/room2.html')

@bp.route('/room3', methods=('GET', 'POST'))
def room3():
    return render_template('game/room3.html')

@bp.route('/room4', methods=('GET', 'POST'))
def room4():
    return render_template('game/room4.html')

@bp.route('/room5', methods=('GET', 'POST'))
def room5():
    return render_template('game/room5.html')

@bp.route('/death', methods=('GET', 'POST'))
def death():
    return render_template('game/death.html')
