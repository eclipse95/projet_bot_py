from class_node import *
from re import *


class plateau():
    def __init__(self, uid=0, ls_node=[], flag=0):
        self.uid = uid  # UID du bot
        self.flag = flag  # couleur joueur
        self.liste_node = ls_node  # liste contenant les noeuds
        # self.liste_joueur=[]
        self.dico_aretes = dict()  #dico pour stocker les arretes

    def add_node(self, node):  # methode pour ajouter un noeud (inutile normalement)
        self.liste_node.append(node)

    def define_dico(self, int_node1, int_node2):  # methode pour inserer les aretes
        self.dico_aretes = {}
        self.dico_aretes[int_node1] = int_node2


def init_parser(chain):  # parser pas propre
    #"INIT20ac18ab-6d18-450e-94af-bee53fdc8fcaTO6[2];1;3CELLS:1(23,9)'2'30'8'I,2(41,55)'1'30'8'II,3(23,103)'1'20'5'I;2LINES:1@3433OF2,1@6502OF3"
    k = 1  #compteur pour la chain
    while (str(chain[k - 1]) != str('T') or str(chain[k]) != str('O')):  #avance jusqu'à la chaine 'TO'
        k += 1
    k += 1
    nb_player = ''
    while (str(chain[k]) != str('[')):  #avance jusqu'au nombre de joueur
        nb_player += chain[k]
        k += 1
    k += 1
    flag = ''
    while (str(chain[k] != str(']'))):
        flag += chain[k]
        k += 1

    print(flag)
    print(nb_player)


def parser_init_clean(chain):
    search('TO(\d)\[(\d)\];(\d);(\d)CELLS:',chain)