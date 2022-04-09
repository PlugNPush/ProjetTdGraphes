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
    print("pas de circuit:",Gv.no_circuit)
    if Gv.no_circuit :
        Gv.rangs = rang()
        print("les rangs:",Gv.rangs)
        Gv.dates_tot,Gv.dates_tard,Gv.marge=dates()
        print("dates au plus tot, au plus tard et marge:",Gv.dates_tot,Gv.dates_tard,Gv.marge)
        critique()
    else :
        print("Nous ne pouvons continuez les calculs du fait de la présence d'un circuit.")


print("Bonjour !")
start = True
while start :

    while Gv.num_file < 1 or Gv.num_file > 10 :
        Gv.num_file = int(input("Choisissez le numero de l'exercice (entre 1 et 10): "))

    # Fichier importés #
    Gv.File_txt = 'Test{}'.format(Gv.num_file) + '/Test{}.txt'.format(Gv.num_file)
    main()

    continuation = ""
    while continuation != "Y" and continuation != "N" :
        continuation = input("\nVoulez-vous continuer et choisir un autre graphe ? (Y ou N): ")
        print(continuation)
        Gv.num_file = 0
    if continuation == "N" : #STOP
        print("Au revoir !\n")
        start = False
