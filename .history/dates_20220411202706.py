import Globalvars as Gv

def dates() :
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        dates_tot = [0]*Gv.nb_sommets
        for rang in Gv.rangs : # on fait dans l'ordre des rangs
            if rang != 0 :
                for sommet in Gv.rangs[rang] :
                    #print(rang,sommet, dates_tot)
                    # on cherche tous ses prédecesseurs parmis dates_tot et ajoute leur temps puis on les compare
                    for pred in Gv.FILE_Ord :
                        if pred[1] == sommet :
                            dates_tot[sommet] = max(dates_tot[pred[0]] + pred[2],dates_tot[sommet])
        #print(dates_tot)
        
        dates_tard = [dates_tot[-1]]*Gv.nb_sommets
        for i_rang in range(len(Gv.rangs)) : # on fait dans l'ordre inverse des rangs
            rang = len(Gv.rangs)-1-i_rang
            if Gv.rangs[rang] != Gv.rangs[len(Gv.rangs)-1] : #diff du dernier rang
                for i_sommet in range(len(Gv.rangs[rang])) :
                    sommet = len(Gv.rangs[rang]) - 1 - i_sommet
                    # on cherche tous ses succésseurs parmis dates_tard et enlève leur temps puis on les compare
                    #print(rang,sommet,dates_tard)
                    for i_suc in range(len(Gv.FILE_Ord)) :
                        suc = len(Gv.FILE_Ord) - 1 - i_suc
                        if Gv.FILE_Ord[suc][0] == Gv.rangs[rang][sommet] :
                            dates_tard[Gv.FILE_Ord[suc][0]] = min(dates_tard[Gv.FILE_Ord[suc][1]] - Gv.FILE_Ord[suc][2],dates_tard[Gv.FILE_Ord[suc][0]])
        #print(dates_tard)

        marge = [b - a for a, b in zip(dates_tot, dates_tard)]
        #print(marge)
        
        Trace.write("----- CALCUL DES DATES -----\n")
        Trace.write("Dates au plus tot : " + str(Gv.dates_tot) + "\nDates au plus tard :" + str(Gv.dates_tard) + "\nMarge : " + str(Gv.marge) + "\n")
        Trace.write("\n")
        return dates_tot,dates_tard,marge