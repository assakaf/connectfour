# type case := string
# type colonne := list[case]
# type grille := list[colonne]


#################################
##                             ##
##        Moteur de Jeu        ##
##                             ##
#################################


def creer_grille(nb_colonnes, nb_lignes): #VRAI
    """
    int * int -> grille
    Hyp : nb_colonnes > 0, nb_lignes > 0

    Créer une grille de nb_colonnes contenant nb_lignes case vide
    """
    grille=[]
    for x in range(nb_colonnes):
        grille.append(["vide"] * nb_lignes)
        
    return grille
    
#FONCTION INUTILE
def p4_sequence(seq): 
    """
    case list -> case

    Renvoie la case "vide" si la liste ne contient pas 4 cases consécutives non vides
    et renvoie une case de la couleur en question sinon


    EXEMPLES :
    p4_sequence(["vide", "rouge", "jaune", "vide", "vide"]) -> "vide"
    p4_sequence(["vide", "rouge", "rouge", "rouge", "rouge", "jaune", "vide"]) -> "rouge"

    """
    for x in range(len(seq)-2):
        if seq[x]==seq[x+1]==seq[x+2]==seq[x+3]=="rouge" :
            return "rouge"
        elif seq[x]==seq[x+1]==seq[x+2]==seq[x+3]=="jaune":
            return "jaune"
    return "vide"
         
        
def p4_lignes(grille): #VRAI
    """
    grille -> case

    Renvoie la case "vide" si aucune des lignes ne contient de Puissance 4
    renvoie la case de la couleur du Puissance 4 sinon

    INDICATION : utilisez p4_sequence
    """
    for x in range(len(grille[0])-1): #AVEC x l'ordonnee et y l'abscisse
        for y in range(len(grille)-2):#len(grille)=nb_de_colonnes et
            #len(grille[0])=nb_de_lignes
            if grille[x][y]==grille[x][y+1]==grille[x][y+2]==grille[x][y+3] == "rouge":
                return "rouge"
            elif grille[x][y]==grille[x][y+1]==grille[x][y+2]==grille[x][y+3] == "jaune":
                return "jaune"
    return "vide"
def p4_colonnes(grille): #VRAI
    """
    grille -> case

    Renvoie la case "vide" si aucune des colonnes ne contient de Puissance 4
    renvoie la case de la couleur du Puissance 4 sinon

    INDICATION : utilisez p4_sequence
    """
    for y in range(len(grille)+1):
        for x in range(len(grille[0]) - 4):
            if grille[x][y]==grille[x+1][y]==grille[x+2][y]==grille[x+3][y] == "rouge":
                return "rouge"
            elif grille[x][y]==grille[x+1][y]==grille[x+2][y]==grille[x+3][y] == "jaune":
                return "jaune"
    return "vide"


def p4_diagonales(grille): #VRAI
    """
    grille -> case

    Renvoie la case "vide" si aucune des diagonales ne contient de Puissance 4
    renvoie la case de la couleur du Puissance 4 sinon

    INDICATIONS :
      - utilisez p4_sequence
      - n'oubliez pas de construire toutes les diagonales,
        si les même sections de diagonales sont reconstruites
        plusieurs fois, ce n'est pas grave
    """
    for x in range(len(grille[0])-4): #DIAGONALES /
        for y in range(len(grille)-2):
            if grille[x][y]==grille[x+1][y+1]==grille[x+2][y+2]==grille[x+3][y+3]=="rouge":
                return "rouge"
            elif grille[x][y]==grille[x+1][y+1]==grille[x+2][y+2]==grille[x+3][y+3]=="jaune":
                return "jaune"
    
    for y in range(len(grille)-2): #DIAGONALES \
        for x in range(len(grille[0])-1):
            if grille[x][y]==grille[x-1][y+1]==grille[x-2][y+2]==grille[x-3][y+3]=="rouge":
                return "rouge"
            elif grille[x][y]==grille[x-1][y+1]==grille[x-2][y+2]==grille[x-3][y+3]=="jaune":
                return "jaune"
    return "vide"
    
