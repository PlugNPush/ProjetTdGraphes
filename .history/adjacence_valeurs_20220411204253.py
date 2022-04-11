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
        for line in MA :
            for element in line :
                Trace.write(str(element) + ' ')
            Trace.write('\n')
        Trace.write('\n')

        Trace.write('----- Matrice Valeurs MV -----\n')
        for line in MV :
            for element in line :
                if element == "*":
                    Trace.write(str(element) * 2 + ' ')
                else:
                    Trace.write(str(element).zfill(2) + ' ')
            Trace.write('\n')
        Trace.write('\n')

    return MA,MV