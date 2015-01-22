#---------fichier pour stocker l'IA L1

#----------LIBS----------
from class_plateau import *
from poooc import order, state, state_on_update, etime
import parser
import inspect
import logging
import random

global plateau              #les variables globales, ça craint
board = plateau()                  #variable plateau


def register_pooo(uid):
    board.set_uid(uid)
    logging.info('[register_pooo] Bot {} registered'.format(uid))
    global UID              #inutile?
    UID = uid                 #inutile?
    pass


def init_pooo(init_string):
    #logging.info('[init_pooo] Game init: {!r}'.format(init_string))
    parser.parser_init(str(init_string),board)
    board.display()
    pass


def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))

    while True:
        msg = state_on_update()
        if 'STATE' in msg:
            logging.debug('[play_pooo] Received state: {}'.format(msg))
            parser.parser_state(msg,board)
            for i in range (board.nb_node):
                if board.liste_node[i].offsize > 10 and board.liste_node[i].owner == board.flag:
                    target_id = random.choice(board.liste_node[i].neighbor)
                    order(board.uid, random.randint(0, 100), board.liste_node[i].id, target_id)

        elif 'GAMEOVER' in msg:      # on arrête d'envoyer des ordres. On observe seulement...
            order ('[{}]GAMEOVEROK'.format(UID))
            logging.debug('[play_pooo] Received game over: {}'.format(msg))
        elif 'ENDOFGAME' in msg:     # on sort de la boucle de jeu
            logging.debug('[play_pooo] Received end of game: {}'.format(msg))
            break
        else:
            logging.error('[play_pooo] Unknown msg: {!r}'.format(msg))
    logging.info('>>> Exit play_pooo function')
    pass