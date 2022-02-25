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
FILE=[] # liste de str
FILE_Ord=[] # liste de int

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
            raise Exception("\nErreur de type sommet/durée\n")
        if int(line[0]) != i: # les sommets commencent à 1 et sont dans l'ordre (à réfléchir)
            raise Exception("\nErreur de type ordre des sommets\n")
        for element in line:
            if int(element) < 0: # tout les éléments sont positifs
                raise Exception("\nErreur de type négatif\n")

# Graphe d'ordonnancement #
def ordonnancement():
    with open("Ord1.txt","w") as Ord1:
        nb_sommets=len(FILE)+2
        Ord1.write(str(nb_sommets)+" sommets\n")
        print(str(nb_sommets)+" sommets")

        #recherche des arcs de fâçon ordonnée
        i_debut=0
        liste_fin=[]
        for line in FILE:
            if len(line)==2: # pas de prédecesseur
                FILE_Ord.insert(i_debut,[0,int(line[0]),0]) # 0->sommet=durée
                i_debut+=1
            else:
                for i_element in range(len(line)-2): # on s'occupe de chaque prédecesseurs
                    if line[i_element+2] not in liste_fin: # on cherche tous les prédecesseurs pour trouver plus tard tous ceux sans successeurs 
                        liste_fin.append(line[i_element+2])
                    for line_pred in FILE: # on cherche la durée du prédecesseur
                        if line_pred[0] == line[i_element+2]:
                            pred_duree=int(line_pred[1])
                            break
                    ### simplification possible print(pred_duree, line[int(line[i_element+2])][1])        
                    FILE_Ord.append([int(line[i_element+2]),int(line[0]),pred_duree]) #pred->sommet=pred_durée
        #print(liste_fin)
        for line in FILE: # on recherche les sommets sans successeurs pour leur ajouter w
            if line[0] not in liste_fin:
                FILE_Ord.append([int(line[0]),nb_sommets-1,int(line[1])]) #sommet->fin=sommet_durée
        
        nb_arcs=len(FILE_Ord)
        Ord1.write(str(nb_arcs)+" arcs\n")
        print(str(nb_arcs)+" arcs")
        for arc in FILE_Ord:
            Ord1.write(str(arc[0])+" -> "+str(arc[1])+" = "+str(arc[2])+"\n")
        
        return nb_sommets,nb_arcs

# Matrices d'adjacence et de valeurs #
def adjacence_valeurs():
    MA = [[0 for x in range(nb_sommets)] for i in range(nb_sommets)]
    MV = [['*' for x in range(nb_sommets)] for i in range(nb_sommets)]
    for arc in FILE_Ord:
        MA[arc[0]][arc[1]]=1
        MV[arc[0]][arc[1]]=str(arc[2])

    #write MA et MV
    with open("MA1.txt","w") as MA1:
        for line in MA:
            for element in line:
                MA1.write(str(element)+' ')
            MA1.write('\n')
    with open("MV1.txt","w") as MV1:
        for line in MV:
            for element in line:
                MV1.write(element+' ')
            MV1.write('\n')

    return MA,MV

# Detection de circuit (par suppression des points d'entrées) #
def detection_circuit():
    entry = [0]
    entryed = []
    MA_circuit=MA
    no_circuit=True
    while entry and no_circuit :
        for i in range(len(MA_circuit[entry[0]])): # on enlève les arcs de l'entrée
            if MA_circuit[entry[0]][i]==1:
                #print(i)
                MA_circuit[entry[0]][i]=0
                if i not in entry:
                    entry.append(i) # on ajoute les successeurs des arcs enlevés aux entrées
                if i in entryed:
                    no_circuit=False #circuit
        #for i in range(len(MA_circuit)): # on enlève la colonne de l'entrée
        #    del(MA_circuit[i][entry[0]])
        entryed.append(entry[0]) # entrée faite
        del(entry[0])
        #print("mes entrees",entry,entryed)
        #for i in range(len(MA_circuit)):
            #print(MA_circuit[i])
    return no_circuit

