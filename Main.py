__author__ = 'E149248B'

from class_plateau import *
from parser import *
import inspect
import logging

#global board=plateau()                  #variable global plateau
                                        #les variables globales, c'est mal, je sais

def register_pooo(uid):
    #board.set_uid(uid)
    pass
def init_pooo(init_string):
    tmp=parser_init(init_string)
    print(tmp)
    #board.set_settings()
    pass
def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))
    pass