# Variables partagées entre les fichiers

# ----- Système de gestion de données Globalvars ----- 
# Lorsqu'une vairiable a besoin d'être appelée depuis différents fichiers, elle doit
# être déclarée dans la fonction init() ci-dessous. La fonction init() est appelée
# qu'une seule fois dans le main, puis vous n'avez qu'à importer Globalvars dans les
# autres fichiers.
# 
# ATTENTION : N'oubliez pas de déclarer chaque variable avec le terme 'global' devant
# dans la fonction init(), autrement la variable ne sera pas accessible depuis les 
# autres fichiers !
#
# Pour récupérer une variable, utilisez simplement Globalvars.variable_souhaitée
# n'importe où, et les modifications seront prises en compte à travers tous les autres
# fichiers instantanément.
# ----- Système de gestion de données Globalvars -----

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

    # Attributs #
    global rangs
    global dates_tot
    global dates_tard
    global marge



    # Valeurs par défaut ou constantes 
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
    

def reset():
    init()