def est_gagne(grille): #VRAI
    """
    grille -> case

    Renvoie "vide" si il n'y a pas de Puissance 4 dans la grille
    renvoie une case de la couleur du Puissance 4 sinon

    INDICATION : utilisez les fonctions précédentes
    """
    if (p4_diagonales(grille)== "rouge") or (p4_lignes(grille)== "rouge") or (p4_colonnes(grille)== "rouge"):
        return "rouge"
    elif (p4_diagonales(grille)== "jaune") or (p4_lignes(grille)== "jaune") or (p4_colonnes(grille)== "jaune"):
        return "jaune"
    else :
        return "vide"
    
def ajoute_jeton(grille, num_colonne, jeton): #VRAI
    """
    grille -> tuple[grille,bool]

    Hyp : num_colonne < len(grille) = nombres de colonnes de la grille

    Ajoute un jeton à la grille dans la colonne num_colonne et renvoie
    un couple composé de la nouvelle grille et de True.
    Si l'ajout ne peut pas se faire (la colonne est déjà pleine),
    renvoie l'ancienne grille et False.
    """
    x=0
    while grille[x][num_colonne]!="vide":
        x=x+1
        if x>=len(grille):
            return [grille,False]
    grille[x][num_colonne]=jeton
    return [grille,True]
#################################
##                             ##
##          Affichage          ##
##                             ##
#################################

    
def string_jeton(jeton): #VRAI
    """
    case -> string

    Renvoie " " pour une case vide
            "x" pour une case rouge
            "o" pour une case jaune
    """
    if jeton=="vide":
        return " "
    elif jeton=="rouge":
        return "x"
    else:
        return "o"
def string_ligne_jeton(ligne): #VRAI
    """
    ligne -> string

    Renvoie la chaîne de caractères correspondant à la ligne de jeton

    EXEMPLE:
    string_ligne_jeton(["rouge", "jaune", "vide", "jaune", "rouge"]) ->
    "| x | o |   | o | x |"

    INDICATION : utilisez string_jeton
    """
    s="| "
    for x in ligne: 
        s=s+string_jeton(x)+" | "
    
    return s

def string_ligne(n): #VRAI
    """
    int -> string

    Renvoie une chaîne de caractères de n "-"

    EXEMPLE :
    string_ligne(5) -> "-----"
    """
    ch=""
    ch=ch+n*"-"
    return ch
def string_grille(grille): #VRAI #FONCTION INUTILE ???
    """
    grille -> list[string]

    Renvoie une liste de chaîne de caractères correspondant aux lignes d'une grille

    EXEMPLE :
    string_grille([["jaune", "rouge"], ["rouge", "vide"]]) ->
    ['---------',
     '| x |   |',
     '---------',
     '| o | x |',
     '---------']

    INDICATION : Utilisez les fonctions précédentes
    """
    X=[]
    grilleinv=grille[::-1]
    for ligne in (grilleinv):
        n=len(string_ligne_jeton(ligne))
        X.append(string_ligne(n))
        X.append(string_ligne_jeton(ligne))
    
    return X

    
 
def affiche_grille(grille):
    """
    grille -> None

    Affiche une grille à l'écran

    EXEMPLE :

    affiche_grille([["jaune", "rouge"], ["rouge", "vide"]])
    va afficher :
    ---------
    | x |   |
    ---------
    | o | x |
    ---------
      1   2 

    INDICATION : Utilisez les fonctions précédentes
    """
    X=[]
    grilleinv=grille[::-1]
    for ligne in (grilleinv):
        n=len(string_ligne_jeton(ligne))
        X.append(string_ligne(n))
        X.append(string_ligne_jeton(ligne))
        print('',string_ligne(n-1),'\n',string_ligne_jeton(ligne))
    print('',string_ligne(n-1))
    L="   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22"
    LR=""
    for i in range(n):
        LR=LR+(L[i])
    print(LR)
#################################
##                             ##
##        Boucle de jeu        ##
##                             ##
#################################

