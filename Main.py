# ---------fichier pour stocker l'IA L1
# envoi un nombre aléatoire d'unité offensive si un noeud atteint 10 unités offensive
# ----------LIBS----------
from parser import *
import parser
import inspect
import logging
import random
from class_plateau import *
from poooc import order, state, state_on_update, etime


global plateau              # les variables globales, ça craint
board = plateau()                  # variable plateau
global chain

def register_pooo(uid):
    board.set_uid(uid)
    logging.info('[register_pooo] Bot {} registered'.format(uid))
    global UID
    UID = uid
    pass


def init_pooo(init_string):
    # logging.info('[init_pooo] Game init: {!r}'.format(init_string))
    chain = init_string
    pass


def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))
    parser.parser_init(chain, board)
    board.display()
    while True:
        msg = state_on_update()
        if 'STATE' in msg:
            logging.debug('[play_pooo] Received state: {}'.format(msg))
            parser_state(msg, board)
            board.display()
            nb_node = 0
            for i in range(board.nb_node):
                if board.liste_node[i].owner == board.flag:
                    nb_node += 1
                    if board.liste_node[i].offsize > 10:
                        target_id = random.choice(board.liste_node[i].neighbor)
                        order(ordre_builder(board.uid, random.randint(0, 100), board.liste_node[i].id, target_id))
            logging.info('============ ( {} / {} ) ============='.format(nb_node, board.nb_node))

        elif 'GAMEOVER' in msg:      # on arrête d'envoyer des ordres. On observe seulement...
            order('[{}]GAMEOVEROK'.format(UID))
            logging.debug('[play_pooo] Received game over: {}'.format(msg))
        elif 'ENDOFGAME' in msg:     # on sort de la boucle de jeu
            logging.debug('[play_pooo] Received end of game: {}'.format(msg))
            break
        else:
            logging.error('[play_pooo] Unknown msg: {!r}'.format(msg))
    logging.info('>>> Exit play_pooo function')
    pass