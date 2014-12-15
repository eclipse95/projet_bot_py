class node():
    def __init__(self,owner=0,radius=None,pos=[],offsize=None,defsize=None,prod=1,nb_player=1):
        self.owner=owner
        self.radius=radius
        self.pos=pos
        self.offsize=offsize
        self.defsize=defsize
        self.prod=prod
        self.neighbor=[]
        self.nb_player=nb_player                    #nb de joueur sur le plateau
    def update(self,owner,offsize,defsize):         #mise à jour du noeud
        self.owner=owner
        self.offsize=offsize
        self.defsize=defsize

    def addneighbor(self,int_value):                #ajoute le numéro des voisins aux noeuds
        self.neighbor.append(int_value)
