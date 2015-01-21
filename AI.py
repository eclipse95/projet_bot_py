#---------fichier pour stocker les IA

import random
import poooc


def strategy_level1(board):
    for i in range (board.nb_node):
        if board.liste_node[i].offsize > 10 and board.liste_node[i].owner == board.flag:
            target_id = random.choice(board.liste_node[i].neighbor)
            poooc.order(board.uid, random.randint(0, 100), board.liste_node[i].id, target_id)

