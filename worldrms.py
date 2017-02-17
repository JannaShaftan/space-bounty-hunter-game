__author__ = 'Janna'

DESC = 'desc'
DESC2 = 'desc2'
NORTH = 'north'
WEST = 'west'
EAST = 'east'
SOUTH = 'south'
APPROACH_W_KNIFE = 'approach2'
APPROACH = 'approach1'


#The game's world data is stored in a dictionary.
worldRooms = {
    'start': {
        DESC: 'You\'ve always been lucky, but surely surviving this fall has sapped the luck ' +
     'reservoir for all generations to follow.'
    },
    'start2': {
        DESC: 'You open your eyes slowly, first one, then the other and check that your limbs are still intact.'
    },
    'start3': {
        DESC: 'They are. You must be quite liked by the Gods. But ah, the spaceplane...'
    },
    'start4': {
        DESC: 'The fusion engine steams and sputters hopelessly. How are you going to get off this damned asteroid before they find you?'
    },
    'start5': {
        DESC: 'Outside, the asteroid surface resembles a vacant desert with a few radioactive tumbleweeds bouncing across.\n' +
              'To the far \033[1mwest\033[0m, your heart surges in hope when you make out the outline of what seems to be a farmhouse, with a sleepily turning windmill and the distant, ghostly sound of chimes.\n' +
              'To the \033[1meast\033[0m, a crater glows eerily, planes of sharp blue light jutting vertically into the sky.\n' +
              'The deserted landscape fades into the distance up \033[1mnorth\033[0m.\n\n' +
              'Before you go off and explore, you should \033[1mexamine\033[0m your \033[1mship\033[0m.\n'
    },
    'ship': {
      DESC: 'Despite being a robust craft, she has been worn down by your heavy abuse and years of bounty-hunting in space.\n' +
            'Looks like she\'ll need \033[1mfuel\033[0m and a \033[1mheavy plasma band\033[0m to patch up the hole before you can fly again.\n',
      DESC2: 'Ah she\'s all patched up now. How clever you are. The crumpled bounty in your hand, you\'re back to business.\n' +
            'Hyperspace welcomes you back and a crystal you\'ve managed to snag from the mystic will look lovely round your neck.' +
            '\033[1m[GAME WON]\033[0m\n',
      NORTH: 'asteroid',
      WEST: 'mystic',
      EAST: 'crater',
    },
    'mystic': {
        DESC: 'No signs of life as you approach the farmhouse. You knock and wait... \n"Ah yes, right on time.." the door swings open.\n' +
        'You\'re face to face with one of the secluded asteroid mystics of Euphrosyne belt.\n' +
        '"I don\'t suppose you stopped in for a cup of tea, then." You explain your current misgiving situation, while his third eye rolls around, detecting untruths.\n' +
        '"No, I don\'t think you\'re as innocent as you say..." he says. "But I will help you."\n' +
        '"Fetch me some glowing crystals from the crater down yonder and I\'ll have you in the air back to your nefarious ways."\n' +
        '"You may need this". \033[94m\033[1m[[ACQUIRED MACHETE]]\033[0m ...Um, okay',
        DESC2: '"Wow, did not think I\'d be seeing you again" says the mystic, throwing the glowing crystals into what seems to be a... huge burlap sack of glowing crystals.\n' +
               '"Well a promise is a promise." \033[94m\033[1m[[ACQUIRED FUEL]] \033[0m\n \033[94m\033[1m[[ACQUIRED PLASMA BAND]]\033[0m\n',
        EAST: 'asteroid',
        SOUTH: 'ship',
    },
    'asteroid': {
        DESC: 'The asteroid terrain unfolds around you.\n' +
              'The great vacancy of the sky overhead is so vast that language becomes undone until you feel like a nameless animal.\n',
        WEST: 'mystic',
        EAST: 'crater',
        SOUTH: 'ship',
    },
    'crater': {
        DESC: 'As you approach, the blissful lights emanating from the crater seem alive themselves.\n' +
        'A beast lays dormant in the center, it\'s mammoth-size ivory fangs lead you to believe it is probably an introvert...\n' +
        '\033[1m\x1B[3mApproach\033[0m\x1B[3m at your own caution...\x1B[0m',
        APPROACH: 'You decide your stealth needs some work as a opal eyeball emerges from behind closed lids.\n' +
        'Seconds later, you\'re hurtling through the air and sliding down a throat canal... \033[1m[GAME OVER]\033[0m\n',
        APPROACH_W_KNIFE: 'The beast stirs, rising up in fury once her pupils narrow in on you.\n' +
        "Her virulent scream is swallowed by space and cut short by the quicksilver flash of your machete.\n" +
        "You chip off some glowing crystals from the crater's entrails.\n" +
        "\033[94m\033[1m[[ACQUIRED GLOWING CRYSTALS]]\033[0m\n",
        WEST: 'asteroid',
        SOUTH: 'ship',
    },
}