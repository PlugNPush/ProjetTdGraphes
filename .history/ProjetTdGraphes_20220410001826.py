# -*- coding: utf8 -*-
### ProjetTdGraphes ###

# Bibliothéques #
from lecture_fichier import *
from ordonnancement import *
from adjacence_valeurs import *
from detection_circuit import *
from rang import *
from dates import *
from critique import *
import Globalvars as Gv


## Main ##

# Les couleurs #


print("Bonjour !")
start = True
while start :
    num_file = 0
    while num_file < 1 or num_file > 10 :
        num_file = int(input("Choisissez le numero de l'exercice (entre 1 et 10): "))

    # Fichier importés #
    File_txt = 'Test{}'.format(num_file) + '\Test{}.txt'.format(num_file)

    # Initialisation #
    FILE = [] # liste de str
    FILE_Ord = [] # liste de int
    nb_sommets =- 1
    nb_arcs =- 1
    #taille_max=99
    no_circuit = True
    MA = [] # tableau de int
    MV = [] # tableau de str

    # Corps #
    lecture_fichier()
    print(FILE)
    nb_sommets,nb_arcs=ordonnancement()
    print("ordonancement",FILE_Ord)
    MA,MV=adjacence_valeurs()
    print("MA",MA)
    print("MV",MV)
    no_circuit=detection_circuit()
    print("pas de circuit:",no_circuit)
    if no_circuit :
        rangs = rang()
        print("les rangs:",rangs)
        dates_tot,dates_tard,marge=dates()
        print("dates au plus tot, au plus tard et marge:",dates_tot,dates_tard,marge)
        critique()
    else :
        print("Nous ne pouvons continuez les calculs du fait de la présence d'un circuit.")

    continuation = ""
    while continuation != "Y" and continuation != "N" :
        continuation = input("\nVoulez-vous continuer et choisir un autre graphe ? (Y ou N): ")
        print(continuation)
    if continuation == "N" : #STOP
        print("Au revoir !\n")
        start = False
