#---------fichier pour stocker l'IA suggeré par Pierre

#----------LIBS----------
from class_plateau import *
from poooc import order, state, state_on_update, etime
import parser
import inspect
import logging
from order import *
import random

global plateau              #les variables globales, ça craint
board = plateau()                  #variable plateau


def register_pooo(uid):
    board.set_uid(uid)
    logging.info('[register_pooo] Bot {} registered'.format(uid))
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
            liste_node_ennemi = []
            liste_node_neutre = []
            liste_node_allie = []
            logging.debug('[play_pooo] Received state: {}'.format(msg))
            parser.parser_state(msg,board)
            for i in range (board.nb_node):
                if board.liste_node[i].owner == board.flag:
                    liste_node_allie.append(board.liste_node[i].id)
                elif board.liste_node[i]== -1:
                    liste_node_neutre.append(board.liste_node[i].id)
                else:
                    liste_node_ennemi.append(board.liste_node[i].id)
            for a in range (len(liste_node_allie)):   # Parcours des cellules alliées
                source=board.find_node(a)
                if source.neighbor not in liste_node_ennemi and source.neighbor in liste_node_neutre :       #Si les voisins sont neutres (ou allié)
                    cible = board.find_node(source.neighbor[0])
                    troupe_a_envoyer_min = (cible.defsize+cible.offsize+1)
                    #Nbre de vaisseaux à envoyé pour prendre la planète
                    for b in range(len(source.neighbor)) :
                    #On parcourt les voisins neutres
                        cible_2 = board.find_node(source.neighbor[b])
                        troupe_a_envoyer = (cible_2.defsize+cible_2.offsize+1)
                        if troupe_a_envoyer < troupe_a_envoyer_min :
                            troupe_a_envoyer_min = troupe_a_envoyer
                            cible = cible_2
    
                    if  troupe_a_envoyer_min < source.offsize :     #Teste si on peut attaquer
                        #order = parametre_move(board.uid,100,liste_node_allie[a],cible)
                        #crée l'ordre d'attaque
                        #poooc.order(order)
                        order(board.uid,100,source.id,cible.id)
                        #A l'ATTAQUE

            logging.info('============  {}  ============='.format(liste_node_allie))

        elif 'GAMEOVER' in msg:      # on arrête d'envoyer des ordres. On observe seulement...
            order ('[{}]GAMEOVEROK'.format(board.uid))
            logging.debug('[play_pooo] Received game over: {}'.format(msg))
        elif 'ENDOFGAME' in msg:     # on sort de la boucle de jeu
            logging.debug('[play_pooo] Received end of game: {}'.format(msg))
            break
        else:
            logging.error('[play_pooo] Unknown msg: {!r}'.format(msg))
    logging.info('>>> Exit play_pooo function')
    pass