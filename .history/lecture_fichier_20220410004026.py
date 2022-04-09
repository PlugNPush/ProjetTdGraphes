import Globalvars as Gv

# Lecture de fichier #
def lecture_fichier() :
    file = open(File_txt,"r") # ouverture du fichier en lecture seule
    lines = file.readlines() # lecture entier du fichier stocker ligne par ligne
    file.close() # fermeture du fichier après l'avoir lu

    for line in lines : # décomposition des lignes sans retour et par 'espace'
        Gv.FILE.append(line.strip().split(' '))

    # test de corruption des données (test des entiers?)
    i = 0
    for line in Gv.FILE :
        i+=1
        if len(line) < 2 : # il y a au moins 2 éléments
            raise Exception("\nErreur de type sommet/durée\n")
        if int(line[0]) != i : # les sommets commencent à 1 et sont dans l'ordre (à réfléchir)
            raise Exception("\nErreur de type ordre des sommets\n")
        for element in line :
            if int(element) < 0: # tout les éléments sont positifs
                raise Exception("\nErreur de type négatif\n")