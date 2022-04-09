import Globalvars as Gv

# Matrices d'adjacence et de valeurs #
def adjacence_valeurs() :
    MA = [[0 for x in range(Gv.nb_sommets)] for i in range(Gv.nb_sommets)]
    MV = [['*' for x in range(Gv.nb_sommets)] for i in range(Gv.nb_sommets)]
    for arc in Gv.FILE_Ord :
        MA[arc[0]][arc[1]] = 1
        MV[arc[0]][arc[1]] = str(arc[2])

    #write MA et MV
    with open("tables/table {}".format(Gv.num_file) + '/MA{}.txt'.format(Gv.num_file),"w") as MA1 :
        for line in MA :
            for element in line :
                MA1.write(str(element) + ' ')
            MA1.write('\n')
    with open("tables/table {}".format(Gv.num_file) + '/MV{}.txt'.format(Gv.num_file),"w") as MV1 :
        for line in MV :
            for element in line :
                MV1.write(element + ' ')
            MV1.write('\n')

    return MA,MV