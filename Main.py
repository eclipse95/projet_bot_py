__author__ = 'E149248B'

from class_plateau import *
from parser import *
import inspect
import logging

global board=plateau()                  #variable global plateau
                                        #les variables globales, c'est mal, je sais

def register_pooo(uid):                 #je ne sais pas comment ça marche mais ça marche
    board.set_uid(uid)
    pass
def init_pooo(init_string):
    pass
def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))
    pass