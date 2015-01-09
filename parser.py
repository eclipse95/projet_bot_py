from re import *                            # lib regex
from class_node import *

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

def parser_lines(chain):
    pass

def parser_state(chain):
    pass
