from arbres import *
from cours import *
from graphviz import Digraph
import random
import string





def creation_arbre():

    L_L_exo=[[] for k in range(16)]

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
    L_L_exo[1].append(Exercice(nom, niveau, [v1, v2,v3]))



    nom = 'Exo ' + str(1) + '-' + str(1)
    niveau = "Debutant"
    data1 = "Exercice 3-1.png"
    data2 = "Exercice 3-2.png"
    v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
    v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
    L_L_exo[1].append(Exercice(nom, niveau, [v1, v2]))





    for k in range(2,len(L_L_exo)):

        nom = 'Exo ' + str(k) + '-' + str(0)
        niveau = "Debutant"

        data1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))
        data2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))

        v1 = Ex_verion(data1, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        v2 = Ex_verion(data2, random.randint(0, 2) / 2, random.randint(0, 2) / 2)
        L_L_exo[k].append(Exercice(nom, niveau, [v1, v2]))



        for kk in range(random.randint(1,5)):
            nom='Exo '+str(k)+'-'+str(kk+1)
            niveau=["Debutant","Intermediaire","Avance"][random.randint(0,2)]

            data1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))
            data2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))


            v1=Ex_verion(data1,random.randint(0,2)/2,random.randint(0,2)/2)
            v2=Ex_verion(data2,random.randint(0,2)/2,random.randint(0,2)/2)
            L_L_exo[k].append(Exercice(nom,niveau,[v1,v2]))


    print(L_L_exo)




    L_L_cours=[[] for k in range(16)]
    L_L_cours[0].append(Lecon(nom, ['Taux_d_accroissement_def.png']))
    L_L_cours[1].append(Lecon(nom, ['Taux_d_accroissement_inter_graph.png','Taux_d_acc_demo.png']))
    for k in range(2,len(L_L_cours)):
        nom = 'Cours ' + str(k) + '-' + str(0)
        L_L_cours[k].append(Lecon(nom, ['adresse_leconnnnnnnnnnnnnnnnnnnnnnnnnn1','adresse_leconnnnnnnnnnnnnnnnnnnnnnnnnn2']))
    print("ee",L_L_cours)


    Taux_d_accroissement_Definition=Cours("Taux\nd accroissement\n- Definition","Debutant",L_L_cours[1],L_L_exo[1])
    Taux_d_accroissement_Interpretation_graphique=Cours("Taux\nd accroissement  \nInterpretation\ngraphique","Debutant",L_L_cours[2],L_L_exo[2])
    Nombre_derive_Definition=Cours("Nombre derive -\nDefinition","Debutant",L_L_cours[3],L_L_exo[3])
    Tangente_Definition=Cours("Tangente  \nDefinition","Intermediaire",L_L_cours[4],L_L_exo[4])
    Tangente_Coefficient_directeur=Cours("Tangente  \nCoefficient\ndirecteur","Intermediaire",L_L_cours[5],L_L_exo[5])
    Tangente_Equation=Cours("Tangente  \nEquation","Avance",L_L_cours[6],L_L_exo[6])
    Tangente_Equation_Demonstration=Cours("Tangente  \nEquation -\nDemonstration","Avance",L_L_cours[7],L_L_exo[7])
    Fonction_derivee_Definition=Cours("Fonction derivee\n- Definition","Debutant",L_L_cours[8],L_L_exo[8])
    Fonctions_derivees_usuelles=Cours("Fonctions\nderivees usuelles","Debutant",L_L_cours[9],L_L_exo[9])
    Derivation_de_somme_ou_difference_de_fonctions=Cours("Derivation de somme\nou difference de\nfonctions","Debutant",L_L_cours[10],L_L_exo[10])
    Derivation_de_produit_de_fonctions=Cours("Derivation de\nproduit de fonctions","Intermediaire",L_L_cours[11],L_L_exo[11])
    Derivation_de_quotient_de_fonctions=Cours("Derivation de\nquotient de fonctions","Avance",L_L_cours[12],L_L_exo[12])
    Application_de_la_derivee=Cours("Application de la\nderivee","Debutant",L_L_cours[13],L_L_exo[13])
    Theoreme_croissance_n_decroissance=Cours("Theoreme\ncroissance /\ndecroissance","Debutant",L_L_cours[14],L_L_exo[14])
    Trouver_une_valeur_max_ou_min=Cours("Trouver une valeur\nmax ou min","Intermediaire",L_L_cours[15],L_L_exo[15])



    a=Arbre( (Taux_d_accroissement_Definition,(Taux_d_accroissement_Interpretation_graphique,(Nombre_derive_Definition,(Fonction_derivee_Definition),(Tangente_Definition,(Tangente_Coefficient_directeur,(Tangente_Equation,(Tangente_Equation_Demonstration,(Fonction_derivee_Definition)))),(Tangente_Coefficient_directeur,Fonction_derivee_Definition))))))
    #a.view()

    b=Arbre((Fonction_derivee_Definition,(Fonctions_derivees_usuelles,(Derivation_de_somme_ou_difference_de_fonctions,(Derivation_de_produit_de_fonctions,(Derivation_de_quotient_de_fonctions,(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))))))
    #b.view()

    c=Arbre( (Taux_d_accroissement_Definition,(Taux_d_accroissement_Interpretation_graphique,(Nombre_derive_Definition,((Fonction_derivee_Definition,(Fonctions_derivees_usuelles,(Derivation_de_somme_ou_difference_de_fonctions,(Derivation_de_produit_de_fonctions,(Derivation_de_quotient_de_fonctions,(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min))))))),(Tangente_Definition,(Tangente_Coefficient_directeur,(Tangente_Equation,(Tangente_Equation_Demonstration,((Fonction_derivee_Definition,(Fonctions_derivees_usuelles,(Derivation_de_somme_ou_difference_de_fonctions,(Derivation_de_produit_de_fonctions,(Derivation_de_quotient_de_fonctions,(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))))))))),(Tangente_Coefficient_directeur,(Fonction_derivee_Definition,(Fonctions_derivees_usuelles,(Derivation_de_somme_ou_difference_de_fonctions,(Derivation_de_produit_de_fonctions,(Derivation_de_quotient_de_fonctions,(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min)))),(Application_de_la_derivee,(Theoreme_croissance_n_decroissance,(Trouver_une_valeur_max_ou_min))))))))))))
    c.view()
    return c



def parcours(arbre,niveau):
    L_parcours=[]

    fils=[0]
    while fils!=[]:

        L_parcours+=[arbre.racine]
        fils=arbre.lesfils()

        if len(fils)>1:
            Prio_inter=False
            Prio_avancer=False
            for k in range(len(fils)):
                if niveau=="Debutant":
                    if fils[k].racine.niveau=="Debutant":
                        arbre=fils[k]
                    elif fils[k].racine.niveau=="Intermediaire":
                        print('rien')
                    else:
                        print('rien')

                elif niveau=="Intermediaire":

                    if fils[k].racine.niveau == "Debutant" and Prio_inter==False:
                        arbre = fils[k]
                    elif fils[k].racine.niveau == "Intermediaire":
                        Prio_inter=True
                        arbre = fils[k]
                    else:
                        print('rien')

                else:
                    print('avancé')
                    if fils[k].racine.niveau == "Debutant" and Prio_inter == False and Prio_avancer==False:
                        arbre_pro = fils[k]
                    elif fils[k].racine.niveau == "Intermediaire" and Prio_avancer==False:
                        print('inter',fils[0].racine.niveau,fils[1].racine.niveau,Prio_inter,Prio_avancer)

                        Prio_inter = True
                        arbre_pro=fils[k]
                    else:
                        print('av',fils[0].racine.niveau,fils[1].racine.niveau,Prio_inter,Prio_avancer)
                        Prio_avancer =True
                        arbre_pro = fils[k]

            if niveau=="Avance":
                arbre=arbre_pro



        elif len(fils)==1:
            Prio_inter=False
            Prio_avancer=False


            if niveau == "Debutant":
                if fils[0].racine.niveau == "Debutant":
                    arbre = fils[0]
                elif fils[0].racine.niveau == "Intermediaire":
                    fils = []
                else:
                    fils = []

            elif niveau == "Intermediaire":

                if fils[0].racine.niveau == "Debutant" and Prio_inter == False:
                    arbre = fils[0]
                elif fils[0].racine.niveau == "Intermediaire":
                    Prio_inter = True
                    arbre = fils[0]
                else:
                    fils = []

            else:

                if fils[0].racine.niveau == "Debutant" and Prio_inter == False and Prio_avancer == False:
                    arbre = fils[0]
                elif fils[0].racine.niveau == "Intermediaire" and Prio_avancer == False:
                    Prio_inter= True
                    arbre = fils[0]
                else:
                    Prio_avancer = True
                    arbre = fils[0]

        else:
            arbre=fils

    def liste_to_arbre(L):

        if len(L)>1:
            return (L[0],(liste_to_arbre(L[1:(len(L))])))

        else:
            return (L[0])




    aa=Arbre(liste_to_arbre(L_parcours))
    aa.view()

    return L_parcours



def defintion_exercice(L_parcours,niveau_s):
    L_parcour_avec_exo=[]

    print("nv_s",niveau_s)

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

        def liste_to_arbre(L):

            if len(L) > 1:
                return (L[0], (liste_to_arbre(L[1:(len(L))])))

            else:
                return (L[0])

    aa = Arbre(liste_to_arbre(L_parcour_avec_exo))
    aa.view()

    return L_parcour_avec_exo





