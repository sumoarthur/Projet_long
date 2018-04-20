from src.modele.ChargeGraphe import ChargeGraphe
from src.modele.arbre import  *
from src.modele.DataUser import GrapheDeConnaissance,ResultatExo


class Graphe:


    def __init__(self,preference):

        a=ChargeGraphe(preference)
        self.graphe=a.get_arbre()
        self.parcours = []
        self.parcour_avec_exo = []

    def getRessourceFromId(self,id,preference):
        a = ChargeGraphe(preference)
        exo=a.getExo()
        cours=a.getCours()

        print(exo+cours)

        for k in exo+cours:
            if type(k)==list:
                for kk in k:
                    if kk.nom==id:
                        return kk
            else:
                if k.nom==id:
                    return k


    def duration_parcours(self):

        temps_parcours = 0
        temps_parcours_avec_exo = 0

        for k in self.parcours:
            temps_parcours += k.duree

        for i in self.parcour_avec_exo:
            temps_parcours_avec_exo += i.duree
        return temps_parcours, temps_parcours_avec_exo

    def view_graphe(self):
        self.graphe.view()

    def view_parcours(self):
        def liste_to_arbre(L):

            if len(L) > 1:
                return (L[0], (liste_to_arbre(L[1:(len(L))])))

            else:
                return (L[0])

        aa = Arbre(liste_to_arbre(self.parcours))
        aa.view()

    def view_exercice(self):
        def liste_to_arbre(L):

            if len(L) > 1:
                return (L[0], (liste_to_arbre(L[1:(len(L))])))

            else:
                return (L[0])

        if len(self.parcour_avec_exo) == 0:
            print("impossible d'affiche l'arbre le parcours avec exo est vide")
        else:
            aa = Arbre(liste_to_arbre(self.parcour_avec_exo))
            aa.view()

    def cal_parcours(self, matiere,notion,niveau,graphe_de_connaissance):
        arbre = self.graphe



        L_parcours = []

        fils = [0]
        fils = arbre.lesfils()
        L_parcours += [arbre.racine]

        fin = False
        ct=0
        while fils != [] and ct<1000:
            ct+=1

            if len(fils) > 1:
                L_info = [fils[k].racine.niveau for k in range(len(fils))]

                if niveau == "Debutant":
                    if "Debutant" in L_info:
                        arbre = fils[L_info.index("Debutant")]


                elif niveau == "Intermediaire":
                    if "Debutant" in L_info:
                        arbre = fils[L_info.index("Debutant")]

                    if "Intermediaire" in L_info:
                        arbre = fils[L_info.index("Intermediaire")]


                elif niveau == "Avance":

                    if "Debutant" in L_info:
                        arbre = fils[L_info.index("Debutant")]

                    if "Intermediaire" in L_info:
                        arbre = fils[L_info.index("Intermediaire")]

                    if "Avance" in L_info:
                        arbre = fils[L_info.index("Avance")]



                else:
                    a = 1




            elif len(fils) == 1:

                if niveau == "Debutant":
                    if "Debutant" == fils[0].racine.niveau:
                        arbre = fils[0]
                    else:
                        fils = []
                        fin = True

                elif niveau == "Intermediaire":

                    if ("Debutant" == fils[0].racine.niveau) or ("Intermediaire" == fils[0].racine.niveau):
                        arbre = fils[0]

                    else:
                        fils = []
                        fin = True




                elif niveau == "Avance":
                    arbre = fils[0]

                else:
                    print("niveau non valide | cal_parcours 45453")

            else:
                arbre = fils

            if fin == False:
                fils = arbre.lesfils()

            L_parcours += [arbre.racine]

        if niveau == "Debutant":
            L_parcours.pop()

        L_parcours_notion_Non_Matrisé=graphe_de_connaissance.selectionDesNotionNonMaitrise(L_parcours)
        self.parcours = L_parcours_notion_Non_Matrisé

    def defintion_exercice(self, niveau_s, opti,res_exo):

        #if opti==    #TODO conversion de l entre apti

        L_parcour_avec_exo = []
        L_parcours = self.parcours

        if opti == "normal":

            for k in L_parcours:
                L_exo = k.exo
                L_exo_selec = []

                for kk in L_exo:

                    if res_exo.exerciceNonRealise(kk.nom):
                        if niveau_s == "Debutant":

                            if kk.niveau == "Debutant":
                                L_exo_selec += [kk]

                        elif niveau_s == "Intermediaire":

                            if (kk.niveau == "Debutant") or (kk.niveau == "Intermediaire"):
                                L_exo_selec += [kk]

                        else:
                            L_exo_selec += [kk]

                L_parcour_avec_exo += [k] + L_exo_selec

            self.parcour_avec_exo = L_parcour_avec_exo

        elif opti == "date_limite":

            taille_min_cours = 0
            for k in self.parcours:
                taille_min_cours += k.duree

            L_exo_selec = []

            for k in L_parcours:
                L_exo = k.exo

                for kk in L_exo:

                    if res_exo.exerciceNonRealise(kk.nom):

                        if niveau_s == "Debutant":

                            if kk.niveau == "Debutant":
                                L_exo_selec += [kk]

                        elif niveau_s == "Intermediaire":

                            if (kk.niveau == "Debutant") or (kk.niveau == "Intermediaire"):
                                L_exo_selec += [kk]

                        else:
                            L_exo_selec += [kk]

            #######
            # Exo validation

            L_Exo_Validation = []
            for kkkk in L_exo_selec:
                if "Validation" in kkkk.nom:
                    L_Exo_Validation += [kkkk]

            print("L_Exo_Validation    ", len(L_Exo_Validation), L_Exo_Validation)

            ######

            taille_min_exo = 0
            for kil in L_Exo_Validation:
                taille_min_exo += kil.duree

            taille_min = taille_min_cours + taille_min_exo

            if temps_limite - taille_min >= 0:
                temps_limite = temps_limite - taille_min

                L_exo_selec = []

                for k in L_parcours:
                    L_exo = k.exo

                    for kk in L_exo:

                        if not ("Validation" in kk.nom):

                            if res_exo.exerciceNonRealise(kk.nom):

                                if niveau_s == "Debutant":

                                    if kk.niveau == "Debutant":
                                        L_exo_selec += [kk]

                                elif niveau_s == "Intermediaire":

                                    if (kk.niveau == "Debutant") or (kk.niveau == "Intermediaire"):
                                        L_exo_selec += [kk]

                                else:
                                    L_exo_selec += [kk]

                a = sorted(L_exo_selec, key=lambda bb: bb.duree / bb.score)

                sum = 0
                L_ex_valide = []

                for k_v in a:

                    if sum + k_v.duree < temps_limite:
                        sum += +k_v.duree

                        L_ex_valide.append(k_v)

                print("L_ex_valide    ", len(L_ex_valide), L_ex_valide)
                print(len(L_parcours))

                for k in L_parcours:
                    L_exo = k.exo
                    L_exo_selec = []

                    for kk in L_exo:

                        if kk in L_ex_valide:

                            if niveau_s == "Debutant":

                                if kk.niveau == "Debutant":
                                    L_exo_selec += [kk]

                            elif niveau_s == "Intermediaire":

                                if (kk.niveau == "Debutant") or (kk.niveau == "Intermediaire"):
                                    L_exo_selec += [kk]

                            else:
                                L_exo_selec += [kk]

                    L_parcour_avec_exo += [k] + L_exo_selec + [L_Exo_Validation.pop(0)]




                self.parcour_avec_exo = L_parcour_avec_exo


            else:
                print("Le temps critique est de " + str(
                    2 * taille_min) + " le parcours ne peut pas etre determiner si le temps disponible est inferieur au temps critique")

    def update_resu(self, ):
        pass

    def selection_cognitive(self):
        pass

