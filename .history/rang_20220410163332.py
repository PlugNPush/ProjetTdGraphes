import Globalvars as Gv

# Calcul des rangs #
def rang() :
    entry = [0] # mes entrées
    nb_rang = 0 # le rang actuel
    rangs = {nb_rang:[entry[0]]} # dico des rangs {rang:[sommets]}
    while entry :
        succ = []

        for i in Gv.FILE_Ord : # Pour toutes les entrées
            if i[0] in entry and i[0] not in succ: # on recherche tous les successeurs de nos entrées
                succ.append(i[1])
        
        if succ:
            nb_rang += 1
            rangs[nb_rang] = succ

            for i in range(0, nb_rang):
                for e in succ:
                    print("MATCHING ", e, " AGAINST ", rangs[i])
                    if e in rangs[i]:
                        print("REMOVING ", e, " FROM ", rangs[i])
                        rangs[i].remove(e)
        
        entry = succ
    return rangs