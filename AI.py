#---------fichier pour stocker les IA

from class_node import *
from class_plateau import *
import parser
import random
import order

def strategy_level1(board):
    for i in range (board.nb_node):
        if(board.liste_node[i].offsize > 10 and board.liste_node[i].ower == board.flag):
            target_id = random.choice(board.liste_node[i].neighbor)
            order.parametre_move(board.uid, random.randint(100/board.liste_node[i].offsize,100), board.liste_node[i].id, target_id)
