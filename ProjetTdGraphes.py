# -*- coding: utf8 -*-
### ProjetTdGraphes ###

# Bibliothéques #


# Fichier importés #
File_txt = 'Test1.txt'

# Les couleurs #
W='\33[0m' #white
R='\33[31m' #red
G='\33[32m' #green
Y='\33[33m' #yellow
B='\33[34m' #blue
P='\33[35m' #purple
C='\33[36m' #cyan

# Variable général #
FILE=[]
FILE_Ord=[]

# Lecture de fichier #
def lecture_fichier():
    file = open(File_txt,"r") # ouverture du fichier en lecture seule
    lines = file.readlines() # lecture entier du fichier stocker ligne par ligne
    file.close() # fermeture du fichier après l'avoir lu

    for line in lines: # décomposition des lignes sans retour et par 'espace'
        FILE.append(line.strip().split(' '))

    # test de corruption des données (test des entiers?)
    i=0
    for line in FILE:
        i+=1
        if len(line) < 2: # il y a au moins 2 éléments
            print("\nErreur de type sommet/durée\n")
            break
        if int(line[0]) != i: # les sommets commencent à 1 et sont dans l'ordre (à réfléchir)
            print("\nErreur de type ordre des sommets\n")
            break
        for element in line:
            if int(element) < 0: # tout les éléments sont positifs
                print("\nErreur de type négatif\n")
                break

# Graphe d'ordonnancement #
def ordonnancement():
    with open("Ord1.txt","w") as Ord1:
        nb_sommets=len(FILE)+2
        Ord1.write(str(nb_sommets)+" sommets\n")
        print(G+ str(nb_sommets)+ "sommets\n" +W)

        #recherche des arcs de fâçon ordonnée
        i_début=0
        liste_fin=[]
        for line in FILE:
            if len(line)==2: # pas de prédecesseur
                FILE_Ord.insert(i_début,[0,int(line[0]),0]) # 0->sommet=durée
                i_début+=1
            else:
                for i_element in range(len(line)-2): # on s'occupe de chaque prédecesseurs
                    if line[i_element+2] not in liste_fin: # on cherche tous les prédecesseurs pour trouver plus tard tous ceux sans successeurs 
                        liste_fin.append(line[i_element+2])
                    for line_pred in FILE: # on cherche la durée du prédecesseur
                        if line_pred[0] == line[i_element+2]:
                            pred_duree=int(line_pred[1])
                            #exit?
                    FILE_Ord.append([int(line[i_element+2]),int(line[0]),pred_duree]) #pred->sommet=pred_durée
        #print(liste_fin)
        for line in FILE:
            if line[0] not in liste_fin:
                FILE_Ord.append([int(line[0]),nb_sommets-1,int(line[1])]) #sommet->fin=sommet_durée



## Main ##

# Initialisation #

lecture_fichier()
print(FILE)
ordonnancement()
print(FILE_Ord)
