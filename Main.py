__author__ = 'E149248B'

from class_plateau import *
from parser import *
import inspect
import logging

global plateau              #les variables globales, ça craint
board=plateau()                  #variable plateau

def register_pooo(uid):
    board.set_uid(uid)
    pass

def init_pooo(init_string):
    tmp=parser_init(init_string)
    print(tmp)
    board.set_settings(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])
    pass

def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))
    pass