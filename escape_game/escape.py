#-- Develop by Julio Pochet
#-- Escape The Curse Of Chucky

# Global imports
#from os.path import exists
from sys import exit
import random
import time
from rooms import *
##
#import rooms
#rooms.room01()
#rooms.room02()
#rooms.room03()
#rooms.room04()
#rooms.room05()
##

#- Functions

def cls():
    print("\n" * 70)

def loading_game():
    cls()
    print("LOADING GAME...")
    time.sleep(3)
    print("THE GAME WILL START IN 5 SECONDS...")
    time.sleep(5)
    cls()
    display_intro()

def display_intro():
    start_game_key = ["5"]
    start_game_user_choice = ""

    print('-' * 60)
    print('''WELCOME TO THE "ESCAPE THE CURSE OF CHUCKY GAME"''')
    print('-' * 60)
    time.sleep(3)
    print("In this text based game, you will have to make the right choices in order to win/escape from Chucky.")
    print('-' * 60)
    time.sleep(3)
    print("GOOD LUCK! You'll need it. HA..HA")
    print('-' * 60)
    time.sleep(3)
    print("Press CTRL + D if you want to exit the game.")
    print("If you want to Continue to the game, please press 5")

    continue_game = input("> ")

    if continue_game == start_game_key[0]:
        start_room()
    elif continue_game != start_game_key[0]:
        cls()
        display_intro()

def start_room():

    print("What is your name?")
    player_name = str(input("> "))

    start_room_options = ["1", "2", "3", "4", "5"]
    user_choice = ""
    while user_choice not in start_room_options:
        cls()
        print(f"{player_name}...")
        print('''
    You were stressed from work, so you went on a vacation to a Cabin in the Caribbean to reconnect with life.
    After a couple drinks and the sun sets behind the mountains you went and turned all the lights on, however a few hours later the lights started to malfunction.
    Then you hear someone knocking on the front door, so you went to see who it was and after you opened the door there was nobody there.
    You didn't worry too much about it and went to your bedroom to watch some movies.
    A few minutes passed, someone knocked on the front door again...
    What do you do?
    1) Ignore it and stay in bed.
    2) Go out and see who's knocking on the door.
    3) Call the Cabin owner and complain about people knocking on your door.
    4) Go out with a baseball bat.
    5) Ignore life and fall asleep.
    ''')

        user_choice = input("> ")

    print(f"You have selected {user_choice}")

    if user_choice == start_room_options[0]:
        room01()
    elif user_choice == start_room_options[1]:
        room02()
    elif user_choice == start_room_options[2]:
        room03()
    elif user_choice == start_room_options[3]:
        room04()
    elif user_choice == start_room_options[4]:
        room05()
    #elif user_choice.int() == False:
    #    print("PLEASE ENTER A NUMBER FROM 1 TO 5")
    #    user_choice = int(input("> "))

    #elif type(user_choice) != int:
    #    print("ENTER A NUMBER FROM 1 TO 5")
    #else:
    #    print("ENTER A NUMBER FROM 1 TO 5")
    #    user_choice = int(input("> "))

#- Main Program
loading_game()
#display_intro()
#start_room()
