import Globalvars as Gv

def critique() :
    chemin_crit = []
    sommets_par_rangs = []
    for rang in rangs :
        for sommet in rangs[rang] :
            sommets_par_rangs.append(sommet)
    print("ordre des sommets celon le rang ",sommets_par_rangs)

    for index,element in enumerate(marge) :
        if element == 0 :
            chemin_crit.append(sommets_par_rangs[index])
    print("le chemin critique est",chemin_crit)