def entier_utilisateur(s):
    """
    string -> int | None

    Affiche s et renvoie un entier rentré par l'utilisateur ou None
    si l'utilisateur n'a pas donné d'entier

    EXEMPLES :

    entier_utilisateur("Quel est ton âge ?") -> 
    Quel est ton âge ?  # <- affichage 
    42 # <- entier rentré par l'utilisateur
    -> 42 # retourner par la fonction

    entier_utilisateur("Quel est ton âge ?") -> 
    Quel est ton âge ?  # <- affichage 
    quarante-deux # <- entier rentré par l'utilisateur
    -> None # retourner par la fonction
    """
    
    t = input(s)
    try:
        t = int(t)
        return t
    except:
        return None
import random



def main():
    """
    -> None

    Réalise une partie de Puissance 4
    """
    nb_lignes=7
    nb_colonnes=6
    grille=creer_grille(nb_colonnes,nb_lignes)
    affiche_grille(grille)
    f=entier_utilisateur("""Combien de joueurs?(1 ou 2)
""")
    while(est_gagne(grille)=="vide"):
        
        if f==2:    #PARTIE A DEUX JOUEURS
            #TOUR DU JOUEUR 1#
            print("Joueur x")
            x=entier_utilisateur("""Quelle colonne?
""")
   
            while (type(x)!=int or x>7 or x<1):
            
                x=entier_utilisateur("""Quelle colonne?
""")
            ajoute_jeton(grille,x-1,"rouge")    
            affiche_grille(grille)
            if est_gagne(grille)=="rouge":
                print("VICTOIRE DU JOUEUR x")
                break

        
            #TOUR DU JOUEUR 2#
            print("Joueur o")
            o=entier_utilisateur("""Quelle colonne?
""")
        
            while (type(o)!=int or o>7 or o<1)and (ajoute_jeton(grille,o-1,"jaune")==[grille,False]): #VALIDITE DE LA COLONNE
                o=entier_utilisateur("""Quelle colonne?
""")
            ajoute_jeton(grille,o-1,"jaune")    
            affiche_grille(grille)
            if est_gagne(grille)=="jaune":
                print("VICTOIRE DU JOUEUR o")
                break
            ######################
            ##                  ##
            #  PARTIE AVEC I.A.  #
            ##                  ##
            ######################
        else:
            hasard=random.random()
            while hasard>0.5: #POUR SAVOIR QUI COMMENCE
                
            #####################
            #  JOUEUR COMMENCE  #
            #####################
            
            #TOUR DU JOUEUR#
                print("Joueur x")
                x=entier_utilisateur("""Quelle colonne?
""") 
                while (type(x)!=int or x>7 or x<=0):
            
                    x=entier_utilisateur("""Quelle colonne?
""")
                a=ajoute_jeton(grille,x-1,"rouge")
                g,boo=a
                if boo==False:
                
                    while (type(x)!=int or x>7 or boo==False or x<=0):
                        print('MOUVEMENT NON VALIDE')
                        x=entier_utilisateur("""Quelle colonne?
""")
                        if type(x)==int and x<7 and x>0:
                            a=ajoute_jeton(grille,x-1,"rouge")
                        g,boo=a
                affiche_grille(grille)
                
                if est_gagne(grille)=="rouge":
                    print("VICTOIRE DU JOUEUR x")
                    break
            
                #TOUR DE L'I.A.#
                joueur_artificiel(grille,"jaune")
                ajoute_jeton(grille,joueur_artificiel(grille,"rouge")-1,"jaune")    
                affiche_grille(grille)
                if est_gagne(grille)=="jaune":
                    print("VICTOIRE DE L'IA")
                    break
            while hasard<=0.5:
            #####################
            #    IA COMMENCE    #
            #####################
            
                #TOUR DE L'I.A.#
                joueur_artificiel(grille,"jaune")
                ajoute_jeton(grille,joueur_artificiel(grille,"rouge")-1,"jaune")    
                affiche_grille(grille)
                if est_gagne(grille)=="jaune":
                    print("VICTOIRE DE L'IA")
                    break
                
                #TOUR DU JOUEUR#
                print("Joueur x")
                x=entier_utilisateur("""Quelle colonne?
""") 
                while (type(x)!=int or x>7 or x<=0):
            
                    x=entier_utilisateur("""Quelle colonne?
""")
            
            
            
                a=ajoute_jeton(grille,x-1,"rouge")
                g,boo=a
                if boo==False:
                
                    while (type(x)!=int or x>7 or boo==False or x<=0):
                        print('MOUVEMENT NON VALIDE')
                        x=entier_utilisateur("""Quelle colonne?
""")
                        if type(x)==int and x<7 and x>0:
                            a=ajoute_jeton(grille,x-1,"rouge")
                        g,boo=a
                affiche_grille(grille)
               
                if est_gagne(grille)=="rouge":
                    print("VICTOIRE DU JOUEUR x")
                    break
                             



