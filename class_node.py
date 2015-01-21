class node():
    def __init__(self, id=0, owner=0, radius=None, pos=[], offsize=None, defsize=None, prod_def=1, prod_off=1, ls_neighbor=None):
        self.id=id
        self.owner=owner                #n° du joueur
        self.radius=radius              #rayon du noeud
        self.pos=pos                    #position
        self.offsize=offsize            #unité off
        self.defsize=defsize            #unité def
        self.prod_def=prod_def          #
        self.prod_off=prod_off
        self.neighbor=ls_neighbor       #liste des noueds voisins

    def update(self,owner,offsize,defsize):         #mise à jour du noeud
        self.owner=owner                #n° joueur
        self.offsize=offsize            #unité off
        self.defsize=defsize            #unité def

#    def addneighbor(self,int_value,dist):            #ajoute le numéro des voisins aux noeuds
#        self.neighbor.append([int_value,dist])

    def addneighbor(self,int_value):            #ajoute le numéro des voisins aux noeuds
        self.neighbor.append([int_value])

    def display(self):                  #fonction affichage (non finie)
        print('id:', self.id, 'propriétaire:', self.owner, 'position:', self.pos, 'off:',self. offsize)