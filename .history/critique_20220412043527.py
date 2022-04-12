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
        

        # On établit tous les chemins possibles utilisant les sommets des chemins critiques
        liste_chemin_crit=[[0]]
        for i in range(len(chemin_crit)-1):
            for j in range(len(chemin_crit)-1):
                if Gv.MA[chemin_crit[i]][chemin_crit[j]]==1:
                    added=0
                    for n in range(len(liste_chemin_crit)):
                        added=0
                        for m in range(len(liste_chemin_crit[n])):
                            if chemin_crit[i] == liste_chemin_crit[n][len(liste_chemin_crit[n])-1-added]:
                                if added==0:
                                    liste_chemin_crit[n].append(chemin_crit[j]) # Soit on ajoute l'élément parcouru à un chemin existant
                                    added+=1
                            else:
                                if chemin_crit[i] == liste_chemin_crit[n][len(liste_chemin_crit[n])-1-m-added]:
                                    if added == 0:
                                        liste_chemin_crit.append(copy.deepcopy(liste_chemin_crit[n][:len(liste_chemin_crit[n])-added-m]))
                                        liste_chemin_crit[len(liste_chemin_crit)-1].append(chemin_crit[j]) # Soit on copie un début de chemin pour le compléter avec l'élément parcouru
                                        added += 1

        liste_triee_chemin_crit = []
        liste_finale_chemin_crit = []

        for e in liste_chemin_crit: # On ajoute l'élément final (omega, ici n+1)
            if e not in liste_triee_chemin_crit:
                e.append(chemin_crit[len(chemin_crit)-1])
                liste_triee_chemin_crit.append(e)


        for e in liste_triee_chemin_crit:
            total = 0
            for i in e:
                f = 0
                match = False
                while f < len(Gv.FILE_Ord) and not match:
                    if i == Gv.FILE_Ord[f][0]:
                        total += Gv.FILE_Ord[f][2] # On calcule le poids total pour chaque chemin
                        match = True
                    f += 1
            if total == Gv.dates_tot[len(Gv.dates_tot)-1]:
                liste_finale_chemin_crit.append(e) # Si le poids total est le même que la date au plus tôt pour le dernier sommet, alors c'est un chemin critique
                


        # Ancien code pour afficher un chemin critique
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

        print("le(s) chemin(s) critique(s) est/sont",liste_finale_chemin_crit)
        if len(liste_finale_chemin_crit) > 1:
            Trace.write("Les chemins critiques sont : \n")
            for e in liste_finale_chemin_crit:
                Trace.write(str(e) + "\n")
        else:
            Trace.write("Le chemin critique est : " + str(liste_finale_chemin_crit[0]) + "\n")
        Trace.write("\n")