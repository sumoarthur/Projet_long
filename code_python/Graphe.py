



from code_python.arbre import *
from code_python.structure_data import *

class Graphe :

    def __init__(self):
        import random
        import string

        ############
        L_L_exo = [[] for k in range(16)]

        # nom = 'Exo ' + str(0) + '-' + str(0)
        # niveau = "Debutant"
        # data1 = "Exercice 1.png"
        # v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        # L_L_exo[0].append(Exercice(nom, niveau, [v1]))
        #
        # nom = 'Exo ' + str(1) + '-' + str(0)
        # niveau = "Debutant"
        # data1 = "Exercice 2-1.png"
        # data2 = "Exercice 2-2.png"
        # data3 = "Exercice 2-3.png"
        # v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        # v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        # v3 = Ex_verion(data3, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        # L_L_exo[1].append(Exercice(nom, niveau, [v1, v2, v3]))
        #
        # nom = 'Exo ' + str(1) + '-' + str(1)
        # niveau = "Debutant"
        # data1 = "Exercice 3-1.png"
        # data2 = "Exercice 3-2.png"
        # v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        # v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        # L_L_exo[1].append(Exercice(nom, niveau, [v1, v2]))

        for k in range(1, len(L_L_exo)):

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
        Nombre_derive_Definition, (Fonction_derivee_Definition), (Tangente_Definition, (Tangente_Coefficient_directeur,
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
                                                         Application_de_la_derivee, (Theoreme_croissance_n_decroissance,
                                                                                     (Trouver_une_valeur_max_ou_min)))),
        (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))))))
        # b.view()

        c = Arbre((Taux_d_accroissement_Definition, (Taux_d_accroissement_Interpretation_graphique, (
        Nombre_derive_Definition, ((Fonction_derivee_Definition, (Fonctions_derivees_usuelles, (
        Derivation_de_somme_ou_difference_de_fonctions, (Derivation_de_produit_de_fonctions, (
        Derivation_de_quotient_de_fonctions,
        (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))), (
                                                         Application_de_la_derivee, (Theoreme_croissance_n_decroissance,
                                                                                     (Trouver_une_valeur_max_ou_min)))),
        (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min))))))), (
        Tangente_Definition, (Tangente_Coefficient_directeur,  (Tangente_Equation, (Tangente_Equation_Demonstration, ((
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
        (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min)))), (
                                                         Application_de_la_derivee, (Theoreme_croissance_n_decroissance,
                                                                                     (Trouver_une_valeur_max_ou_min)))),
        (Application_de_la_derivee, (Theoreme_croissance_n_decroissance, (Trouver_une_valeur_max_ou_min))))))))))))

        ############




        self.graphe=c
        self.parcours=[]
        self.parcour_avec_exo =[]

    def duration_parcours(self):

        temps_parcours=0
        temps_parcours_avec_exo=0

        for k in self.parcours:
            temps_parcours+=k.duree

        for i in self.parcour_avec_exo :
            temps_parcours_avec_exo += i.duree
        return temps_parcours,temps_parcours_avec_exo

    def view_graphe(self):
        self.graphe.view()

    def view_parcours(self):
        def liste_to_arbre(L):

            if len(L) > 1:
                return (L[0], (liste_to_arbre(L[1:(len(L))])))

            else:
                return (L[0])


        aa=Arbre(liste_to_arbre(self.parcours))
        aa.view()

    def view_exercice(self):
        def liste_to_arbre(L):

            if len(L) > 1:
                return (L[0], (liste_to_arbre(L[1:(len(L))])))

            else:
                return (L[0])

        if len(self.parcour_avec_exo)==0:
            print("impossible d'affiche l'arbre le parcours avec exo est vide")
        else:
            aa = Arbre(liste_to_arbre(self.parcour_avec_exo))
            aa.view()

    def cal_parcours(self,niveau):
        arbre=self.graphe

        L_parcours=[]

        fils=[0]
        fils = arbre.lesfils()
        L_parcours += [arbre.racine]

        fin=False
        while fils!=[]:




            if len(fils)>1:
                L_info=[fils[k].racine.niveau for k in range(len(fils))]

                if niveau=="Debutant":
                    if "Debutant" in L_info:
                        arbre=fils[L_info.index("Debutant")]


                elif niveau=="Intermediaire":
                    if "Debutant" in L_info:
                        arbre = fils[L_info.index("Debutant")]

                    if "Intermediaire" in L_info:
                        arbre = fils[L_info.index("Intermediaire")]


                elif niveau =="Avance" :

                    if "Debutant" in L_info:
                        arbre = fils[L_info.index("Debutant")]

                    if "Intermediaire" in L_info:
                        arbre = fils[L_info.index("Intermediaire")]

                    if "Avance" in L_info:
                        arbre = fils[L_info.index("Avance")]



                else:
                    a=1




            elif len(fils)==1:


                if niveau == "Debutant":
                    if "Debutant" ==fils[0].racine.niveau:
                        arbre=fils[0]
                    else:
                        fils=[]
                        fin=True

                elif niveau == "Intermediaire":


                    if ("Debutant" ==fils[0].racine.niveau) or ("Intermediaire" ==fils[0].racine.niveau):
                        arbre = fils[0]

                    else:
                        fils = []
                        fin=True




                elif niveau == "Avance":
                    arbre = fils[0]

                else:
                    print("niveau non valide | cal_parcours 45453")

            else:
                arbre=fils

            if fin ==False:
                fils = arbre.lesfils()
            L_parcours += [arbre.racine]


        self.parcours= L_parcours

    def defintion_exercice(self,niveau_s,opti,temps_limite):
        L_parcour_avec_exo=[]
        L_parcours=self.parcours


        if opti=="normal":

            for k in L_parcours:
                L_exo=k.exo
                L_exo_selec=[]

                for kk in L_exo:

                    if niveau_s=="Debutant":

                        if kk.niveau=="Debutant":
                            L_exo_selec+=[kk]

                    elif niveau_s=="Intermediaire":

                        if (kk.niveau=="Debutant") or (kk.niveau=="Intermediaire"):
                            L_exo_selec+=[kk]

                    else:
                        L_exo_selec+=[kk]

                L_parcour_avec_exo+=[k]+L_exo_selec

            self.parcour_avec_exo = L_parcour_avec_exo

        elif opti=="date_limite":

            taille_min_cours=0
            for k in self.parcours:
                taille_min_cours+=k.duree



            L_exo_selec = []

            for k in L_parcours:
                L_exo=k.exo


                for kk in L_exo:


                    if niveau_s=="Debutant":

                        if kk.niveau=="Debutant":
                            L_exo_selec+=[kk]

                    elif niveau_s=="Intermediaire":

                        if (kk.niveau=="Debutant") or (kk.niveau=="Intermediaire"):
                            L_exo_selec+=[kk]

                    else:
                        L_exo_selec+=[kk]




            #######
            #Exo validation

            L_Exo_Validation=[]
            for kkkk in L_exo_selec:
                if "Validation" in kkkk.nom:

                    L_Exo_Validation+=[kkkk]

            print("L_Exo_Validation    ",len(L_Exo_Validation),L_Exo_Validation)


            ######

            taille_min_exo=0
            for kil in L_Exo_Validation:
                taille_min_exo+=kil.duree


            taille_min=taille_min_cours+taille_min_exo


            if temps_limite - taille_min >= 0:
                temps_limite = temps_limite -  taille_min






                L_exo_selec = []

                for k in L_parcours:
                    L_exo=k.exo


                    for kk in L_exo:

                        if  not("Validation" in kk.nom):

                            if niveau_s=="Debutant":

                                if kk.niveau=="Debutant":
                                    L_exo_selec+=[kk]

                            elif niveau_s=="Intermediaire":

                                if (kk.niveau=="Debutant") or (kk.niveau=="Intermediaire"):
                                    L_exo_selec+=[kk]

                            else:
                                L_exo_selec+=[kk]








                a = sorted(L_exo_selec, key=lambda bb: bb.duree / bb.score)

                sum=0
                L_ex_valide=[]


                for k_v in a:

                    if sum+k_v.duree<temps_limite:

                        sum+=+k_v.duree

                        L_ex_valide.append(k_v)




                print("L_ex_valide    ",len(L_ex_valide), L_ex_valide)
                print(len(L_parcours))

                for k in L_parcours:
                    L_exo=k.exo
                    L_exo_selec=[]

                    for kk in L_exo:


                        if kk in L_ex_valide:

                            if niveau_s=="Debutant":

                                if kk.niveau=="Debutant":
                                    L_exo_selec+=[kk]

                            elif niveau_s=="Intermediaire":

                                if (kk.niveau=="Debutant") or (kk.niveau=="Intermediaire"):
                                    L_exo_selec+=[kk]

                            else:
                                L_exo_selec+=[kk]


                    L_parcour_avec_exo+=[k]+L_exo_selec+[L_Exo_Validation.pop(0)]

                self.parcour_avec_exo = L_parcour_avec_exo



            else :
                print("Le temps critique est de "+str(2*taille_min)+" le parcours ne peut pas etre determiner si le temps disponible est inferieur au temps critique")

    def update_resu(self,):
        pass







