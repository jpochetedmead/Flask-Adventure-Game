import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort

from sys import exit

import random

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

@bp.route('/menu/<name>', methods=('GET', 'POST'))
def menu(name):
    return render_template('game/menu.html', person=name)

@bp.route('/guide', methods=('GET', 'POST'))
def guide():
    return render_template('game/guide.html')

@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    return render_template('game/profile.html')

@bp.route('/room', methods=('GET', 'POST'))
def start_room():
    current_room = {
        "title": "Main Room",
        "intro": '''You were stressed from work, so you went on a vacation to a Cabin in the Caribbean to reconnect with life.
        After a couple drinks and the sun sets behind the mountains you went and turned all the lights on, however a few hours later the lights started to malfunction.
        Then you hear someone knocking on the front door, so you went to see who it was and after you opened the door there was nobody there.
        You didn't worry too much about it and went to your bedroom to watch some movies.
        A few minutes passed, someone knocked on the front door again...
        What do you do?
        1) Ignore it and stay in bed.
        2) Go out and see who's knocking on the door.
        3) Call the Cabin owner and complain about people knocking on your door.
        4) Go out with a baseball bat.
        5) Ignore life and fall asleep.'''
        }

    start_room_options = ["1", "2", "3", "4", "5"]
    user_choice = ""

    if request.method == 'POST':
        user_choice = request.form['action']
        if user_choice == start_room_options[0]:
            return redirect(url_for('engine.room1'))
        elif user_choice == start_room_options[1]:
            return redirect(url_for('engine.room2'))
        elif user_choice == start_room_options[2]:
            return redirect(url_for('engine.room3'))
        elif user_choice == start_room_options[3]:
            return redirect(url_for('engine.room4'))
        elif user_choice == start_room_options[4]:
            return redirect(url_for('engine.room5'))
        else:
            return redirect(url_for('engine.death'))

    return render_template('game/room.html', room=current_room)


@bp.route('/room1', methods=('GET', 'POST'))
def room1():
    current_room = {
        "title": "Room 1 - Living Room",
        "intro": '''Hurry, Chuky is going to find you!
        Where do you want to go now?
        1) Stay hiding here
        2) Kitchen
        3) Bedroom
        4) Bathroom
        5) Basement'''
        }

    correctPath = random.randint(1, 5)

    if request.method == 'POST':
        correctPath = request.form['action']
        if correctPath == 1:
            return redirect(url_for('engine.room1'))
        elif correctPath == 2:
            return redirect(url_for('engine.room2'))
        elif correctPath == 3:
            return redirect(url_for('engine.room3'))
        elif correctPath == 4:
            return redirect(url_for('engine.room4'))
        elif correctPath == 5:
            return redirect(url_for('engine.room5'))
        else:
            return redirect(url_for('engine.death'))

    return render_template('game/room1.html', room=current_room)


@bp.route('/room2', methods=('GET', 'POST'))
def room2():
    current_room = {
        "title": "Room 2 - Kitchen",
        "intro": ''' Hurry, Chuky is going to find you!
         Where do you want to go now?
           1) Living Room
           2) Stay hiding here
           3) Bedroom
           4) Bathroom
           5) Basement'''
        }

    correctPath = random.randint(1, 5)

    if request.method == 'POST':
        correctPath = request.form['action']
        if correctPath == 1:
            return redirect(url_for('engine.room1'))
        elif correctPath == 2:
            return redirect(url_for('engine.room2'))
        elif correctPath == 3:
            return redirect(url_for('engine.room3'))
        elif correctPath == 4:
            return redirect(url_for('engine.room4'))
        elif correctPath == 5:
            return redirect(url_for('engine.room5'))
        else:
            return redirect(url_for('engine.death'))

    return render_template('game/room2.html', room=current_room)


@bp.route('/room3', methods=('GET', 'POST'))
def room3():
    current_room = {
        "title": "Room 3 - Bedroom",
        "intro": '''Hurry, Chuky is going to find you!
        Where do you want to go now?
          1) Living Room
          2) Kitchen
          3) Stay hiding here
          4) Bathroom
          5) Basement'''
        }

    correctPath = random.randint(1, 5)

    if request.method == 'POST':
        correctPath = request.form['action']
        if correctPath == 1:
            return redirect(url_for('engine.room1'))
        elif correctPath == 2:
            return redirect(url_for('engine.room2'))
        elif correctPath == 3:
            return redirect(url_for('engine.room3'))
        elif correctPath == 4:
            return redirect(url_for('engine.room4'))
        elif correctPath == 5:
            return redirect(url_for('engine.room5'))
        else:
            return redirect(url_for('engine.death'))

    return render_template('game/room3.html', room=current_room)


@bp.route('/room4', methods=('GET', 'POST'))
def room4():
    current_room = {
        "title": "Room 4 - Bathroom",
        "intro": '''Hurry, Chuky is going to find you!
        Where do you want to go now?
          1) Living Room
          2) Kitchen
          3) Bedroom
          4) Stay hiding here
          5) Basement'''
        }

    correctPath = random.randint(1, 5)

    if request.method == 'POST':
        correctPath = request.form['action']
        if correctPath == 1:
            return redirect(url_for('engine.room1'))
        elif correctPath == 2:
            return redirect(url_for('engine.room2'))
        elif correctPath == 3:
            return redirect(url_for('engine.room3'))
        elif correctPath == 4:
            return redirect(url_for('engine.room4'))
        elif correctPath == 5:
            return redirect(url_for('engine.room5'))
        else:
            return redirect(url_for('engine.death'))

    return render_template('game/room4.html', room=current_room)


@bp.route('/room5', methods=('GET', 'POST'))
def room5():
    current_room = {
        "title": "Room 5 - Basement",
        "intro": '''Hurry, Chuky is going to find you!
        Where do you want to go now?
          1) Living Room
          2) Kitchen
          3) Bedroom
          4) Bathroom
          5) Stay hiding here'''
        }

    correctPath = random.randint(1, 5)

    if request.method == 'POST':
        correctPath = request.form['action']
        if correctPath == 1:
            return redirect(url_for('engine.room1'))
        elif correctPath == 2:
            return redirect(url_for('engine.room2'))
        elif correctPath == 3:
            return redirect(url_for('engine.room3'))
        elif correctPath == 4:
            return redirect(url_for('engine.room4'))
        elif correctPath == 5:
            return redirect(url_for('engine.room5'))
        else:
            return redirect(url_for('engine.death'))

    return render_template('game/room5.html', room=current_room)


@bp.route('/death', methods=('GET', 'POST'))
def death():
    return render_template('game/death.html')
