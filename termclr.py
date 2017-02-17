__author__ = 'Janna'

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from termcolor import cprint

#Colored Text for Terminal

print_wg = lambda x: cprint(x, 'grey', 'on_white')
print_c = lambda x: cprint(x, 'red', attrs=['bold'])
