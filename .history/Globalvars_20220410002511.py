# Variables partagées entre les fichiers

def init():

    # Déclaration du statut global
    global W
    global R
    global G
    global Y
    global B
    global P
    global C


    # Fichier importé #
    global num_file
    global File_txt
    
    # Initialisation #
    global FILE
    global FILE_Ord
    global nb_sommets
    global nb_arcs
    #global taille_max
    global no_circuit
    global MA
    global MV


    # Couleurs
    W = '\33[0m' #white
    R = '\33[31m' #red
    G = '\33[32m' #green
    Y = '\33[33m' #yellow
    B = '\33[34m' #blue
    P = '\33[35m' #purple
    C = '\33[36m' #cyan

    num_file = 0

    FILE = [] # liste de str
    FILE_Ord = [] # liste de int
    nb_sommets =- 1
    nb_arcs =- 1
    #taille_max=99
    no_circuit = True
    MA = [] # tableau de int
    MV = [] # tableau de str


