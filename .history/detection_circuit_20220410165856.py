import Globalvars as Gv

# Detection de circuit (par suppression des points d'entrées) #
def detection_circuit() :
    entry = [0]
    #nb_no_entry=0
    nb_repeat = []
    entryed = []
    MA_circuit = Gv.MA
    no_circuit = True
    print(MA_circuit)
    while entry and no_circuit : # tant qu'on a pas finis de se déplacer sur le graphe ou que l'on a pas détecté un circuit
        nb_pred=0
        for i in range(len(MA_circuit[entry[0]])): # test des pred
            if MA_circuit[i][entry[0]]==1: # un pred (i) !
                nb_pred+=1
        #print(nb_pred, entry, entryed)
        if nb_pred>0:# on ajoute notre élément à la fin de la liste
            if nb_repeat.sort() == entry.sort():
                print(nb_repeat.sort(), entry.sort())
                print("circuit :",entry[0],MA_circuit[entry[0]])
                no_circuit=False
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
                        no_circuit = False #circuit
            entryed.append(entry[0])
            if entry[0] in nb_repeat:
                nb_repeat.remove(entry[0])
            #print("entryed", entryed,entry[0])
        del(entry[0]) # on a finis avec ce sommet

    """
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
        if nb_no_entry==Gv.nb_sommets:
            print("aucune entrée(s)")
            no_circuit=False

        pred_i = [pred_i[0] for pred_i in FILE_Ord if pred_i[1]==entry[0]] # recherche des pred de entry[0]
        #print(pred_i)
        #print(set(pred_i)&set(entryed))
        if len(set(pred_i)&set(entryed))==len(pred_i): # ses pred sont tous dans entryed
            entryed.append(entry[0]) # entrée faite (s'il n'y a plus de pred)
        else:
            entry.append(entry[0]) # on reboucle à la fin
        """
        
        ##del(entry[0])
        #print("mes entrees",entry,entryed)
        #for i in range(len(MA_circuit)):
            #print(MA_circuit[i])
    return no_circuit