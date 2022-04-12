import Globalvars as Gv
import copy

def critique() :
    chemin_crit = []
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        Trace.write("----- CHEMIN CRITIQUE -----\n")
        for index, element in enumerate(Gv.marge) :
            if element == 0 :
                chemin_crit.append(Gv.liste_rangs[index])
        print("Les sommets comportant le(s) chemin(s) critique(s) sont :",chemin_crit)
        Trace.write("Les sommets comportant le(s) chemin(s) critique(s) sont : " + str(chemin_crit) + "\n")
        

        liste_chemin_crit=[[0]]
        for i in range(len(chemin_crit)-1):
            for j in range(len(chemin_crit)-1):
                if Gv.MA[chemin_crit[i]][chemin_crit[j]]==1:
                    print(liste_chemin_crit)
                    print(i,j, chemin_crit[i],chemin_crit[j])
                    added=0
                    for n in range(len(liste_chemin_crit)):
                        if chemin_crit[i] == liste_chemin_crit[n][len(liste_chemin_crit[n])-1-added]:
                            if added==0:
                                liste_chemin_crit[n].append(chemin_crit[j])
                                added+=1
                        else:
                            if added == 0:
                                liste_chemin_crit.append(copy.deepcopy(liste_chemin_crit[n][:len(liste_chemin_crit[n])-added-1]))
                                liste_chemin_crit[n+1].append(chemin_crit[j])
                                added += 1

                    if added==0:
                        detected=1
                        for n in range(len(liste_chemin_crit)):
                            if chemin_crit[i] not in liste_chemin_crit[n]:
                                detected=0
                        if detected==1:
                            liste_chemin_crit.append([chemin_crit[i]])
                            for n in range(len(liste_chemin_crit)):
                                if chemin_crit[i] == liste_chemin_crit[n][len(liste_chemin_crit[n])-1]:
                                    liste_chemin_crit[n].append(chemin_crit[j])
                        
        print(liste_chemin_crit)


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