# Calcul des rangs #
def rang():
    entry=[0] # mes entrées
    entryed=[] # mes anciennes entrées
    nb_rang=0 # le rang actuel
    rangs={nb_rang:[entry[0]]} # dico des rangs {rang:[sommets]}
    while entry:
        nb_rang+=1
        for i in FILE_Ord: # recherche des successeurs i[1]
            if i[0]==entry[0] and i[1] not in entryed:
                pred=0
                for index,j in enumerate(FILE_Ord): # recherche des prédécesseurs pour chaque succésseurs
                    if j[1] == i[1] and j[0] not in entryed and (j[0] not in entry[0:index]): # on cherche le nombre de predecesseur de i[1]
                        pred+=1
                        #print("pred=",j)
                #print(i,pred)
                if pred<=1 and i[1] not in entry:
                    entry.append(i[1]) # 0->1=2
                    if nb_rang in rangs:
                        (rangs[nb_rang]).append(i[1]) # ajout
                    else:
                        rangs[nb_rang]=[i[1]] # nouvelle entrée
        entryed.append(entry[0])
        del(entry[0])
        #print("les entrees:",entry, entryed,"le fichier: ", FILE_Ord,"les rangs: ", rangs)
    return rangs

def dates():
    dates_tot=[0]*nb_sommets
    for rang in rangs: # on fait dans l'ordre des rangs
        if rang != 0:
            for sommet in rangs[rang]:
                #print(rang,sommet, dates_tot)
                # on cherche tous ses prédecesseurs parmis dates_tot et ajoute leur temps puis on les compare
                for pred in FILE_Ord:
                    if pred[1] == sommet:
                        dates_tot[sommet]=max(dates_tot[pred[0]]+pred[2],dates_tot[sommet])
    #print(dates_tot)
    
    dates_tard=[dates_tot[-1]]*nb_sommets
    for i_rang in range(len(rangs)): # on fait dans l'ordre inverse des rangs
        rang=len(rangs)-1-i_rang
        if rangs[rang] != rangs[len(rangs)-1]: #diff du dernier rang
            for i_sommet in range(len(rangs[rang])):
                sommet=len(rangs[rang])-1-i_sommet
                # on cherche tous ses succésseurs parmis dates_tard et enlève leur temps puis on les compare
                #print(rang,sommet,dates_tard)
                for i_suc in range(len(FILE_Ord)):
                    suc=len(FILE_Ord)-1-i_suc
                    if FILE_Ord[suc][0] == rangs[rang][sommet]:
                        dates_tard[FILE_Ord[suc][0]]=min(dates_tard[FILE_Ord[suc][1]]-FILE_Ord[suc][2],dates_tard[FILE_Ord[suc][0]])
    #print(dates_tard)

    marge=[b - a for a, b in zip(dates_tot, dates_tard)]
    #print(marge)

    return dates_tot,dates_tard,marge

def critique():
    chemin_crit=[]
    sommets_par_rangs=[]
    for rang in rangs:
        for sommet in rangs[rang]:
            sommets_par_rangs.append(sommet)
    print(sommets_par_rangs)

    for index,element in enumerate(marge):
        if element==0:
            chemin_crit.append(sommets_par_rangs[index])
    print("le chemin critique est",chemin_crit)

## Main ##

# Initialisation #
nb_sommets=-1
nb_arcs=-1
#taille_max=99
no_circuit=True
MA=[] # tableau de int
MV=[] # tableau de str

# Corps #
lecture_fichier()
print(FILE)
nb_sommets,nb_arcs=ordonnancement()
print("ordonancement",FILE_Ord)
MA,MV=adjacence_valeurs()
print("MA",MA)
print("MV",MV)
no_circuit=detection_circuit()
print("pas de circuit:",no_circuit)
if no_circuit:
    rangs=rang()
    print("les rangs:",rangs)
    dates_tot,dates_tard,marge=dates()
    print("dates au plus tot, au plus tard et marge:",dates_tot,dates_tard,marge)
    critique()
