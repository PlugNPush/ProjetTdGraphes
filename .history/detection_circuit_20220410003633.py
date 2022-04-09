import Globalvars as Gv

# Detection de circuit (par suppression des points d'entrées) #
def detection_circuit() :
    entry = [0]
    nb_no_entry=0
    entryed = []
    MA_circuit = MA
    no_circuit = True
    while entry and no_circuit :
        for i in range(len(MA_circuit[entry[0]])) : # on enlève les arcs de l'entrée
            if MA_circuit[entry[0]][i] == 1 :
                #print(i)
                MA_circuit[entry[0]][i] = 0
                if i not in entry :
                    entry.append(i) # on ajoute les successeurs des arcs enlevés aux entrées
                if i in entryed :        
                    print("circuit :",i)
                    no_circuit = False #circuit
            else :
                nb_no_entry+=1
        #for i in range(len(MA_circuit)): # on enlève la colonne de l'entrée
        #    del(MA_circuit[i][entry[0]])
        if nb_no_entry==nb_sommets:
            print("aucune entrée(s)")
            no_circuit=False
        """
        pred_i = [pred_i[0] for pred_i in FILE_Ord if pred_i[1]==entry[0]] # recherche des pred de entry[0]
        #print(pred_i)
        #print(set(pred_i)&set(entryed))
        if len(set(pred_i)&set(entryed))==len(pred_i): # ses pred sont tous dans entryed
            entryed.append(entry[0]) # entrée faite (s'il n'y a plus de pred)
        else:
            entry.append(entry[0]) # on reboucle à la fin
        """
        del(entry[0])
        #print("mes entrees",entry,entryed)
        #for i in range(len(MA_circuit)):
            #print(MA_circuit[i])
    return no_circuit