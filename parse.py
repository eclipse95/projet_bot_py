from re import *                            # lib regex
from class_node import *

# ###### Module contenant les parsers #########


def parser_init(chain, board):                     # parser chaine init
    res = search('INIT(.+)TO(\d+)\[(\d+)\];(\d+);(\d+)CELLS:', chain)  # parse parametres match
    board.matchid = str(res.group(1))
    board.nb_player = int(res.group(2))
    board.flag = int(res.group(3))
    board.speed = int(res.group(4))
    board.nb_node = int(res.group(5))
    res1 = findall("(\d+)\((-\d+|\d+),(-\d+|\d+)\)'(\d+)'(\d+)'(\d+)'(\w*)", chain)     # parse les noeuds
    nb_aretes = int(search(";(\d)LINES:", chain).group(1))
    res = findall("(\d+)@(\d+)OF(\d+)", chain)           # parse les aretes (n° noeud, distance, n° noeud suivant)
    board.liste_node = []
    for i in range(board.nb_node):                       # assemblage des noeuds
        id = int(res1[i][0])
        xpos = int(res1[i][1])
        ypos = int(res1[i][2])
        radius = int(res1[i][3])
        offsize = int(res1[i][4])
        defsize = int(res1[i][5])
        prod = str(res1[i][6])
        ls_aretes = []
        for j in range(nb_aretes):
            if id == int(res[j][0]):                   # A->B
                # ls_aretes.append([res[j][2],res[j][1]])
                ls_aretes.append(int(res[j][2]))         # pas de gestion des distances
            elif id == int(res[j][2]):                 # B->A
                # ls_aretes.append([res[j][0],res[j][1]])
                ls_aretes.append(int(res[j][0]))
        board.liste_node.append(node(id, 0, radius, [xpos, ypos], offsize, defsize, prod, ls_aretes))    # liste de noeud
    return board


def parser_state(chain, board):          # parser state optimisé
    cells = findall("(-\d+|\d+)\[(-\d+|\d+)\](\d+)'(\d+)", chain)
    # moves = findall("(\d+)[<>](\d+)\[(\d+)\]@(\d+)'", chain)      # desactiver car on ne gere pas encore les mouvmnts
    for i in range(len(cells)):
        cellid = int(cells[i][0])
        owner = int(cells[i][1])
        offunit = int(cells[i][2])
        defunit = int(cells[i][3])
        board.find_node(cellid).update(owner, offunit, defunit)
    return board


def ordre_builder(uid, offunits, sourceID, targetID):
    # [<userid>]MOV<%offunits>FROM<cellid>TO<cellid>
    ordre = '[' + str(uid) + ']' + 'MOV' + str(offunits)
    ordre += "FROM" + str(sourceID) + 'TO'
    ordre += str(targetID)
    return ordre
