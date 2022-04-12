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
                        added=0
                        for m in range(len(liste_chemin_crit[n])):
                            if chemin_crit[i] == liste_chemin_crit[n][len(liste_chemin_crit[n])-1-added]:
                                if added==0:
                                    print("APPENDING", chemin_crit[j], "TO", liste_chemin_crit[n])
                                    liste_chemin_crit[n].append(chemin_crit[j])
                                    added+=1
                            else:
                                if chemin_crit[i] == liste_chemin_crit[n][len(liste_chemin_crit[n])-1-m-added]:
                                    if added == 0:
                                        print("COPY", copy.deepcopy(liste_chemin_crit[n][:len(liste_chemin_crit[n])-added-m]), "APPENDING", chemin_crit[j])
                                        liste_chemin_crit.append(copy.deepcopy(liste_chemin_crit[n][:len(liste_chemin_crit[n])-added-m]))
                                        liste_chemin_crit[len(liste_chemin_crit)-1].append(chemin_crit[j])
                                        added += 1

                    if added==0:
                        print("CREATING", chemin_crit[i], "WITH", chemin_crit[j])
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

        liste_triee_chemin_crit = []
        liste_finale_chemin_crit = []

        for e in liste_chemin_crit:
            if e not in liste_triee_chemin_crit:
                e.append(chemin_crit[len(chemin_crit)-1])
                liste_triee_chemin_crit.append(e)

        print(liste_triee_chemin_crit)

        for e in liste_triee_chemin_crit:
            total = 0
            print(e)
            print(Gv.FILE_Ord)
            for i in e:
                print(i)
                f = 0
                match = False
                while f < len(Gv.FILE_Ord) and not match:
                    if i == Gv.FILE_Ord[f][0]:
                        print("FOR I", i, "WEIGHT", Gv.FILE_Ord[f][2])
                        total += Gv.FILE_Ord[f][2]
                        match = True
                    f += 1
            print(total, Gv.dates_tot[len(Gv.dates_tot)-1])
            if total == Gv.dates_tot[len(Gv.dates_tot)-1]:
                liste_finale_chemin_crit.append(e)
                
        print(liste_finale_chemin_crit)
                


        #i=0
        #max=chemin_crit[-1]
        #while chemin_crit[i] != max:
            #print("i=",i)
            #print(chemin_crit[i+1])
            #print(chemin_crit)
            #if Gv.MA[chemin_crit[i]][chemin_crit[i+1]]==0:
                #print("supr")
                #del(chemin_crit[i+1])
                #i-=1
            #i+=1

        print("les chemins critiques sont",liste_finale_chemin_crit)
        if len(liste_finale_chemin_crit) > 1:
            Trace.write("Les chemins critiques sont : ")
            for e in liste_finale_chemin_crit:
                Trace.write(str(e) + "\n")
        else:
            Trace.write("Le chemin critique est : " + str(liste_finale_chemin_crit) + "\n")
        Trace.write("\n")