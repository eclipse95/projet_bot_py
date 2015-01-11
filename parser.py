from re import *                            # lib regex
from class_node import *

def parser_init_header(chain):               #parser regex (obsolète)
    res=search('TO(\d)\[(\d)\];(\d);(\d)CELLS:',chain)
    nb_player=res.group(1)
    flag=res.group(2)
    speed=res.group(3)
    nb_node=res.group(4)
    print(nb_player,flag,speed,nb_node)


def parser_init_node(chain):                #parser obsolète
    res=findall("(\d*?)\((\d*?)\,(\d*?)\)'(\d*?)'(\d*?)'(\d)'(\w*)",chain)
    print(res)

def parser_init(chain):                     # parser chaine init
    res=search('INIT(.+)TO(\d)\[(\d)\];(\d);(\d)CELLS:',chain)  #parse parametres match
    matchid=str(res.group(1))
    nb_player=int(res.group(2))
    flag=int(res.group(3))
    speed=int(res.group(4))
    nb_node=int(res.group(5))
    res1=findall("(\d*?)\((\d*?)\,(\d*?)\)'(\d*?)'(\d*?)'(\d)'(\w*)",chain)     #parse les noeuds
    nb_aretes=int(search(";(\d)LINES:",chain).group(0))
    res=findall("(\d)@(\d+)OF(\d)",chain)           #parse les aretes
    ls_node=[]
    for i in range (nb_node):                       #assemblage des noeuds
        id=int(res1[i][0])
        xpos=int(res1[i][1])
        ypos=int(res1[i][2])
        radius=int(res1[i][3])
        offsize=int(res1[i][4])
        defsize=int(res1[i][5])
        prod=(res1[i][6])
        ls_aretes=[]
        for j in range(nb_aretes):
            if(id==res[j][0]):
                ls_aretes.append(res[j][2],res[j][1])
        ls_node.append(node(id,0,radius,[xpos,ypos],offsize,defsize,prod,ls_aretes))    #liste de noeud
    return matchid, nb_player, nb_node, ls_node, flag, speed         #retourne une liste

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

def parser_state(chain,board):
    #STATE20ac18ab-6d18-450e-94af-bee53fdc8fcaIS2;3CELLS:1[2]12'4,2[2]15'2,3[1]33'6;4MOVES:1<5[2]@232'>6[2]@488'>3[1]@4330'2,1<10[1]@2241'3
    if(str(search('STATE(.+)IS\d;\dCELLS',chain).group(0))==str(board.matchid)):    #verifie le match ID
        cells=findall("(\d+)\[(\d+)\](\d)'(\d)",chain)

