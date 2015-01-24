# Fonction permettant de créer le paramètre pour la fonction order(move)
def parametre_move(userid, pourcent, planete_depart, planete_arrive):
    deplacement = '[' + userid + ']' + 'MOV' + str(pourcent) + 'FROM' + str(planete_depart.id) + 'TO' + str(planete_arrive.id)
    return deplacement