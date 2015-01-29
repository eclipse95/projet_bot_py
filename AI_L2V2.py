# ---------fichier pour stocker l'IA L2V2
# --------- niveau standard
# passage par reference[ok]

# Libs
import random
from poooc import order, state, state_on_update, etime
from class_plateau import *
import parse
import inspect
import logging


global plateau              # les variables globales, ça craint
global target_list
board = plateau()                  # variable plateau
target_list = []                   # liste des cibles prioritaires (production II et III)


def register_pooo(uid):
    board.set_uid(uid)              # stocke UID dans le plateau
    logging.info('[register_pooo] Bot {} registered'.format(uid))
    pass


def init_pooo(init_string):
    logging.info('[init_pooo] Game init: {!r}'.format(init_string))
    parse.parser_init(init_string, board)           # parse INIT
    board.display()                                 # affichage du plateau pour les tests
    for i in range(len(board.liste_node)):          # determine les noeuds prioritaires
        if board.liste_node[i].prod_off == 'II' or board.liste_node[i].prod_off == 'III':
            target_list.append(board.liste_node[i].id)
        tmp_ls = []
        for j in range(len(board.liste_node[i].neighbor)):
            tmp_ls.append(board.find_node(board.liste_node[i].neighbor[j]))
        board.liste_node[i].neighbor = tmp_ls
    pass


def play_pooo():
    logging.info('Entering play_pooo fonction from {} module...'.format(inspect.currentframe().f_back.f_code.co_filename))

    while True:
        msg = state_on_update()
        if 'STATE' in msg:
            logging.debug('[play_pooo] Received state: {}'.format(msg))
            parse.parser_state(msg, board)          # parse la chaine STATE
            board.display_v2()                         # affiche le plateau, pratique pour voir l'évolution du jeu
            nb_mynode = 0                           # compteur nombre de noeuds possedés
            for i in range(int(board.nb_node)):     # examine tous les noeuds
                if board.liste_node[i].owner == board.flag:   # si le noeud m'appartient
                    nb_mynode += 1
                    b_attaque = False   # témoin d'attaque
                    if board.liste_node[i].offsize > 0:
                        for current_node in board.liste_node[i].neighbor:     # je regarde ses voisins
                            if current_node.owner != board.flag and current_node.owner != -1:
                                b_attaque = True
                                if board.liste_node[i].offsize > (current_node.offsize + current_node.defsize):
                                    # si j'ai suffisament d'unité pour prendre le noeud
                                    order(parse.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                                elif board.liste_node[i].offsize == board.liste_node[i].max_off:
                                    # si le noeud est plein
                                    order(parse.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                            elif current_node.owner != board.flag and check_in([current_node.id], target_list):
                                # si un de ses voisins est un ennemi et fait partie de la liste prioritaire
                                b_attaque = True
                                if board.liste_node[i].offsize > (current_node.offsize + current_node.defsize):
                                    # si j'ai suffisament d'unité pour prendre le noeud
                                    order(parse.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                                elif board.liste_node[i].offsize == board.liste_node[i].max_off:
                                    # si le noeud est plein
                                    order(parse.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                            elif current_node.owner != board.flag:    # si un de ses voisins est un ennemi ou neutre
                                b_attaque = True
                                if board.liste_node[i].offsize > (current_node.offsize + current_node.defsize):
                                    # si j'ai suffisament d'unité pour prendre le noeud
                                    order(parse.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                                elif board.liste_node[i].offsize == board.liste_node[i].max_off:
                                    # si le noeud est plein
                                    order(parse.ordre_builder(board.uid, 100, board.liste_node[i].id, current_node.id))
                        if not b_attaque:    # pas encore déplacer d'unité et pas d'ennemi
                            if len(board.liste_node[i].neighbor) == 1 and board.liste_node[i].offsize > 0:
                                # si le noeud n'a qu'un voisin
                                b_attaque = True
                                if current_node.offsize <= board.liste_node[i].max_off:
                                    # si le noeud voisin n'est pas plein
                                    order(parse.ordre_builder(board.uid, max_renfort(board.liste_node[i], current_node),
                                                              board.liste_node[i].id, current_node.id))
                                    print(board.liste_node[i].id,' a aidé' ,current_node.id,'avec' ,max_renfort(board.liste_node[i], current_node), 'unités')
                            for current_node in board.liste_node[i].neighbor:     # je regarde ses voisins
                                if current_node.owner == board.flag:  # si ses voisins sont alliés
                                    for current_node_k in current_node.neighbor:     # je regarde leur voisins
                                        if current_node_k.owner != board.flag:  # si un des voisins est ennemi
                                            # j'envois des unités de renfort
                                            move = parse.ordre_builder(board.uid, max_renfort(board.liste_node[i], current_node), board.liste_node[i].id, current_node.id)
                                            order(move)
                                            print(board.liste_node[i].id,' a aidé' ,current_node.id,'avec' ,max_renfort(board.liste_node[i], current_node), 'unités')
                                            b_attaque = True
                            if not b_attaque:
                                for current_node in board.liste_node[i].neighbor:   # je regarde ses voisins
                                    if current_node.owner == board.flag:  # si ses voisins sont alliés
                                        for current_node_k in current_node.neighbor:     # je regarde leur voisins
                                            if current_node_k.owner == board.flag:
                                                for current_node_l in current_node_k.neighbor:
                                                    if current_node_l.owner != board.flag:
                                                        # si un des voisins est ennemi  # j'envois des unités de renfort
                                                        move = parse.ordre_builder(board.uid, max_renfort(board.liste_node[i], current_node), board.liste_node[i].id, current_node.id)
                                                        order(move)
                                                        b_attaque = True
                                                        print(board.liste_node[i].id,' a aidé' ,current_node.id,'avec' ,max_renfort(board.liste_node[i], current_node), 'unités')
                                if not b_attaque:
                                    # je prends un noeud au hasard est je lui des troupes
                                    cible = board.liste_node[i].neighbor[random.randint(0, len((board.liste_node[i].neighbor)))-1]
                                    order(parse.ordre_builder(board.uid, max_renfort(board.liste_node[i], cible), board.liste_node[i].id, cible.id))
                                    print(board.liste_node[i].id,' a aidé' ,cible.id,'avec' ,max_renfort(board.liste_node[i], cible), 'unités')

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


def check_in(liste1, liste2):   # fonction qui verifie la présence d'un élément commun aux deux listes
    for i in range(len(liste1)):
        for j in range(len(liste2)):
            if liste1[i] == liste2[j]:
                return True
    return False


def max_renfort(source, cible):  # calcul le nombre d'unités à envoyer
    max_off = int(((cible.max_off-cible.offsize))/source.offsize)*100
    if max_off > 100:
        return 100
    else:
        return max_off
