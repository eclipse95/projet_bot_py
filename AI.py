# ---------fichier pour stocker l'IA L2
# ---------véritable usine à gaz
import random
from poooc import order, state, state_on_update, etime
from class_plateau import *
import parser
import inspect
import logging
from order import *


global plateau              # les variables globales, ça craint
board = plateau()                  # variable plateau
global node_prod2
node_prod2 = None

def register_pooo(uid):
    board.set_uid(uid)
    logging.info('[register_pooo] Bot {} registered'.format(uid))
    #global UID              # inutile?
    #UID = uid                 # inutile?
    pass


def init_pooo(init_string):
    #logging.info('[init_pooo] Game init: {!r}'.format(init_string))
    parser.parser_init(str(init_string), board)
    board.display()
    for i in range(int(board.nb_node)):
        if len(board.liste_node[i].prod_off) == 2 or str(board.liste_node[i].prod_off) == 'II':
            node_prod2 = board.liste_node[i]
    pass


def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))

    while True:
        msg = state_on_update()
        if 'STATE' in msg:
            logging.debug('[play_pooo] Received state: {}'.format(msg))
            parser.parser_state(msg, board)
            board.display()
            nb_mynode=0
            for i in range(int(board.nb_node)):
                if (board.liste_node[i].owner == board.flag):   # si le noeud m'appartient
                    nb_mynode+=1
                    if len(board.liste_node[i].neighbor) == 1:
                        current_node = board.find_node(board.liste_node[i].neighbor[0])
                        if (current_node.offsize < 30):
                            order(parser.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                    else:
                        for j in  board.liste_node[i].neighbor:     # je regarde ses voisins
                            current_node = board.find_node(j)
                            if current_node.owner != board.flag:    # si un de ces voisins est un ennemi
                                if board.liste_node[i].offsize > (current_node.offsize + current_node.defsize):
                                    order(parser.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                                elif board.liste_node[i].offsize > 29:
                                    order(parser.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                            elif current_node.owner == board.flag:  # si ces voisins sont alliés
                                for k in current_node.neighbor:
                                    current_node_k = board.find_node(k)
                                    if current_node_k.owner != board.flag:  # si un des voisins est ennemi
                                        move = parser.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node_k.id)
                                        order(move)
                                    else:
                                        order(parser.ordre_builder(board.uid, 100, current_node.id, node_prod2.id))
            logging.info('============ ( {} / {} ) ============='.format(nb_mynode, board.nb_node))
        elif 'GAMEOVER' in msg:      # on arrête d'envoyer des ordres. On observe seulement...
            order('[{}]GAMEOVEROK'.format(board.uid))
            logging.debug('[play_pooo] Received game over: {}'.format(msg))
        elif 'ENDOFGAME' in msg:     # on sort de la boucle de jeu
            logging.debug('[play_pooo] Received end of game: {}'.format(msg))
            break
        else:
            logging.error('[play_pooo] Unknown msg: {!r}'.format(msg))
    logging.info('>>> Exit play_pooo function')
    pass

