
from code_python.Graphe import *

print('Presentation des uses cases : ')
print('\t\t Use case 1: "Demande de parcours de niveau debutant sans limite de temps" ')
print('\t\t Use case 2: "Demande de parcours de niveau intermediaire sans limite de temps" ')
print('\t\t Use case 3: "Demande de parcours de niveau avancer sans limite de temps"  ')
print()
print('\t\t Use case 4: "Demande de parcours de niveau debutant avec limite de temps" ')
print('\t\t Use case 5: "Demande de parcours de niveau intermediaire avec limite de temps" ')
print('\t\t Use case 6: "Demande de parcours de niveau avancer avec limite de temps"  ')


nn = int(input())





if nn == 1:
    print("Use case "+str(nn))


    #creation aleatoir des données + chargement du graphe
    graph=Graphe()
    print("donnée crée / ou charger")
    niveau="Debutant"
    graph.cal_parcours(niveau)
    graph.defintion_exercice(niveau,"normal","")

    graph.view_parcours()
    graph.view_exercice()




    temps_parcours, temps_parcours_avec_exo = graph.duration_parcours()
    print("\n\n \Temps de parcours sans exo:  "+str(temps_parcours))
    print("\n\n \Temps de parcours avec exo:  "+str(temps_parcours_avec_exo))

elif nn == 2:
    print("Use case "+str(nn))


    #creation aleatoir des données + chargement du graphe
    graph=Graphe()
    print("donnée crée / ou charger")
    niveau="Intermediaire"
    graph.cal_parcours(niveau)
    graph.defintion_exercice(niveau,"normal","")

    graph.view_parcours()
    graph.view_exercice()




    temps_parcours, temps_parcours_avec_exo = graph.duration_parcours()
    print("\n\n \Temps de parcours sans exo:  "+str(temps_parcours))
    print("\n\n \Temps de parcours avec exo:  "+str(temps_parcours_avec_exo))

elif nn == 3:
    print("Use case "+str(nn))


    #creation aleatoir des données + chargement du graphe
    graph=Graphe()
    print("donnée crée / ou charger")
    niveau="Avance"
    graph.cal_parcours(niveau)
    graph.defintion_exercice(niveau,"normal","")

    graph.view_parcours()
    graph.view_exercice()




    temps_parcours, temps_parcours_avec_exo = graph.duration_parcours()
    print("\n\n \Temps de parcours sans exo:  "+str(temps_parcours))
    print("\n\n \Temps de parcours avec exo:  "+str(temps_parcours_avec_exo))

elif nn == 4:
    print("Use case " + str(nn))

    print("\n Combien de temps voulez vous  revisez")

    temps_rev=int(input())


    # creation aleatoir des données + chargement du graphe
    graph = Graphe()
    print("donnée crée / ou charger")
    niveau = "Debutant"
    graph.cal_parcours(niveau)
    graph.defintion_exercice(niveau, "date_limite", temps_rev)

    graph.view_parcours()
    graph.view_exercice()

    temps_parcours, temps_parcours_avec_exo = graph.duration_parcours()
    print("\n\n \Temps de parcours sans exo:  " + str(temps_parcours))
    print("\n\n \Temps de parcours avec exo:  " + str(temps_parcours_avec_exo))

elif nn == 5:
    print("Use case " + str(nn))

    print("\n Combien de temps voulez vous  revisez")

    temps_rev=int(input())


    # creation aleatoir des données + chargement du graphe
    graph = Graphe()
    print("donnée crée / ou charger")
    niveau = "Intermediaire"
    graph.cal_parcours(niveau)
    graph.defintion_exercice(niveau, "date_limite", temps_rev)

    graph.view_parcours()
    graph.view_exercice()

    temps_parcours, temps_parcours_avec_exo = graph.duration_parcours()
    print("\n\n \Temps de parcours sans exo:  " + str(temps_parcours))
    print("\n\n \Temps de parcours avec exo:  " + str(temps_parcours_avec_exo))

elif nn == 6:
    print("Use case " + str(nn))

    print("\n Combien de temps voulez vous  revisez")

    temps_rev=int(input())

    # creation aleatoir des données + chargement du graphe
    graph = Graphe()
    print("donnée crée / ou charger")
    niveau = "Avance"
    graph.cal_parcours(niveau)
    graph.defintion_exercice(niveau, "date_limite", temps_rev)

    graph.view_parcours()
    graph.view_exercice()

    temps_parcours, temps_parcours_avec_exo = graph.duration_parcours()
    print("\n\n \Temps de parcours sans exo:  " + str(temps_parcours))
    print("\n\n \Temps de parcours avec exo:  " + str(temps_parcours_avec_exo))

