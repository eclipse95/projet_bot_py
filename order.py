#Fonction permettant de créer le paramètre pour la fonction order(move)
def parametre_move(userid,pourcent,planetes_depart,planetes_arrive):
    deplacement = ''
    deplacement = deplacement  + userid + 'MOV' + str((pourcent*planetes_depart.offsize)/100) + 'FROM' + str(planetes_depart.id_node) + 'TO' + str(planetes_arrive.id_node)
    return deplacement
