#---------fichier pour stocker l'IA suggeré par Pierre

#----------LIBS----------
from class_plateau import *
from poooc import order, state, state_on_update, etime
import parser
import inspect
import logging
from order import *
import random

global board              #les variables globales, ça craint
board = plateau()                  #variable plateau


def register_pooo(uid):
    board.set_uid(uid)
    logging.info('[register_pooo] Bot {} registered'.format(uid))
    pass


def init_pooo(init_string):
    # logging.info('[init_pooo] Game init: {!r}'.format(init_string))
    parser.parser_init(str(init_string), board)
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
            parser.parser_state(msg, board)
            board.display()
            for i in range(board.nb_node):
                if board.liste_node[i].owner == board.flag:
                    liste_node_allie.append(board.liste_node[i].id)
                elif board.liste_node[i] == -1:
                    liste_node_neutre.append(board.liste_node[i].id)
                else:
                    liste_node_ennemi.append(board.liste_node[i].id)
            for a in range(len(liste_node_allie)):     # Parcours des cellules alliées
                source = board.find_node(a)            # Copie l'addresse memoire dans source # source est de "type Node"
                cible = None
                if check_in(source.neighbor, liste_node_ennemi) and source.offsize > 0:     # si le node a un ennemi
                    for i in range(len(source.neighbor)):
                        cible = board.find_node(source.neighbor[i])
                        if (cible != board.flag and cible != -1):   # on trouve l'ennemi
                            if source.offsize > (cible.offsize + cible.defsize) or source.offsize == 30:
                                order(parser.ordre_builder(board.uid, 100, source.id, cible.id))   # on l'attaque
                elif check_in(source.neighbor, liste_node_neutre) and source.offsize > 0:
                    # on peut mettre qu'une seule condition, l'autre est déjà testé
                    # Si les voisins sont neutres (ou allié)
                    cible = board.find_node(source.neighbor[0])  # cible est de type node
                    troupe_a_envoyer_min = cible.defsize + cible.offsize + 1
                    # Nbre de vaisseaux à envoyé pour prendre la planète
                    for b in range(len(source.neighbor)):
                        # On parcourt les voisins neutres
                        cible_2 = board.find_node(source.neighbor[b])       # 2e cible pour comparer avec cible
                        troupe_a_envoyer = (cible_2.defsize + cible_2.offsize + 1)
                        if troupe_a_envoyer < troupe_a_envoyer_min:
                            troupe_a_envoyer_min = troupe_a_envoyer
                            cible = cible_2         # la cible 2 devient la cible

                    if troupe_a_envoyer_min < source.offsize:     # Teste si on peut attaquer
                        ordre = parser.ordre_builder(board.uid, 100, source.id, cible.id)   # creer l'ordre
                        # crée l'ordre d'attaque
                        order(ordre)
                        # A l'ATTAQUE
                elif source.offsize > 0:
                    # Si les voisins sont alliés
                    if len(source.neighbor) == 1:   # le noeud n'a qu'un voisin allié
                        cible = board.find_node(source.neighbor[0])
                        order(parser.ordre_builder(board.uid,(30-cible.offsize)*100/source.offsize, source.id, cible.id))
                    else:
                        for b in range(len(source.neighbor)):   # On parcourt ses voisins
                            source_2 = source.neighbor[b]
                            if check_in(source_2.neighbor,liste_node_ennemi) or check_in(source_2,liste_node_neutre):
                                # on envoie des renforts
                                if (source.offsize != 0):
                                    order(parser.ordre_builder(board.uid,(30-source_2.offsize)*100/source.offsize, source.id, source_2.id))
                                    pass
                        if source.offsize != 0:
                            cible = board.find_node(random.choice(source.neighbor))
                            order(parser.ordre_builder(board.uid,(30-cible.offsize)*100/source.offsize, source.id, cible.id))

            logging.info('============ ( {} / {} ) ============='.format(len(liste_node_allie), board.nb_node))

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


def check_in(liste1, liste2):
    for i in range(len(liste1)):
        for j in range(len(liste2)):
            if liste1[j] == liste2[i]:
                return True
    return False