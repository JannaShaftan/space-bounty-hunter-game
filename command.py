__author__ = 'Janna'

import cmd
import textwrap
from worldrms import worldRooms
from worlditms import worldItems
from tabulate import tabulate


#Constant Vars
EXAMINE_SHIP = 0
MYSTIC_SEEN = 0
DESC = 'desc'
DESC2 = 'desc2'
SCREEN_WIDTH = 80
GAME_WON = False
GAME_LOST = False
loc = 'ship'
inventory = ['bounty']

def displayLocation(loc):
    #Print room and description
    if loc == "mystic":
        global MYSTIC_SEEN
        if MYSTIC_SEEN == 0:
            global MYSTIC_SEEN
            MYSTIC_SEEN = 1
            global inventory
            inventory.append('machete')
            print('\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))
        elif 'crystals' in inventory:
            print('\n'.join(textwrap.wrap(worldRooms[loc][DESC2], SCREEN_WIDTH)))
            global inventory
            inventory.append('plasma')
            inventory.append('fuel')
    elif loc == "ship" and 'fuel' in inventory:
            print('\n'.join(textwrap.wrap(worldRooms[loc][DESC2], SCREEN_WIDTH)))
            global GAME_WON
            GAME_WON = 1
            return True
    else:
        print('\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))


def moveDirection(direction):
    #Change location of player
    global loc
    if direction in worldRooms[loc]:
        loc = worldRooms[loc][direction]
        displayLocation(loc)
    else:
        print("You go " + direction + ". But there's nothing there for you.")



class processCmd(cmd.Cmd):
    prompt = '\n>'
    def default(self, arg):
        print('If you need some help, why not just ask..? Type "help".')
    def do_quit(self, arg):
        return True
    def do_examine(self, arg):
        "Examine <location> or <item>"
        if not arg:
            print("What would you like to examine?")
        elif arg == 'ship':
            displayLocation(arg)
            global EXAMINE_SHIP
            EXAMINE_SHIP = 1
        elif arg in worldItems:
            print('\n'.join(textwrap.wrap(worldItems[arg][DESC], SCREEN_WIDTH)))
        else:
            print('You can\'t examine that.')
    def do_go(self, arg):
        "Move in a direction - go <North, South, East, West>"
        if EXAMINE_SHIP == 0:
            print("You should check out your ship's condition before you head off into the unknown.")
        else:
            if not arg:
                print("Where to darlin?")
                print(tabulate([[' ', 'North / Asteroid Turf', ' '], ['West/Mystic', ' Asteroid Turf ', 'East/Crater'], [' ', 'South / Plane Crash', ' ']], tablefmt='fancy_grid'))
            else:
                moveDirection(arg)
    def do_inventory(self, arg):
        "Look at your inventory - type inventory."
        print('\n\033[1mINVENTORY:\033[0m')
        global inventory
        for item in inventory:
            print('*' + item)
        print('\n\x1B[3mFor a closer look, type examine <item>\x1B[0m')
    def do_approach(self, arg):
        if loc == "crater":
            global inventory
            "type 'approach' to get closer to an entity"
            if 'machete' not in inventory:
                print('\n'.join(textwrap.wrap(worldRooms['crater']['approach1'], SCREEN_WIDTH)))
                global GAME_LOST
                return True
            else:
                print('\n'.join(textwrap.wrap(worldRooms['crater']['approach2'], SCREEN_WIDTH)))
                inventory.append('crystals')
        else:
            print("Nothing to approach, but also nothing to recoil from. ")

    do_inv = do_inventory





