
#fonction qui permet de lister tous les noeuds qui nous appartiennent
def nos_noeuds(plateau):
    monflag = plateau.flag
    #print('mon drapeau:',monflag)
    noeuds = list()
    for i in range(len(plateau.liste_node)):
        #print('propriétaire du noeud' ,plateau.liste_node[i],' est ',plateau.liste_node[i].owner)
        if int(plateau.liste_node[i].owner) == int(monflag):

            noeuds.append(plateau.liste_node[i])
    return noeuds

#annalyser les moves ici!!! voir le nouveau parser de Alexis!
def defendre(plateau):
    global idd
    global nos_noeuds

#va servir pour voisins neutres
def jailetemps(off, deff, offenemis, distance, vitesse):
    production_ennemie = deff + (vitesse*distance) + offenemis
    if off <= production_ennemie:
        return False
    else:
        return True

#fonction qui cherche a attaquer les ennemis adjacents
def voisins_ennemis(plateau, nos_noeuds):
    for i in range(len(nos_noeuds)):
        for j in range(len(nos_noeuds[i].neighbor)):
            if nos_noeuds[i].neighbor[j] not in nos_noeuds:                    
                a = creation_attaque(nos_noeuds[i].id,nos_noeuds[i].neighbor[j].id,100, plateau.uid)
                #print(a)
                print('ORDRE DU TYPE VOISIN ENNEMI')
                return a
    return True

#calcul pour savoir a quel moment conquerir une planete
def voisins_neutres(plateau, nos_noeuds):
    for i in range(len(nos_noeuds)):
        for j in range(len(nos_noeuds[i].neighbor)):
            if int(nos_noeuds[i].neighbor[j].owner) == -1:#on a trouvé un voisin neutre
#annaliser maintenant s'il se fait attaquer!!
                a = creation_attaque(nos_noeuds[i].id,nos_noeuds[i].neighbor[j].id,100,plateau.uid)
                #print(a)
                print('ORDRE DU TYPE VOISIN NEUTRE')
                return a

#si mon seul voisin c'est moi alors j'envoie toutes mes unités vers lui
def monseulvoisin_estmoi(plateau, nos_noeuds):
    for i in range(len(nos_noeuds)):
        if len(nos_noeuds[i].neighbor) == 1:
            a = creation_attaque(nos_noeuds[i].id,nos_noeuds[i].neighbor[0].id,100,plateau.uid)
            print('ORDRE DU TYPE MON SEUL VOISIN EST MOI',a)
            return a

#fonction qui cherche le parcourt pour aller au voisin avec la plus petite distance(dijkstra)
def ennemi_le_plus_proche(plateau):
    pass


#fonction appellée pour creer un ordre
def creation_attaque(depart, cible, quantitee, monflag):
    string = '['+str(monflag)+']'+'MOV'+str(quantitee)+'FROM'+str(depart)+'TO'+str(cible)
    return string

#si je suis dans une chaine, je parcourt des deux cotés pour savoir s'il y a des ennemis d'un côté
#récursif
def de_quel_cote_aller(plateau,nos_noeuds):
    for i in range(len(nos_noeuds)):
        if len(nos_noeuds[i].neighbor) == 2:#si j'ai deux voisins
            if nos_noeuds[i].neighbor[0].owner == plateau.flag:#si le 1er voisin est a moi
                if nos_noeuds[i].neighbor[1].owner == plateau.flag:   #si le second est aussi a moi
                    if regarder_dans_chaine(plateau,nos_noeuds[i].neighbor[0]):#regarder si j'envoie vers le 1er voisin
                        print('ORDRE DU TYPE DE QUEL COTE ALLER')
                        return creation_attaque(nos_noeuds[i].id,nos_noeuds[i].neighbor[0].id,100,plateau.uid)
def regarder_dans_chaine(plateau,noeud):#envoie True des qu'on croise un ennemi
    if noeud.owner == plateau.flag:#si le noeud est a moi
        if len(noeud.neighbor) == 0:
            return False
        for i in range(len(noeud.neighbor)):#parcourt les voisins de ce noeud
            return regarder_dans_chaine(plateau,noeud.neighbor[i])
    else:
        return True


#if __name__ == "__main__":

    #identifiant = "[20ac18ab-6d18-450e-94af-bee53fdc8fca]"
    #print(creation_attaque(1,2,120))

    #"[0947e717-02a1-4d83-9470-a941b6e8ed07]MOV33FROM1TO4"

    #[<userid>]MOV<%offunits>FROM<cellid>TO<cellid>

    #le pourcentage des unités offensives utilise la divion entière. Par exemple : 25% de 50=50*25/100=12.
    #un ordre dont l'effectif d'unités off est nul (par ex., 33% de 2 unités) est ignoré.
