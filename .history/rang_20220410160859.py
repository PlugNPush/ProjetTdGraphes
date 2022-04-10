import Globalvars as Gv

# Calcul des rangs #
def rang() :
    entry = [0] # mes entrées
    entryed = [] # mes anciennes entrées
    nb_rang = 0 # le rang actuel
    rangs = {nb_rang:[entry[0]]} # dico des rangs {rang:[sommets]}
    while entry :
        succ = []

        for i in Gv.FILE_Ord : # Pour toutes les entrées
            if i[0] in entry: # on recherche tous les successeurs de nos entrées
                succ.append(i[1])
        print("For ", entry, " successors are ", succ)
        
        if succ:
            nb_rang += 1
            rangs[nb_rang] = succ

            for i in range(0, nb_rang-1):
                for e in succ:
                    if e in rangs[i]:
                        rangs[i].remove(e)
        
        entry = succ


        """
        for i in Gv.FILE_Ord : # recherche des successeurs i[1]
            if i[0] in entry and i[1] not in entryed :
                
                for j in Gv.FILE_Ord : # recherche des prédécesseurs pour chaque succésseurs
                    if j[0] == i[0]: # on cherche le nombre de predecesseur de i[1]
                        succ.append(j[1])
                        #print("pred=",j)
                print(i,pred)
                if pred <= 1 and i[1] not in entry :
                    entry.append(i[1]) # 0->1=2
                    if nb_rang in rangs :
                        (rangs[nb_rang]).append(i[1]) # ajout
                    else:
                        rangs[nb_rang]=[i[1]] # nouvelle entrée
            entryed.append(i[0])
            entry.remove(i[0])
        print("les entrees:",entry, entryed,"les rangs: ", rangs)
        """
    print(rangs)
    return rangs