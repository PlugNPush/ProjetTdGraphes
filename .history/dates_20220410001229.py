def dates() :
    dates_tot = [0]*nb_sommets
    for rang in rangs : # on fait dans l'ordre des rangs
        if rang != 0 :
            for sommet in rangs[rang] :
                #print(rang,sommet, dates_tot)
                # on cherche tous ses prédecesseurs parmis dates_tot et ajoute leur temps puis on les compare
                for pred in FILE_Ord :
                    if pred[1] == sommet :
                        dates_tot[sommet] = max(dates_tot[pred[0]] + pred[2],dates_tot[sommet])
    #print(dates_tot)
    
    dates_tard = [dates_tot[-1]]*nb_sommets
    for i_rang in range(len(rangs)) : # on fait dans l'ordre inverse des rangs
        rang = len(rangs)-1-i_rang
        if rangs[rang] != rangs[len(rangs)-1] : #diff du dernier rang
            for i_sommet in range(len(rangs[rang])) :
                sommet = len(rangs[rang]) - 1 - i_sommet
                # on cherche tous ses succésseurs parmis dates_tard et enlève leur temps puis on les compare
                #print(rang,sommet,dates_tard)
                for i_suc in range(len(FILE_Ord)) :
                    suc = len(FILE_Ord) - 1 - i_suc
                    if FILE_Ord[suc][0] == rangs[rang][sommet] :
                        dates_tard[FILE_Ord[suc][0]] = min(dates_tard[FILE_Ord[suc][1]] - FILE_Ord[suc][2],dates_tard[FILE_Ord[suc][0]])
    #print(dates_tard)

    marge = [b - a for a, b in zip(dates_tot, dates_tard)]
    #print(marge)

    return dates_tot,dates_tard,marge