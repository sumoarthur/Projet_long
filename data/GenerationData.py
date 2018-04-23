
from src.modele.arbre import *
import pickle
from src.modele.StructureData import *


class GenerationData:
    def __init__(self):
        pass

    def GenerationGarphe(self):
        ############


        import random
        import string
        L_L_exo = [[] for k in range(16)]

        nom = 'Exo ' + str(0) + '-' + str(0)
        niveau = "Debutant"
        data1 = "Exercice 1.png"
        v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        L_L_exo[0].append(Exercice(nom, niveau, [v1]))

        nom = 'Exo ' + str(1) + '-' + str(0)
        niveau = "Debutant"
        data1 = "Exercice 2-1.png"
        data2 = "Exercice 2-2.png"
        data3 = "Exercice 2-3.png"
        v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        v3 = Ex_verion(data3, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        L_L_exo[1].append(Exercice(nom, niveau, [v1, v2, v3]))

        nom = 'Exo ' + str(1) + '-' + str(1)
        niveau = "Debutant"
        data1 = "Exercice 3-1.png"
        data2 = "Exercice 3-2.png"
        v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        L_L_exo[1].append(Exercice(nom, niveau, [v1, v2]))

        for k in range(2, len(L_L_exo)):

            nom = 'Exo ' + str(k) + '-' + str(0)
            niveau = "Debutant"

            data1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))
            data2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))

            v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
            v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
            L_L_exo[k].append(Exercice(nom, niveau, [v1, v2]))

            for kk in range(random.randint(1, 5)):
                nom = 'Exo ' + str(k) + '-' + str(kk + 1)
                niveau = ["Debutant", "Intermediaire", "Avance"][random.randint(0, 2)]

                data1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))
                data2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))

                v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
                v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
                L_L_exo[k].append(Exercice(nom, niveau, [v1, v2]))



                #############
                # Exercice final validation

            nom = 'Exo ' + str(k) + '-' + ' - Validation'
            niveau = "Debutant"

            data1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))
            data2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))

            v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
            v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
            L_L_exo[k].append(Exercice(nom, niveau, [v1, v2]))

        #############


        L_L_cours = [[] for k in range(16)]
        L_L_cours[0].append(Lecon(nom, ['Taux_d_accroissement_def.png']))
        L_L_cours[1].append(Lecon(nom, ['Taux_d_accroissement_inter_graph.png', 'Taux_d_acc_demo.png']))
        for k in range(2, len(L_L_cours)):
            nom = 'Cours ' + str(k) + '-' + str(0)
            L_L_cours[k].append(
                Lecon(nom, ['adresse_leconnnnnnnnnnnnnnnnnnnnnnnnnn1', 'adresse_leconnnnnnnnnnnnnnnnnnnnnnnnnn2']))

        Taux_d_accroissement_Definition = Cours("Taux\nd accroissement\n- Definition", "Debutant", L_L_cours[1],
                                                L_L_exo[1])
        Taux_d_accroissement_Interpretation_graphique = Cours("Taux\nd accroissement  \nInterpretation\ngraphique",
                                                              "Debutant", L_L_cours[2], L_L_exo[2])
        Nombre_derive_Definition = Cours("Nombre derive -\nDefinition", "Debutant", L_L_cours[3], L_L_exo[3])
        Tangente_Definition = Cours("Tangente  \nDefinition", "Intermediaire", L_L_cours[4], L_L_exo[4])
        Tangente_Coefficient_directeur = Cours("Tangente  \nCoefficient\ndirecteur", "Intermediaire", L_L_cours[5],
                                               L_L_exo[5])
        Tangente_Equation = Cours("Tangente  \nEquation", "Avance", L_L_cours[6], L_L_exo[6])
        Tangente_Equation_Demonstration = Cours("Tangente  \nEquation -\nDemonstration", "Avance", L_L_cours[7],
                                                L_L_exo[7])
        Fonction_derivee_Definition = Cours("Fonction derivee\n- Definition", "Debutant", L_L_cours[8], L_L_exo[8])
        Fonctions_derivees_usuelles = Cours("Fonctions\nderivees usuelles", "Debutant", L_L_cours[9], L_L_exo[9])
        Derivation_de_somme_ou_difference_de_fonctions = Cours("Derivation de somme\nou difference de\nfonctions",
                                                               "Debutant", L_L_cours[10], L_L_exo[10])
        Derivation_de_produit_de_fonctions = Cours("Derivation de\nproduit de fonctions", "Intermediaire",
                                                   L_L_cours[11], L_L_exo[11])
        Derivation_de_quotient_de_fonctions = Cours("Derivation de\nquotient de fonctions", "Avance", L_L_cours[12],
                                                    L_L_exo[12])
        Application_de_la_derivee = Cours("Application de la\nderivee", "Debutant", L_L_cours[13], L_L_exo[13])
        Theoreme_croissance_n_decroissance = Cours("Theoreme\ncroissance /\ndecroissance", "Debutant", L_L_cours[14],
                                                   L_L_exo[14])
        Trouver_une_valeur_max_ou_min = Cours("Trouver une valeur\nmax ou min", "Intermediaire", L_L_cours[15],
                                              L_L_exo[15])

        a = Arbre((Taux_d_accroissement_Definition, (Taux_d_accroissement_Interpretation_graphique, (
            Nombre_derive_Definition, (Fonction_derivee_Definition),
            (Tangente_Definition, (Tangente_Coefficient_directeur,
                                   (Tangente_Equation, (
                                       Tangente_Equation_Demonstration,
                                       (
                                           Fonction_derivee_Definition)))),
             (Tangente_Coefficient_directeur,
              Fonction_derivee_Definition))))))
        # a.view()

        b = Arbre((Fonction_derivee_Definition, (Fonctions_derivees_usuelles, (
            Derivation_de_somme_ou_difference_de_fonctions, (Derivation_de_produit_de_fonctions, (
                Derivation_de_quotient_de_fonctions,
                (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))), (
                                                                 Application_de_la_derivee,
                                                                 (Theoreme_croissance_n_decroissance,
                                                                  (Trouver_une_valeur_max_ou_min)))),
            (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))))))
        # b.view()

        c = Arbre((Taux_d_accroissement_Definition, (Taux_d_accroissement_Interpretation_graphique, (
            Nombre_derive_Definition, ((Fonction_derivee_Definition, (Fonctions_derivees_usuelles, (
                Derivation_de_somme_ou_difference_de_fonctions, (Derivation_de_produit_de_fonctions, (
                    Derivation_de_quotient_de_fonctions,
                    (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))),
                                                                 (
                                                                     Application_de_la_derivee,
                                                                     (Theoreme_croissance_n_decroissance,
                                                                      (Trouver_une_valeur_max_ou_min)))),
                (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min))))))),
            (
                Tangente_Definition,
                (Tangente_Coefficient_directeur, (Tangente_Equation, (Tangente_Equation_Demonstration, ((
                    Fonction_derivee_Definition,
                    (
                        Fonctions_derivees_usuelles,
                        (
                            Derivation_de_somme_ou_difference_de_fonctions,
                            (
                                Derivation_de_produit_de_fonctions,
                                (
                                    Derivation_de_quotient_de_fonctions,
                                    (
                                        Application_de_la_derivee,
                                        (
                                            Theoreme_croissance_n_decroissance,
                                            (
                                                Trouver_une_valeur_max_ou_min)))),
                                (
                                    Application_de_la_derivee,
                                    (
                                        Theoreme_croissance_n_decroissance,
                                        (
                                            Trouver_une_valeur_max_ou_min)))),
                            (
                                Application_de_la_derivee,
                                (
                                    Theoreme_croissance_n_decroissance,
                                    (
                                        Trouver_une_valeur_max_ou_min))))))))),
                 (Fonction_derivee_Definition, (Fonctions_derivees_usuelles, (
                     Derivation_de_somme_ou_difference_de_fonctions, (Derivation_de_produit_de_fonctions, (
                         Derivation_de_quotient_de_fonctions,
                         (Application_de_la_derivee,
                          (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))), (
                                                                          Application_de_la_derivee,
                                                                          (Theoreme_croissance_n_decroissance,
                                                                           (Trouver_une_valeur_max_ou_min)))),
                     (Application_de_la_derivee,
                      (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min))))))))))))

        N_L_L_cours=[]

        N_L_L_cours += [Cours("Taux\nd accroissement\n- Definition", "Debutant", L_L_cours[1],
                                                L_L_exo[1])]
        N_L_L_cours += [Cours("Taux\nd accroissement  \nInterpretation\ngraphique",
                                                              "Debutant", L_L_cours[2], L_L_exo[2])]
        N_L_L_cours += [Cours("Nombre derive -\nDefinition", "Debutant", L_L_cours[3], L_L_exo[3])]
        N_L_L_cours += [Cours("Tangente  \nDefinition", "Intermediaire", L_L_cours[4], L_L_exo[4])]
        N_L_L_cours += [Cours("Tangente  \nCoefficient\ndirecteur", "Intermediaire", L_L_cours[5],
                                               L_L_exo[5])]
        N_L_L_cours += [Cours("Tangente  \nEquation", "Avance", L_L_cours[6], L_L_exo[6])]
        N_L_L_cours += [Cours("Tangente  \nEquation -\nDemonstration", "Avance", L_L_cours[7],
                                                L_L_exo[7])]
        N_L_L_cours += [Cours("Fonction derivee\n- Definition", "Debutant", L_L_cours[8], L_L_exo[8])]
        N_L_L_cours += [Cours("Fonctions\nderivees usuelles", "Debutant", L_L_cours[9], L_L_exo[9])]
        N_L_L_cours += [Cours("Derivation de somme\nou difference de\nfonctions",
                                                               "Debutant", L_L_cours[10], L_L_exo[10])]
        N_L_L_cours += [Cours("Derivation de\nproduit de fonctions", "Intermediaire",
                                                   L_L_cours[11], L_L_exo[11])]
        N_L_L_cours += [Cours("Derivation de\nquotient de fonctions", "Avance", L_L_cours[12],
                                                    L_L_exo[12])]
        N_L_L_cours += [Cours("Application de la\nderivee", "Debutant", L_L_cours[13], L_L_exo[13])]
        N_L_L_cours += [Cours("Theoreme\ncroissance /\ndecroissance", "Debutant", L_L_cours[14],
                                                   L_L_exo[14])]
        N_L_L_cours += [Cours("Trouver une valeur\nmax ou min", "Intermediaire", L_L_cours[15],
                                              L_L_exo[15])]
        print(L_L_exo)
        print(N_L_L_cours)




        filename_data = open('/home/quince-art/PycharmProjects/Projet_long/data/Exo.txt', 'wb')
        pickle.dump(L_L_exo, filename_data)
        filename_data.close()
        print("Graphe généré \n\n")


        filename_data = open('/home/quince-art/PycharmProjects/Projet_long/data/Cours.txt', 'wb')
        pickle.dump(N_L_L_cours, filename_data)
        filename_data.close()
        print("Graphe généré \n\n")


        filename_data = open('/home/quince-art/PycharmProjects/Projet_long/data/graphe.txt', 'wb')
        pickle.dump(c, filename_data)
        filename_data.close()
        print("Graphe généré \n\n")




a=GenerationData()
a.GenerationGarphe()

