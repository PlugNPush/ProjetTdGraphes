import Globalvars as Gv

# Graphe d'ordonnancement #
def ordonnancement() :
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"w") as Trace:
        nb_sommets = len(Gv.FILE) + 2
        Trace.write(str(nb_sommets) + " sommets\n")
        print(str(nb_sommets) + " sommets")

        #recherche des arcs de fâçon ordonnée
        i_debut = 0
        liste_fin = []
        for line in Gv.FILE :
            if len(line) == 2 : # pas de prédecesseur
                Gv.FILE_Ord.insert(i_debut,[0,int(line[0]),0]) # 0->sommet=durée
                i_debut += 1
            else :
                for i_element in range(len(line)-2) : # on s'occupe de chaque prédecesseurs
                    if line[i_element+2] not in liste_fin : # on cherche tous les prédecesseurs pour trouver plus tard tous ceux sans successeurs 
                        liste_fin.append(line[i_element+2])
                    for line_pred in Gv.FILE: # on cherche la durée du prédecesseur
                        if line_pred[0] == line[i_element+2] :
                            pred_duree=int(line_pred[1])
                            break
                    ### simplification possible print(pred_duree, line[int(line[i_element+2])][1])        
                    Gv.FILE_Ord.append([int(line[i_element+2]),int(line[0]),pred_duree]) #pred->sommet=pred_durée
        #print(liste_fin)
        for line in Gv.FILE : # on recherche les sommets sans successeurs pour leur ajouter w
            if line[0] not in liste_fin :
                Gv.FILE_Ord.append([int(line[0]),nb_sommets-1,int(line[1])]) #sommet->fin=sommet_durée
        
        nb_arcs=len(Gv.FILE_Ord)
        Trace.write(str(nb_arcs) + " arcs\n")
        print(str(nb_arcs) + " arcs")
        for arc in Gv.FILE_Ord :
            Trace.write(str(arc[0]) + " -> " + str(arc[1]) + " = " + str(arc[2]) + "\n")
        
        return nb_sommets,nb_arcs