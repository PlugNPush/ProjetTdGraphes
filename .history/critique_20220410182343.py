import Globalvars as Gv

def critique() :
    chemin_crit = []

    for index, element in enumerate(Gv.marge) :
        if element == 0 :
            chemin_crit.append(index)
    print("le chemin critique est",chemin_crit)