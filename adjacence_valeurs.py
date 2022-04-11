import Globalvars as Gv

# Matrices d'adjacence et de valeurs #
def adjacence_valeurs() :
    MA = [[0 for x in range(Gv.nb_sommets)] for i in range(Gv.nb_sommets)]
    MV = [['*' for x in range(Gv.nb_sommets)] for i in range(Gv.nb_sommets)]
    for arc in Gv.FILE_Ord :
        MA[arc[0]][arc[1]] = 1
        MV[arc[0]][arc[1]] = str(arc[2])

    #write MA et MV
    with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
        Trace.write('----- Matrice Adjacence MA -----\n')
        Trace.write(' '*(len(str(Gv.nb_sommets))-1))
        for i in range(Gv.nb_sommets):
            Trace.write(' '*(1+len(str(Gv.nb_sommets))-len(str(i)))+str(i))
        Trace.write('\n')
        i=0
        for line in MA :
            Trace.write(str(i)+' '*(1+len(str(Gv.nb_sommets))-len(str(i))))
            for element in line :
                Trace.write(str(element)+' '*len(str(Gv.nb_sommets)))
            Trace.write('\n')
            i+=1
        Trace.write('\n')

        Trace.write('----- Matrice Valeurs MV -----\n')
        taille=Gv.nb_sommets
        for j in Gv.FILE_Ord: # on cherche la taille max parmis les durées et la taille du dernier sommet
            taille=max(taille,j[2])
        taille=len(str(taille))
        print("taille :",taille)
        Trace.write(' '*taille)
        for i in range(Gv.nb_sommets):
            Trace.write(' '*(1+taille-len(str(i)))+str(i))
        Trace.write('\n')
        
        i=0
        for line in MV :
            Trace.write(str(i)+' '*(taille-len(str(i))))
            for element in line :
                Trace.write(' '*(1+taille-len(str(element)))+str(element))
            Trace.write('\n')
            i+=1
        Trace.write('\n')

    return MA,MV