

class plateau():
    def __init__(self, uid=-1, nb_player=-1, nb_node=-1, ls_node=[], flag=-1, speed=1):
        self.uid = uid                  # UID du bot
        self.flag = flag                # couleur joueur
        self.nb_node = nb_node          # nb de noeud
        self.liste_node = ls_node       # liste contenant les noeuds
        self.nb_player = nb_player      # nb de joueur
        self.speed = speed              # vitesse

    def set_settings(self, nb_player, nb_node, ls_node, flag, speed, matchid):
        self.flag = flag                # couleur joueur
        self.matchid = matchid            # match ID
        self.nb_node = nb_node            # nb de noeud
        self.liste_node = ls_node       # liste contenant les noeuds
        self.nb_player = nb_player        # nb de joueur
        self.speed = speed                # vitesse

    def add_node(self, node):           # methode pour ajouter un noeud (inutile normalement)
        self.liste_node.append(node)

    def display(self):           # méthode d'affichage
        print('uid: ', self.uid, '; flag: ', self.flag, '; vitesse:', self.speed)
        for i in range(len(self.liste_node)):
            self.liste_node[i].display()

    def display_v2(self):           # méthode d'affichage
        print('uid: ', self.uid, '; flag: ', self.flag, '; vitesse:', self.speed)
        for i in range(len(self.liste_node)):
            self.liste_node[i].display_v2()

    def set_uid(self, uid):             # ajoute l'UID au plateau
        self.uid = uid

    def find_node(self, integer):
        if integer == self.liste_node[integer].id:      # si les noeuds sont triés
            return self.liste_node[integer]
        else:                                             # sinon cherche sequentiellement
            for i in range(len(self.liste_node)):
                if integer == self.liste_node[i].id:
                    return self.liste_node[i]