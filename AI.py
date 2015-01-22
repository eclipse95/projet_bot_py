#---------fichier pour stocker l'IA L2

import random
from poooc import order, state, state_on_update, etime
from class_plateau import *
import parser
import inspect
import logging



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
            nb_mynode=0
            for i in range (int(board.nb_node)):
                if (board.liste_node[i].owner == board.flag):
                    nb_mynode+=1
                    for j in  board.liste_node[i].neighbor:
                        current_node = board.find_node(j)
                        if current_node.owner != board.flag:
                            if board.liste_node[i].offsize > current_node.offsize + 2:
                                order(board.uid, 100, board.liste_node[i].id, current_node.id)
                            if board.liste_node[i].offsize > 29:
                                order(board.uid, 100, board.liste_node[i].id, current_node.id)
                        elif current_node.owner == board.flag:
                            for k in current_node.neighbor:
                                current_node_k = board.find_node(k)
                                if current_node_k.owner != board.flag:
                                    order(board.uid, 100, board.liste_node[i].id, current_node_k.id)
            logging.info('============ ( {} / {} ) ============='.format(nb_mynode,board.nb_node))
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

