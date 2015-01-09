from class_node import *


class plateau():
    def __init__(self, uid=0,nb_player=2 ,nb_node=2, ls_node=[], flag=0,speed=1,matchid=0):
        self.uid = uid                  # UID du bot
        self.flag = flag                # couleur joueur
        self.matchid=matchid
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

    def display(self):                            # méthode d'affichage non terminée
        print('uid: ',self.uid,'; flag: ',self.flag)
        for i in range (len(self.liste_node)):
            self.liste_node[i].display()
