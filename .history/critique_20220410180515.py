import Globalvars as Gv

def critique() :
    chemin_crit = []
    sommets_par_rangs = []
    for rang in Gv.rangs :
        for sommet in Gv.rangs[rang] :
            sommets_par_rangs.append(sommet)
    print("ordre des sommets selon le rang ",sommets_par_rangs)

    for index,element in enumerate(Gv.marge) :
        if element == 0 :
            chemin_crit.append(sommets_par_rangs[index])
    print("le chemin critique est",chemin_crit)