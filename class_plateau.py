from class_node import *

class plateau():
    def __init__(self,uid,ls_node=[],flag):
        self.uid=uid                        #UID du bot
        self.flag=flag                      #couleur joueur
        self.liste_node=ls_node             #liste contenant les noeuds
        #self.liste_joueur=[]
        self.dico_aretes=dict()             #dico pour stocker les arretes

    def add_node(self,node):                #methode pour ajouter un noeud (inutile normalement)
        self.liste_node.append(node)

    def define_dico(self,int_node1,int_node2):                  #methode pour inserer les aretes
        self.dico_aretes={}
        self.dico_aretes[int_node1]=int_node2