def joueur_artificiel(grille,jeton):
    """grille*str->int

    prend une grille et la couleur du joueur qui joue et renvoie
    un entier correspondant a l'indice de la colonne du coup à jouer"""
    #COLONNES_3_ATTAQUE
    for b in range(len(grille)+1):
        for a in range(len(grille[0]) - 4):
            if grille[a][b]==grille[a+1][b]==grille[a+2][b]!=(jeton and "vide") and grille[a+3][b]=="vide":
                    return b+1
    #LIGNES_3_ATTAQUE
    for a in range(len(grille[0])-1): #AVEC a l'ordonnee et b l'abscisse
        for b in range(len(grille)-2):#len(grille)=nb_de_colonnes et
                #len(grille[0])=nb_de_lignes
            if grille[a][b+1]==grille[a][b+2]==grille[a][b+3]!=(jeton and "vide") and grille[a][b]=="vide":
                return b+1
            if grille[a][b]==grille[a][b+2]==grille[a][b+3]!=(jeton and "vide") and grille[a][b+1]=="vide":
                return b+2
            if grille[a][b]==grille[a][b+1]==grille[a][b+3]!=(jeton and "vide") and grille[a][b+2]=="vide":
                return b+3
            if grille[a][b]==grille[a][b+1]==grille[a][b+2]!=(jeton and "vide") and grille[a][b+3]=="vide":
                return b+4
            
    #DIAGONALES_3_ATTAQUE
    for a in range(len(grille[0])-4): #DIAGONALES /
        for b in range(len(grille)-2): 
            if grille[a][b]==grille[a+1][b+1]==grille[a+2][b+2]!=(jeton and "vide") and grille[a+2][b+3]!=grille[a+3][b+3]=="vide":
                return b+4
            if grille[a][b]==grille[a+1][b+1]==grille[a+3][b+3]!=(jeton and "vide") and grille[a+1][b+2]!=grille[a+2][b+2]=="vide":
                return b+3
            if grille[a][b]==grille[a+2][b+2]==grille[a+3][b+3]!=(jeton and "vide") and grille[a][b+1]!=grille[a+1][b+1]=="vide":
                return b+2
            if grille[a+1][b+1]==grille[a+2][b+2]==grille[a+3][b+3]!=(jeton and "vide") and grille[a][b]=="vide":
                return b+1
    for b in range(len(grille)-2): #DIAGONALES \
        for a in range(len(grille[0])-1):
            if grille[a][b]==grille[a-1][b+1]==grille[a-2][b+2]!=(jeton and "vide") and grille[a-3][b+3]=="vide":
                return b+4
            if grille[a][b]==grille[a-1][b+1]==grille[a-2][b+2]!=(jeton and "vide") and grille[a-3][b+2]!=grille[a-2][b+2]=="vide":
                return b+3
            if grille[a][b]==grille[a-2][b+2]==grille[a-3][b+3]!=(jeton and "vide") and grille[a-2][b+1]!=grille[a-1][b+1]=="vide":
                return b+2
            if grille[a-1][b+1]==grille[a-2][b+2]==grille[a-3][b+3]!=(jeton and "vide") and (grille[a-1][b]!=grille[a][b]=="vide"):
                return b+1
            
    #COLONNES_3_DEFENSE    
    for b in range(len(grille)+1):
        for a in range(len(grille[0]) - 4):
            if grille[a][b]==grille[a+1][b]==grille[a+2][b]==jeton and grille[a+3][b]=="vide":
                    return b+1
                
    #LIGNES_3_DEFENSE
    for a in range(len(grille[0])-1): #AVEC a l'ordonnee et b l'abscisse
        for b in range(len(grille)-2):#len(grille)=nb_de_colonnes et
                #len(grille[0])=nb_de_lignes  
            if grille[a][b]==grille[a][b+1]==grille[a][b+2]==jeton and grille[a][b+3]=="vide":
                return b+4
    #DIAGONALES_3_DEFENSE
    for a in range(len(grille[0])-4): #DIAGONALES /
        for b in range(len(grille)-2): 
            if grille[a][b]==grille[a+1][b+1]==grille[a+2][b+2]==jeton and grille[a+2][b+3]!=grille[a+3][b+3]=="vide":
                return b+4
            if grille[a][b]==grille[a+1][b+1]==grille[a+3][b+3]==jeton and grille[a+1][b+2]!=grille[a+2][b+2]=="vide":
                return b+3
            if grille[a][b]==grille[a+2][b+2]==grille[a+3][b+3]==jeton and grille[a][b+1]!=grille[a+1][b+1]=="vide":
                return b+2
            if grille[a+1][b+1]==grille[a+2][b+2]==grille[a+3][b+3]==jeton and grille[a][b]=="vide":
                return b+1
    for b in range(len(grille)-2): #DIAGONALES \
        for a in range(len(grille[0])-1):
            if grille[a][b]==grille[a-1][b+1]==grille[a-2][b+2]==jeton and grille[a-3][b+3]=="vide":
                return b+4
            if grille[a][b]==grille[a-1][b+1]==grille[a-2][b+2]==jeton and grille[a-3][b+2]!=grille[a-2][b+2]=="vide":
                return b+3
            if grille[a][b]==grille[a-2][b+2]==grille[a-3][b+3]==jeton and grille[a-2][b+1]!=grille[a-1][b+1]=="vide":
                return b+2
            if grille[a-1][b+1]==grille[a-2][b+2]==grille[a-3][b+3]==jeton and (grille[a-1][b]!=grille[a][b]=="vide"):
                return b+1
            
    #LIGNES_2_ATTAQUE        
    for a in range(len(grille[0])-1): #AVEC a l'ordonnee et b l'abscisse
        for b in range(len(grille)-2):#len(grille)=nb_de_colonnes et
                #len(grille[0])=nb_de_lignes
                
            if grille[a][b]==grille[a][b+1]!=(jeton and "vide") and grille[a][b+2]=="vide":
                return b+3
            if (grille[a][b]=="vide") and grille[a][b+1]==grille[a][b+2]!=(jeton and "vide"):
                return b+1
            elif grille[a][b]==grille[a][b+2]!=(jeton and "vide") and grille[a][b+1]=="vide":
                return b+2
            
    #LIGNES_2_DEFENSE        
    for a in range(len(grille[0])-1): 
        for b in range(len(grille)-2):
                
            if grille[a][b]==grille[a][b+1]==jeton and grille[a][b+2]=="vide":
                return b+3
            if (grille[a][b]=="vide") and grille[a][b+1]==grille[a][b+2]==jeton:
                return b+1
            elif grille[a][b]==grille[a][b+2]==jeton and grille[a][b+1]=="vide":
                return b+2
            
    
    #LIGNE_1_attaque
    for a in range(len(grille[0])-1): 
        for b in range(len(grille)-2):
                
            if grille[a][b+1]!=(jeton and "vide") and grille[a][b]==grille[a][b+2]=="vide":
                return b+3
                  
    return int(random.random()*7+1)


    

    

    











    
if __name__ == '__main__':
    main()


