import Globalvars as Gv

def critique() :
    chemin_crit = []
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        for index, element in enumerate(Gv.marge) :
            if element == 0 :
                chemin_crit.append(index)
        print("le chemin critique est",chemin_crit)
        Trace.write("le chemin critique est",chemin_crit, "\n")