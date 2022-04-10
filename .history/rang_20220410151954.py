import Globalvars as Gv

# Calcul des rangs #
def rang() :
    entry = [0] # mes entrées
    entryed = [] # mes anciennes entrées
    nb_rang = 0 # le rang actuel
    rangs = {nb_rang:[entry[0]]} # dico des rangs {rang:[sommets]}
    while entry :
        nb_rang += 1
        for i in Gv.FILE_Ord : # recherche des successeurs i[1]
            if i[0] == entry[0] and i[1] not in entryed :
                pred = 0
                for index,j in enumerate(Gv.FILE_Ord) : # recherche des prédécesseurs pour chaque succésseurs
                    if j[1] == i[1] and j[0] not in entryed and (j[0] not in entry[0:index]) : # on cherche le nombre de predecesseur de i[1]
                        pred += 1
                        #print("pred=",j)
                print(i,pred)
                if pred <= 1 and i[1] not in entry :
                    entry.append(i[1]) # 0->1=2
                    if nb_rang in rangs :
                        (rangs[nb_rang]).append(i[1]) # ajout
                    else:
                        rangs[nb_rang]=[i[1]] # nouvelle entrée
        entryed.append(entry[0])
        del(entry[0])
        print("les entrees:",entry, entryed,"les rangs: ", rangs)
    return rangs