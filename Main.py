__author__ = 'E149248B'
#----------LIBS----------
from class_plateau import *
from parser import *
from poooc import order, state, state_on_update, etime

import inspect
import logging

global plateau              #les variables globales, ça craint
board=plateau()                  #variable plateau

def register_pooo(uid):
    board.set_uid(uid)
    logging.info('[register_pooo] Bot {} registered'.format(uid))
    global UID              #inutile?
    UID=uid                 #inutile?
    pass

def init_pooo(init_string):
    logging.info('[init_pooo] Game init: {!r}'.format(init_string))
    tmp=parser_init(init_string)
    print(tmp)
    board.set_settings(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])
    pass

def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))

    while True:
        msg=state_on_update()
        if 'STATE' in msg:
            logging.debug('[play_pooo] Received state: {}'.format(msg))
        elif 'GAMEOVER' in msg: # on arrête d'envoyer des ordres. On observe seulement...
            order ('[{}]GAMEOVEROK'.format(UID))
            logging.debug('[play_pooo] Received game over: {}'.format(msg))
        elif 'ENDOFGAME' in msg: # on sort de la boucle de jeu
            logging.debug('[play_pooo] Received end of game: {}'.format(msg))
            break
        else:
            logging.error('[play_pooo] Unknown msg: {!r}'.format(msg))
    logging.info('>>> Exit play_pooo function')
    pass