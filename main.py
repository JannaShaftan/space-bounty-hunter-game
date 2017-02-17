#!/usr/bin/env python
__author__ = 'Janna Shaftan'

from termclr import print_wg, print_c
from command import processCmd, displayLocation, GAME_LOST, GAME_WON
import time

def startgame():
    #print_wg('\x1B[3mMemento Vivere\x1B[3m')
    print('\n\n')
    print_c('\x1B[3mCRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRACK!!\x1B[3m')
    time.sleep(2)
    loc = 'start'
    displayLocation(loc)
    loc = 'start2'
    time.sleep(3)
    displayLocation(loc)
    loc = 'start3'
    time.sleep(4)
    displayLocation(loc)
    loc = 'start4'
    time.sleep(5)
    displayLocation(loc)
    loc= 'start5'
    time.sleep(7)
    print('\n')
    displayLocation(loc)


if __name__ == '__main__':
    startgame()
    processCmd().cmdloop()
