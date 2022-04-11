import Globalvars as Gv
import copy

# Detection de circuit (par suppression des points d'entrées) #
def detection_circuit() :
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        Trace.write("----- DETECTION CIRCUIT -----\n")
        entry = [0]
        #nb_no_entry=0
        nb_repeat = []
        entryed = []
        MA_circuit = copy.deepcopy(Gv.MA)
        no_circuit = True
        warning = 0
        #print(MA_circuit)
        while entry and no_circuit : # tant qu'on a pas finis de se déplacer sur le graphe ou que l'on a pas détecté un circuit
            nb_pred=0
            for i in range(len(MA_circuit[entry[0]])): # test des pred
                if MA_circuit[i][entry[0]]==1: # un pred (i) !
                    nb_pred+=1
            #print(nb_pred, entry, entryed)
            if nb_pred>0:# on ajoute notre élément à la fin de la liste
                if sorted(nb_repeat) == sorted(entry):
                    if warning == len(nb_repeat):
                        print("circuit : ",nb_repeat)
                        Trace.write("Circuit : " + str(nb_repeat) + "\n")
                        no_circuit=False
                    warning += 1
                entry.append(entry[0])
                if entry[0] not in nb_repeat:
                    nb_repeat.append(entry[0])
            else: # on applique
                for i in range(len(MA_circuit[entry[0]])) : 
                    if MA_circuit[entry[0]][i] == 1 : # un suc (i) !
                        #print(i)
                        MA_circuit[entry[0]][i] = 0 # on enlève les arcs de l'entrée
                        if i not in entry :
                            entry.append(i) # on ajoute les successeurs des arcs enlevés aux entrées
                        if i in entryed :
                            print("circuit :",i,MA_circuit[entry[0]],MA_circuit[i])
                            Trace.write("circuit :" + str(i) + str(MA_circuit[entry[0]]) + str(MA_circuit[i]) + "\n")
                            no_circuit = False #circuit
                entryed.append(entry[0])
                if entry[0] in nb_repeat:
                    nb_repeat.remove(entry[0])
                #print("entryed", entryed,entry[0])
                warning = 0
            del(entry[0]) # on a finis avec ce sommet
        
        Trace.write("Statut de circuit : " + str(not no_circuit) + "\n")
        Trace.write("\n")
        return no_circuit