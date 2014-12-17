from class_node import *
from re import *


class plateau():
    def __init__(self, uid=0,nb_player=2 ,nb_node=2, ls_node=[], flag=0,speed=1):
        self.uid = uid                  # UID du bot
        self.flag = flag                # couleur joueur
        self.nb_node=nb_node            # nb de noeud
        self.liste_node = ls_node       # liste contenant les noeuds
        self.nb_player=nb_player        # nb de joueur
        self.dico_aretes = dict()       #dico pour stocker les arretes
        self.speed=speed                # vitesse
    def add_node(self, node):           # methode pour ajouter un noeud (inutile normalement)
        self.liste_node.append(node)

    def define_dico(self, int_node1, int_node2):  # methode pour inserer les aretes
        self.dico_aretes = {}
        self.dico_aretes[int_node1] = int_node2

    def update_uid(self,uid):                     # mise à jour uid
        self.uid=uid

def parser_init_header(chain):               #parser regex
    res=search('TO(\d)\[(\d)\];(\d);(\d)CELLS:',chain)
    nb_player=res.group(1)
    flag=res.group(2)
    speed=res.group(3)
    nb_node=res.group(4)
    print(nb_player,flag,speed,nb_node)


def parser_init_node(chain):
    res=findall("(\d*?)\((\d*?)\,(\d*?)\)'(\d*?)'(\d*?)'(\d)'(\w*)",chain)
    print(res)

def parser_init(chain):
    res=search('TO(\d)\[(\d)\];(\d);(\d)CELLS:',chain)
    nb_player=res.group(1)
    flag=res.group(2)
    speed=res.group(3)
    nb_node=res.group(4)
    res=findall("(\d*?)\((\d*?)\,(\d*?)\)'(\d*?)'(\d*?)'(\d)'(\w*)",chain)
    ls_node=[]

    for i in range (nb_node):
        id=res.group(1+7*i)
        xpos=res.group(2+7*i)
        ypos=res.group(3+7*i)
        radius=res.group(4+7*i)
        offsize=res.group(5+7*i)
        defsize=res.group(6+7*i)
        prod=res.group(7+7*i)
        ls_node.append(node(id,0,radius,[xpos,ypos],offsize,defsize,prod))
    return nb_player,nb_node,ls_node,flag,speed