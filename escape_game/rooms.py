from escape import *

correctPath = random.randint(1, 5)

class Rooms(object):
    def __init__(self, theroom):
        self.theroom = theroom

    def whereat(self):
        for line in self.theroom:
            print(line)

living_room = Rooms([
    "\n \n -->You are in the living room now"
])

kitchen = Rooms([
    "\n \n -->You are in the kitchen now"
])

bedroom = Rooms([
    "\n \n -->You are in the bedroom now"
])

bathroom = Rooms([
    "\n \n -->You are in the bathroom now"
])

basement = Rooms([
    "\n \n -->You are in the basement now"
])

def room01():
    #cls()
    #print("\n \n --> ROOM 1")
    print(living_room)
    time.sleep(3)
    print('''
  Hurry, Chuky is going to find you!
  Where do you want to go now?
    1) Stay hiding here
    2) Kitchen
    3) Bedroom
    4) Bathroom
    5) Basement
    ''')
    path_choice = int(input("> "))

    #living_room.whereat()

    if path_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")
        print("Press CTRL + D if you want to exit the game.")
        print("Press 6 if you want to restart the game.")
        restart_game = int(input("> "))

    if restart_game == 6:
        display_intro()
    else:
        room01()


def room02():
    #cls()

    print("\n \n --> ROOM 2")
    print(kitchen)
    time.sleep(3)
    print('''
  Hurry, Chuky is going to find you!
  Where do you want to go now?
    1) Living Room
    2) Stay hiding here
    3) Bedroom
    4) Bathroom
    5) Basement
    ''')
    path_choice = input("> ")

    #kitchen.whereat()

    if path_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")
        print("Press CTRL + D if you want to exit the game.")
        print("Press 6 if you want to restart the game.")
        restart_game = int(input("> "))

    if restart_game == 6:
        display_intro()
    else:
        room02()

def room03():
    #cls()

    print("\n \n --> ROOM 3")
    print(bedroom)
    time.sleep(3)
    print('''
  Hurry, Chuky is going to find you!
  Where do you want to go now?
    1) Living Room
    2) Kitchen
    3) Stay hiding here
    4) Bathroom
    5) Basement
    ''')
    path_choice = input("> ")

    #bedroom.whereat()

    if path_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")
        print("Press CTRL + D if you want to exit the game.")
        print("Press 6 if you want to restart the game.")
        restart_game = int(input("> "))

    if restart_game == 6:
        display_intro()
    else:
        room03()

def room04():
    #cls()

    print("\n \n --> ROOM 4")
    print(bathroom)
    time.sleep(3)
    print('''
  Hurry, Chuky is going to find you!
  Where do you want to go now?
    1) Living Room
    2) Kitchen
    3) Bedroom
    4) Stay hiding here
    5) Basement
    ''')
    path_choice = input("> ")

    #bathroom.whereat()

    if path_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")
        print("Press CTRL + D if you want to exit the game.")
        print("Press 6 if you want to restart the game.")
        restart_game = int(input("> "))

    if restart_game == 6:
        display_intro()
    else:
        room04()

def room05():
    #cls()

    print("\n \n --> ROOM 5")
    print(basement)
    time.sleep(3)
    print('''
  Hurry, Chuky is going to find you!
  Where do you want to go now?
    1) Living Room
    2) Kitchen
    3) Bedroom
    4) Bathroom
    5) Stay hiding here
    ''')
    path_choice = input("> ")

    #basement.whereat()

    if path_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")
        print("Press CTRL + D if you want to exit the game.")
        print("Press 6 if you want to restart the game.")
        restart_game = int(input("> "))

    if restart_game == 6:
        display_intro()
    else:
        room05()
