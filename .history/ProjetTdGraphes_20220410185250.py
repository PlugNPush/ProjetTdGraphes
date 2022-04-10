# -*- coding: utf8 -*-
### ProjetTdGraphes ###

# Bibliothéques #
from lecture_fichier import lecture_fichier
from ordonnancement import ordonnancement
from adjacence_valeurs import adjacence_valeurs
from detection_circuit import detection_circuit
from rang import rang
from dates import dates
from critique import critique
import Globalvars as Gv

# Charger les variables globales (UNE SEULE FOIS)
Gv.init()

## Main ##
def main():

    # Corps #
    lecture_fichier()
    print(Gv.FILE)
    Gv.nb_sommets, Gv.nb_arcs=ordonnancement()
    print("ordonancement",Gv.FILE_Ord)
    Gv.MA,Gv.MV=adjacence_valeurs()
    print("MA",Gv.MA)
    print("MV",Gv.MV)
    Gv.no_circuit=detection_circuit()
    print("statut de circuit:", not Gv.no_circuit)
    if Gv.no_circuit :
        
        with open("L3-C4-trace{}.txt".format(Gv.num_file),"a") as Trace :
            Gv.rangs = rang()
            Trace.write("----- CALCUL DES RANGS -----\n")
            print("les rangs:", Gv.rangs)
            Trace.write("les rangs:" + str(Gv.rangs) + "\n")
            Trace.write("----- CALCUL DES DATES -----\n")
            Gv.dates_tot,Gv.dates_tard,Gv.marge=dates()
            print("dates au plus tot, au plus tard et marge:",Gv.dates_tot,Gv.dates_tard,Gv.marge, "\n")
            Trace.write("dates au plus tot, au plus tard et marge:" + str(Gv.dates_tot) + str(Gv.dates_tard) + str(Gv.marge) + "\n")
            critique()
    else :
        print("Nous ne pouvons continuez les calculs du fait de la présence d'un circuit.")


print("Bonjour !")
start = True
while start :

    while Gv.num_file < 1 or Gv.num_file > 12 :
        Gv.num_file = int(input("Choisissez le numero de l'exercice (entre 1 et 12): "))

    # Fichier importés #
    Gv.File_txt = "L3-C4-graphe{}.txt".format(Gv.num_file)
    main()

    continuation = ""
    while continuation != "y" and continuation != "n" :
        continuation = input("\nVoulez-vous continuer et choisir un autre graphe ? (y ou n): ")
        print(continuation)
        Gv.reset()
    if continuation == "n" : #STOP
        print("Au revoir !\n")
        start = False
