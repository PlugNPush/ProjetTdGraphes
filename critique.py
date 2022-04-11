import Globalvars as Gv

def critique() :
    chemin_crit = []
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        Trace.write("----- CHEMIN CRITIQUE -----\n")
        for index, element in enumerate(Gv.marge) :
            if element == 0 :
                chemin_crit.append(Gv.liste_rangs[index])
        print("Les sommets comportant le(s) chemin(s) critique(s) sont :",chemin_crit)
        Trace.write("Les sommets comportant le(s) chemin(s) critique(s) sont : " + str(chemin_crit) + "\n")
        
        i=0
        max=chemin_crit[-1]
        while chemin_crit[i] != max:
            #print("i=",i)
            #print(chemin_crit[i+1])
            #print(chemin_crit)
            if Gv.MA[chemin_crit[i]][chemin_crit[i+1]]==0:
                #print("supr")
                del(chemin_crit[i+1])
                i-=1
            i+=1

        print("un chemin critique est",chemin_crit)
        Trace.write("Un chemin critique est : " + str(chemin_crit) + "\n")
        Trace.write("\n")