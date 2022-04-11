import Globalvars as Gv

# Calcul des rangs #
def rang() :
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        entry = [0] # mes entrées
        nb_rang = 0 # le rang actuel
        rangs = {nb_rang:[entry[0]]} # dico des rangs {rang:[sommets]}
        while entry :
            succ = []

            for i in Gv.FILE_Ord : # Pour toutes les entrées
                if i[0] in entry and i[1] not in succ: # on recherche tous les successeurs de nos entrées
                    succ.append(i[1])
            
            if succ:
                nb_rang += 1
                rangs[nb_rang] = succ

                for i in range(0, nb_rang):
                    for e in succ:
                        if e in rangs[i]:
                            rangs[i] = list(filter(lambda a: a != e, rangs[i])) # On enlève toutes les occurences des nouveaux successeurs dans les rangs inférieurs
            
            entry = succ

        Trace.write("----- CALCUL DES RANGS -----\n")
        Trace.write("Les rangs sont : " + str(rangs) + "\n")
        Trace.write("\n")
        return rangs