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

    def display(self):                            # méthode d'affichage non terminée
        print('uid: ',self.uid,'; flag: ',self.flag)
        for i in range (len(self.liste_node)):
            self.liste_node[i].display()

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
    nb_player=int(res.group(1))
    flag=int(res.group(2))
    speed=int(res.group(3))
    nb_node=int(res.group(4))
    res1=findall("(\d*?)\((\d*?)\,(\d*?)\)'(\d*?)'(\d*?)'(\d)'(\w*)",chain)
    ls_node=[]
    for i in range (nb_node):
        id=int(res1[i][0])
        xpos=int(res1[i][1])
        ypos=int(res1[i][2])
        radius=int(res1[i][3])
        offsize=int(res1[i][4])
        defsize=int(res1[i][5])
        prod=(res1[i][6])
        ls_node.append(node(id,0,radius,[xpos,ypos],offsize,defsize,prod))
    return nb_player, nb_node, ls_node, flag, speed         #problème de retour
    
def lire_state(string):
    
    regex = re.compile('STATE.+;\dCELLS')
    regex2 = re.compile('\d+CELLS.+MOVES')
    regex3 = re.compile('\d+MOVES.+')
    regex4 = re.compile('.+;')
    regex5 = re.compile('(\d+\W+\d+\W+\d+\W+\d+)+')
    regex6 = re.compile("(\d*[<>]\d+\[\d+\]@\d+'\d*)")
    
    #1er filtrage 
    identifiant = regex.search(string).group(0)
    identifiant = identifiant[5:len(identifiant)-7]    
    cells = regex2.search(string).group(0)
    cells = cells[:len(cells)-7]    
    moves = regex3.search(string).group(0)

    #2nd filtrage
    cells = regex5.findall(cells)
    moves = regex6.findall(moves)
    for i in range(len(moves)):
        if moves[i][0] == '<' or '>':
            nb = moves[i-1][0]#le nb de la case d'avant: a faire en expression regulieres
            strr = str(nb) + moves[i]
            moves[i] = strr
    
    print("identifiant: ", identifiant)
    print("les cellules:", cells)
    print("les mouvements:",moves)
