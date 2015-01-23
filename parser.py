from re import *                            # lib regex
from class_node import *

####### Module contenant les parsers #########


def parser_init(chain, board):                     # parser chaine init #passer la board en paramètre?
    res=search('INIT(.+)TO(\d+)\[(\d+)\];(\d);(\d+)CELLS:', chain)  #parse parametres match
    board.matchid = str(res.group(1))
    board.nb_player = int(res.group(2))
    board.flag = int(res.group(3))
    board.speed = int(res.group(4))
    board.nb_node = int(res.group(5))
    res1 = findall("(\d+)\((-\d+|\d+),(-\d+|\d+)\)'(\d+)'(\d+)'(\d+)'(\w*)", chain)     #parse les noeuds
    nb_aretes = int(search(";(\d)LINES:", chain).group(1))
    res = findall("(\d+)@(\d+)OF(\d+)", chain)           #parse les aretes (n° noeud, distance, n° noeud suivant)
    board.liste_node = []
    for i in range (board.nb_node):                       #assemblage des noeuds
        id = int(res1[i][0])
        xpos = int(res1[i][1])
        ypos = int(res1[i][2])
        radius = int(res1[i][3])
        offsize = int(res1[i][4])
        defsize = int(res1[i][5])
        prod = (res1[i][6])
        ls_aretes = []
        for j in range(nb_aretes):
            if id == int(res[j][0]):                   # A->B
#                ls_aretes.append([res[j][2],res[j][1]])
                ls_aretes.append(int(res[j][2]))         #pas de gestion des distances
            elif id == int(res[j][2]):                 # B->A
#                ls_aretes.append([res[j][0],res[j][1]])
                ls_aretes.append(int(res[j][0]))
        board.liste_node.append(node(id, 0, radius, [xpos,ypos], offsize, defsize, prod, ls_aretes))    #liste de noeud
    return board         #retourne la board #inutile?


def lire_state(string):
    regex = compile('STATE.+;\dCELLS')
    regex2 = compile('\d+CELLS.+MOVES')
    regex3 = compile('\d+MOVES.*')
    regex5 = compile('(\d+\W+\d+\W+\d+\W+\d+)+')
    regex6 = compile("(\d*[<>]\d+\[\d+\]@\d+'\d*)")
    regex7 = compile('\d+')
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
        if moves[i][0] == '<' or moves[i][0] == '>':
            pa = regex7.search(moves[i-1]).group(0)
            moves[i] = pa+moves[i]          

    print("identifiant: ", identifiant)
    print("les cellules:", cells)
    print("les mouvements:",moves)


def parser_state(chain, board):          #parser state optimisé
    #STATE20ac18ab-6d18-450e-94af-bee53fdc8fcaIS2;3CELLS:1[2]12'4,2[2]15'2,3[1]33'6;4MOVES:1<5[2]@232'>6[2]@488'>3[1]@4330'2,1<10[1]@2241'3
    cells = findall("(-\d+|\d+)\[(-\d+|\d+)\](\d+)'(\d+)", chain)
    #moves = findall("(\d+)[<>](\d+)\[(\d+)\]@(\d+)'", chain)      #desactiver car on ne gere pas encore les mouvmnts
    for i in range (len(cells)):
        cellid = int(cells[i][0])
        owner = int(cells[i][1])
        offunit = int(cells[i][2])
        defunit = int(cells[i][3])
        board.find_node(cellid).update(owner, offunit, defunit)
    return board

def ordre_builder(uid, offunits, source, target):
#[<userid>]MOV<%offunits>FROM<cellid>TO<cellid>
    ordre=str(uid,'MOV<',offunits)
    ordre+=str(">FROM<",source,'>TO<')
    ordre+=str(target,'>')
    return ordre