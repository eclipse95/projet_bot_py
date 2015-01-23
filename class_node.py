class node():
    def __init__(self, id=-1, owner=-1, radius=-1, pos=[], offsize=-1, defsize=-1, prod_off=1, ls_neighbor=[]):
        self.id = id
        self.owner = owner                #n° du joueur
        self.radius = radius              #rayon du noeud
        self.pos = pos                    #position
        self.offsize = offsize            #unité off
        self.defsize = defsize            #unité def
        self.prod_off = prod_off
        self.neighbor = ls_neighbor       #liste des noueds voisins

    def update(self, owner, offsize, defsize):         #mise à jour du noeud
        self.owner = owner                #n° joueur
        self.offsize = offsize            #unité off
        self.defsize = defsize            #unité def

#    def addneighbor(self,int_value,dist):            #ajoute le numéro des voisins aux noeuds
#        self.neighbor.append([int_value,dist])

    def addneighbor(self, int_value):            #ajoute le numéro des voisins aux noeuds
        self.neighbor.append(int_value)

    def display(self):                  #fonction affichage
        print('id:', self.id, 'propriétaire:', self.owner, 'position:', self.pos, 'off:', self. offsize, 'def:', self.defsize)
        print('production:', self.prod_off, 'voisins :', self.neighbor)